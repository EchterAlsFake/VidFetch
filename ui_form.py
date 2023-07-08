# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QProgressBar, QPushButton, QRadioButton,
    QSizePolicy, QTextBrowser, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1854, 349)
        Widget.setStyleSheet(u"background-color: rgb(0, 0, 0)")
        self.gridLayout_4 = QGridLayout(Widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupbox_urls = QGroupBox(Widget)
        self.groupbox_urls.setObjectName(u"groupbox_urls")
        self.groupbox_urls.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid #757575;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* margin-top sorgt f\u00fcr einen Abstand zwischen dem Titel und dem Rand */\n"
"	border-color: rgb(255, 255, 255)}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px; /* left verschiebt den Titel etwas nach rechts, damit er nicht direkt am Rand anliegt */\n"
"    padding: 0 3px 0 3px; /* padding gibt dem Titel etwas Platz rundherum */\n"
"}\n"
"")
        self.gridLayout_10 = QGridLayout(self.groupbox_urls)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.playlist_start_button = QPushButton(self.groupbox_urls)
        self.playlist_start_button.setObjectName(u"playlist_start_button")
        self.playlist_start_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #5468ff;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    color: #fff;\n"
"    font-family: \"JetBrains Mono\", monospace;\n"
"    font-size: 15px;\n"
"	text-align: center;\n"
"    height: 24px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3c4fe0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c4fe0;\n"
"}\n"
"")

        self.gridLayout_10.addWidget(self.playlist_start_button, 1, 2, 1, 1)

        self.playlist_url_lineedit = QLineEdit(self.groupbox_urls)
        self.playlist_url_lineedit.setObjectName(u"playlist_url_lineedit")
        self.playlist_url_lineedit.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #757575;\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    background: rgb(94, 92, 100);  /* setzt den Hintergrund auf Schwarz */\n"
"    color: #FFFFFF;  /* setzt die Textfarbe auf Wei\u00df */\n"
"    font-size: 16px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
" border-color: rgb(107, 0, 255)\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background: #444444;  /* setzt den Hintergrund auf ein dunkles Grau, wenn das QLineEdit deaktiviert ist */\n"
"    color: #aaaaaa;  /* setzt die Textfarbe auf ein helles Grau, wenn das QLineEdit deaktiviert ist */\n"
"    border-color: #aaaaaa;\n"
"}")
        self.playlist_url_lineedit.setReadOnly(False)

        self.gridLayout_10.addWidget(self.playlist_url_lineedit, 1, 1, 1, 1)

        self.video_thumbnail_copy_button = QPushButton(self.groupbox_urls)
        self.video_thumbnail_copy_button.setObjectName(u"video_thumbnail_copy_button")
        self.video_thumbnail_copy_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #5468ff;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    color: #fff;\n"
"    font-family: \"JetBrains Mono\", monospace;\n"
"    font-size: 16px;\n"
"    padding: 0px 16px 0px 16px;\n"
"    height: 24px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3c4fe0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c4fe0;\n"
"}\n"
"")

        self.gridLayout_10.addWidget(self.video_thumbnail_copy_button, 2, 2, 1, 1)

        self.playlist_url_label = QLabel(self.groupbox_urls)
        self.playlist_url_label.setObjectName(u"playlist_url_label")
        self.playlist_url_label.setStyleSheet(u"color: white")

        self.gridLayout_10.addWidget(self.playlist_url_label, 1, 0, 1, 1)

        self.video_url_lineedit = QLineEdit(self.groupbox_urls)
        self.video_url_lineedit.setObjectName(u"video_url_lineedit")
        self.video_url_lineedit.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #757575;\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    background: rgb(94, 92, 100);  /* setzt den Hintergrund auf Schwarz */\n"
"    color: #FFFFFF;  /* setzt die Textfarbe auf Wei\u00df */\n"
"    font-size: 16px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: rgb(107, 0, 255)\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background: #444444;  /* setzt den Hintergrund auf ein dunkles Grau, wenn das QLineEdit deaktiviert ist */\n"
"    color: #aaaaaa;  /* setzt die Textfarbe auf ein helles Grau, wenn das QLineEdit deaktiviert ist */\n"
"    border-color: #aaaaaa;\n"
"}")
        self.video_url_lineedit.setReadOnly(False)

        self.gridLayout_10.addWidget(self.video_url_lineedit, 0, 1, 1, 1)

        self.video_download_start_button = QPushButton(self.groupbox_urls)
        self.video_download_start_button.setObjectName(u"video_download_start_button")
        self.video_download_start_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #5468ff;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    color: #fff;\n"
