print("Initializing...")
import time
import distro
import os
import requests
import shutil
import sys
import tarfile
import wget
import zipfile
from configparser import ConfigParser
from PySide6.QtCore import Qt, QTimer, QThread, Signal
from PySide6.QtGui import QPixmap, QPalette, QPainter, QColor, Qt
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QGraphicsScene, QLabel, QLineEdit, QPushButton, QDialogButtonBox, QDialog, QVBoxLayout, QProgressBar, QRadioButton
from colorama import *
from ffmpeg_progress_yield import FfmpegProgress
from pytube import YouTube
from tqdm import tqdm
from ui_form import Ui_Widget

__version__ = "0.1"
__author__ = "EchterAlsFake"
__license__ = "LGPLv3"
__date__ = "2023"

class VidFetch_Core():

    def stripping(self, title):

        disallowed_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', "|"]
        for char in disallowed_chars:
            title = title.replace(char, '')

        return title

    def check_path(self, path):

        return bool(os.path.exists(path))


    def check_video(self, url):

        try:
            y = YouTube(url).check_availability()
            return True, y

        except Exception as e:
            return False, e

    def get_highest_resolution(self, youtube_object): # YouTube object must be an object from Pytube

        resolutions = ["144p", "240p", "360p", "480p", "720p", "1080p", "1440p", "2160p", "3840p"]
        y = youtube_object
        data = y.streams.all() # I know this is deprecated, but it's the only way to get a list of resolutions.
        valid_resolutions = []

        for resolution in resolutions:

            valid_resolutions.extend(
                data_frames for data_frames in data if resolution in data_frames
            )

        return False if valid_resolutions is None else valid_resolutions







class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.resolutions = ['144p', '240p', '360p', '480p', '720p', '1080p', '1440p', '2160p', '4320p']
        self.video_output = self.ui.output_video_lineedit.text()
        self.music_output = self.ui.output_music_lineedit.text()
        self.thumb_output = self.ui.output_thumbnail_lineedit.text()



    def disable_resolutions(self, available_resolutions):
        for resolution in available_resolutions:
            radioButton = getattr(self.ui, f"radio_{resolution}")
            radioButton.setDisabled(True)
            radioButton.setStyleSheet("QRadioButton::indicator:disabled { color: gray; }")

    def enable_resolutions(self):
        for resolution in self.resolutions:
            radioButton = getattr(self.ui, f"radio_{resolution}")
            radioButton.setEnabled(True)
            radioButton.setStyleSheet("")

    def qmsg(self, text):

        qmessage_box = QMessageBox()
        qmessage_box.setText(text)
        qmessage_box.exec()


    def start(self, url):

            if VidFetch_Core().check_video(url)[0]:

                y = VidFetch_Core().check_video(url)[1]


                if self.ui.radio_music_mode.isChecked():

                    mode = "music"
                    output_path = self.music_output
                    quality = False


                elif self.ui.radio_video_mode.isChecked():

                    mode = "video"
                    output_path = self.video_output
                    quality = VidFetch_Core().get_highest_resolution(y)

                elif self.ui.radio_video_only.isChecked():

                    mode = "video_only"
                    output_path = self.video_output
                    quality = VidFetch_Core().get_highest_resolution()


                else:

                    self.qmsg(text="Please choose a download mode, before pressing the start button.")

                try:

                    VidFetch_Core().check_path(output_path)

                except PermissionError:
                    self.qmsg(text="Sorry, it seems like you don't have permissions to write to that path. Try "
                                   "executing the Application as root, even though, that this is NOT recommended")

                try:

                    title = y[1].title
                    title = VidFetch_Core().stripping(title)

                except Exception as e:
                    self.qmsg(text=e)


            else:

                self.qmsg(text="Error with the URL. Please check for updates and make sure the URL you've entered is "
                               "correct.")


    def download(self, mode, output, resolution, quality, youtube_object, title):


        if mode == "music":

            stream = youtube_object.streams.filter(only_audio=True).first()

        elif mode == "video_only":

            stream = youtube_object.streams.filter(only_video=True, resolution=resolution).first()

        










if __name__ == "__main__":
    conf = ConfigParser()
    conf.read('config.ini')
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()


    sys.exit(app.exec())



