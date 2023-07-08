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
from pytube import YouTube, exceptions, Playlist
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

        return path if os.path.exists(path) else False

    def get_highest_resolution(self, youtube_object):  # YouTube object must be an object from Pytube

        resolutions = ["144p", "240p", "360p", "480p", "720p", "1080p", "1440p", "2160p", "3840p"]
        y = youtube_object
        data = y.streams.all()  # I know this is deprecated, but it's the only way to get a list of resolutions.
        valid_resolutions = []

        for resolution in resolutions:

            for stream in data:

                if stream.resolution == resolution:
                    valid_resolutions.append(resolution)

        return valid_resolutions





class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.resolutions = ['144p', '240p', '360p', '480p', '720p', '1080p', '1440p', '2160p', '4320p']
        self.video_output = self.ui.output_video_lineedit.text()
        self.music_output = self.ui.output_music_lineedit.text()
        self.thumb_output = self.ui.output_thumbnail_lineedit.text()
        self.disable_resolutions()
        self.ui.video_start_prep_button.clicked.connect(self.start)


    def disable_resolutions(self):
        for resolution in self.resolutions:
            radioButton = getattr(self.ui, f"radio_{resolution}")
            radioButton.setDisabled(True)

    def enable_resolutions(self, available_resolutions):
        for resolution in available_resolutions:
            radioButton = getattr(self.ui, f"radio_{resolution}")
            radioButton.setEnabled(True)

    def qmsg(self, text):

        qmessage_box = QMessageBox()
        qmessage_box.setText(text)
        qmessage_box.exec()

    def check_video(self, url):

        try:

            return YouTube(url)

        except Exception as e:
            self.qmsg(f"Error with the video.  If you are sure, that the URL is correct, then report it on GitHub. Thanks :) {str(e)}")
            return False




    def start(self):

        url = self.ui.video_url_lineedit.text()

        try:
            y = self.check_video(url)
            available_resolutions = VidFetch_Core().get_highest_resolution(y)
            self.enable_resolutions(available_resolutions)

        except Exception as e:

            self.qmsg(e)






if __name__ == "__main__":
    conf = ConfigParser()
    conf.read('config.ini')
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()


    sys.exit(app.exec())



