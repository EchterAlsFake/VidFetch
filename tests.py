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
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QGraphicsScene, QLabel, QLineEdit, QPushButton, QDialog, QDialogButtonBox, QVBoxLayout
from colorama import *
from ffmpeg_progress_yield import FfmpegProgress
from pytube import YouTube
from tqdm import tqdm
from ui_form import Ui_Widget

__version__ = "0.1"
__author__ = "EchterAlsFake"

class CustomDialog(QWidget):

    def __init__(self):
        super().__init__()

        QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Help

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.helpRequested.connect(self.qusstion)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.rejected)

        self.layout = QVBoxLayout()
        message = QLabel("ffmpeg was not found on your system.  Do you want to automatically install it?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.buttonBox
        self.setLayout(self.layout)

    def accept(self):
        print("Accepted")



    def qusstion(self):
        print("Question marked")

    def rejected(self):

        print("Rejected")

app = QApplication(sys.argv)
w = CustomDialog()
w.show()
app.exec()