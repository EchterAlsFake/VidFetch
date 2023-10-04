"""
Copyright (C) 2023  EchterAlsFake | Johannes Habel

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""

from PySide6.QtWidgets import QApplication, QWidget, QButtonGroup, QMessageBox, QPushButton, QRadioButton, QVBoxLayout, QDialog
from PySide6.QtCore import QThread, Signal
from shared_functions.functions import *
from configparser import ConfigParser
from ffmpeg_progress_yield import FfmpegProgress
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_files.VidFetch import Ui_VidFetch

import requests
import random

def ui_popup(text):
    qmessage_box = QMessageBox()
    qmessage_box.setText(text)
    qmessage_box.setIcon(QMessageBox.Information)
    qmessage_box.exec()


def choose_resolution(resolutions):
    """Display a dialog for the user to choose a resolution."""
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)

    class ResolutionDialog(QDialog):
        def __init__(self, resolutions):
            super().__init__()
            self.setWindowTitle("Choose a resolution")
            layout = QVBoxLayout()

            self.radio_buttons = []
            for res in resolutions:
                rb = QRadioButton(res)
                layout.addWidget(rb)
                self.radio_buttons.append(rb)

            self.chosen_resolution = None

            btn = QPushButton("Select")
            btn.clicked.connect(self.on_select)
            layout.addWidget(btn)

            self.setLayout(layout)

        def on_select(self):
            for rb in self.radio_buttons:
                if rb.isChecked():
                    self.chosen_resolution = rb.text()
                    break
            self.accept()

    dialog = ResolutionDialog(resolutions)
    dialog.exec_()

    return dialog.chosen_resolution



class DownloadThread(QThread):
    progress_signal = Signal(int)  # Signal to update progress bar

    def __init__(self, url, destination):
        super().__init__()
        self.url = url
        self.destination = destination

    def run(self):
        with requests.get(self.url, stream=True) as response:
            response.raise_for_status()

            # Get the total file size from headers
            total_size = int(response.headers.get('content-length', 0))
            block_size = 8192  # Set block size

            with open(self.destination, 'wb') as file:
                for data in response.iter_content(block_size):
                    file.write(data)

                    # Update progress bar using signal
                    downloaded_size = file.tell()
                    progress = (downloaded_size / total_size) * 100
                    self.progress_signal.emit(int(progress))

class FFMPEG_thread(QThread):
    progress_signal = Signal(int)  # Signal to update the progress bar

    def __init__(self, cmd):
        super().__init__()
        self.cmd = cmd

    def run(self):

        ff = FfmpegProgress(self.cmd)
        for progress in ff.run_command_with_progress():
            self.progress_signal.emit(int(round(progress)))


class DownloadThread_pytube(QThread):
    progress_signal = Signal(int)  # Signal to update the progress bar
    completed_signal = Signal()    # Signal when download is complete

    def __init__(self, y, mode, quality, output_path, random_int):
        super().__init__()
        print("Connected")
        self.y = y
        self.mode = mode
        self.quality = quality
        self.output_path = output_path
        self.random_int = random_int

    def run(self):
        print("Run")
        self.y.register_on_progress_callback(self.progress_callback)

        print(self.mode)
        print(type(self.mode))

        if self.mode == 1:
            print("Downlading Audio")
            self.y.streams.get_audio_only().first().download(filename=self.output_path)

        elif self.mode == 2:
            print("Downloading video")
            self.y.streams.filter(only_video=True, resolution=self.quality).first().download(filename=str(self.random_int) + ".mp4")
            self.y.streams.get_audio_only().download(filename=str(self.random_int) + ".mp3")

        else:
            print("Yeah")

    def progress_callback(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage = int((bytes_downloaded / total_size) * 100)
        self.progress_signal.emit(percentage)
        if bytes_remaining == 0:
            self.completed_signal.emit()

class VidFetch(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_VidFetch()
        self.ui.setupUi(self)
        #setup_config_file()
        self.setup_ffmpeg()
        self.conf = ConfigParser()
        self.conf.read("config.ini")

        self.buttons = None
        self.buttongroups()

        self.mode = 1
        self.quality = 1
        self.codec = 1
        self.output_path = None
        self.ffmpeg_path = None

        self.load_user_settings()
        self.button_connections()

    def buttongroups(self):
        """
        Needed to keep the buttons in each group, otherwise the selection of the radio buttons
        won't work properly!
        """

        button_group_mode = QButtonGroup()
        button_group_mode.addButton(self.ui.radio_mode_music)
        button_group_mode.addButton(self.ui.radio_mode_video)

        button_group_codec = QButtonGroup()
        button_group_codec.addButton(self.ui.radio_codec_mp3)
        button_group_codec.addButton(self.ui.radio_codec_aac)

        button_group_quality = QButtonGroup()
        button_group_quality.addButton(self.ui.radio_quality_ask)
        button_group_quality.addButton(self.ui.radio_quality_highest)

        self.buttons = button_group_quality, button_group_codec, button_group_mode

    def button_connections(self):
        self.ui.button_start_video.clicked.connect(self.start_video)


    def load_user_settings(self):
        if self.conf["VidFetch"]["default_mode"] == "music":
            self.ui.radio_mode_music.setChecked(True)
            self.mode = 1

        elif self.conf["VidFetch"]["default_mode"] == "video":
            self.ui.radio_mode_video.setChecked(True)
            self.mode = 2

        if self.conf["VidFetch"]["default_quality"] == "highest":
            self.ui.radio_quality_highest.setChecked(True)
            self.quality = 1

        elif self.conf["VidFetch"]["default_quality"] == "ask":
            self.ui.radio_quality_ask.setChecked(True)
            self.quality = 2

        if self.conf["VidFetch"]["default_codec"] == "mp3":
            self.ui.radio_codec_mp3.setChecked(True)
            self.codec = 1

        elif self.conf["VidFetch"]["default_codec"] == "aac":
            self.ui.radio_codec_aac.setChecked(True)
            self.codec = 2

        if os.path.isfile("ffmpeg"):
            self.ffmpeg_path = "ffmpeg"

        elif os.path.isfile("ffmpeg.exe"):
            self.ffmpeg_path = "ffmpeg.exe"

        self.output_path = self.conf["VidFetch"]["output_path"]



    def setup_ffmpeg(self):
        if not os.path.exists("ffmpeg") and not os.path.exists("ffmpeg.exe"):
            ui_popup("ffmpeg was not found.  It will be downloaded now.  Please wait...")
            url = ""
            path = ""
            if sys.platform == "linux":
                url = "https://drive.google.com/uc?export=download&id=1TjnA9oISF58DWWZ0zss22uJuQYi3ltLU"
                path = "ffmpeg"

            elif sys.platform == "win":
                url = "https://drive.google.com/uc?export=download&id=1hls6bh_TFux8Agk5y9VkaEJ3LlXcNTIq"
                path = "ffmpeg.exe"

            self.thread = DownloadThread(url, path)
            self.thread.progress_signal.connect(self.update_progress_bar)
            self.thread.start()

    def update_progress_bar(self, progress):
        """
        Updates the progress bar with the given progress.
        """
        self.ui.progressbar_download.setValue(progress)

    def start_video(self):
        url = self.ui.lineedit_video_url.text()
        self.start_video_connection(url)

    def start_video_connection(self, url):

        try:
            y = YouTube(url)

        except exceptions.RegexMatchError or exceptions.VideoUnavailable:
            ui_popup("Invalid URL / Video not available!")

        else:
            self.title = strip_title(y.title)
            output_path = self.output_path

            if not str(output_path).endswith(os.sep):
                output_path += os.sep

            if self.quality == 1:
                quality = get_highest_resolution(y)

            elif self.quality == 2:
                available_resolutions = get_available_resolutions(y)
                quality = choose_resolution(available_resolutions)

            self.random_int = random.randint(0, 1000000000)
            self.download(y, output_path=output_path, mode=self.mode, resolution=quality)




    def download(self, y, output_path, mode, resolution):
        self.download_thread = DownloadThread_pytube(y=y, output_path=output_path, mode=mode, quality=resolution, random_int=self.random_int)
        self.download_thread.progress_signal.connect(self.ui.progressbar_download.setValue)
        self.download_thread.completed_signal.connect(self.on_download_complete)
        self.download_thread.start()

    def on_download_complete(self):

        if self.codec == 1:
            codec = "libmp3lame"

        elif self.codec == 2:
            codec = "aac"


        if self.mode == 2:

            command = [
                f'{self.ffmpeg_path}',
                '-i', f'{self.random_int}.mp4',
                '-i', f'{self.random_int}.mp3',
                '-c:v', 'copy',
                '-c:a', f'{codec}',
                '-strict', 'experimental',
                f'{self.output_path + self.title + ".mp4"}'
            ]

            self.concat_thread = FFMPEG_thread(cmd=command)
            print("Defined thread")
            self.ui.progressbar_converting.setMaximum(100)
            self.concat_thread.progress_signal.connect(self.ui.progressbar_converting.setValue)
            self.concat_thread.start()
            print("Started thread")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
        widget = VidFetch()
        widget.show()

    except Exception as e:
        ui_popup(str(e))

    sys.exit(app.exec())
