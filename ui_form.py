# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGraphicsView, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QProgressBar, QPushButton, QRadioButton, QSizePolicy,
    QTextBrowser, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1782, 719)
        self.gridLayout_14 = QGridLayout(Widget)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.groupbox_urls = QGroupBox(Widget)
        self.groupbox_urls.setObjectName(u"groupbox_urls")
        self.gridLayout_10 = QGridLayout(self.groupbox_urls)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.video_thumbnail_copy_button = QPushButton(self.groupbox_urls)
        self.video_thumbnail_copy_button.setObjectName(u"video_thumbnail_copy_button")

        self.gridLayout_10.addWidget(self.video_thumbnail_copy_button, 2, 2, 1, 1)

        self.video_thumbnail_label = QLabel(self.groupbox_urls)
        self.video_thumbnail_label.setObjectName(u"video_thumbnail_label")

        self.gridLayout_10.addWidget(self.video_thumbnail_label, 2, 0, 1, 1)

        self.playlist_url_label = QLabel(self.groupbox_urls)
        self.playlist_url_label.setObjectName(u"playlist_url_label")

        self.gridLayout_10.addWidget(self.playlist_url_label, 1, 0, 1, 1)

        self.playlist_url_lineedit = QLineEdit(self.groupbox_urls)
        self.playlist_url_lineedit.setObjectName(u"playlist_url_lineedit")
        self.playlist_url_lineedit.setStyleSheet(u"QLineEdit: { border: 2px rgb(192, 97, 203) !mportant; }")
        self.playlist_url_lineedit.setReadOnly(False)

        self.gridLayout_10.addWidget(self.playlist_url_lineedit, 1, 1, 1, 1)

        self.video_url_lineedit = QLineEdit(self.groupbox_urls)
        self.video_url_lineedit.setObjectName(u"video_url_lineedit")
        self.video_url_lineedit.setStyleSheet(u"QLineEdit: { border: 2px rgb(192, 97, 203); }")
        self.video_url_lineedit.setReadOnly(False)

        self.gridLayout_10.addWidget(self.video_url_lineedit, 0, 1, 1, 1)

        self.video_url_label = QLabel(self.groupbox_urls)
        self.video_url_label.setObjectName(u"video_url_label")

        self.gridLayout_10.addWidget(self.video_url_label, 0, 0, 1, 1)

        self.video_thumbnail_lineedit = QLineEdit(self.groupbox_urls)
        self.video_thumbnail_lineedit.setObjectName(u"video_thumbnail_lineedit")
        self.video_thumbnail_lineedit.setStyleSheet(u"QLineEdit: { border: 2px solid gray; }")
        self.video_thumbnail_lineedit.setReadOnly(True)

        self.gridLayout_10.addWidget(self.video_thumbnail_lineedit, 2, 1, 1, 1)

        self.playlist_start_button = QPushButton(self.groupbox_urls)
        self.playlist_start_button.setObjectName(u"playlist_start_button")
        self.playlist_start_button.setStyleSheet(u"")

        self.gridLayout_10.addWidget(self.playlist_start_button, 1, 2, 1, 1)

        self.video_start_prep_button = QPushButton(self.groupbox_urls)
        self.video_start_prep_button.setObjectName(u"video_start_prep_button")
        self.video_start_prep_button.setStyleSheet(u"")

        self.gridLayout_10.addWidget(self.video_start_prep_button, 0, 2, 1, 1)

        self.video_download_start_button = QPushButton(self.groupbox_urls)
        self.video_download_start_button.setObjectName(u"video_download_start_button")

        self.gridLayout_10.addWidget(self.video_download_start_button, 0, 3, 1, 1)


        self.gridLayout_14.addWidget(self.groupbox_urls, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(Widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_12 = QGridLayout(self.groupBox_2)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.groupbox_format = QGroupBox(self.groupBox_2)
        self.groupbox_format.setObjectName(u"groupbox_format")
        self.gridLayout_3 = QGridLayout(self.groupbox_format)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.radio_mov = QRadioButton(self.groupbox_format)
        self.radio_mov.setObjectName(u"radio_mov")

        self.gridLayout_3.addWidget(self.radio_mov, 0, 0, 1, 1)

        self.radio_mp4 = QRadioButton(self.groupbox_format)
        self.radio_mp4.setObjectName(u"radio_mp4")

        self.gridLayout_3.addWidget(self.radio_mp4, 1, 0, 1, 1)

        self.radio_mkv = QRadioButton(self.groupbox_format)
        self.radio_mkv.setObjectName(u"radio_mkv")

        self.gridLayout_3.addWidget(self.radio_mkv, 2, 0, 1, 1)

        self.radio_avi = QRadioButton(self.groupbox_format)
        self.radio_avi.setObjectName(u"radio_avi")

        self.gridLayout_3.addWidget(self.radio_avi, 3, 0, 1, 1)


        self.gridLayout_12.addWidget(self.groupbox_format, 0, 3, 1, 1)

        self.group_box_music = QGroupBox(self.groupBox_2)
        self.group_box_music.setObjectName(u"group_box_music")
        self.gridLayout_2 = QGridLayout(self.group_box_music)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.radio_opus = QRadioButton(self.group_box_music)
        self.radio_opus.setObjectName(u"radio_opus")

        self.gridLayout_2.addWidget(self.radio_opus, 2, 0, 1, 1)

        self.radio_m4a = QRadioButton(self.group_box_music)
        self.radio_m4a.setObjectName(u"radio_m4a")

        self.gridLayout_2.addWidget(self.radio_m4a, 1, 0, 1, 1)

        self.radio_wav = QRadioButton(self.group_box_music)
        self.radio_wav.setObjectName(u"radio_wav")

        self.gridLayout_2.addWidget(self.radio_wav, 3, 0, 1, 1)

        self.radio_mp3 = QRadioButton(self.group_box_music)
        self.radio_mp3.setObjectName(u"radio_mp3")

        self.gridLayout_2.addWidget(self.radio_mp3, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.group_box_music, 0, 4, 1, 1)

        self.groupbox_resolutions = QGroupBox(self.groupBox_2)
        self.groupbox_resolutions.setObjectName(u"groupbox_resolutions")
        self.gridLayout_8 = QGridLayout(self.groupbox_resolutions)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.radio_144p = QRadioButton(self.groupbox_resolutions)
        self.radio_144p.setObjectName(u"radio_144p")

        self.gridLayout_8.addWidget(self.radio_144p, 0, 0, 1, 1)

        self.radio_1080p = QRadioButton(self.groupbox_resolutions)
        self.radio_1080p.setObjectName(u"radio_1080p")

        self.gridLayout_8.addWidget(self.radio_1080p, 0, 1, 1, 1)

        self.radio_240p = QRadioButton(self.groupbox_resolutions)
        self.radio_240p.setObjectName(u"radio_240p")

        self.gridLayout_8.addWidget(self.radio_240p, 1, 0, 1, 1)

        self.radio_1440p = QRadioButton(self.groupbox_resolutions)
        self.radio_1440p.setObjectName(u"radio_1440p")

        self.gridLayout_8.addWidget(self.radio_1440p, 1, 1, 1, 1)

        self.radio_360p = QRadioButton(self.groupbox_resolutions)
        self.radio_360p.setObjectName(u"radio_360p")

        self.gridLayout_8.addWidget(self.radio_360p, 2, 0, 1, 1)

        self.radio_2160p = QRadioButton(self.groupbox_resolutions)
        self.radio_2160p.setObjectName(u"radio_2160p")

        self.gridLayout_8.addWidget(self.radio_2160p, 2, 1, 1, 1)

        self.radio_480p = QRadioButton(self.groupbox_resolutions)
        self.radio_480p.setObjectName(u"radio_480p")

        self.gridLayout_8.addWidget(self.radio_480p, 3, 0, 1, 1)

        self.radio_4320p = QRadioButton(self.groupbox_resolutions)
        self.radio_4320p.setObjectName(u"radio_4320p")

        self.gridLayout_8.addWidget(self.radio_4320p, 3, 1, 1, 1)

        self.radio_720p = QRadioButton(self.groupbox_resolutions)
        self.radio_720p.setObjectName(u"radio_720p")

        self.gridLayout_8.addWidget(self.radio_720p, 4, 0, 1, 1)


        self.gridLayout_12.addWidget(self.groupbox_resolutions, 0, 2, 1, 1)

        self.groupbox_video = QGroupBox(self.groupBox_2)
        self.groupbox_video.setObjectName(u"groupbox_video")
        self.gridLayout_7 = QGridLayout(self.groupbox_video)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.radio_interactive = QRadioButton(self.groupbox_video)
        self.radio_interactive.setObjectName(u"radio_interactive")

        self.gridLayout_7.addWidget(self.radio_interactive, 0, 0, 1, 1)

        self.radio_video_only = QRadioButton(self.groupbox_video)
        self.radio_video_only.setObjectName(u"radio_video_only")

        self.gridLayout_7.addWidget(self.radio_video_only, 1, 0, 1, 1)

        self.radio_video_mode = QRadioButton(self.groupbox_video)
        self.radio_video_mode.setObjectName(u"radio_video_mode")

        self.gridLayout_7.addWidget(self.radio_video_mode, 2, 0, 1, 1)

        self.radio_music_mode = QRadioButton(self.groupbox_video)
        self.radio_music_mode.setObjectName(u"radio_music_mode")

        self.gridLayout_7.addWidget(self.radio_music_mode, 3, 0, 1, 1)


        self.gridLayout_12.addWidget(self.groupbox_video, 0, 1, 1, 1)


        self.gridLayout_14.addWidget(self.groupBox_2, 0, 1, 3, 1)

        self.groupbox_downloads = QGroupBox(Widget)
        self.groupbox_downloads.setObjectName(u"groupbox_downloads")
        self.gridLayout_11 = QGridLayout(self.groupbox_downloads)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.video_remain_video_label = QLabel(self.groupbox_downloads)
        self.video_remain_video_label.setObjectName(u"video_remain_video_label")

        self.gridLayout_11.addWidget(self.video_remain_video_label, 0, 0, 1, 1)

        self.playlist_remain_vieos_label = QLabel(self.groupbox_downloads)
        self.playlist_remain_vieos_label.setObjectName(u"playlist_remain_vieos_label")

        self.gridLayout_11.addWidget(self.playlist_remain_vieos_label, 1, 0, 1, 1)


        self.gridLayout_14.addWidget(self.groupbox_downloads, 1, 0, 1, 1)

        self.groupbox_metadata = QGroupBox(Widget)
        self.groupbox_metadata.setObjectName(u"groupbox_metadata")
        self.gridLayout_5 = QGridLayout(self.groupbox_metadata)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.video_graphics_view = QGraphicsView(self.groupbox_metadata)
        self.video_graphics_view.setObjectName(u"video_graphics_view")

        self.gridLayout_5.addWidget(self.video_graphics_view, 1, 3, 9, 1)

        self.hLayout_filesize = QHBoxLayout()
        self.hLayout_filesize.setObjectName(u"hLayout_filesize")
        self.metadata_filesize_label = QLabel(self.groupbox_metadata)
        self.metadata_filesize_label.setObjectName(u"metadata_filesize_label")

        self.hLayout_filesize.addWidget(self.metadata_filesize_label)

        self.metadata_filesize_lineedit = QLineEdit(self.groupbox_metadata)
        self.metadata_filesize_lineedit.setObjectName(u"metadata_filesize_lineedit")
        self.metadata_filesize_lineedit.setReadOnly(True)

        self.hLayout_filesize.addWidget(self.metadata_filesize_lineedit)


        self.gridLayout_5.addLayout(self.hLayout_filesize, 6, 0, 1, 3)

        self.hLayout_fps = QHBoxLayout()
        self.hLayout_fps.setObjectName(u"hLayout_fps")
        self.metadata_fps_label = QLabel(self.groupbox_metadata)
        self.metadata_fps_label.setObjectName(u"metadata_fps_label")

        self.hLayout_fps.addWidget(self.metadata_fps_label)

        self.metadata_fps_lineedit = QLineEdit(self.groupbox_metadata)
        self.metadata_fps_lineedit.setObjectName(u"metadata_fps_lineedit")
        self.metadata_fps_lineedit.setReadOnly(True)

        self.hLayout_fps.addWidget(self.metadata_fps_lineedit)


        self.gridLayout_5.addLayout(self.hLayout_fps, 2, 0, 1, 3)

        self.hLayout_views = QHBoxLayout()
        self.hLayout_views.setObjectName(u"hLayout_views")
        self.metadata_views_label = QLabel(self.groupbox_metadata)
        self.metadata_views_label.setObjectName(u"metadata_views_label")

        self.hLayout_views.addWidget(self.metadata_views_label)

        self.metadata_views_lineedit = QLineEdit(self.groupbox_metadata)
        self.metadata_views_lineedit.setObjectName(u"metadata_views_lineedit")
        self.metadata_views_lineedit.setReadOnly(True)

        self.hLayout_views.addWidget(self.metadata_views_lineedit)


        self.gridLayout_5.addLayout(self.hLayout_views, 8, 0, 1, 3)

        self.metadata_thumbnail_label = QLabel(self.groupbox_metadata)
        self.metadata_thumbnail_label.setObjectName(u"metadata_thumbnail_label")

        self.gridLayout_5.addWidget(self.metadata_thumbnail_label, 0, 3, 1, 1)

        self.hLayout_hdr = QHBoxLayout()
        self.hLayout_hdr.setObjectName(u"hLayout_hdr")
        self.metadata_hdr_label = QLabel(self.groupbox_metadata)
        self.metadata_hdr_label.setObjectName(u"metadata_hdr_label")

        self.hLayout_hdr.addWidget(self.metadata_hdr_label)

        self.metadata_hdr_lineedit = QLineEdit(self.groupbox_metadata)
        self.metadata_hdr_lineedit.setObjectName(u"metadata_hdr_lineedit")
        self.metadata_hdr_lineedit.setReadOnly(True)

        self.hLayout_hdr.addWidget(self.metadata_hdr_lineedit)


        self.gridLayout_5.addLayout(self.hLayout_hdr, 9, 0, 1, 3)

        self.hLayout_resolution = QHBoxLayout()
        self.hLayout_resolution.setObjectName(u"hLayout_resolution")

        self.gridLayout_5.addLayout(self.hLayout_resolution, 3, 0, 2, 3)

        self.hLayout_ = QHBoxLayout()
        self.hLayout_.setObjectName(u"hLayout_")
        self.metadata_title_label = QLabel(self.groupbox_metadata)
        self.metadata_title_label.setObjectName(u"metadata_title_label")

        self.hLayout_.addWidget(self.metadata_title_label)

        self.metadata_title_lineedit = QLineEdit(self.groupbox_metadata)
        self.metadata_title_lineedit.setObjectName(u"metadata_title_lineedit")
        self.metadata_title_lineedit.setReadOnly(True)

        self.hLayout_.addWidget(self.metadata_title_lineedit)


        self.gridLayout_5.addLayout(self.hLayout_, 1, 0, 1, 3)

        self.hLayout_bitrate = QHBoxLayout()
        self.hLayout_bitrate.setObjectName(u"hLayout_bitrate")
        self.metadata_bitrate_label = QLabel(self.groupbox_metadata)
        self.metadata_bitrate_label.setObjectName(u"metadata_bitrate_label")

        self.hLayout_bitrate.addWidget(self.metadata_bitrate_label)

        self.metadata_bitrate_lineedit = QLineEdit(self.groupbox_metadata)
        self.metadata_bitrate_lineedit.setObjectName(u"metadata_bitrate_lineedit")
        self.metadata_bitrate_lineedit.setReadOnly(True)

        self.hLayout_bitrate.addWidget(self.metadata_bitrate_lineedit)


        self.gridLayout_5.addLayout(self.hLayout_bitrate, 5, 0, 1, 3)

        self.hLayout_length = QHBoxLayout()
        self.hLayout_length.setObjectName(u"hLayout_length")
        self.metadata_length_label = QLabel(self.groupbox_metadata)
        self.metadata_length_label.setObjectName(u"metadata_length_label")

        self.hLayout_length.addWidget(self.metadata_length_label)

        self.metadata_length_lineedit = QLineEdit(self.groupbox_metadata)
        self.metadata_length_lineedit.setObjectName(u"metadata_length_lineedit")
        self.metadata_length_lineedit.setReadOnly(True)

        self.hLayout_length.addWidget(self.metadata_length_lineedit)


        self.gridLayout_5.addLayout(self.hLayout_length, 7, 0, 1, 3)


        self.gridLayout_14.addWidget(self.groupbox_metadata, 2, 0, 3, 1)

        self.groupBox_3 = QGroupBox(Widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_13 = QGridLayout(self.groupBox_3)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.groupbox_output = QGroupBox(self.groupBox_3)
        self.groupbox_output.setObjectName(u"groupbox_output")
        self.gridLayout_6 = QGridLayout(self.groupbox_output)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.output_thumbnail_label = QLabel(self.groupbox_output)
        self.output_thumbnail_label.setObjectName(u"output_thumbnail_label")

        self.gridLayout_6.addWidget(self.output_thumbnail_label, 0, 0, 1, 1)

        self.output_thumbnail_lineedit = QLineEdit(self.groupbox_output)
        self.output_thumbnail_lineedit.setObjectName(u"output_thumbnail_lineedit")

        self.gridLayout_6.addWidget(self.output_thumbnail_lineedit, 0, 1, 1, 1)

        self.output_thumbnail_button = QPushButton(self.groupbox_output)
        self.output_thumbnail_button.setObjectName(u"output_thumbnail_button")
        self.output_thumbnail_button.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.output_thumbnail_button, 0, 2, 1, 1)

        self.output_music_label = QLabel(self.groupbox_output)
        self.output_music_label.setObjectName(u"output_music_label")

        self.gridLayout_6.addWidget(self.output_music_label, 1, 0, 1, 1)

        self.output_music_lineedit = QLineEdit(self.groupbox_output)
        self.output_music_lineedit.setObjectName(u"output_music_lineedit")

        self.gridLayout_6.addWidget(self.output_music_lineedit, 1, 1, 1, 1)

        self.output_music_button = QPushButton(self.groupbox_output)
        self.output_music_button.setObjectName(u"output_music_button")
        self.output_music_button.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.output_music_button, 1, 2, 1, 1)

        self.output_video_label = QLabel(self.groupbox_output)
        self.output_video_label.setObjectName(u"output_video_label")

        self.gridLayout_6.addWidget(self.output_video_label, 2, 0, 1, 1)

        self.output_video_lineedit = QLineEdit(self.groupbox_output)
        self.output_video_lineedit.setObjectName(u"output_video_lineedit")

        self.gridLayout_6.addWidget(self.output_video_lineedit, 2, 1, 1, 1)

        self.output_video_button = QPushButton(self.groupbox_output)
        self.output_video_button.setObjectName(u"output_video_button")
        self.output_video_button.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.output_video_button, 2, 2, 1, 1)


        self.gridLayout_13.addWidget(self.groupbox_output, 0, 0, 1, 1)

        self.groupbox_progress_bars = QGroupBox(self.groupBox_3)
        self.groupbox_progress_bars.setObjectName(u"groupbox_progress_bars")
        self.gridLayout = QGridLayout(self.groupbox_progress_bars)
        self.gridLayout.setObjectName(u"gridLayout")
        self.progressbar_metadata_label = QLabel(self.groupbox_progress_bars)
        self.progressbar_metadata_label.setObjectName(u"progressbar_metadata_label")

        self.gridLayout.addWidget(self.progressbar_metadata_label, 0, 0, 1, 1)

        self.progressbar_metadata = QProgressBar(self.groupbox_progress_bars)
        self.progressbar_metadata.setObjectName(u"progressbar_metadata")
        self.progressbar_metadata.setValue(0)

        self.gridLayout.addWidget(self.progressbar_metadata, 0, 1, 1, 1)

        self.progressbar_video_label = QLabel(self.groupbox_progress_bars)
        self.progressbar_video_label.setObjectName(u"progressbar_video_label")

        self.gridLayout.addWidget(self.progressbar_video_label, 1, 0, 1, 1)

        self.progressbar_video = QProgressBar(self.groupbox_progress_bars)
        self.progressbar_video.setObjectName(u"progressbar_video")
        self.progressbar_video.setValue(0)

        self.gridLayout.addWidget(self.progressbar_video, 1, 1, 1, 1)

        self.progressbar_playlist_label = QLabel(self.groupbox_progress_bars)
        self.progressbar_playlist_label.setObjectName(u"progressbar_playlist_label")

        self.gridLayout.addWidget(self.progressbar_playlist_label, 2, 0, 1, 1)

        self.progressbar_playlist = QProgressBar(self.groupbox_progress_bars)
        self.progressbar_playlist.setObjectName(u"progressbar_playlist")
        self.progressbar_playlist.setValue(0)

        self.gridLayout.addWidget(self.progressbar_playlist, 2, 1, 1, 1)

        self.progressbar_converting_label = QLabel(self.groupbox_progress_bars)
        self.progressbar_converting_label.setObjectName(u"progressbar_converting_label")

        self.gridLayout.addWidget(self.progressbar_converting_label, 3, 0, 1, 1)

        self.progressbar_converting = QProgressBar(self.groupbox_progress_bars)
        self.progressbar_converting.setObjectName(u"progressbar_converting")
        self.progressbar_converting.setValue(0)

        self.gridLayout.addWidget(self.progressbar_converting, 3, 1, 1, 1)


        self.gridLayout_13.addWidget(self.groupbox_progress_bars, 0, 1, 1, 1)

        self.groupbox_ui = QGroupBox(self.groupBox_3)
        self.groupbox_ui.setObjectName(u"groupbox_ui")
        self.gridLayout_4 = QGridLayout(self.groupbox_ui)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.radio_dark_mode = QRadioButton(self.groupbox_ui)
        self.radio_dark_mode.setObjectName(u"radio_dark_mode")
        self.radio_dark_mode.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.radio_dark_mode, 2, 0, 1, 1)

        self.radio_echteralsfake = QRadioButton(self.groupbox_ui)
        self.radio_echteralsfake.setObjectName(u"radio_echteralsfake")
        self.radio_echteralsfake.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.radio_echteralsfake, 3, 0, 1, 1)

        self.radio_white_theme = QRadioButton(self.groupbox_ui)
        self.radio_white_theme.setObjectName(u"radio_white_theme")
        self.radio_white_theme.setCursor(QCursor(Qt.ForbiddenCursor))

        self.gridLayout_4.addWidget(self.radio_white_theme, 1, 0, 1, 1)

        self.label_reset = QLabel(self.groupbox_ui)
        self.label_reset.setObjectName(u"label_reset")

        self.gridLayout_4.addWidget(self.label_reset, 0, 0, 1, 1)

        self.checkbox_linux_override_dark = QCheckBox(self.groupbox_ui)
        self.checkbox_linux_override_dark.setObjectName(u"checkbox_linux_override_dark")
        self.checkbox_linux_override_dark.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.checkbox_linux_override_dark, 4, 0, 1, 1)

        self.ui_theme_apply = QPushButton(self.groupbox_ui)
        self.ui_theme_apply.setObjectName(u"ui_theme_apply")

        self.gridLayout_4.addWidget(self.ui_theme_apply, 5, 0, 1, 1)


        self.gridLayout_13.addWidget(self.groupbox_ui, 0, 2, 1, 1)


        self.gridLayout_14.addWidget(self.groupBox_3, 3, 1, 1, 1)

        self.groupbox_info = QGroupBox(Widget)
        self.groupbox_info.setObjectName(u"groupbox_info")
        self.gridLayout_9 = QGridLayout(self.groupbox_info)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.info_text_1 = QLabel(self.groupbox_info)
        self.info_text_1.setObjectName(u"info_text_1")

        self.gridLayout_9.addWidget(self.info_text_1, 0, 0, 1, 1)

        self.info_text_2 = QLabel(self.groupbox_info)
        self.info_text_2.setObjectName(u"info_text_2")

        self.gridLayout_9.addWidget(self.info_text_2, 1, 0, 1, 1)

        self.info_text_3 = QLabel(self.groupbox_info)
        self.info_text_3.setObjectName(u"info_text_3")

        self.gridLayout_9.addWidget(self.info_text_3, 2, 0, 1, 1)


        self.gridLayout_14.addWidget(self.groupbox_info, 4, 1, 2, 1)

        self.license_text = QTextBrowser(Widget)
        self.license_text.setObjectName(u"license_text")

        self.gridLayout_14.addWidget(self.license_text, 5, 0, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"VidFetch - 0.1", None))
        self.groupbox_urls.setTitle("")
        self.video_thumbnail_copy_button.setText(QCoreApplication.translate("Widget", u"Copy", None))
        self.video_thumbnail_label.setText(QCoreApplication.translate("Widget", u"Thumbnail:", None))
        self.playlist_url_label.setText(QCoreApplication.translate("Widget", u"Playlist URL:", None))
        self.video_url_label.setText(QCoreApplication.translate("Widget", u"Video URL:", None))
        self.playlist_start_button.setText(QCoreApplication.translate("Widget", u"Downlaod", None))
        self.video_start_prep_button.setText(QCoreApplication.translate("Widget", u"Start Prep", None))
        self.video_download_start_button.setText(QCoreApplication.translate("Widget", u"Download", None))
        self.groupBox_2.setTitle("")
        self.groupbox_format.setTitle(QCoreApplication.translate("Widget", u"Output Format", None))
        self.radio_mov.setText(QCoreApplication.translate("Widget", u"MOV Format", None))
        self.radio_mp4.setText(QCoreApplication.translate("Widget", u"MP4 Format", None))
        self.radio_mkv.setText(QCoreApplication.translate("Widget", u"MKV Format", None))
        self.radio_avi.setText(QCoreApplication.translate("Widget", u"AVI Format", None))
        self.group_box_music.setTitle(QCoreApplication.translate("Widget", u"Music", None))
        self.radio_opus.setText(QCoreApplication.translate("Widget", u"OPUS Format", None))
        self.radio_m4a.setText(QCoreApplication.translate("Widget", u"M4A Format", None))
        self.radio_wav.setText(QCoreApplication.translate("Widget", u"WAV Format", None))
        self.radio_mp3.setText(QCoreApplication.translate("Widget", u"MP3 Format", None))
        self.groupbox_resolutions.setTitle(QCoreApplication.translate("Widget", u"Resolutions", None))
        self.radio_144p.setText(QCoreApplication.translate("Widget", u"144p SD", None))
        self.radio_1080p.setText(QCoreApplication.translate("Widget", u"1080p F-HD", None))
        self.radio_240p.setText(QCoreApplication.translate("Widget", u"240p SD", None))
        self.radio_1440p.setText(QCoreApplication.translate("Widget", u"1440p 2K", None))
        self.radio_360p.setText(QCoreApplication.translate("Widget", u"360p SD", None))
        self.radio_2160p.setText(QCoreApplication.translate("Widget", u"2160p 4K", None))
        self.radio_480p.setText(QCoreApplication.translate("Widget", u"480p SD", None))
        self.radio_4320p.setText(QCoreApplication.translate("Widget", u"4320p 8K", None))
        self.radio_720p.setText(QCoreApplication.translate("Widget", u"720p HD", None))
        self.groupbox_video.setTitle(QCoreApplication.translate("Widget", u"Video", None))
        self.radio_interactive.setText(QCoreApplication.translate("Widget", u"Interactive Mode", None))
        self.radio_video_only.setText(QCoreApplication.translate("Widget", u"Video Only", None))
        self.radio_video_mode.setText(QCoreApplication.translate("Widget", u"Video Mode", None))
        self.radio_music_mode.setText(QCoreApplication.translate("Widget", u"Music Mode", None))
        self.groupbox_downloads.setTitle(QCoreApplication.translate("Widget", u"Downloads ", None))
        self.video_remain_video_label.setText(QCoreApplication.translate("Widget", u"Downloaded: / of / Videos", None))
        self.playlist_remain_vieos_label.setText(QCoreApplication.translate("Widget", u"Downloaded: / of / Videos", None))
        self.groupbox_metadata.setTitle(QCoreApplication.translate("Widget", u"Metadata:", None))
        self.metadata_filesize_label.setText(QCoreApplication.translate("Widget", u"File Size (MB):", None))
        self.metadata_fps_label.setText(QCoreApplication.translate("Widget", u"FPS:", None))
        self.metadata_views_label.setText(QCoreApplication.translate("Widget", u"Views:", None))
        self.metadata_thumbnail_label.setText(QCoreApplication.translate("Widget", u"Thumbnail:", None))
        self.metadata_hdr_label.setText(QCoreApplication.translate("Widget", u"HDR:", None))
        self.metadata_title_label.setText(QCoreApplication.translate("Widget", u"Processing: ", None))
        self.metadata_title_lineedit.setText(QCoreApplication.translate("Widget", u" -", None))
        self.metadata_bitrate_label.setText(QCoreApplication.translate("Widget", u"Bitrate:\u00b4", None))
        self.metadata_length_label.setText(QCoreApplication.translate("Widget", u"Length:", None))
        self.groupBox_3.setTitle("")
        self.groupbox_output.setTitle(QCoreApplication.translate("Widget", u"Output stuff", None))
        self.output_thumbnail_label.setText(QCoreApplication.translate("Widget", u"Thumbnails:", None))
        self.output_thumbnail_lineedit.setText(QCoreApplication.translate("Widget", u"output/thumb/", None))
        self.output_thumbnail_button.setText(QCoreApplication.translate("Widget", u"Change", None))
        self.output_music_label.setText(QCoreApplication.translate("Widget", u"Music output:", None))
        self.output_music_lineedit.setText(QCoreApplication.translate("Widget", u"output/music/", None))
        self.output_music_button.setText(QCoreApplication.translate("Widget", u"Change", None))
        self.output_video_label.setText(QCoreApplication.translate("Widget", u"Video output:", None))
        self.output_video_lineedit.setText(QCoreApplication.translate("Widget", u"output/video/", None))
        self.output_video_button.setText(QCoreApplication.translate("Widget", u"Change", None))
        self.groupbox_progress_bars.setTitle(QCoreApplication.translate("Widget", u"Progress Bars", None))
        self.progressbar_metadata_label.setText(QCoreApplication.translate("Widget", u"Metadata:", None))
        self.progressbar_video_label.setText(QCoreApplication.translate("Widget", u"Video Download:", None))
        self.progressbar_playlist_label.setText(QCoreApplication.translate("Widget", u"Playlist Download:", None))
        self.progressbar_converting_label.setText(QCoreApplication.translate("Widget", u"Converting:", None))
        self.groupbox_ui.setTitle(QCoreApplication.translate("Widget", u"User Interface", None))
        self.radio_dark_mode.setText(QCoreApplication.translate("Widget", u"Dark Mode (default)", None))
        self.radio_echteralsfake.setText(QCoreApplication.translate("Widget", u"EchterAlsFake", None))
        self.radio_white_theme.setText(QCoreApplication.translate("Widget", u"White Theme", None))
        self.label_reset.setText(QCoreApplication.translate("Widget", u"After changing this you need to restart", None))