"    font-family: \"JetBrains Mono\", monospace;\n"
"    font-size: 15\n"
"px;\n"
"    padding: 0px 16px 0px 16px;\n"
"    height: 24px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3c4fe0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c4fe0;\n"
"}\n"
"")

        self.gridLayout_10.addWidget(self.video_download_start_button, 0, 3, 1, 1)

        self.video_thumbnail_label = QLabel(self.groupbox_urls)
        self.video_thumbnail_label.setObjectName(u"video_thumbnail_label")
        self.video_thumbnail_label.setStyleSheet(u"color: white")

        self.gridLayout_10.addWidget(self.video_thumbnail_label, 2, 0, 1, 1)

        self.video_thumbnail_lineedit = QLineEdit(self.groupbox_urls)
        self.video_thumbnail_lineedit.setObjectName(u"video_thumbnail_lineedit")
        self.video_thumbnail_lineedit.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #757575;\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    background: rgb(94, 92, 100);  /* setzt den Hintergrund auf Schwarz */\n"
"    color: #FFFFFF;  /* setzt die Textfarbe auf Wei\u00df */\n"
"    font-size: 16px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-color: rgb(107, 0, 255)\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background: #444444;  /* setzt den Hintergrund auf ein dunkles Grau, wenn das QLineEdit deaktiviert ist */\n"
"    color: #aaaaaa;  /* setzt die Textfarbe auf ein helles Grau, wenn das QLineEdit deaktiviert ist */\n"
"    border-color: #aaaaaa;\n"
"}")
        self.video_thumbnail_lineedit.setReadOnly(True)

        self.gridLayout_10.addWidget(self.video_thumbnail_lineedit, 2, 1, 1, 1)

        self.video_start_prep_button = QPushButton(self.groupbox_urls)
        self.video_start_prep_button.setObjectName(u"video_start_prep_button")
        self.video_start_prep_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #5468ff;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    color: #fff;\n"
