# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VidFetch.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QGroupBox,
    QHeaderView, QLabel, QLineEdit, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QTreeWidget,
    QTreeWidgetItem, QWidget)

class Ui_VidFetch(object):
    def setupUi(self, VidFetch):
        if not VidFetch.objectName():
            VidFetch.setObjectName(u"VidFetch")
        VidFetch.resize(1264, 528)
        VidFetch.setStyleSheet(u"QWidget {\n"
"color: white;\n"
"background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 2px solid #757575;\n"
"    border-radius: 12px;\n"
"    padding: 0 8px;\n"
"    background: rgb(94, 92, 100); \n"
"    color: #FFFFFF; \n"
"    font-size: 16px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: rgb(107, 0, 255)\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background: #444444;  \n"
"    color: #aaaaaa; \n"
"    border-color: #aaaaaa;\n"
"}\n"
"\n"
"QPushButton {\n"
"        background-color: #5a2a82;\n"
"        color: #ffffff; \n"
"        border: none;\n"
"        border-radius: 10px;\n"
"        padding: 5px 20px; \n"
"        font-size: 12px;\n"
"        outline: none;\n"
"    }\n"
"    \n"
"    QPushButton:hover {\n"
"        background-color: #7b3ca3; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: #481f61; \n"
"    }\n"
"\n"
"    QPushButton:disabled {\n"
"        background-color: #3f1d4d; \n"
"        color: #8a7b9a; \n"
"  "
                        "  }\n"
"\n"
"QProgressBar {\n"
"    border: 2px solid #5a2a82;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    background-color: rgb(94, 92, 100);\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #5a2a82;\n"
"    width: 10px; /* You can adjust this to change the width of the 'chunk' */\n"
"}\n"
"QRadioButton {\n"
"	color: (255,255,255)}\n"
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
"QSlider::groove:horizontal {\n"
"    border: 1px solid #5a2a82;\n"
"    height: 8px;\n"
"    background: #e0e0e0;\n"
"    margin: 0px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #5a2a82;\n"
"    border: 1px solid #5a2a82;\n"
"    width: 18px;\n"
"    margin: -6px 0;\n"
"    border-radius: 9px;\n"
"}\n"
"\n"
"QS"
                        "lider::add-page:horizontal {\n"
"    background: #e0e0e0;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: #5a2a82;\n"
"}\n"
"\n"
"QTreeWidget {\n"
"    background-color: rgb(94, 94, 94);\n"
"    color: white;\n"
"}\n"
"\n"
"QTreeWidget::header {\n"
"    background-color: rgb(94, 94, 94);\n"
"    color: black; /* Set color to black or any other color that you prefer for the header text */\n"
"}\n"
"")
        self.gridLayout_4 = QGridLayout(VidFetch)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.button_start_file = QPushButton(VidFetch)
        self.button_start_file.setObjectName(u"button_start_file")

        self.gridLayout.addWidget(self.button_start_file, 2, 2, 1, 1)

        self.label_file = QLabel(VidFetch)
        self.label_file.setObjectName(u"label_file")

        self.gridLayout.addWidget(self.label_file, 2, 0, 1, 1)

        self.label_video = QLabel(VidFetch)
        self.label_video.setObjectName(u"label_video")

        self.gridLayout.addWidget(self.label_video, 0, 0, 1, 1)

        self.lineedit_video_url = QLineEdit(VidFetch)
        self.lineedit_video_url.setObjectName(u"lineedit_video_url")

        self.gridLayout.addWidget(self.lineedit_video_url, 0, 1, 1, 1)

        self.button_start_playlist = QPushButton(VidFetch)
        self.button_start_playlist.setObjectName(u"button_start_playlist")

        self.gridLayout.addWidget(self.button_start_playlist, 1, 2, 1, 1)

        self.lineedit_file = QLineEdit(VidFetch)
        self.lineedit_file.setObjectName(u"lineedit_file")

        self.gridLayout.addWidget(self.lineedit_file, 2, 1, 1, 1)

        self.lineedit_playlist_url = QLineEdit(VidFetch)
        self.lineedit_playlist_url.setObjectName(u"lineedit_playlist_url")

        self.gridLayout.addWidget(self.lineedit_playlist_url, 1, 1, 1, 1)

        self.label_playlist = QLabel(VidFetch)
        self.label_playlist.setObjectName(u"label_playlist")

        self.gridLayout.addWidget(self.label_playlist, 1, 0, 1, 1)

        self.button_start_video = QPushButton(VidFetch)
        self.button_start_video.setObjectName(u"button_start_video")

        self.gridLayout.addWidget(self.button_start_video, 0, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.tree_widget = QTreeWidget(VidFetch)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.tree_widget.setHeaderItem(__qtreewidgetitem)
        self.tree_widget.setObjectName(u"tree_widget")
        self.tree_widget.setStyleSheet(u"background-image: url(\"graphics/VidFetch.jpg\");")

        self.gridLayout_4.addWidget(self.tree_widget, 1, 0, 1, 1)

        self.groupbox_settings = QGroupBox(VidFetch)
        self.groupbox_settings.setObjectName(u"groupbox_settings")
        self.gridLayout_3 = QGridLayout(self.groupbox_settings)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.radio_quality_ask = QRadioButton(self.groupbox_settings)
        self.radio_quality_ask.setObjectName(u"radio_quality_ask")
        self.radio_quality_ask.setChecked(False)

        self.gridLayout_2.addWidget(self.radio_quality_ask, 1, 1, 1, 1)

        self.radio_quality_highest = QRadioButton(self.groupbox_settings)
        self.radio_quality_highest.setObjectName(u"radio_quality_highest")
        self.radio_quality_highest.setChecked(False)

        self.gridLayout_2.addWidget(self.radio_quality_highest, 1, 2, 1, 1)

        self.radio_mode_music = QRadioButton(self.groupbox_settings)
        self.radio_mode_music.setObjectName(u"radio_mode_music")
        self.radio_mode_music.setChecked(False)

        self.gridLayout_2.addWidget(self.radio_mode_music, 0, 1, 1, 1)

        self.radio_mode_video = QRadioButton(self.groupbox_settings)
        self.radio_mode_video.setObjectName(u"radio_mode_video")

        self.gridLayout_2.addWidget(self.radio_mode_video, 0, 2, 1, 1)

        self.radio_codec_aac = QRadioButton(self.groupbox_settings)
        self.radio_codec_aac.setObjectName(u"radio_codec_aac")
        self.radio_codec_aac.setChecked(True)

        self.gridLayout_2.addWidget(self.radio_codec_aac, 2, 1, 1, 1)

        self.radio_codec_mp3 = QRadioButton(self.groupbox_settings)
        self.radio_codec_mp3.setObjectName(u"radio_codec_mp3")

        self.gridLayout_2.addWidget(self.radio_codec_mp3, 2, 2, 1, 1)

        self.label_quality = QLabel(self.groupbox_settings)
        self.label_quality.setObjectName(u"label_quality")

        self.gridLayout_2.addWidget(self.label_quality, 1, 0, 1, 1)

        self.label_output_path = QLabel(self.groupbox_settings)
        self.label_output_path.setObjectName(u"label_output_path")

        self.gridLayout_2.addWidget(self.label_output_path, 3, 0, 1, 1)

        self.lineedit_output_path = QLineEdit(self.groupbox_settings)
        self.lineedit_output_path.setObjectName(u"lineedit_output_path")

        self.gridLayout_2.addWidget(self.lineedit_output_path, 3, 1, 1, 2)

        self.label_download_mode = QLabel(self.groupbox_settings)
        self.label_download_mode.setObjectName(u"label_download_mode")

        self.gridLayout_2.addWidget(self.label_download_mode, 0, 0, 1, 1)

        self.label_music_codec = QLabel(self.groupbox_settings)
        self.label_music_codec.setObjectName(u"label_music_codec")

        self.gridLayout_2.addWidget(self.label_music_codec, 2, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 2)

        self.button_settings_save = QPushButton(self.groupbox_settings)
        self.button_settings_save.setObjectName(u"button_settings_save")

        self.gridLayout_3.addWidget(self.button_settings_save, 1, 0, 1, 2)


        self.gridLayout_4.addWidget(self.groupbox_settings, 2, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.progressbar_download = QProgressBar(VidFetch)
        self.progressbar_download.setObjectName(u"progressbar_download")
        self.progressbar_download.setValue(0)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.progressbar_download)

        self.label_downloading = QLabel(VidFetch)
        self.label_downloading.setObjectName(u"label_downloading")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_downloading)

        self.label_converting = QLabel(VidFetch)
        self.label_converting.setObjectName(u"label_converting")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_converting)

        self.progressbar_converting = QProgressBar(VidFetch)
        self.progressbar_converting.setObjectName(u"progressbar_converting")
        self.progressbar_converting.setValue(0)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.progressbar_converting)

        self.progressbar_processing = QProgressBar(VidFetch)
        self.progressbar_processing.setObjectName(u"progressbar_processing")
        self.progressbar_processing.setValue(0)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.progressbar_processing)

        self.label_processing = QLabel(VidFetch)
        self.label_processing.setObjectName(u"label_processing")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_processing)


        self.gridLayout_4.addLayout(self.formLayout, 3, 0, 1, 1)


        self.retranslateUi(VidFetch)

        QMetaObject.connectSlotsByName(VidFetch)
    # setupUi

    def retranslateUi(self, VidFetch):
        VidFetch.setWindowTitle(QCoreApplication.translate("VidFetch", u"VidFetch v1.0  (GPLv3)", None))
        self.button_start_file.setText(QCoreApplication.translate("VidFetch", u"Start", None))
        self.label_file.setText(QCoreApplication.translate("VidFetch", u"File:", None))
        self.label_video.setText(QCoreApplication.translate("VidFetch", u"Video:", None))
        self.lineedit_video_url.setPlaceholderText(QCoreApplication.translate("VidFetch", u"Enter YouTube video URL", None))
        self.button_start_playlist.setText(QCoreApplication.translate("VidFetch", u"Start", None))
        self.lineedit_file.setPlaceholderText(QCoreApplication.translate("VidFetch", u"Enter file with URLs   (Separated by white spaces)", None))
        self.lineedit_playlist_url.setPlaceholderText(QCoreApplication.translate("VidFetch", u"Enter YouTube Playlist URL", None))
        self.label_playlist.setText(QCoreApplication.translate("VidFetch", u"Playlist:", None))
        self.button_start_video.setText(QCoreApplication.translate("VidFetch", u"Start", None))
        self.groupbox_settings.setTitle(QCoreApplication.translate("VidFetch", u"Settings:", None))
        self.radio_quality_ask.setText(QCoreApplication.translate("VidFetch", u"Ask everytime", None))
        self.radio_quality_highest.setText(QCoreApplication.translate("VidFetch", u"Highest available", None))
        self.radio_mode_music.setText(QCoreApplication.translate("VidFetch", u"Music", None))
        self.radio_mode_video.setText(QCoreApplication.translate("VidFetch", u"Video", None))
        self.radio_codec_aac.setText(QCoreApplication.translate("VidFetch", u"AAC     (recommended for Apple devices)", None))
        self.radio_codec_mp3.setText(QCoreApplication.translate("VidFetch", u"MP3", None))
        self.label_quality.setText(QCoreApplication.translate("VidFetch", u"Quality:", None))
        self.label_output_path.setText(QCoreApplication.translate("VidFetch", u"Output path:", None))
        self.label_download_mode.setText(QCoreApplication.translate("VidFetch", u"Download Mode: ", None))
        self.label_music_codec.setText(QCoreApplication.translate("VidFetch", u"Music codec", None))
        self.button_settings_save.setText(QCoreApplication.translate("VidFetch", u"Save", None))
        self.label_downloading.setText(QCoreApplication.translate("VidFetch", u"Downloading:", None))
        self.label_converting.setText(QCoreApplication.translate("VidFetch", u"Converting:", None))
        self.label_processing.setText(QCoreApplication.translate("VidFetch", u"Processing:", None))
    # retranslateUi