#if QT_CONFIG(tooltip)
        self.checkbox_linux_override_dark.setToolTip(QCoreApplication.translate("Widget", u"If your Linux distro doesn't enable dark mode by default, you can go with that", None))
#endif // QT_CONFIG(tooltip)
        self.checkbox_linux_override_dark.setText(QCoreApplication.translate("Widget", u"Override default linux dark mode", None))
        self.ui_theme_apply.setText(QCoreApplication.translate("Widget", u"Apply", None))
        self.groupbox_info.setTitle("")
#if QT_CONFIG(tooltip)
        self.info_text_1.setToolTip(QCoreApplication.translate("Widget", u"You found an Easter Egg :D", None))
#endif // QT_CONFIG(tooltip)
        self.info_text_1.setText(QCoreApplication.translate("Widget", u"* Program will ask you what resolution etc...  while downloading", None))
        self.info_text_2.setText(QCoreApplication.translate("Widget", u"** Video is downloaded seperately with the Audio and then combined to one file.", None))
        self.info_text_3.setText(QCoreApplication.translate("Widget", u"*** Downloads video with the endpoint url. (No VPN, takes longer, but real-time progress bar)", None))
        self.license_text.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Author:    EchterAlsFake</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Version:   0.1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Website:  https://github.com/echteralsfake/VidFetch</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; "
                        "margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">License:   GPL 3</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">I am using Qt for the Graphical User Interface. I don't have a Qt License, so this Project is Open Source. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">You are free to modify, change and distribute the program.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin"
                        "-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Usually I would license it under Creative Commons. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">It would be nice, if you could include the Source to this project in your project, but you don't have to.  I only ask you for that.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Credits:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Thanks to Tabnine. O"
                        "ne of the best code complete plugins I know.  If you want, buy their subscription, it's fucking awesome.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Thanks to ChatGPT. It helped a lot and I didn't understand shit when it comes to working with threads and progress bars. Without ChatGPT this project wouldn't be possible.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Thanks to Pytube, they created the Python Library, which I am downloading the videos with. Creating all that by myself would take years.</p>\n"
"<p style=\"-qt-paragrap"
                        "h-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Thanks to ffmpeg for their great and open source video converting tool.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Thanks to @slhck who created the pip package: </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ffmpeg-progress-yield  </p>\n"
"<p style=\"-qt-paragraph-type:empty"
                        "; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> It's the only way that I found, where I can create a progress bar for the converting process.  I searched like 6 hours and my mental health was at the end, but this guy just made my day :) </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Thanks to all contributors, or the ones, that will be a contributor in the future :) </p>\n"
"<p style=\" margin-top:0px; margin-bottom:"
                        "0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />You can support me here:  https://paypal.me/EchterAlsFake</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Thanks :) </p></body></html>", None))
    # retranslateUi