"    font-family: \"JetBrains Mono\", monospace;\n"
"    font-size: 15px;\n"
"    padding: 0px 16px 0px 16px;\n"
"    height: 24px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3c4fe0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c4fe0;\n"
"}\n"
"")

        self.gridLayout_10.addWidget(self.video_start_prep_button, 0, 2, 1, 1)

        self.video_url_label = QLabel(self.groupbox_urls)
        self.video_url_label.setObjectName(u"video_url_label")
        self.video_url_label.setStyleSheet(u"color: white")

        self.gridLayout_10.addWidget(self.video_url_label, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupbox_urls, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(Widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_12 = QGridLayout(self.groupBox_2)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.groupbox_resolutions = QGroupBox(self.groupBox_2)
        self.groupbox_resolutions.setObjectName(u"groupbox_resolutions")
        self.groupbox_resolutions.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid #757575;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* margin-top sorgt f\u00fcr einen Abstand zwischen dem Titel und dem Rand */\n"
"	border-color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px; /* left verschiebt den Titel etwas nach rechts, damit er nicht direkt am Rand anliegt */\n"
"    padding: 0 3px 0 3px; /* padding gibt dem Titel etwas Platz rundherum */\n"
"}\n"
"")
        self.gridLayout_8 = QGridLayout(self.groupbox_resolutions)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.radio_144p = QRadioButton(self.groupbox_resolutions)
        self.radio_144p.setObjectName(u"radio_144p")
        self.radio_144p.setStyleSheet(u"QRadioButton {\n"
"	color: rgb(255, 0, 0) }\n"
"\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"	border: 1px solid white;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    border : 4px solid;\n"
"	border-color: black;\n"
"	border-radius: 6px;\n"
"	background-color: rgb(0, 255, 183);\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator:disabled { color: gray; }\n"
"")

        self.gridLayout_8.addWidget(self.radio_144p, 0, 0, 1, 1)

        self.radio_1080p = QRadioButton(self.groupbox_resolutions)
        self.radio_1080p.setObjectName(u"radio_1080p")
        self.radio_1080p.setStyleSheet(u"QRadioButton {\n"
"	color: rgb(0, 255, 250) }\n"
"\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"	border: 1px solid white;\n"
"	border-radius: 5px;\n"
"}\n"
"QRadioButton::indicator:disabled { color: gray; }\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    border : 4px solid;\n"
"	border-color: black;\n"
"	border-radius: 6px;\n"
"	background-color: rgb(0, 255, 183);\n"
"\n"
"}\n"
"\n"
"")

        self.gridLayout_8.addWidget(self.radio_1080p, 0, 1, 1, 1)

        self.radio_240p = QRadioButton(self.groupbox_resolutions)
        self.radio_240p.setObjectName(u"radio_240p")
        self.radio_240p.setAutoFillBackground(False)
        self.radio_240p.setStyleSheet(u"QRadioButton {\n"
"	color: rgb(255, 0, 0)  }\n"
"\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"	border: 1px solid white;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"QRadioButton::disabled {\n"
"\n"
"	color: gray;\n"
"\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    border : 4px solid;\n"
"	border-color: black;\n"
"	border-radius: 6px;\n"
"	background-color: rgb(0, 255, 183);\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator:disabled { color: gray; }\n"
"")

        self.gridLayout_8.addWidget(self.radio_240p, 1, 0, 1, 1)

        self.radio_1440p = QRadioButton(self.groupbox_resolutions)
        self.radio_1440p.setObjectName(u"radio_1440p")
        self.radio_1440p.setStyleSheet(u"QRadioButton {\n"
"	color:  rgb(0, 255, 250)}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"	border: 1px solid white;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    border : 4px solid;\n"
"	border-color: black;\n"
"	border-radius: 6px;\n"
"	background-color: rgb(0, 255, 183);\n"
"\n"
"}\n"
"QRadioButton::indicator:disabled { color: gray; }\n"
"")

        self.gridLayout_8.addWidget(self.radio_1440p, 1, 1, 1, 1)

        self.radio_360p = QRadioButton(self.groupbox_resolutions)
        self.radio_360p.setObjectName(u"radio_360p")
        self.radio_360p.setAutoFillBackground(False)
        self.radio_360p.setStyleSheet(u"QRadioButton {\n"
"	color: rgb(255, 0, 0)  }\n"
"\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"	border: 1px solid white;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    border : 4px solid;\n"
"	border-color: black;\n"
"	border-radius: 6px;\n"
"	background-color: rgb(0, 255, 183);\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator:disabled { color: gray; }\n"
"")

        self.gridLayout_8.addWidget(self.radio_360p, 2, 0, 1, 1)

        self.radio_2160p = QRadioButton(self.groupbox_resolutions)
        self.radio_2160p.setObjectName(u"radio_2160p")
        self.radio_2160p.setStyleSheet(u"QRadioButton {\n"
"	color: rgb(255, 160, 0) }\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"	border: 1px solid white;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    border : 4px solid;\n"
"	border-color: black;\n"
"	border-radius: 6px;\n"
"	background-color: rgb(0, 255, 183);\n"
"\n"
"}\n"
"QRadioButton::indicator:disabled { color: gray; }\n"
"")

        self.gridLayout_8.addWidget(self.radio_2160p, 2, 1, 1, 1)

        self.radio_480p = QRadioButton(self.groupbox_resolutions)
        self.radio_480p.setObjectName(u"radio_480p")
        self.radio_480p.setStyleSheet(u"QRadioButton {\n"
"	color: rgb(255, 0, 0) }\n"
"\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"	border: 1px solid white;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    border : 4px solid;\n"
"	border-color: black;\n"
"	border-radius: 6px;\n"
"	background-color: rgb(0, 255, 183);\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator:disabled { color: gray; }")

        self.gridLayout_8.addWidget(self.radio_480p, 3, 0, 1, 1)

        self.radio_4320p = QRadioButton(self.groupbox_resolutions)
        self.radio_4320p.setObjectName(u"radio_4320p")
        self.radio_4320p.setStyleSheet(u"QRadioButton {\n"
"	color: rgb(179, 0, 255) }\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"	border: 1px solid white;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    border : 4px solid;\n"
"	border-color: black;\n"
"	border-radius: 6px;\n"
"	background-color: rgb(0, 255, 183);\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator:disabled { color: gray; }")

        self.gridLayout_8.addWidget(self.radio_4320p, 3, 1, 1, 1)

        self.radio_720p = QRadioButton(self.groupbox_resolutions)
        self.radio_720p.setObjectName(u"radio_720p")
        self.radio_720p.setStyleSheet(u"QRadioButton {\n"
"	color: rgb(169, 255, 0) }\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"	border: 1px solid white;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QRadioButton::indicator:disabled { color: gray; }\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    border : 4px solid;\n"
"	border-color: black;\n"
"	border-radius: 6px;\n"
"	background-color: rgb(0, 255, 183);\n"
"\n"
"}\n"
"\n"
"")

        self.gridLayout_8.addWidget(self.radio_720p, 4, 0, 1, 1)


        self.gridLayout_12.addWidget(self.groupbox_resolutions, 0, 2, 1, 1)

        self.group_box_music = QGroupBox(self.groupBox_2)
        self.group_box_music.setObjectName(u"group_box_music")
        self.group_box_music.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid #757575;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* margin-top sorgt f\u00fcr einen Abstand zwischen dem Titel und dem Rand */\n"
"	border-color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px; /* left verschiebt den Titel etwas nach rechts, damit er nicht direkt am Rand anliegt */\n"
"    padding: 0 3px 0 3px; /* padding gibt dem Titel etwas Platz rundherum */\n"
"}\n"
"")
        self.gridLayout_2 = QGridLayout(self.group_box_music)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.radio_mp3 = QRadioButton(self.group_box_music)
        self.radio_mp3.setObjectName(u"radio_mp3")
        self.radio_mp3.setStyleSheet(u"QRadioButton {\n"
"	color: rgb(0, 208, 255) }\n"
"\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"	border: 1px solid white;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    border : 4px solid;\n"
"	border-color: black;\n"
"	border-radius: 6px;\n"
"	background-color: rgb(0, 255, 183);\n"
"\n"
"}\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.radio_mp3, 0, 0, 1, 1)

        self.radio_wav = QRadioButton(self.group_box_music)
        self.radio_wav.setObjectName(u"radio_wav")
        self.radio_wav.setStyleSheet(u"\n"
"\n"
"QRadioButton {\n"
"	color: rgb(255, 255, 255) }\n"
"\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"	border: 1px solid white;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    border : 4px solid;\n"
"	border-color: black;\n"
"	border-radius: 6px;\n"
"	background-color: rgb(0, 255, 183);\n"
"\n"
"}\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.radio_wav, 3, 0, 1, 1)

        self.radio_m4a = QRadioButton(self.group_box_music)
        self.radio_m4a.setObjectName(u"radio_m4a")
        self.radio_m4a.setStyleSheet(u"QRadioButton {\n"
"	color: rgb(96, 0, 255) }\n"
"\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"	border: 1px solid white;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    border : 4px solid;\n"
"	border-color: black;\n"
"	border-radius: 6px;\n"
"	background-color: rgb(0, 255, 183);\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.radio_m4a, 1, 0, 1, 1)

        self.radio_opus = QRadioButton(self.group_box_music)
        self.radio_opus.setObjectName(u"radio_opus")
        self.radio_opus.setStyleSheet(u"\n"
"\n"
"QRadioButton {\n"
"	color: rgb(255, 160, 0) }\n"
"\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"	border: 1px solid white;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    border : 4px solid;\n"
"	border-color: black;\n"
"	border-radius: 6px;\n"
"	background-color: rgb(0, 255, 183);\n"
"\n"
"}\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.radio_opus, 2, 0, 1, 1)


        self.gridLayout_12.addWidget(self.group_box_music, 0, 4, 1, 1)

        self.groupbox_format = QGroupBox(self.groupBox_2)
        self.groupbox_format.setObjectName(u"groupbox_format")
        self.groupbox_format.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid #757575;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* margin-top sorgt f\u00fcr einen Abstand zwischen dem Titel und dem Rand */\n"
"	border-color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px; /* left verschiebt den Titel etwas nach rechts, damit er nicht direkt am Rand anliegt */\n"
"    padding: 0 3px 0 3px; /* padding gibt dem Titel etwas Platz rundherum */\n"
"}\n"
"")
        self.gridLayout_3 = QGridLayout(self.groupbox_format)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.radio_mov = QRadioButton(self.groupbox_format)
        self.radio_mov.setObjectName(u"radio_mov")
        self.radio_mov.setStyleSheet(u"QRadioButton {\n"
"	color: rgb(179, 0, 255) }\n"
"\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"	border: 1px solid white;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    border : 4px solid;\n"
"	border-color: black;\n"
"	border-radius: 6px;\n"
"	background-color: rgb(0, 255, 183);\n"
"\n"
"}\n"
"\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.radio_mov, 0, 0, 1, 1)

        self.radio_mp4 = QRadioButton(self.groupbox_format)
        self.radio_mp4.setObjectName(u"radio_mp4")
        self.radio_mp4.setStyleSheet(u"QRadioButton {\n"
"	color: rgb(0, 255, 84)}\n"
"\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"	border: 1px solid white;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    border : 4px solid;\n"
"	border-color: black;\n"
"	border-radius: 6px;\n"
"	background-color: rgb(0, 255, 183);\n"
"\n"
"}\n"
"\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.radio_mp4, 1, 0, 1, 1)

        self.radio_mkv = QRadioButton(self.groupbox_format)
        self.radio_mkv.setObjectName(u"radio_mkv")
        self.radio_mkv.setStyleSheet(u"QRadioButton {\n"
"color: rgb(255, 150, 0)\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"	border: 1px solid white;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    border : 4px solid;\n"
"	border-color: black;\n"
"	border-radius: 6px;\n"
"	background-color: rgb(0, 255, 183);\n"
"\n"
"}\n"
"\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.radio_mkv, 2, 0, 1, 1)

        self.radio_avi = QRadioButton(self.groupbox_format)
        self.radio_avi.setObjectName(u"radio_avi")
        self.radio_avi.setStyleSheet(u"QRadioButton {\n"
"	color: rgb(255, 62, 0) }\n"
"\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"	border: 1px solid white;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    border : 4px solid;\n"
"	border-color: black;\n"
"	border-radius: 6px;\n"
"	background-color: rgb(0, 255, 183);\n"
"\n"
"}\n"
"\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.radio_avi, 3, 0, 1, 1)


        self.gridLayout_12.addWidget(self.groupbox_format, 0, 3, 1, 1)

        self.groupbox_video = QGroupBox(self.groupBox_2)
        self.groupbox_video.setObjectName(u"groupbox_video")
        self.groupbox_video.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid #757575;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* margin-top sorgt f\u00fcr einen Abstand zwischen dem Titel und dem Rand */\n"
"	border-color: rgb(246, 245, 244)\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px; /* left verschiebt den Titel etwas nach rechts, damit er nicht direkt am Rand anliegt */\n"
"    padding: 0 3px 0 3px; /* padding gibt dem Titel etwas Platz rundherum */\n"
"}\n"
"")
        self.gridLayout_7 = QGridLayout(self.groupbox_video)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.radio_video_mode = QRadioButton(self.groupbox_video)
        self.radio_video_mode.setObjectName(u"radio_video_mode")
        self.radio_video_mode.setStyleSheet(u"QRadioButton {\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"	border: 1px solid white;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    border : 4px solid;\n"
"	border-color: black;\n"
"	border-radius: 6px;\n"
"	background-color: rgb(0, 255, 183);\n"
"\n"
"}\n"
"\n"
"\n"
"")

        self.gridLayout_7.addWidget(self.radio_video_mode, 0, 0, 1, 1)

        self.radio_music_mode = QRadioButton(self.groupbox_video)
        self.radio_music_mode.setObjectName(u"radio_music_mode")
        self.radio_music_mode.setStyleSheet(u"QRadioButton {\n"
"	color: rgb(0, 255, 250)\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"	border: 1px solid white;\n"
"	border-radius: 5px;\n"
"}\n"
"")

        self.gridLayout_7.addWidget(self.radio_music_mode, 1, 0, 1, 1)


        self.gridLayout_12.addWidget(self.groupbox_video, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_2, 0, 1, 2, 1)

        self.groupbox_downloads = QGroupBox(Widget)
        self.groupbox_downloads.setObjectName(u"groupbox_downloads")
        self.groupbox_downloads.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid #757575;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* margin-top sorgt f\u00fcr einen Abstand zwischen dem Titel und dem Rand */\n"
"	border-color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px; /* left verschiebt den Titel etwas nach rechts, damit er nicht direkt am Rand anliegt */\n"
"    padding: 0 3px 0 3px; /* padding gibt dem Titel etwas Platz rundherum */\n"
"}\n"
"")
        self.gridLayout_11 = QGridLayout(self.groupbox_downloads)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.video_remain_video_label = QLabel(self.groupbox_downloads)
        self.video_remain_video_label.setObjectName(u"video_remain_video_label")
        self.video_remain_video_label.setStyleSheet(u"color: white")

        self.gridLayout_11.addWidget(self.video_remain_video_label, 0, 0, 1, 1)

        self.playlist_remain_vieos_label = QLabel(self.groupbox_downloads)
        self.playlist_remain_vieos_label.setObjectName(u"playlist_remain_vieos_label")
        self.playlist_remain_vieos_label.setStyleSheet(u"color: white")

        self.gridLayout_11.addWidget(self.playlist_remain_vieos_label, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupbox_downloads, 1, 0, 2, 1)

        self.groupBox_3 = QGroupBox(Widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_13 = QGridLayout(self.groupBox_3)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.groupbox_progress_bars = QGroupBox(self.groupBox_3)
        self.groupbox_progress_bars.setObjectName(u"groupbox_progress_bars")
        self.groupbox_progress_bars.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid #757575;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* margin-top sorgt f\u00fcr einen Abstand zwischen dem Titel und dem Rand */\n"
"	border-color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px; /* left verschiebt den Titel etwas nach rechts, damit er nicht direkt am Rand anliegt */\n"
"    padding: 0 3px 0 3px; /* padding gibt dem Titel etwas Platz rundherum */\n"
"}\n"
"")
        self.gridLayout = QGridLayout(self.groupbox_progress_bars)
        self.gridLayout.setObjectName(u"gridLayout")
        self.progressbar_converting_label = QLabel(self.groupbox_progress_bars)
        self.progressbar_converting_label.setObjectName(u"progressbar_converting_label")
        self.progressbar_converting_label.setStyleSheet(u"color: white")

        self.gridLayout.addWidget(self.progressbar_converting_label, 2, 0, 1, 1)

        self.progressbar_playlist = QProgressBar(self.groupbox_progress_bars)
        self.progressbar_playlist.setObjectName(u"progressbar_playlist")
        self.progressbar_playlist.setStyleSheet(u"QProgressBar {\n"
"	background-color: rgb(94, 92, 100);\n"
"	text-align: center;\n"
"	color: rgb(0, 255, 183);\n"
"	border-radius: 12px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(198, 70, 0); /* Gr\u00fcn als Vordergrundfarbe */\n"
"}")
        self.progressbar_playlist.setValue(0)

        self.gridLayout.addWidget(self.progressbar_playlist, 1, 1, 1, 1)

        self.progressbar_converting = QProgressBar(self.groupbox_progress_bars)
        self.progressbar_converting.setObjectName(u"progressbar_converting")
        self.progressbar_converting.setStyleSheet(u"QProgressBar {\n"
"	background-color: rgb(94, 92, 100);\n"
"	text-align: center;\n"
"	color: rgb(153, 193, 241);\n"
"	border-radius: 12px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(192, 28, 40); /* Gr\u00fcn als Vordergrundfarbe */\n"
"}")
        self.progressbar_converting.setMinimum(0)
        self.progressbar_converting.setValue(0)

        self.gridLayout.addWidget(self.progressbar_converting, 2, 1, 1, 1)

        self.progressbar_video = QProgressBar(self.groupbox_progress_bars)
        self.progressbar_video.setObjectName(u"progressbar_video")
        self.progressbar_video.setStyleSheet(u"QProgressBar {\n"
"    background-color: rgb(94, 92, 100);\n"
"	text-align: center;\n"
"	color: rgb(249, 240, 107);\n"
"	border-radius: 12px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(97, 53, 131); /* Gr\u00fcn als Vordergrundfarbe */\n"
"}")
        self.progressbar_video.setValue(0)

        self.gridLayout.addWidget(self.progressbar_video, 0, 1, 1, 1)

        self.progressbar_video_label = QLabel(self.groupbox_progress_bars)
        self.progressbar_video_label.setObjectName(u"progressbar_video_label")
        self.progressbar_video_label.setStyleSheet(u"color: white\n"
"")

        self.gridLayout.addWidget(self.progressbar_video_label, 0, 0, 1, 1)

        self.progressbar_playlist_label = QLabel(self.groupbox_progress_bars)
        self.progressbar_playlist_label.setObjectName(u"progressbar_playlist_label")
        self.progressbar_playlist_label.setStyleSheet(u"color: white")

        self.gridLayout.addWidget(self.progressbar_playlist_label, 1, 0, 1, 1)


        self.gridLayout_13.addWidget(self.groupbox_progress_bars, 0, 1, 1, 1)

        self.groupbox_output = QGroupBox(self.groupBox_3)
        self.groupbox_output.setObjectName(u"groupbox_output")
        self.groupbox_output.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid #757575;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* margin-top sorgt f\u00fcr einen Abstand zwischen dem Titel und dem Rand */\n"
"	border-color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px; /* left verschiebt den Titel etwas nach rechts, damit er nicht direkt am Rand anliegt */\n"
"    padding: 0 3px 0 3px; /* padding gibt dem Titel etwas Platz rundherum */\n"
"}\n"
"")
        self.gridLayout_6 = QGridLayout(self.groupbox_output)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.output_music_label = QLabel(self.groupbox_output)
        self.output_music_label.setObjectName(u"output_music_label")
        self.output_music_label.setStyleSheet(u"color: white")

        self.gridLayout_6.addWidget(self.output_music_label, 1, 0, 1, 1)

        self.output_thumbnail_label = QLabel(self.groupbox_output)
        self.output_thumbnail_label.setObjectName(u"output_thumbnail_label")
        self.output_thumbnail_label.setStyleSheet(u"color: white")

        self.gridLayout_6.addWidget(self.output_thumbnail_label, 0, 0, 1, 1)

        self.output_video_label = QLabel(self.groupbox_output)
        self.output_video_label.setObjectName(u"output_video_label")
        self.output_video_label.setStyleSheet(u"color: white")

        self.gridLayout_6.addWidget(self.output_video_label, 2, 0, 1, 1)

        self.output_thumbnail_lineedit = QLineEdit(self.groupbox_output)
        self.output_thumbnail_lineedit.setObjectName(u"output_thumbnail_lineedit")
        self.output_thumbnail_lineedit.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #757575;\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    background: rgb(94, 92, 100);  /* setzt den Hintergrund auf Schwarz */\n"
"    color: #FFFFFF;  /* setzt die Textfarbe auf Wei\u00df */\n"
"    font-size: 16px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #4a90d9;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background: #444444;  /* setzt den Hintergrund auf ein dunkles Grau, wenn das QLineEdit deaktiviert ist */\n"
"    color: #aaaaaa;  /* setzt die Textfarbe auf ein helles Grau, wenn das QLineEdit deaktiviert ist */\n"
"    border-color: #aaaaaa;\n"
"}")

        self.gridLayout_6.addWidget(self.output_thumbnail_lineedit, 0, 1, 1, 1)

        self.output_video_lineedit = QLineEdit(self.groupbox_output)
        self.output_video_lineedit.setObjectName(u"output_video_lineedit")
        self.output_video_lineedit.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #757575;\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    background: rgb(94, 92, 100);  /* setzt den Hintergrund auf Schwarz */\n"
"    color: #FFFFFF;  /* setzt die Textfarbe auf Wei\u00df */\n"
"    font-size: 16px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #4a90d9;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background: #444444;  /* setzt den Hintergrund auf ein dunkles Grau, wenn das QLineEdit deaktiviert ist */\n"
"    color: #aaaaaa;  /* setzt die Textfarbe auf ein helles Grau, wenn das QLineEdit deaktiviert ist */\n"
"    border-color: #aaaaaa;\n"
"}")

        self.gridLayout_6.addWidget(self.output_video_lineedit, 2, 1, 1, 1)

        self.output_music_lineedit = QLineEdit(self.groupbox_output)
        self.output_music_lineedit.setObjectName(u"output_music_lineedit")
        self.output_music_lineedit.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #757575;\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    background: rgb(94, 92, 100);  /* setzt den Hintergrund auf Schwarz */\n"
"    color: #FFFFFF;  /* setzt die Textfarbe auf Wei\u00df */\n"
"    font-size: 16px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #4a90d9;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background: #444444;  /* setzt den Hintergrund auf ein dunkles Grau, wenn das QLineEdit deaktiviert ist */\n"
"    color: #aaaaaa;  /* setzt die Textfarbe auf ein helles Grau, wenn das QLineEdit deaktiviert ist */\n"
"    border-color: #aaaaaa;\n"
"}")

        self.gridLayout_6.addWidget(self.output_music_lineedit, 1, 1, 1, 1)


        self.gridLayout_13.addWidget(self.groupbox_output, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_3, 2, 1, 2, 2)

        self.license_text = QTextBrowser(Widget)
        self.license_text.setObjectName(u"license_text")
        self.license_text.setStyleSheet(u"QTextBrowser {\n"
"    border: 2px solid #757575;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* margin-top sorgt f\u00fcr einen Abstand zwischen dem Titel und dem Rand */\n"
"	border-color: rgb(255, 255, 255)\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.license_text, 3, 0, 1, 1)

        self.textBrowser = QTextBrowser(Widget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout_4.addWidget(self.textBrowser, 0, 2, 2, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"VidFetch 1.0 :: License LGPLv3     Source Code: https://github.com/VidFetch     ", None))
        self.groupbox_urls.setTitle("")
        self.playlist_start_button.setText(QCoreApplication.translate("Widget", u"Downlaod", None))
        self.video_thumbnail_copy_button.setText(QCoreApplication.translate("Widget", u"Copy", None))
        self.playlist_url_label.setText(QCoreApplication.translate("Widget", u"Playlist URL:", None))
        self.video_download_start_button.setText(QCoreApplication.translate("Widget", u"Download", None))
        self.video_thumbnail_label.setText(QCoreApplication.translate("Widget", u"Thumbnail:", None))
        self.video_start_prep_button.setText(QCoreApplication.translate("Widget", u"Start Prep", None))
        self.video_url_label.setText(QCoreApplication.translate("Widget", u"Video URL:", None))
        self.groupBox_2.setTitle("")
        self.groupbox_resolutions.setTitle("")
        self.radio_144p.setText(QCoreApplication.translate("Widget", u"144p SD", None))
        self.radio_1080p.setText(QCoreApplication.translate("Widget", u"1080p F-HD", None))
        self.radio_240p.setText(QCoreApplication.translate("Widget", u"240p SD", None))
        self.radio_1440p.setText(QCoreApplication.translate("Widget", u"1440p 2K", None))
        self.radio_360p.setText(QCoreApplication.translate("Widget", u"360p SD", None))
        self.radio_2160p.setText(QCoreApplication.translate("Widget", u"2160p 4K", None))
        self.radio_480p.setText(QCoreApplication.translate("Widget", u"480p SD", None))
        self.radio_4320p.setText(QCoreApplication.translate("Widget", u"4320p 8K", None))
        self.radio_720p.setText(QCoreApplication.translate("Widget", u"720p HD", None))
        self.group_box_music.setTitle("")
        self.radio_mp3.setText(QCoreApplication.translate("Widget", u"MP3 Format", None))
        self.radio_wav.setText(QCoreApplication.translate("Widget", u"WAV Format", None))
        self.radio_m4a.setText(QCoreApplication.translate("Widget", u"M4A Format", None))
        self.radio_opus.setText(QCoreApplication.translate("Widget", u"OPUS Format", None))
        self.groupbox_format.setTitle("")
        self.radio_mov.setText(QCoreApplication.translate("Widget", u"MOV Format", None))
        self.radio_mp4.setText(QCoreApplication.translate("Widget", u"MP4 Format", None))
        self.radio_mkv.setText(QCoreApplication.translate("Widget", u"MKV Format", None))
        self.radio_avi.setText(QCoreApplication.translate("Widget", u"AVI Format", None))
        self.groupbox_video.setTitle("")
        self.radio_video_mode.setText(QCoreApplication.translate("Widget", u"Video Mode", None))
        self.radio_music_mode.setText(QCoreApplication.translate("Widget", u"Music Mode", None))
        self.groupbox_downloads.setTitle("")
        self.video_remain_video_label.setText(QCoreApplication.translate("Widget", u"Video:  Downloaded: / of / Videos", None))
        self.playlist_remain_vieos_label.setText(QCoreApplication.translate("Widget", u"Playlist:  Downloaded: / of / Videos", None))
        self.groupBox_3.setTitle("")
        self.groupbox_progress_bars.setTitle("")
        self.progressbar_converting_label.setText(QCoreApplication.translate("Widget", u"Converting:", None))
        self.progressbar_video_label.setText(QCoreApplication.translate("Widget", u"Video Download:", None))
        self.progressbar_playlist_label.setText(QCoreApplication.translate("Widget", u"Playlist Download:", None))
        self.groupbox_output.setTitle("")
        self.output_music_label.setText(QCoreApplication.translate("Widget", u"Music output:", None))
        self.output_thumbnail_label.setText(QCoreApplication.translate("Widget", u"Thumbnails:", None))
        self.output_video_label.setText(QCoreApplication.translate("Widget", u"Video output:", None))
        self.output_thumbnail_lineedit.setText(QCoreApplication.translate("Widget", u"output/thumb/", None))
        self.output_video_lineedit.setText(QCoreApplication.translate("Widget", u"output/video/", None))
        self.output_music_lineedit.setText(QCoreApplication.translate("Widget", u"output/music/", None))
        self.license_text.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; color:#ffffff;\">Author:    EchterAlsFake</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; color:#ffffff;\">Version:   1.0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; color:#ffffff;\">Website:  https://github.com/echteralsfake/VidFetch</span></p>\n"
"<p style=\" margin-top:0px"
                        "; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; color:#ffffff;\">License:   LGPLv3</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Ubuntu'; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; color:#ffffff;\">I am using Qt for the Graphical User Interface. I don't have a Qt License, so this Project is Open Source. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Ubuntu'; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'"
                        "Ubuntu'; color:#ffffff;\">You are free to modify, change and distribute the program.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Ubuntu'; color:#ffffff;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; color:#ffffff;\">Credits:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Ubuntu'; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; color:#ffff"
                        "ff;\">Thanks to Tabnine. One of the best code complete plugins I know.  If you want, buy their subscription, it's fucking awesome.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Ubuntu'; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; color:#ffffff;\">Thanks to ChatGPT. It helped a lot and I didn't understand shit when it comes to working with threads and progress bars. Without ChatGPT this project wouldn't be possible.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Ubuntu'; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
                        "<span style=\" font-family:'Ubuntu'; color:#ffffff;\">Thanks to Pytube, they created the Python Library, which I am downloading the videos with. Creating all that by myself would take years.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Ubuntu'; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; color:#ffffff;\">Thanks to ffmpeg for their great and open source video converting tool.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Ubuntu'; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; col"
                        "or:#ffffff;\">Thanks to @slhck who created the pip package: </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Ubuntu'; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; color:#ffffff;\">ffmpeg-progress-yield  </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Ubuntu'; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; color:#ffffff;\"> It's the only way that I found, where I can create a progress bar for the converting process.  I searched like 6 hours and my mental health was at the end, but thi"
                        "s guy just made my day :) </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Ubuntu'; color:#ffffff;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Ubuntu'; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; color:#ffffff;\">Thanks to all contributors, or the ones, that will be a contributor in the future :) </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; color:#ffffff;\"><br />You can support me here:  https://paypal.me/EchterAlsFake</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; marg"
                        "in-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Ubuntu'; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; color:#ffffff;\">Thanks :) </span></p></body></html>", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Please read the following:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Video URL:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent"
                        ":0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">You need to first click on the &quot;start Prep&quot; Button in order to get all available</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">resolutions, that the video supports. Then you can choose your Video and Audio Format and click on the &quot;Download&quot; Button.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Playlists will be downloaded with max Quality if video Mode is selected. Otherwise if Music Mode is"
                        " selected every video will be downloaded as audio file.</span></p></body></html>", None))
    # retranslateUi

