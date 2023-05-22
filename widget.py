print("Initializing...")
import distro
import os
import requests
import shutil
import sys
import tarfile
import wget
import zipfile
from configparser import ConfigParser
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPixmap, QPalette, QPainter, QColor, Qt
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QGraphicsScene, QLabel, QLineEdit, QPushButton
from colorama import *
from ffmpeg_progress_yield import FfmpegProgress
from pytube import YouTube
from tqdm import tqdm
from ui_form import Ui_Widget


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Variables needed later...
        self.resolutions = ['144p', '240p', '360p', '480p', '720p', '1080p', '1440p', '2160p', '4320p']
        self.music_mode = ""
        self.video_mode = ""
        self.video_only = ""
        self.interactive = ""
        self.audio_codec = ""
        self.video_codec = "libx264"
        self.video_format = ""
        self.title = ""
        self.z = Fore.LIGHTGREEN_EX + "[+]"
        self.x = Fore.LIGHTRED_EX + "[!]"
        self.platform = sys.platform
        self.distro = distro.name(pretty=True)


        # Setup UI, ffmpeg and configuration files
        if sys.platform == "windows" or "win32":
            self.add_to_path_windows()

        self.check_ffmpeg_config()
        self.conf = ConfigParser()
        self.conf.read('config.ini')
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.set_ui_start()

        self.ui.ui_theme_apply.clicked.connect(self.apply_theme)
        self.ui.output_video_button.clicked.connect(self.output_path_update)
        self.ui.output_music_button.clicked.connect(self.output_path_update)
        self.ui.output_thumbnail_button.clicked.connect(self.output_path_update)
        self.ui.video_start_prep_button.clicked.connect(self.check_video)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.threads_radio_buttons)
        self.timer.start(1000)

    # The following functions are used to set up the UI, ffmpeg and configuration files
    def add_to_path_windows(self):

        print(Fore.LIGHTGREEN_EX + "[+]" + Fore.LIGHTCYAN_EX + "Adding to PATH...")
        file_path = "ffmpeg\\ffmpeg-master-latest-win64-gpl\\bin"
        current_path = os.environ.get('PATH')
        new_path = current_path + ';' + file_path
        os.environ['PATH'] = new_path

    def check_ffmpeg_config(self):

        if shutil.which("ffmpeg") is not None:
            print(self.z + Fore.LIGHTMAGENTA_EX + "Found: ffmpeg")
            print(self.z + Fore.LIGHTCYAN_EX + f"Running on: {self.distro}")

        else:
            self.ffmpeg_setup()

        if not os.path.isfile("config.ini"):
            self.config_file_setup()

    def config_file_setup(self):

        with open("config.ini", "w") as config_file:
            data = """
        [ffmpeg]
        path = 
    
        [ui]
        mode = dark
        ovveride_linux_dark_mode = false
    
    
        [windows]
        video_output = output\\video\\
        music_output = output\\music\\
        thumbnail_output = output\\thumb\\
    
        [linux]
        video_output = output/video/
        music_output = output/music/
        thumbnail_output = output/thumb/
    
    
    
        """
            config_file.write(data)
            config_file.close()

    def set_ui_start(self):

        if sys.platform == "windows" or "win32":

            video_output = self.conf['windows']['video_output']
            music_output = self.conf['windows']['music_output']
            thumbnail_output = self.conf['windows']['thumbnail_output']

            self.ui.output_video_lineedit.setText(str(video_output))
            self.ui.output_music_lineedit.setText(str(music_output))
            self.ui.output_thumbnail_lineedit.setText(str(thumbnail_output))


        elif sys.platform == "linux":

            video_output = self.conf['linux']['video_output']
            music_output = self.conf['linux']['music_output']
            thumbnail_output = self.conf['linux']['thumbnail_output']

            self.ui.output_video_lineedit.setText(str(video_output))
            self.ui.output_music_lineedit.setText(str(music_output))
            self.ui.output_thumbnail_lineedit.setText(str(thumbnail_output))

        self.ui.radio_mp4.setChecked(True)
        self.ui.radio_m4a.setChecked(True)

        if self.conf['ui']['mode'] == "dark":
            self.ui.radio_dark_mode.setChecked(True)

        if self.conf['ui']['override_linux_dark_mode'] == "true":
            self.ui.checkbox_linux_override_dark.setChecked(True)

        if self.conf['ui']['mode'] == 'white':
            self.ui.radio_white_theme.setChecked(True)

        if self.conf['ui']['mode'] == 'EchterAlsFake':
            self.ui.radio_echteralsfake.setChecked(True)

        self.disable_boxes()


    def enable_checkboxes(self):

        self.ui.video_download_start_button.setEnabled(True)
        self.ui.groupbox_resolutions.setEnabled(True)
        self.ui.groupbox_format.setEnabled(True)
        self.ui.group_box_music.setEnabled(True)

    def disable_boxes(self):

        self.ui.video_download_start_button.setDisabled(True)
        self.ui.groupbox_resolutions.setDisabled(True)
        self.ui.groupbox_format.setDisabled(True)
        self.ui.group_box_music.setDisabled(True)

    def ffmpeg_setup(self):

        if self.platform == "windows" or "win32":

                print(self.x + Fore.LIGHTCYAN_EX + "ffmpeg not found")
                print(self.z + Fore.LIGHTYELLOW_EX + "Trying automatic installation")
                wget.download("https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip")
                print(self.z + Fore.LIGHTCYAN_EX + "Extracting...")
                with zipfile.ZipFile("ffmpeg-master-latest-win64-gpl.zip", "r") as zip_ref:
                    zip_ref.extractall("ffmpeg")
                    print(self.z + Fore.LIGHTMAGENTA_EX + "Extracted")
                    file_path = "ffmpeg\\ffmpeg-master-latest-win64-gpl\\bin"
                    current_path = os.environ.get('PATH')
                    new_path = current_path + ";" + file_path
                    os.environ['PATH'] = new_path
                    if shutil.which("ffmpeg"):
                        print(self.z + Fore.LIGHTMAGENTA_EX + "Successfully installed ffmpeg.  Please note, that the path variable is only valid until your restart your system.  ffmpeg will be added to your PATH everytime the program starts.")
                        print(self.z + Fore.LIGHTCYAN_EX + "Testing...")
                        print(self.z + Fore.LIGHTMAGENTA_EX + "Downloading test files...")
                        wget.download("https://drive.google.com/uc?export=download&id=1u9aKCxjRYTVMxOu3gvGNznwrmjEVRbJx")
                        command = 'ffmpeg -i ELEVEN.mp3 -vn -c:a aac -b:a 256k output.m4a'
                        try:
                            os.system(str(command))
                            print(self.z + Fore.LIGHTYELLOW_EX + "Tests passed :)")
                            os.remove("ELEVEN.mp3")
                            os.remove("output.m4a")

                        except Exception as e:
                            print(f"Tests failed :( {str(e)}")

                    else:
                        print("""
Unknown error...

Please install ffmpeg manually:

1) Download this file: https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip
2) Extract the file
3) Copy the file to any random folder on your PC (like documents or appdata)
4) Copy the folder location (example: C:\\Users\your_name\Documents\\ffmpeg-master-latest-win64-gpl\\bin)
5) Now go to YouTube or ask ChatGPT how to add this directory to your PATH
        """)


        elif self.platform == "linux":

            if shutil.which("ffmpeg") is not None:
                print(Fore.LIGHTGREEN_EX + "[+]" + Fore.LIGHTCYAN_EX + "Found: ffmpeg")
                print(Fore.LIGHTGREEN_EX + "[+]" + Fore.LIGHTMAGENTA_EX + f"Running on: {distro.name(pretty=True)}")

            elif shutil.which("ffmpeg") is None:

                print(Fore.LIGHTRED_EX + "[!]" + Fore.LIGHTBLUE_EX + "Could not find: ffmpeg")
                _ = input("""
Do you want to try an automatic installation of ffmpeg via your package manager? (ROOT)

or 

Do you want me to download an ffmpeg release and include it to the program?  (non ROOT)

1) Package manager
2) Download and include locally

        """)
                if _ == "1":

                    if distro.name(pretty=True) == "Ubuntu":
                        print(Fore.LIGHTGREEN_EX + "[+]" + Fore.LIGHTYELLOW_EX + "Detected: Ubuntu")
                        print(
                            Fore.LIGHTMAGENTA_EX + "Executing: sudo apt-get install ffmpeg, please enter your root password!")
                        os.system("sudo apt-get install ffmpeg")

                    elif distro.name(pretty=True) == "Debian":
                        print(Fore.LIGHTGREEN_EX + "[+]" + Fore.LIGHTYELLOW_EX + "Detected: Debian")
                        print(
                            Fore.LIGHTMAGENTA_EX + "Executing: sudo apt-get install ffmpeg, please enter your root password!")
                        os.system("sudo apt-get install ffmpeg")

                    elif distro.name(pretty=True) == "Fedora":
                        print(Fore.LIGHTGREEN_EX + "[+]" + Fore.LIGHTYELLOW_EX + "Detected: Fedora")
                        print(Fore.LIGHTMAGENTA_EX + "Executing: sudo dnf install ffmpeg, please enter your root password!")
                        os.system("sudo dnf install ffmpeg")

                    elif distro.name(pretty=True) == "Arch":
                        print(Fore.LIGHTGREEN_EX + "[+]" + Fore.LIGHTYELLOW_EX + "Detected: Arch")
                        print(Fore.LIGHTMAGENTA_EX + "Executing: sudo pacman -S ffmpeg, please enter your root password!")
                        os.system("sudo pacman -S ffmpeg")

                    elif distro.name(pretty=True) == "openSUSE":
                        print(Fore.LIGHTGREEN_EX + "[+]" + Fore.LIGHTYELLOW_EX + "Detected: openSUSE")
                        print(
                            Fore.LIGHTMAGENTA_EX + "Executing: sudo zypper install ffmpeg, please enter your root password!")
                        os.system("sudo zypper install ffmpeg")

                    elif distro.name(pretty=True) == "Manjaro":
                        print(Fore.LIGHTGREEN_EX + "[+]" + Fore.LIGHTYELLOW_EX + "Detected: Manjaro")
                        print(Fore.LIGHTMAGENTA_EX + "Executing: sudo pacman -S ffmpeg, please enter your root password!")
                        os.system("sudo pacman -S ffmpeg")

                elif _ == "2":
                    wget.download(
                        "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-linux64-lgpl.tar.xz")
                    file = tarfile.open("ffmpeg-master-latest-linux64-lgpl.tar.xz")
                    file.extractall("ffmpeg")
                    conf.set("ffmpeg", 'path', 'ffmpeg/bin/ffmpeg')
                    with open("config.ini", "w") as config_file:
                        conf.write(config_file)
                        config_file.close()

    def show_error(self, e):

        msg_box = QMessageBox()
        msg_box.setText(str("Unhandled Exception: " + str(e) + "Please report this error to GitHub"))
        msg_box.setWindowTitle("Unhandled Exception")
        msg_box.show()

    def output_path_update(self):

        video_path = self.ui.output_video_lineedit.text()
        music_path = self.ui.output_music_lineedit.text()
        thumnail_path = self.ui.output_thumbnail_lineedit.text()

        if sys.platform == "windows" or "win32":
            self.conf.set("windows", "video_output", video_path)
            self.conf.set("windows", "music_output", music_path)
            self.conf.set("windows", "thumbnail_output", thumnail_path)
            with open("config.ini", "w") as config_file:
                self.conf.write(config_file)
                config_file.close()

                self.show_applied()

        elif sys.platform == "linux":

            self.conf.set("linux", "video_output", video_path)
            self.conf.set("linux", "music_output", music_path)
            self.conf.set("linux", "thumbnail_output", thumnail_path)
            with open("config.ini", "w") as config_file:
                self.conf.write(config_file)
                config_file.close()

                self.show_applied()

    def threads_radio_buttons(self):

        if self.ui.radio_interactive.isChecked():
            self.interactive = True
            self.video_mode = False
            self.video_only = False
            self.music_mode = False

        if self.ui.radio_music_mode.isChecked():
            self.music_mode = True
            self.video_mode = False
            self.video_only = False
            self.interactive = False

            for resolution in self.resolutions:
                radioButton = getattr(self.ui, f"radio_{resolution}")
                radioButton.setDisabled(True)
                radioButton.setStyleSheet("color: grey;")

        if self.ui.radio_video_mode.isChecked():
            self.video_mode = True
            self.video_only = False
            self.interactive = False
            self.music_mode = False

        if self.ui.radio_video_only.isChecked():
            self.video_only = True
            self.ui.radio_mp3.setDisabled(True)
            self.ui.radio_m4a.setDisabled(True)
            self.ui.radio_wav.setDisabled(True)
            self.ui.radio_opus.setDisabled(True)
            self.video_mode = True
            self.interactive = False
            self.music_mode = False

    def apply_theme(self):

        if self.ui.checkbox_linux_override_dark.isChecked():

            self.conf.set("ui", "override_linux_dark_mode", "true")
            self.conf.set("ui", "mode", "dark")
            with open("config.ini", "w") as config_file:
                self.conf.write(config_file)
                config_file.close()

            self.show_applied()

        if self.ui.radio_white_theme.isChecked():

            msgBox = QMessageBox()
            msgBox.setText(str("ARE YOU SURE WANT TO USE THE WHITE THEME?"))
            msgBox.exec()

            msgBox2 = QMessageBox(self)
            msgBox2.setText(str("You are kidding me...."))
            msgBox2.exec()

            self.conf.set("ui", "mode", "white")
            with open("config.ini", "w") as config_file:
                self.conf.write(config_file)
                config_file.close()

            self.show_applied()

        if self.ui.radio_echteralsfake.isChecked():

            msgBox = QMessageBox()
            msgBox.setText(str("Warning: This theme is a meme (joke) theme xD. Please be aware of that and don't ask questions. I have my reason :D"))
            msgBox.exec()

            self.conf.set("ui", "mode", "EchterAlsFake")
            self.conf.set("ui", "override_linux_dark_mode", "false")
            with open("config.ini", "w") as config_file:
                self.conf.write(config_file)
                config_file.close()

            self.show_applied()

        if self.ui.radio_dark_mode.isChecked():

            self.conf.set("ui", "mode", "dark")
            with open("config.ini", "w") as config_file:
                self.conf.write(config_file)
                config_file.close()

            self.show_applied()


    def clear_resolutions(self):

        self.ui.radio_144p.setEnabled(True)
        self.ui.radio_240p.setEnabled(True)
        self.ui.radio_360p.setEnabled(True)
        self.ui.radio_480p.setEnabled(True)
        self.ui.radio_720p.setEnabled(True)
        self.ui.radio_1080p.setEnabled(True)
        self.ui.radio_1440p.setEnabled(True)
        self.ui.radio_2160p.setEnabled(True)
        self.ui.radio_4320p.setEnabled(True)

    def show_applied(self):

        msgBox = QMessageBox()
        msgBox.setText(str("Successfully applied!"))
        msgBox.exec()





    def check_video(self): # Optimizd for automated using with the playlist function.

        url = self.ui.video_url_lineedit.text()

        try:

            YouTube(url).check_availability()
            self.get_metadata(url)


        except Exception as e:
                print("Video unavailable...")
                msgBox = QMessageBox()
                msgBox.setText(str(f"The Video URL is not valid.  Debug information: {e}"))
                msgBox.exec()
                self.ui.video_url_lineedit.clear()

    def get_metadata(self, url):

        y = YouTube(url)

        thumbnail_url = y.thumbnail_url
        video_id = str(y.video_id)
        thumbnail_output = self.ui.output_thumbnail_lineedit.text() + video_id + ".jpg"

        try:

            wget.download(thumbnail_url, out=thumbnail_output)
            if os.path.isfile(thumbnail_output):
                print(Fore.LIGHTGREEN_EX + "[+]" + Fore.LIGHTMAGENTA_EX + "Thumbnail: ✔")
                scene = QGraphicsScene(self)
                pixmap = QPixmap(thumbnail_output)
                pixmapItem = scene.addPixmap(pixmap)
                self.ui.video_graphics_view.setScene(scene)
                self.ui.video_graphics_view.setRenderHint(QPainter.Antialiasing)
                self.ui.video_graphics_view.setSceneRect(pixmapItem.boundingRect())
                self.ui.video_graphics_view.fitInView(pixmapItem, Qt.KeepAspectRatio)
                pixmapItem.show()

            else:
                print(Fore.LIGHTRED_EX + "[!]" + Fore.LIGHTMAGENTA_EX + "Thumbnail: Error")

        except Exception as e:
            self.show_error(e)


        if self.video_mode or self.video_only:
            print("Running Video mode")
            self.enable_checkboxes()
            resolutions = self.resolutions
            dont_know_how_to_name_that_variable_lol = len(resolutions) + 1
            self.ui.progressbar_metadata.setMaximum(dont_know_how_to_name_that_variable_lol)

            data = y.streams.all()
            resolutions_list = []
            bitrate_list = []
            fps_list = []
            file_size_list = []
            legacy_filesize_list = []
            counter = 0

            resolution_status = {resolution: False for resolution in resolutions}

            for resolution in tqdm(resolutions):
                for stream in data:
                    if stream.resolution == resolution:
                        resolutions_list.append(stream.resolution)
                        try:
                            bitrate_list.append(stream.bitrate)
                            fps_list.append(stream.fps)
                            file_size_list.append(str(stream.filesize_mb) + str("MB"))
                            legacy_filesize_list.append(stream.filesize)
                        except AttributeError as e:
                            print("Ignored AttributeError: " + str(e))

                        resolution_status[resolution] = True

                counter += 1
                self.ui.progressbar_metadata.setValue(counter)
            self.ui.progressbar_metadata.setValue(10)

            for resolution, is_available in resolution_status.items():

                if not is_available:
                    radioButton = getattr(self.ui, f'radio_{resolution}')
                    radioButton.setDisabled(True)
                    radioButton.setStyleSheet("color: grey;")

        if self.music_mode:
            for resolution in self.resolutions:
                if self.music_mode:
                    radioButton = getattr(self.ui, f"radio_{resolution}")
                    radioButton.setDisabled(True)
                    radioButton.setStyleSheet("color: grey;")

        self.set_metadata(bitrate=bitrate_list[-1], fps=fps_list[-1], file_size=file_size_list[-1])



    def set_metadata(self, bitrate, fps, file_size):

        self.ui.metadata_bitrate_lineedit.setText(str(bitrate))
        self.ui.metadata_fps_lineedit.setText(str(fps))
        self.ui.metadata_filesize_lineedit.setText(str(file_size))
        self.enable_checkboxes()
        print(Fore.LIGHTGREEN_EX + "[+]" + Fore.LIGHTYELLOW_EX + "✔")


    def download_highest_resolution(self):
        print("")

    def download_alternate_progress_bar(self, filesize, url):
        # Thanks to ChatGPT

        response = requests.get(url, stream=True)
        downloaded_size = 0

        with open("video.mp4", "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    downloaded_size += len(chunk)
                    f.write(chunk)

                    # Update Progress Bar
                    percentage_of_completion = downloaded_size / filesize * 100
                    self.ui.progressbar_video.setValue(int(percentage_of_completion))

    def progress_function(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = bytes_downloaded / total_size * 100
        self.ui.progressbar_video.setValue(int(percentage_of_completion))

    def start_download(self, url):
        yt = YouTube(url, on_progress_callback=self.progress_function)

        yt.streams.filter(only_video=True, resolution=self.resolution).first().download(filename=self.title)
        yt.streams.filter(only_audio=True).first().download(filename=self.title + ".mp3")
        self.convert_to_mp4(video_input=self.title, audio_input=self.title + ".mp3", output=self.ui.output_video_lineedit.text())

    def convert_to_mp4(self, video_input, audio_input, output):

        output = output + self.title + ".mp4"

        command = [f'ffmpeg', '-i', f'{video_input}', '-i', f'{audio_input}', '-c:v', 'copy', '-c:a', 'aac', '-b:a',
                   '256k', f'{output}']

        ff = FfmpegProgress(command)
        self.ui.progressbar_converting.setMaximum(100)
        self.ui.progressbar_converting.setValue(0)
        for progress in ff.run_command_with_progress():
            self.ui.progressbar_converting.setValue(int(progress))

        self.ui.progressbar_converting.setValue(100)

        os.remove(self.title + ".mp3")


class EchterAlsFake(object):

    def setup_lol(self):


        widget.ui.metadata_bitrate_label.setStyleSheet("color: #808000;")  # Olivgrün
        widget.ui.progressbar_metadata_label.setStyleSheet("color: #800080;")  # Lila
        widget.ui.progressbar_video_label.setStyleSheet("color: #FF69B4;")  # Hot Pink
        widget.ui.progressbar_playlist_label.setStyleSheet("color: #FF8C00;")  # Dunkles Orange
        widget.ui.progressbar_converting_label.setStyleSheet("color: #7FFF00;")  # Chartreuse
        widget.ui.metadata_bitrate_lineedit.setStyleSheet("background-color: #008B8B; color: #FFFFFF;")  # Dunkles Cyan
        widget.ui.progressbar_metadata.setStyleSheet("QProgressBar {background-color: #DAA520; color: #FFFFFF;}")
        widget.ui.progressbar_video.setStyleSheet("QProgressBar {background-color: #228B22; color: #FFFFFF;}")
        widget.ui.progressbar_playlist.setStyleSheet("QProgressBar {background-color: #6A5ACD; color: #FFFFFF;}")
        widget.ui.progressbar_converting.setStyleSheet("QProgressBar {background-color: #FF4500; color: #FFFFFF;}")
        widget.ui.groupbox_metadata.setStyleSheet("border: 2px solid #D2691E;")  # Schokolade
        widget.ui.groupbox_progress_bars.setStyleSheet("border: 2px solid #8B4513;")  # Sattelbraun
        widget.ui.radio_opus.setStyleSheet("color: #0000CD;")  # Mittelblau
        widget.ui.radio_m4a.setStyleSheet("color: #BA55D3;")  # Mittleres Orchidee
        widget.ui.radio_wav.setStyleSheet("color: #A0522D;")  # Sienna
        widget.ui.radio_mp3.setStyleSheet("color: #8A2BE2;")  # Blauviolett
        widget.ui.ui_theme_apply.setStyleSheet("QPushButton {background-color: #CD5C5C; color: #FFFFFF;}")  # Indischrot
        widget.ui.video_start_prep_button.setStyleSheet("QPushButton {background-color: #FFD700; color: #000000;}")  # Gold
        widget.ui.playlist_start_button.setStyleSheet(
            "QPushButton {background-color: #3CB371; color: #000000;}")  # Medium Sea Green
        widget.ui.video_thumbnail_copy_button.setStyleSheet(
            "QPushButton {background-color: #7B68EE; color: #000000;}")  # Mittel Schiefer blau
        widget.ui.output_thumbnail_button.setStyleSheet(
            "QPushButton {background-color: #C71585; color: #FFFFFF;}")  # Mittel Violettrot
        widget.ui.output_music_button.setStyleSheet(u"background-color: #9A0EEA")
        widget.ui.gridLayout_6.addWidget(widget.ui.output_music_button, 1, 2, 1, 1)
        output_video_label = QLabel(widget.ui.groupbox_output)
        output_video_label.setObjectName(u"output_video_label")
        output_video_label.setStyleSheet(u"color: #B8860B")
        widget.ui.gridLayout_6.addWidget(widget.ui.output_video_label, 2, 0, 1, 1)
        widget.ui.output_video_lineedit = QLineEdit(widget.ui.groupbox_output)
        widget.ui.output_video_lineedit.setObjectName(u"output_video_lineedit")
        widget.ui.output_video_lineedit.setStyleSheet(u"background-color: #00FFFF")
        widget.ui.gridLayout_6.addWidget(widget.ui.output_video_lineedit, 2, 1, 1, 1)
        widget.ui.output_video_button = QPushButton(widget.ui.groupbox_output)
        widget.ui.output_video_button.setObjectName(u"output_video_button")
        widget.ui.output_video_button.setStyleSheet(u"background-color: #FF69B4")
        widget.ui.gridLayout_6.addWidget(widget.ui.output_video_button, 2, 2, 1, 1)



if __name__ == "__main__":
    conf = ConfigParser()
    conf.read('config.ini')
    app = QApplication(sys.argv)
    widget = Widget()

    if conf['ui']['mode'] == 'dark':
        if sys.platform == "windows" or "win32":
            sys.argv += ['-platform', 'windows:darkmode=2']
            app.setStyle('Fusion')

        elif sys.platform == "linux":

            if conf['ui']['override_linux_dark_mode'] == 'true':
                print(Fore.LIGHTYELLOW_EX + "Overriding Linux Dark Mode")
                dark_palette = QPalette()
                dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
                dark_palette.setColor(QPalette.WindowText, Qt.white)
                dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
                dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
                dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
                dark_palette.setColor(QPalette.ToolTipText, Qt.white)
                dark_palette.setColor(QPalette.Text, Qt.white)
                dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
                dark_palette.setColor(QPalette.ButtonText, Qt.white)
                dark_palette.setColor(QPalette.BrightText, Qt.red)
                dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
                dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
                dark_palette.setColor(QPalette.HighlightedText, Qt.black)
                app.setPalette(dark_palette)
                app.setStyle("Fusion")

    elif conf['ui']['mode'] == 'white':
        if sys.platform == "windows":
            sys.argv += ['-platform', 'windows:darkmode=0']
            app.setStyle('Fusion')

        elif sys.platform == "linux":
            light_palette = QPalette()
            light_palette.setColor(QPalette.Window, QColor(239, 240, 241))
            light_palette.setColor(QPalette.WindowText, Qt.black)
            light_palette.setColor(QPalette.Base, QColor(255, 255, 255))
            light_palette.setColor(QPalette.AlternateBase, QColor(245, 245, 245))
            light_palette.setColor(QPalette.ToolTipBase, Qt.white)
            light_palette.setColor(QPalette.ToolTipText, Qt.white)
            light_palette.setColor(QPalette.Text, Qt.black)
            light_palette.setColor(QPalette.Button, QColor(239, 240, 241))
            light_palette.setColor(QPalette.ButtonText, Qt.black)
            light_palette.setColor(QPalette.BrightText, Qt.red)
            light_palette.setColor(QPalette.Link, QColor(0, 0, 255))
            light_palette.setColor(QPalette.Highlight, QColor(41, 128, 185))
            light_palette.setColor(QPalette.HighlightedText, Qt.white)
            app.setPalette(light_palette)

    elif conf['ui']['mode'] == 'EchterAlsFake':
        EchterAlsFake().setup_lol()

    widget.show()
    sys.exit(app.exec())



