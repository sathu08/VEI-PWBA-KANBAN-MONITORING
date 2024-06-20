# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'andoninterfacejITBjq.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1867, 992)
        MainWindow.setStyleSheet(u"\n"
"\n"
"*{\n"
"background:  transparent;\n"
"border: none;\n"
"color: #fff ;\n"
"}\n"
"#centralwidget{\n"
"	background-color: #05364F;\n"
"}\n"
"#header_nav{\n"
"	background-color: #032436;\n"
"	border-bottom-left-radius: 30px;\n"
"}\n"
"#header_title{\n"
"	background-color:#032436;\n"
"	border-top-right-radius: 30px;\n"
"}\n"
"#header_title * {\n"
"	color: #fff ;\n"
"}\n"
"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0.524118, y1:0, x2:0.671, y2:1, stop:0 #7f5a83, stop:1 #0d324d);\n"
"	padding: 5px 7px;\n"
"	border-radius: 10px;\n"
"}\n"
"#frame_3,#frame_40,#frame_73,#frame_94{\n"
"background-color: #05364F;\n"
"border-radius: 3px;\n"
"}\n"
"#frame_44,#frame_48,#frame_52,#frame_6,#frame_7{\n"
"background-color:#032436;\n"
"border-radius:10px;\n"
"}\n"
"#frame_41,#frame_57,#frame_61,#frame_65,#frame_69{\n"
"background-color:#032436;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"#frame_74,#frame_78,#frame_82,#frame_86,#frame_90{\n"
"background-color:#032436;\n"
"border-radius:10px;\n"
"}\n"
"#f"
                        "rame_103,#frame_107,#frame_111,#frame_95,#frame_99{\n"
"background-color:#032436;\n"
"border-radius:10px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_widget = QWidget(self.centralwidget)
        self.header_widget.setObjectName(u"header_widget")
        self.horizontalLayout = QHBoxLayout(self.header_widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_title = QWidget(self.header_widget)
        self.header_title.setObjectName(u"header_title")
        self.horizontalLayout_3 = QHBoxLayout(self.header_title)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.header_title)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignLeft)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.horizontalLayout.addWidget(self.header_title)

        self.header_nav = QWidget(self.header_widget)
        self.header_nav.setObjectName(u"header_nav")
        self.horizontalLayout_2 = QHBoxLayout(self.header_nav)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, -1, -1, -1)
        self.minimize = QPushButton(self.header_nav)
        self.minimize.setObjectName(u"minimize")
        icon = QIcon()
        icon.addFile(u":/icons/icons/minus-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize.setIcon(icon)
        self.minimize.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.minimize)

        self.restore = QPushButton(self.header_nav)
        self.restore.setObjectName(u"restore")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/stop-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore.setIcon(icon1)
        self.restore.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.restore)

        self.close = QPushButton(self.header_nav)
        self.close.setObjectName(u"close")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close.setIcon(icon2)
        self.close.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.close)


        self.horizontalLayout.addWidget(self.header_nav)


        self.verticalLayout.addWidget(self.header_widget)

        self.main_body_widget = QWidget(self.centralwidget)
        self.main_body_widget.setObjectName(u"main_body_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body_widget.sizePolicy().hasHeightForWidth())
        self.main_body_widget.setSizePolicy(sizePolicy)
        self.horizontalLayout_4 = QHBoxLayout(self.main_body_widget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.main_body_widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1867, 945))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 10, 0, 10)
        self.main_items_cont = QWidget(self.scrollAreaWidgetContents)
        self.main_items_cont.setObjectName(u"main_items_cont")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_items_cont.sizePolicy().hasHeightForWidth())
        self.main_items_cont.setSizePolicy(sizePolicy1)
        self.verticalLayout_63 = QVBoxLayout(self.main_items_cont)
        self.verticalLayout_63.setSpacing(0)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.frame_115 = QFrame(self.main_items_cont)
        self.frame_115.setObjectName(u"frame_115")
        self.frame_115.setMinimumSize(QSize(0, 50))
        self.frame_115.setMaximumSize(QSize(16777215, 50))
        self.frame_115.setFrameShape(QFrame.StyledPanel)
        self.frame_115.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.frame_115)
        self.horizontalLayout_69.setSpacing(0)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, -1, -1)
        self.label_2 = QLabel(self.frame_115)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 50))
        self.label_2.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">SMT-02</span></p></body></html>")

        self.horizontalLayout_69.addWidget(self.label_2)

        self.label_113 = QLabel(self.frame_115)
        self.label_113.setObjectName(u"label_113")

        self.horizontalLayout_69.addWidget(self.label_113)


        self.verticalLayout_63.addWidget(self.frame_115)

        self.frame_3 = QFrame(self.main_items_cont)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(35)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(9, -1, -1, -1)
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(361, 171))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_6)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(351, 50))
        self.frame_4.setStyleSheet(u"background-color: rgb(85, 170, 0);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_71 = QLabel(self.frame_4)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setMinimumSize(QSize(135, 40))
        self.label_71.setTextFormat(Qt.RichText)

        self.horizontalLayout_9.addWidget(self.label_71, 0, Qt.AlignLeft)

        self.label_10 = QLabel(self.frame_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(200, 50))
        self.label_10.setStyleSheet(u"")
        self.label_10.setTextFormat(Qt.RichText)

        self.horizontalLayout_9.addWidget(self.label_10)
        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame = QFrame(self.frame_6)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(351, 40))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(351, 50))

        self.verticalLayout_3.addWidget(self.label_8)

        self.frame_117 = QFrame(self.frame)
        self.frame_117.setObjectName(u"frame_117")
        self.frame_117.setFrameShape(QFrame.StyledPanel)
        self.frame_117.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.frame_117)
        self.horizontalLayout_72.setSpacing(0)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_117)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 15))

        self.horizontalLayout_72.addWidget(self.label_4)

        self.label_6 = QLabel(self.frame_117)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_72.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_117)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 15))

        self.horizontalLayout_72.addWidget(self.label_7)


        self.verticalLayout_3.addWidget(self.frame_117)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_5 = QFrame(self.frame_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(351, 60))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.progressBar_2 = QProgressBar(self.frame_5)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setMinimumSize(QSize(0, 60))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(18)
        self.progressBar_2.setFont(font2)
        self.progressBar_2.setValue(80)
        self.progressBar_2.setAlignment(Qt.AlignCenter)
        self.progressBar_2.setOrientation(Qt.Horizontal)
        self.progressBar_2.setInvertedAppearance(False)
        self.progressBar_2.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_5.addWidget(self.progressBar_2)

        self.progressBar_3 = QProgressBar(self.frame_5)
        self.progressBar_3.setObjectName(u"progressBar_3")
        self.progressBar_3.setMinimumSize(QSize(0, 60))
        self.progressBar_3.setFont(font2)
        self.progressBar_3.setValue(90)
        self.progressBar_3.setAlignment(Qt.AlignCenter)
        self.progressBar_3.setOrientation(Qt.Horizontal)

        self.horizontalLayout_5.addWidget(self.progressBar_3)

        self.progressBar = QProgressBar(self.frame_5)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 60))
        self.progressBar.setFont(font2)
        self.progressBar.setStyleSheet(u"border-color: rgb(255, 0, 0);")
        self.progressBar.setValue(50)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setOrientation(Qt.Horizontal)

        self.horizontalLayout_5.addWidget(self.progressBar)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.horizontalLayout_37.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(361, 171))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_7)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_28 = QFrame(self.frame_7)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(351, 50))
        self.frame_28.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_82 = QLabel(self.frame_28)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setMinimumSize(QSize(135, 40))
        self.label_82.setTextFormat(Qt.RichText)

        self.horizontalLayout_27.addWidget(self.label_82)

        self.label_30 = QLabel(self.frame_28)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(200, 45))
        self.label_30.setStyleSheet(u"")
        self.label_30.setTextFormat(Qt.RichText)

        self.horizontalLayout_27.addWidget(self.label_30)


        self.verticalLayout_25.addWidget(self.frame_28)

        self.frame_32 = QFrame(self.frame_7)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(351, 40))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_32)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self.frame_32)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(351, 40))

        self.verticalLayout_26.addWidget(self.label_31)

        self.frame_118 = QFrame(self.frame_32)
        self.frame_118.setObjectName(u"frame_118")
        self.frame_118.setMaximumSize(QSize(16777215, 15))
        self.frame_118.setFrameShape(QFrame.StyledPanel)
        self.frame_118.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.frame_118)
        self.horizontalLayout_73.setSpacing(0)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.label_68 = QLabel(self.frame_118)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setMaximumSize(QSize(16777215, 15))

        self.horizontalLayout_73.addWidget(self.label_68)

        self.label_69 = QLabel(self.frame_118)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setMaximumSize(QSize(16777215, 15))

        self.horizontalLayout_73.addWidget(self.label_69)

        self.label_70 = QLabel(self.frame_118)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setMaximumSize(QSize(16777215, 15))

        self.horizontalLayout_73.addWidget(self.label_70)


        self.verticalLayout_26.addWidget(self.frame_118)


        self.verticalLayout_25.addWidget(self.frame_32)

        self.frame_36 = QFrame(self.frame_7)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMinimumSize(QSize(351, 60))
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.progressBar_34 = QProgressBar(self.frame_36)
        self.progressBar_34.setObjectName(u"progressBar_34")
        self.progressBar_34.setMaximumSize(QSize(16777215, 60))
        self.progressBar_34.setFont(font2)
        self.progressBar_34.setStyleSheet(u"border-color: rgb(0, 255, 0);")
        self.progressBar_34.setValue(80)
        self.progressBar_34.setAlignment(Qt.AlignCenter)
        self.progressBar_34.setOrientation(Qt.Horizontal)
        self.progressBar_34.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_28.addWidget(self.progressBar_34)

        self.progressBar_35 = QProgressBar(self.frame_36)
        self.progressBar_35.setObjectName(u"progressBar_35")
        self.progressBar_35.setMaximumSize(QSize(16777215, 60))
        self.progressBar_35.setFont(font2)
        self.progressBar_35.setValue(90)
        self.progressBar_35.setAlignment(Qt.AlignCenter)
        self.progressBar_35.setOrientation(Qt.Horizontal)

        self.horizontalLayout_28.addWidget(self.progressBar_35)

        self.progressBar_36 = QProgressBar(self.frame_36)
        self.progressBar_36.setObjectName(u"progressBar_36")
        self.progressBar_36.setMaximumSize(QSize(16777215, 60))
        self.progressBar_36.setFont(font2)
        self.progressBar_36.setStyleSheet(u"border-color: rgb(255, 0, 0);")
        self.progressBar_36.setValue(50)
        self.progressBar_36.setAlignment(Qt.AlignCenter)
        self.progressBar_36.setOrientation(Qt.Horizontal)

        self.horizontalLayout_28.addWidget(self.progressBar_36)


        self.verticalLayout_25.addWidget(self.frame_36)


        self.horizontalLayout_37.addWidget(self.frame_7)

        self.frame_52 = QFrame(self.frame_3)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMinimumSize(QSize(361, 171))
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_52)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.frame_53 = QFrame(self.frame_52)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMinimumSize(QSize(351, 50))
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.label_86 = QLabel(self.frame_53)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setMinimumSize(QSize(135, 40))
        self.label_86.setTextFormat(Qt.RichText)

        self.horizontalLayout_35.addWidget(self.label_86)

        self.label_38 = QLabel(self.frame_53)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(200, 45))
        self.label_38.setTextFormat(Qt.RichText)

        self.horizontalLayout_35.addWidget(self.label_38)


        self.verticalLayout_33.addWidget(self.frame_53)

        self.frame_54 = QFrame(self.frame_52)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMinimumSize(QSize(351, 40))
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_54)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.label_39 = QLabel(self.frame_54)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(351, 40))

        self.verticalLayout_34.addWidget(self.label_39)

        self.frame_119 = QFrame(self.frame_54)
        self.frame_119.setObjectName(u"frame_119")
        self.frame_119.setMaximumSize(QSize(16777215, 20))
        self.frame_119.setFrameShape(QFrame.StyledPanel)
        self.frame_119.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_75 = QHBoxLayout(self.frame_119)
        self.horizontalLayout_75.setSpacing(0)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.label_104 = QLabel(self.frame_119)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setMinimumSize(QSize(0, 15))
        self.label_104.setMaximumSize(QSize(16777215, 15))

        self.horizontalLayout_75.addWidget(self.label_104)

        self.label_105 = QLabel(self.frame_119)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setMaximumSize(QSize(16777215, 15))

        self.horizontalLayout_75.addWidget(self.label_105)

        self.label_106 = QLabel(self.frame_119)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setMaximumSize(QSize(16777215, 15))

        self.horizontalLayout_75.addWidget(self.label_106)


        self.verticalLayout_34.addWidget(self.frame_119)


        self.verticalLayout_33.addWidget(self.frame_54)

        self.frame_55 = QFrame(self.frame_52)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setMinimumSize(QSize(351, 60))
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.progressBar_46 = QProgressBar(self.frame_55)
        self.progressBar_46.setObjectName(u"progressBar_46")
        self.progressBar_46.setMaximumSize(QSize(16777215, 60))
        self.progressBar_46.setFont(font2)
        self.progressBar_46.setValue(80)
        self.progressBar_46.setAlignment(Qt.AlignCenter)
        self.progressBar_46.setOrientation(Qt.Horizontal)
        self.progressBar_46.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_36.addWidget(self.progressBar_46)

        self.progressBar_47 = QProgressBar(self.frame_55)
        self.progressBar_47.setObjectName(u"progressBar_47")
        self.progressBar_47.setMaximumSize(QSize(16777215, 60))
        self.progressBar_47.setFont(font2)
        self.progressBar_47.setValue(90)
        self.progressBar_47.setAlignment(Qt.AlignCenter)
        self.progressBar_47.setOrientation(Qt.Horizontal)

        self.horizontalLayout_36.addWidget(self.progressBar_47)

        self.progressBar_48 = QProgressBar(self.frame_55)
        self.progressBar_48.setObjectName(u"progressBar_48")
        self.progressBar_48.setMaximumSize(QSize(16777215, 60))
        self.progressBar_48.setFont(font2)
        self.progressBar_48.setStyleSheet(u"border-color: rgb(255, 0, 0);")
        self.progressBar_48.setValue(50)
        self.progressBar_48.setAlignment(Qt.AlignCenter)
        self.progressBar_48.setOrientation(Qt.Horizontal)

        self.horizontalLayout_36.addWidget(self.progressBar_48)


        self.verticalLayout_33.addWidget(self.frame_55)


        self.horizontalLayout_37.addWidget(self.frame_52)

        self.frame_48 = QFrame(self.frame_3)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMinimumSize(QSize(361, 171))
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_48)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.frame_49 = QFrame(self.frame_48)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMinimumSize(QSize(351, 50))
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.label_85 = QLabel(self.frame_49)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setMinimumSize(QSize(135, 40))
        self.label_85.setTextFormat(Qt.RichText)

        self.horizontalLayout_33.addWidget(self.label_85)

        self.label_36 = QLabel(self.frame_49)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(200, 45))
        self.label_36.setTextFormat(Qt.RichText)

        self.horizontalLayout_33.addWidget(self.label_36)


        self.verticalLayout_31.addWidget(self.frame_49)

        self.frame_50 = QFrame(self.frame_48)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMinimumSize(QSize(351, 40))
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_50)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.frame_50)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(351, 40))

        self.verticalLayout_32.addWidget(self.label_37)

        self.frame_120 = QFrame(self.frame_50)
        self.frame_120.setObjectName(u"frame_120")
        self.frame_120.setMaximumSize(QSize(16777215, 15))
        self.frame_120.setFrameShape(QFrame.StyledPanel)
        self.frame_120.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.frame_120)
        self.horizontalLayout_76.setSpacing(0)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.label_107 = QLabel(self.frame_120)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setMaximumSize(QSize(16777215, 15))

        self.horizontalLayout_76.addWidget(self.label_107)

        self.label_108 = QLabel(self.frame_120)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setMaximumSize(QSize(16777215, 15))

        self.horizontalLayout_76.addWidget(self.label_108)

        self.label_109 = QLabel(self.frame_120)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setMaximumSize(QSize(16777215, 15))

        self.horizontalLayout_76.addWidget(self.label_109)


        self.verticalLayout_32.addWidget(self.frame_120)


        self.verticalLayout_31.addWidget(self.frame_50)

        self.frame_51 = QFrame(self.frame_48)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMinimumSize(QSize(351, 60))
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.progressBar_43 = QProgressBar(self.frame_51)
        self.progressBar_43.setObjectName(u"progressBar_43")
        self.progressBar_43.setMaximumSize(QSize(16777215, 60))
        self.progressBar_43.setFont(font2)
        self.progressBar_43.setValue(80)
        self.progressBar_43.setAlignment(Qt.AlignCenter)
        self.progressBar_43.setOrientation(Qt.Horizontal)
        self.progressBar_43.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_34.addWidget(self.progressBar_43)

        self.progressBar_44 = QProgressBar(self.frame_51)
        self.progressBar_44.setObjectName(u"progressBar_44")
        self.progressBar_44.setMaximumSize(QSize(16777215, 60))
        self.progressBar_44.setFont(font2)
        self.progressBar_44.setValue(90)
        self.progressBar_44.setAlignment(Qt.AlignCenter)
        self.progressBar_44.setOrientation(Qt.Horizontal)

        self.horizontalLayout_34.addWidget(self.progressBar_44)

        self.progressBar_45 = QProgressBar(self.frame_51)
        self.progressBar_45.setObjectName(u"progressBar_45")
        self.progressBar_45.setMaximumSize(QSize(16777215, 60))
        self.progressBar_45.setFont(font2)
        self.progressBar_45.setStyleSheet(u"border-color: rgb(255, 0, 0);")
        self.progressBar_45.setValue(50)
        self.progressBar_45.setAlignment(Qt.AlignCenter)
        self.progressBar_45.setOrientation(Qt.Horizontal)

        self.horizontalLayout_34.addWidget(self.progressBar_45)


        self.verticalLayout_31.addWidget(self.frame_51)


        self.horizontalLayout_37.addWidget(self.frame_48)

        self.frame_44 = QFrame(self.frame_3)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setMinimumSize(QSize(361, 171))
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_44)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_45 = QFrame(self.frame_44)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(351, 50))
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_84 = QLabel(self.frame_45)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setMinimumSize(QSize(135, 40))
        self.label_84.setTextFormat(Qt.RichText)

        self.horizontalLayout_31.addWidget(self.label_84)

        self.label_34 = QLabel(self.frame_45)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(200, 45))
        self.label_34.setTextFormat(Qt.RichText)

        self.horizontalLayout_31.addWidget(self.label_34)


        self.verticalLayout_29.addWidget(self.frame_45)

        self.frame_46 = QFrame(self.frame_44)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setMinimumSize(QSize(351, 40))
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_46)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_35 = QLabel(self.frame_46)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(351, 40))

        self.verticalLayout_30.addWidget(self.label_35)

        self.frame_121 = QFrame(self.frame_46)
        self.frame_121.setObjectName(u"frame_121")
        self.frame_121.setMaximumSize(QSize(16777215, 15))
        self.frame_121.setFrameShape(QFrame.StyledPanel)
        self.frame_121.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_77 = QHBoxLayout(self.frame_121)
        self.horizontalLayout_77.setSpacing(0)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.label_110 = QLabel(self.frame_121)
        self.label_110.setObjectName(u"label_110")

        self.horizontalLayout_77.addWidget(self.label_110)

        self.label_111 = QLabel(self.frame_121)
        self.label_111.setObjectName(u"label_111")

        self.horizontalLayout_77.addWidget(self.label_111)

        self.label_112 = QLabel(self.frame_121)
        self.label_112.setObjectName(u"label_112")

        self.horizontalLayout_77.addWidget(self.label_112)


        self.verticalLayout_30.addWidget(self.frame_121)


        self.verticalLayout_29.addWidget(self.frame_46)

        self.frame_47 = QFrame(self.frame_44)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMinimumSize(QSize(351, 60))
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.progressBar_40 = QProgressBar(self.frame_47)
        self.progressBar_40.setObjectName(u"progressBar_40")
        self.progressBar_40.setMaximumSize(QSize(16777215, 60))
        self.progressBar_40.setFont(font2)
        self.progressBar_40.setValue(80)
        self.progressBar_40.setAlignment(Qt.AlignCenter)
        self.progressBar_40.setOrientation(Qt.Horizontal)
        self.progressBar_40.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_32.addWidget(self.progressBar_40)

        self.progressBar_41 = QProgressBar(self.frame_47)
        self.progressBar_41.setObjectName(u"progressBar_41")
        self.progressBar_41.setMaximumSize(QSize(16777215, 60))
        self.progressBar_41.setFont(font2)
        self.progressBar_41.setValue(90)
        self.progressBar_41.setAlignment(Qt.AlignCenter)
        self.progressBar_41.setOrientation(Qt.Horizontal)

        self.horizontalLayout_32.addWidget(self.progressBar_41)

        self.progressBar_42 = QProgressBar(self.frame_47)
        self.progressBar_42.setObjectName(u"progressBar_42")
        self.progressBar_42.setMaximumSize(QSize(16777215, 60))
        self.progressBar_42.setFont(font2)
        self.progressBar_42.setStyleSheet(u"border-color: rgb(255, 0, 0);")
        self.progressBar_42.setValue(50)
        self.progressBar_42.setAlignment(Qt.AlignCenter)
        self.progressBar_42.setOrientation(Qt.Horizontal)

        self.horizontalLayout_32.addWidget(self.progressBar_42)


        self.verticalLayout_29.addWidget(self.frame_47)


        self.horizontalLayout_37.addWidget(self.frame_44)


        self.verticalLayout_63.addWidget(self.frame_3)

        self.frame_116 = QFrame(self.main_items_cont)
        self.frame_116.setObjectName(u"frame_116")
        self.frame_116.setMinimumSize(QSize(0, 50))
        self.frame_116.setMaximumSize(QSize(16777215, 50))
        self.frame_116.setFrameShape(QFrame.StyledPanel)
        self.frame_116.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.frame_116)
        self.horizontalLayout_71.setSpacing(0)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.label_5 = QLabel(self.frame_116)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 50))
        self.label_5.setMaximumSize(QSize(16777215, 50))
        self.label_5.setFont(font1)

        self.horizontalLayout_71.addWidget(self.label_5)

        self.label_115 = QLabel(self.frame_116)
        self.label_115.setObjectName(u"label_115")

        self.horizontalLayout_71.addWidget(self.label_115)


        self.verticalLayout_63.addWidget(self.frame_116)

        self.frame_94 = QFrame(self.main_items_cont)
        self.frame_94.setObjectName(u"frame_94")
        sizePolicy2.setHeightForWidth(self.frame_94.sizePolicy().hasHeightForWidth())
        self.frame_94.setSizePolicy(sizePolicy2)
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_94)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(9, -1, -1, -1)
        self.frame_95 = QFrame(self.frame_94)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setMinimumSize(QSize(361, 171))
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_95)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.frame_96 = QFrame(self.frame_95)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setMinimumSize(QSize(351, 50))
        self.frame_96.setMaximumSize(QSize(16777215, 60))
        self.frame_96.setFrameShape(QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_96)
        self.horizontalLayout_59.setSpacing(0)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.label_96 = QLabel(self.frame_96)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setMinimumSize(QSize(117, 50))
        self.label_96.setTextFormat(Qt.RichText)

        self.horizontalLayout_59.addWidget(self.label_96)

        self.label_58 = QLabel(self.frame_96)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMinimumSize(QSize(234, 45))
        self.label_58.setTextFormat(Qt.RichText)

        self.horizontalLayout_59.addWidget(self.label_58)


        self.verticalLayout_53.addWidget(self.frame_96)

        self.frame_97 = QFrame(self.frame_95)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setMinimumSize(QSize(351, 40))
        self.frame_97.setFrameShape(QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_97)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.label_59 = QLabel(self.frame_97)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMinimumSize(QSize(351, 50))

        self.verticalLayout_54.addWidget(self.label_59)

        self.frame_98 = QFrame(self.frame_97)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setMinimumSize(QSize(351, 60))
        self.frame_98.setFrameShape(QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.frame_98)
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.progressBar_76 = QProgressBar(self.frame_98)
        self.progressBar_76.setObjectName(u"progressBar_76")
        self.progressBar_76.setMaximumSize(QSize(16777215, 60))
        self.progressBar_76.setFont(font2)
        self.progressBar_76.setValue(80)
        self.progressBar_76.setAlignment(Qt.AlignCenter)
        self.progressBar_76.setOrientation(Qt.Horizontal)
        self.progressBar_76.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_60.addWidget(self.progressBar_76)

        self.progressBar_77 = QProgressBar(self.frame_98)
        self.progressBar_77.setObjectName(u"progressBar_77")
        self.progressBar_77.setMaximumSize(QSize(16777215, 60))
        self.progressBar_77.setFont(font2)
        self.progressBar_77.setValue(90)
        self.progressBar_77.setAlignment(Qt.AlignCenter)
        self.progressBar_77.setOrientation(Qt.Horizontal)

        self.horizontalLayout_60.addWidget(self.progressBar_77)

        self.progressBar_78 = QProgressBar(self.frame_98)
        self.progressBar_78.setObjectName(u"progressBar_78")
        self.progressBar_78.setMaximumSize(QSize(16777215, 60))
        self.progressBar_78.setFont(font2)
        self.progressBar_78.setStyleSheet(u"border-color: rgb(255, 0, 0);")
        self.progressBar_78.setValue(50)
        self.progressBar_78.setAlignment(Qt.AlignCenter)
        self.progressBar_78.setOrientation(Qt.Horizontal)

        self.horizontalLayout_60.addWidget(self.progressBar_78)


        self.verticalLayout_54.addWidget(self.frame_98)


        self.verticalLayout_53.addWidget(self.frame_97)


        self.horizontalLayout_58.addWidget(self.frame_95)

        self.frame_99 = QFrame(self.frame_94)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setMinimumSize(QSize(361, 171))
        self.frame_99.setFrameShape(QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_99)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.frame_100 = QFrame(self.frame_99)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setMinimumSize(QSize(351, 50))
        self.frame_100.setFrameShape(QFrame.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_100)
        self.horizontalLayout_61.setSpacing(0)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.label_97 = QLabel(self.frame_100)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setMinimumSize(QSize(117, 40))
        self.label_97.setTextFormat(Qt.RichText)

        self.horizontalLayout_61.addWidget(self.label_97)

        self.label_60 = QLabel(self.frame_100)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMinimumSize(QSize(234, 45))
        self.label_60.setTextFormat(Qt.RichText)

        self.horizontalLayout_61.addWidget(self.label_60)


        self.verticalLayout_55.addWidget(self.frame_100)

        self.frame_101 = QFrame(self.frame_99)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setMinimumSize(QSize(351, 40))
        self.frame_101.setFrameShape(QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_101)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.label_61 = QLabel(self.frame_101)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMinimumSize(QSize(351, 40))

        self.verticalLayout_56.addWidget(self.label_61)


        self.verticalLayout_55.addWidget(self.frame_101)

        self.frame_102 = QFrame(self.frame_99)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setMinimumSize(QSize(351, 60))
        self.frame_102.setFrameShape(QFrame.StyledPanel)
        self.frame_102.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.frame_102)
        self.horizontalLayout_62.setSpacing(0)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.progressBar_79 = QProgressBar(self.frame_102)
        self.progressBar_79.setObjectName(u"progressBar_79")
        self.progressBar_79.setMaximumSize(QSize(16777215, 60))
        self.progressBar_79.setFont(font2)
        self.progressBar_79.setValue(80)
        self.progressBar_79.setAlignment(Qt.AlignCenter)
        self.progressBar_79.setOrientation(Qt.Horizontal)
        self.progressBar_79.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_62.addWidget(self.progressBar_79)

        self.progressBar_80 = QProgressBar(self.frame_102)
        self.progressBar_80.setObjectName(u"progressBar_80")
        self.progressBar_80.setMaximumSize(QSize(16777215, 60))
        self.progressBar_80.setFont(font2)
        self.progressBar_80.setValue(90)
        self.progressBar_80.setAlignment(Qt.AlignCenter)
        self.progressBar_80.setOrientation(Qt.Horizontal)

        self.horizontalLayout_62.addWidget(self.progressBar_80)

        self.progressBar_81 = QProgressBar(self.frame_102)
        self.progressBar_81.setObjectName(u"progressBar_81")
        self.progressBar_81.setMaximumSize(QSize(16777215, 60))
        self.progressBar_81.setFont(font2)
        self.progressBar_81.setStyleSheet(u"border-color: rgb(255, 0, 0);")
        self.progressBar_81.setValue(50)
        self.progressBar_81.setAlignment(Qt.AlignCenter)
        self.progressBar_81.setOrientation(Qt.Horizontal)

        self.horizontalLayout_62.addWidget(self.progressBar_81)


        self.verticalLayout_55.addWidget(self.frame_102)


        self.horizontalLayout_58.addWidget(self.frame_99)

        self.frame_103 = QFrame(self.frame_94)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setMinimumSize(QSize(361, 171))
        self.frame_103.setFrameShape(QFrame.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.frame_103)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.frame_104 = QFrame(self.frame_103)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setMinimumSize(QSize(351, 50))
        self.frame_104.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.frame_104.setFrameShape(QFrame.StyledPanel)
        self.frame_104.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_104)
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.label_98 = QLabel(self.frame_104)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setMinimumSize(QSize(117, 40))
        self.label_98.setTextFormat(Qt.RichText)

        self.horizontalLayout_63.addWidget(self.label_98)

        self.label_62 = QLabel(self.frame_104)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMinimumSize(QSize(234, 45))
        self.label_62.setTextFormat(Qt.RichText)

        self.horizontalLayout_63.addWidget(self.label_62)


        self.verticalLayout_57.addWidget(self.frame_104)

        self.frame_105 = QFrame(self.frame_103)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setMinimumSize(QSize(351, 40))
        self.frame_105.setFrameShape(QFrame.StyledPanel)
        self.frame_105.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.frame_105)
        self.verticalLayout_58.setSpacing(0)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.label_63 = QLabel(self.frame_105)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMinimumSize(QSize(351, 40))

        self.verticalLayout_58.addWidget(self.label_63)


        self.verticalLayout_57.addWidget(self.frame_105)

        self.frame_106 = QFrame(self.frame_103)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setMinimumSize(QSize(351, 60))
        self.frame_106.setFrameShape(QFrame.StyledPanel)
        self.frame_106.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.frame_106)
        self.horizontalLayout_64.setSpacing(0)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.progressBar_82 = QProgressBar(self.frame_106)
        self.progressBar_82.setObjectName(u"progressBar_82")
        self.progressBar_82.setMaximumSize(QSize(16777215, 60))
        self.progressBar_82.setFont(font2)
        self.progressBar_82.setValue(80)
        self.progressBar_82.setAlignment(Qt.AlignCenter)
        self.progressBar_82.setOrientation(Qt.Horizontal)
        self.progressBar_82.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_64.addWidget(self.progressBar_82)

        self.progressBar_83 = QProgressBar(self.frame_106)
        self.progressBar_83.setObjectName(u"progressBar_83")
        self.progressBar_83.setMaximumSize(QSize(16777215, 60))
        self.progressBar_83.setFont(font2)
        self.progressBar_83.setValue(90)
        self.progressBar_83.setAlignment(Qt.AlignCenter)
        self.progressBar_83.setOrientation(Qt.Horizontal)

        self.horizontalLayout_64.addWidget(self.progressBar_83)

        self.progressBar_84 = QProgressBar(self.frame_106)
        self.progressBar_84.setObjectName(u"progressBar_84")
        self.progressBar_84.setMaximumSize(QSize(16777215, 60))
        self.progressBar_84.setFont(font2)
        self.progressBar_84.setStyleSheet(u"border-color: rgb(255, 0, 0);")
        self.progressBar_84.setValue(50)
        self.progressBar_84.setAlignment(Qt.AlignCenter)
        self.progressBar_84.setOrientation(Qt.Horizontal)

        self.horizontalLayout_64.addWidget(self.progressBar_84)


        self.verticalLayout_57.addWidget(self.frame_106)


        self.horizontalLayout_58.addWidget(self.frame_103)

        self.frame_107 = QFrame(self.frame_94)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setMinimumSize(QSize(361, 171))
        self.frame_107.setFrameShape(QFrame.StyledPanel)
        self.frame_107.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frame_107)
        self.verticalLayout_59.setSpacing(0)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.frame_108 = QFrame(self.frame_107)
        self.frame_108.setObjectName(u"frame_108")
        self.frame_108.setMinimumSize(QSize(351, 50))
        self.frame_108.setFrameShape(QFrame.StyledPanel)
        self.frame_108.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.frame_108)
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.label_99 = QLabel(self.frame_108)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setMinimumSize(QSize(117, 40))
        self.label_99.setTextFormat(Qt.RichText)

        self.horizontalLayout_65.addWidget(self.label_99)

        self.label_64 = QLabel(self.frame_108)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMinimumSize(QSize(234, 45))
        self.label_64.setTextFormat(Qt.RichText)

        self.horizontalLayout_65.addWidget(self.label_64)


        self.verticalLayout_59.addWidget(self.frame_108)

        self.frame_109 = QFrame(self.frame_107)
        self.frame_109.setObjectName(u"frame_109")
        self.frame_109.setMinimumSize(QSize(351, 40))
        self.frame_109.setFrameShape(QFrame.StyledPanel)
        self.frame_109.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_109)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.label_65 = QLabel(self.frame_109)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMinimumSize(QSize(351, 40))

        self.verticalLayout_60.addWidget(self.label_65)


        self.verticalLayout_59.addWidget(self.frame_109)

        self.frame_110 = QFrame(self.frame_107)
        self.frame_110.setObjectName(u"frame_110")
        self.frame_110.setMinimumSize(QSize(351, 60))
        self.frame_110.setFrameShape(QFrame.StyledPanel)
        self.frame_110.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.frame_110)
        self.horizontalLayout_66.setSpacing(0)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.progressBar_85 = QProgressBar(self.frame_110)
        self.progressBar_85.setObjectName(u"progressBar_85")
        self.progressBar_85.setMaximumSize(QSize(16777215, 60))
        self.progressBar_85.setFont(font2)
        self.progressBar_85.setValue(80)
        self.progressBar_85.setAlignment(Qt.AlignCenter)
        self.progressBar_85.setOrientation(Qt.Horizontal)
        self.progressBar_85.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_66.addWidget(self.progressBar_85)

        self.progressBar_86 = QProgressBar(self.frame_110)
        self.progressBar_86.setObjectName(u"progressBar_86")
        self.progressBar_86.setMaximumSize(QSize(16777215, 60))
        self.progressBar_86.setFont(font2)
        self.progressBar_86.setValue(90)
        self.progressBar_86.setAlignment(Qt.AlignCenter)
        self.progressBar_86.setOrientation(Qt.Horizontal)

        self.horizontalLayout_66.addWidget(self.progressBar_86)

        self.progressBar_87 = QProgressBar(self.frame_110)
        self.progressBar_87.setObjectName(u"progressBar_87")
        self.progressBar_87.setMaximumSize(QSize(16777215, 60))
        self.progressBar_87.setFont(font2)
        self.progressBar_87.setStyleSheet(u"border-color: rgb(255, 0, 0);")
        self.progressBar_87.setValue(50)
        self.progressBar_87.setAlignment(Qt.AlignCenter)
        self.progressBar_87.setOrientation(Qt.Horizontal)

        self.horizontalLayout_66.addWidget(self.progressBar_87)


        self.verticalLayout_59.addWidget(self.frame_110)


        self.horizontalLayout_58.addWidget(self.frame_107)

        self.frame_111 = QFrame(self.frame_94)
        self.frame_111.setObjectName(u"frame_111")
        self.frame_111.setMinimumSize(QSize(361, 171))
        self.frame_111.setFrameShape(QFrame.StyledPanel)
        self.frame_111.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_111)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.frame_112 = QFrame(self.frame_111)
        self.frame_112.setObjectName(u"frame_112")
        self.frame_112.setMinimumSize(QSize(351, 50))
        self.frame_112.setFrameShape(QFrame.StyledPanel)
        self.frame_112.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_112)
        self.horizontalLayout_67.setSpacing(0)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.label_100 = QLabel(self.frame_112)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setMinimumSize(QSize(117, 40))
        self.label_100.setTextFormat(Qt.RichText)

        self.horizontalLayout_67.addWidget(self.label_100)

        self.label_66 = QLabel(self.frame_112)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMinimumSize(QSize(234, 45))
        self.label_66.setTextFormat(Qt.RichText)

        self.horizontalLayout_67.addWidget(self.label_66)


        self.verticalLayout_61.addWidget(self.frame_112)

        self.frame_113 = QFrame(self.frame_111)
        self.frame_113.setObjectName(u"frame_113")
        self.frame_113.setMinimumSize(QSize(351, 40))
        self.frame_113.setFrameShape(QFrame.StyledPanel)
        self.frame_113.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.frame_113)
        self.verticalLayout_62.setSpacing(0)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.label_67 = QLabel(self.frame_113)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMinimumSize(QSize(351, 40))

        self.verticalLayout_62.addWidget(self.label_67)


        self.verticalLayout_61.addWidget(self.frame_113)

        self.frame_114 = QFrame(self.frame_111)
        self.frame_114.setObjectName(u"frame_114")
        self.frame_114.setMinimumSize(QSize(351, 60))
        self.frame_114.setFrameShape(QFrame.StyledPanel)
        self.frame_114.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.frame_114)
        self.horizontalLayout_68.setSpacing(0)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.progressBar_88 = QProgressBar(self.frame_114)
        self.progressBar_88.setObjectName(u"progressBar_88")
        self.progressBar_88.setMaximumSize(QSize(16777215, 60))
        self.progressBar_88.setFont(font2)
        self.progressBar_88.setValue(80)
        self.progressBar_88.setAlignment(Qt.AlignCenter)
        self.progressBar_88.setOrientation(Qt.Horizontal)
        self.progressBar_88.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_68.addWidget(self.progressBar_88)

        self.progressBar_89 = QProgressBar(self.frame_114)
        self.progressBar_89.setObjectName(u"progressBar_89")
        self.progressBar_89.setMaximumSize(QSize(16777215, 60))
        self.progressBar_89.setFont(font2)
        self.progressBar_89.setValue(90)
        self.progressBar_89.setAlignment(Qt.AlignCenter)
        self.progressBar_89.setOrientation(Qt.Horizontal)

        self.horizontalLayout_68.addWidget(self.progressBar_89)

        self.progressBar_90 = QProgressBar(self.frame_114)
        self.progressBar_90.setObjectName(u"progressBar_90")
        self.progressBar_90.setMaximumSize(QSize(16777215, 60))
        self.progressBar_90.setFont(font2)
        self.progressBar_90.setStyleSheet(u"border-color: rgb(255, 0, 0);")
        self.progressBar_90.setValue(50)
        self.progressBar_90.setAlignment(Qt.AlignCenter)
        self.progressBar_90.setOrientation(Qt.Horizontal)

        self.horizontalLayout_68.addWidget(self.progressBar_90)


        self.verticalLayout_61.addWidget(self.frame_114)


        self.horizontalLayout_58.addWidget(self.frame_111)


        self.verticalLayout_63.addWidget(self.frame_94)

        self.frame_73 = QFrame(self.main_items_cont)
        self.frame_73.setObjectName(u"frame_73")
        sizePolicy2.setHeightForWidth(self.frame_73.sizePolicy().hasHeightForWidth())
        self.frame_73.setSizePolicy(sizePolicy2)
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_73)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(9, -1, -1, -1)
        self.frame_74 = QFrame(self.frame_73)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setMinimumSize(QSize(361, 171))
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_74)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.frame_75 = QFrame(self.frame_74)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setMinimumSize(QSize(351, 50))
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_75)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.label_91 = QLabel(self.frame_75)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setMinimumSize(QSize(117, 40))
        self.label_91.setTextFormat(Qt.RichText)

        self.horizontalLayout_48.addWidget(self.label_91)

        self.label_48 = QLabel(self.frame_75)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMinimumSize(QSize(234, 45))
        self.label_48.setTextFormat(Qt.RichText)

        self.horizontalLayout_48.addWidget(self.label_48)


        self.verticalLayout_43.addWidget(self.frame_75)

        self.frame_76 = QFrame(self.frame_74)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setMinimumSize(QSize(351, 40))
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_76)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.label_49 = QLabel(self.frame_76)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMinimumSize(QSize(351, 40))

        self.verticalLayout_44.addWidget(self.label_49)


        self.verticalLayout_43.addWidget(self.frame_76)

        self.frame_77 = QFrame(self.frame_74)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setMinimumSize(QSize(351, 60))
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_77)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.progressBar_61 = QProgressBar(self.frame_77)
        self.progressBar_61.setObjectName(u"progressBar_61")
        self.progressBar_61.setMaximumSize(QSize(16777215, 60))
        self.progressBar_61.setFont(font2)
        self.progressBar_61.setValue(80)
        self.progressBar_61.setAlignment(Qt.AlignCenter)
        self.progressBar_61.setOrientation(Qt.Horizontal)
        self.progressBar_61.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_49.addWidget(self.progressBar_61)

        self.progressBar_62 = QProgressBar(self.frame_77)
        self.progressBar_62.setObjectName(u"progressBar_62")
        self.progressBar_62.setMaximumSize(QSize(16777215, 60))
        self.progressBar_62.setFont(font2)
        self.progressBar_62.setValue(90)
        self.progressBar_62.setAlignment(Qt.AlignCenter)
        self.progressBar_62.setOrientation(Qt.Horizontal)

        self.horizontalLayout_49.addWidget(self.progressBar_62)

        self.progressBar_63 = QProgressBar(self.frame_77)
        self.progressBar_63.setObjectName(u"progressBar_63")
        self.progressBar_63.setMaximumSize(QSize(16777215, 60))
        self.progressBar_63.setFont(font2)
        self.progressBar_63.setStyleSheet(u"border-color: rgb(255, 0, 0);")
        self.progressBar_63.setValue(50)
        self.progressBar_63.setAlignment(Qt.AlignCenter)
        self.progressBar_63.setOrientation(Qt.Horizontal)

        self.horizontalLayout_49.addWidget(self.progressBar_63)


        self.verticalLayout_43.addWidget(self.frame_77)


        self.horizontalLayout_47.addWidget(self.frame_74)

        self.frame_78 = QFrame(self.frame_73)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setMinimumSize(QSize(361, 171))
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_78)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.frame_79 = QFrame(self.frame_78)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setMinimumSize(QSize(351, 50))
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_79)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.label_92 = QLabel(self.frame_79)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setMinimumSize(QSize(117, 40))
        self.label_92.setTextFormat(Qt.RichText)

        self.horizontalLayout_50.addWidget(self.label_92)

        self.label_50 = QLabel(self.frame_79)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMinimumSize(QSize(234, 45))
        self.label_50.setTextFormat(Qt.RichText)

        self.horizontalLayout_50.addWidget(self.label_50)


        self.verticalLayout_45.addWidget(self.frame_79)

        self.frame_80 = QFrame(self.frame_78)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setMinimumSize(QSize(351, 40))
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_80)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.label_51 = QLabel(self.frame_80)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMinimumSize(QSize(351, 40))

        self.verticalLayout_46.addWidget(self.label_51)


        self.verticalLayout_45.addWidget(self.frame_80)

        self.frame_81 = QFrame(self.frame_78)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setMinimumSize(QSize(351, 60))
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_81)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.progressBar_64 = QProgressBar(self.frame_81)
        self.progressBar_64.setObjectName(u"progressBar_64")
        self.progressBar_64.setMaximumSize(QSize(16777215, 60))
        self.progressBar_64.setFont(font2)
        self.progressBar_64.setValue(80)
        self.progressBar_64.setAlignment(Qt.AlignCenter)
        self.progressBar_64.setOrientation(Qt.Horizontal)
        self.progressBar_64.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_51.addWidget(self.progressBar_64)

        self.progressBar_65 = QProgressBar(self.frame_81)
        self.progressBar_65.setObjectName(u"progressBar_65")
        self.progressBar_65.setMaximumSize(QSize(16777215, 60))
        self.progressBar_65.setFont(font2)
        self.progressBar_65.setValue(90)
        self.progressBar_65.setAlignment(Qt.AlignCenter)
        self.progressBar_65.setOrientation(Qt.Horizontal)

        self.horizontalLayout_51.addWidget(self.progressBar_65)

        self.progressBar_66 = QProgressBar(self.frame_81)
        self.progressBar_66.setObjectName(u"progressBar_66")
        self.progressBar_66.setMaximumSize(QSize(16777215, 60))
        self.progressBar_66.setFont(font2)
        self.progressBar_66.setStyleSheet(u"border-color: rgb(255, 0, 0);")
        self.progressBar_66.setValue(50)
        self.progressBar_66.setAlignment(Qt.AlignCenter)
        self.progressBar_66.setOrientation(Qt.Horizontal)

        self.horizontalLayout_51.addWidget(self.progressBar_66)


        self.verticalLayout_45.addWidget(self.frame_81)


        self.horizontalLayout_47.addWidget(self.frame_78)

        self.frame_82 = QFrame(self.frame_73)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setMinimumSize(QSize(361, 171))
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_82)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.frame_83 = QFrame(self.frame_82)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setMinimumSize(QSize(351, 50))
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_83)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.label_93 = QLabel(self.frame_83)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setMinimumSize(QSize(117, 40))
        self.label_93.setTextFormat(Qt.RichText)

        self.horizontalLayout_52.addWidget(self.label_93)

        self.label_52 = QLabel(self.frame_83)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMinimumSize(QSize(234, 45))
        self.label_52.setTextFormat(Qt.RichText)

        self.horizontalLayout_52.addWidget(self.label_52)


        self.verticalLayout_47.addWidget(self.frame_83)

        self.frame_84 = QFrame(self.frame_82)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setMinimumSize(QSize(351, 40))
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_84)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.label_53 = QLabel(self.frame_84)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setMinimumSize(QSize(351, 40))

        self.verticalLayout_48.addWidget(self.label_53)


        self.verticalLayout_47.addWidget(self.frame_84)

        self.frame_85 = QFrame(self.frame_82)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setMinimumSize(QSize(351, 60))
        self.frame_85.setMaximumSize(QSize(16777215, 60))
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_85)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.progressBar_67 = QProgressBar(self.frame_85)
        self.progressBar_67.setObjectName(u"progressBar_67")
        self.progressBar_67.setMaximumSize(QSize(16777215, 60))
        self.progressBar_67.setFont(font2)
        self.progressBar_67.setValue(80)
        self.progressBar_67.setAlignment(Qt.AlignCenter)
        self.progressBar_67.setOrientation(Qt.Horizontal)
        self.progressBar_67.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_53.addWidget(self.progressBar_67)

        self.progressBar_68 = QProgressBar(self.frame_85)
        self.progressBar_68.setObjectName(u"progressBar_68")
        self.progressBar_68.setMaximumSize(QSize(16777215, 60))
        self.progressBar_68.setFont(font2)
        self.progressBar_68.setValue(90)
        self.progressBar_68.setAlignment(Qt.AlignCenter)
        self.progressBar_68.setOrientation(Qt.Horizontal)

        self.horizontalLayout_53.addWidget(self.progressBar_68)

        self.progressBar_69 = QProgressBar(self.frame_85)
        self.progressBar_69.setObjectName(u"progressBar_69")
        self.progressBar_69.setMaximumSize(QSize(16777215, 60))
        self.progressBar_69.setFont(font2)
        self.progressBar_69.setStyleSheet(u"border-color: rgb(255, 0, 0);")
        self.progressBar_69.setValue(50)
        self.progressBar_69.setAlignment(Qt.AlignCenter)
        self.progressBar_69.setOrientation(Qt.Horizontal)

        self.horizontalLayout_53.addWidget(self.progressBar_69)


        self.verticalLayout_47.addWidget(self.frame_85)


        self.horizontalLayout_47.addWidget(self.frame_82)

        self.frame_86 = QFrame(self.frame_73)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setMinimumSize(QSize(361, 171))
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_86)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.frame_87 = QFrame(self.frame_86)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setMinimumSize(QSize(351, 50))
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_87)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.label_94 = QLabel(self.frame_87)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setMinimumSize(QSize(117, 40))
        self.label_94.setTextFormat(Qt.RichText)

        self.horizontalLayout_54.addWidget(self.label_94)

        self.label_54 = QLabel(self.frame_87)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMinimumSize(QSize(234, 45))
        self.label_54.setTextFormat(Qt.RichText)

        self.horizontalLayout_54.addWidget(self.label_54)


        self.verticalLayout_49.addWidget(self.frame_87)

        self.frame_88 = QFrame(self.frame_86)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setMinimumSize(QSize(351, 40))
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_88)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.label_55 = QLabel(self.frame_88)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMinimumSize(QSize(351, 40))

        self.verticalLayout_50.addWidget(self.label_55)


        self.verticalLayout_49.addWidget(self.frame_88)

        self.frame_89 = QFrame(self.frame_86)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setMinimumSize(QSize(351, 60))
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_89)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.progressBar_70 = QProgressBar(self.frame_89)
        self.progressBar_70.setObjectName(u"progressBar_70")
        self.progressBar_70.setMaximumSize(QSize(16777215, 60))
        self.progressBar_70.setFont(font2)
        self.progressBar_70.setValue(80)
        self.progressBar_70.setAlignment(Qt.AlignCenter)
        self.progressBar_70.setOrientation(Qt.Horizontal)
        self.progressBar_70.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_55.addWidget(self.progressBar_70)

        self.progressBar_71 = QProgressBar(self.frame_89)
        self.progressBar_71.setObjectName(u"progressBar_71")
        self.progressBar_71.setMaximumSize(QSize(16777215, 60))
        self.progressBar_71.setFont(font2)
        self.progressBar_71.setValue(90)
        self.progressBar_71.setAlignment(Qt.AlignCenter)
        self.progressBar_71.setOrientation(Qt.Horizontal)

        self.horizontalLayout_55.addWidget(self.progressBar_71)

        self.progressBar_72 = QProgressBar(self.frame_89)
        self.progressBar_72.setObjectName(u"progressBar_72")
        self.progressBar_72.setMaximumSize(QSize(16777215, 60))
        self.progressBar_72.setFont(font2)
        self.progressBar_72.setStyleSheet(u"border-color: rgb(255, 0, 0);")
        self.progressBar_72.setValue(50)
        self.progressBar_72.setAlignment(Qt.AlignCenter)
        self.progressBar_72.setOrientation(Qt.Horizontal)

        self.horizontalLayout_55.addWidget(self.progressBar_72)


        self.verticalLayout_49.addWidget(self.frame_89)


        self.horizontalLayout_47.addWidget(self.frame_86)

        self.frame_90 = QFrame(self.frame_73)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setMinimumSize(QSize(361, 171))
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_90)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.frame_91 = QFrame(self.frame_90)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setMinimumSize(QSize(351, 50))
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_91)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.label_95 = QLabel(self.frame_91)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setMinimumSize(QSize(117, 40))
        self.label_95.setTextFormat(Qt.RichText)

        self.horizontalLayout_56.addWidget(self.label_95)

        self.label_56 = QLabel(self.frame_91)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMinimumSize(QSize(234, 45))
        self.label_56.setTextFormat(Qt.RichText)

        self.horizontalLayout_56.addWidget(self.label_56)


        self.verticalLayout_51.addWidget(self.frame_91)

        self.frame_92 = QFrame(self.frame_90)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setMinimumSize(QSize(351, 40))
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_92)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.label_57 = QLabel(self.frame_92)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(351, 40))

        self.verticalLayout_52.addWidget(self.label_57)


        self.verticalLayout_51.addWidget(self.frame_92)

        self.frame_93 = QFrame(self.frame_90)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setMinimumSize(QSize(351, 60))
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_93)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.progressBar_73 = QProgressBar(self.frame_93)
        self.progressBar_73.setObjectName(u"progressBar_73")
        self.progressBar_73.setMaximumSize(QSize(16777215, 60))
        self.progressBar_73.setFont(font2)
        self.progressBar_73.setValue(80)
        self.progressBar_73.setAlignment(Qt.AlignCenter)
        self.progressBar_73.setOrientation(Qt.Horizontal)
        self.progressBar_73.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_57.addWidget(self.progressBar_73)

        self.progressBar_74 = QProgressBar(self.frame_93)
        self.progressBar_74.setObjectName(u"progressBar_74")
        self.progressBar_74.setMaximumSize(QSize(16777215, 60))
        self.progressBar_74.setFont(font2)
        self.progressBar_74.setValue(90)
        self.progressBar_74.setAlignment(Qt.AlignCenter)
        self.progressBar_74.setOrientation(Qt.Horizontal)

        self.horizontalLayout_57.addWidget(self.progressBar_74)

        self.progressBar_75 = QProgressBar(self.frame_93)
        self.progressBar_75.setObjectName(u"progressBar_75")
        self.progressBar_75.setMaximumSize(QSize(16777215, 60))
        self.progressBar_75.setFont(font2)
        self.progressBar_75.setStyleSheet(u"border-color: rgb(255, 0, 0);")
        self.progressBar_75.setValue(50)
        self.progressBar_75.setAlignment(Qt.AlignCenter)
        self.progressBar_75.setOrientation(Qt.Horizontal)

        self.horizontalLayout_57.addWidget(self.progressBar_75)


        self.verticalLayout_51.addWidget(self.frame_93)


        self.horizontalLayout_47.addWidget(self.frame_90)


        self.verticalLayout_63.addWidget(self.frame_73)

        self.frame_40 = QFrame(self.main_items_cont)
        self.frame_40.setObjectName(u"frame_40")
        sizePolicy2.setHeightForWidth(self.frame_40.sizePolicy().hasHeightForWidth())
        self.frame_40.setSizePolicy(sizePolicy2)
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(9, -1, -1, -1)
        self.frame_41 = QFrame(self.frame_40)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMinimumSize(QSize(361, 171))
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_41)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_42 = QFrame(self.frame_41)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMinimumSize(QSize(351, 50))
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_83 = QLabel(self.frame_42)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setMinimumSize(QSize(117, 40))
        self.label_83.setTextFormat(Qt.RichText)

        self.horizontalLayout_29.addWidget(self.label_83)

        self.label_32 = QLabel(self.frame_42)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(234, 45))
        self.label_32.setTextFormat(Qt.RichText)

        self.horizontalLayout_29.addWidget(self.label_32)


        self.verticalLayout_27.addWidget(self.frame_42)

        self.frame_43 = QFrame(self.frame_41)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMinimumSize(QSize(351, 40))
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_43)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_33 = QLabel(self.frame_43)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(351, 40))

        self.verticalLayout_28.addWidget(self.label_33)


        self.verticalLayout_27.addWidget(self.frame_43)

        self.frame_56 = QFrame(self.frame_41)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setMinimumSize(QSize(351, 60))
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.progressBar_37 = QProgressBar(self.frame_56)
        self.progressBar_37.setObjectName(u"progressBar_37")
        self.progressBar_37.setMaximumSize(QSize(16777215, 60))
        self.progressBar_37.setFont(font2)
        self.progressBar_37.setValue(80)
        self.progressBar_37.setAlignment(Qt.AlignCenter)
        self.progressBar_37.setOrientation(Qt.Horizontal)
        self.progressBar_37.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_30.addWidget(self.progressBar_37)

        self.progressBar_38 = QProgressBar(self.frame_56)
        self.progressBar_38.setObjectName(u"progressBar_38")
        self.progressBar_38.setMaximumSize(QSize(16777215, 60))
        self.progressBar_38.setFont(font2)
        self.progressBar_38.setValue(90)
        self.progressBar_38.setAlignment(Qt.AlignCenter)
        self.progressBar_38.setOrientation(Qt.Horizontal)

        self.horizontalLayout_30.addWidget(self.progressBar_38)

        self.progressBar_39 = QProgressBar(self.frame_56)
        self.progressBar_39.setObjectName(u"progressBar_39")
        self.progressBar_39.setMaximumSize(QSize(16777215, 60))
        self.progressBar_39.setFont(font2)
        self.progressBar_39.setStyleSheet(u"border-color: rgb(255, 0, 0);")
        self.progressBar_39.setValue(50)
        self.progressBar_39.setAlignment(Qt.AlignCenter)
        self.progressBar_39.setOrientation(Qt.Horizontal)

        self.horizontalLayout_30.addWidget(self.progressBar_39)


        self.verticalLayout_27.addWidget(self.frame_56)


        self.horizontalLayout_38.addWidget(self.frame_41)

        self.frame_57 = QFrame(self.frame_40)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setMinimumSize(QSize(361, 171))
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_57)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.frame_58 = QFrame(self.frame_57)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setMinimumSize(QSize(351, 50))
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_58)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_87 = QLabel(self.frame_58)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setMinimumSize(QSize(117, 40))
        self.label_87.setTextFormat(Qt.RichText)

        self.horizontalLayout_39.addWidget(self.label_87)

        self.label_40 = QLabel(self.frame_58)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(234, 45))
        self.label_40.setTextFormat(Qt.RichText)

        self.horizontalLayout_39.addWidget(self.label_40)


        self.verticalLayout_35.addWidget(self.frame_58)

        self.frame_59 = QFrame(self.frame_57)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setMinimumSize(QSize(351, 40))
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_59)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.label_41 = QLabel(self.frame_59)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(351, 40))

        self.verticalLayout_36.addWidget(self.label_41)


        self.verticalLayout_35.addWidget(self.frame_59)

        self.frame_60 = QFrame(self.frame_57)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMinimumSize(QSize(351, 60))
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.progressBar_49 = QProgressBar(self.frame_60)
        self.progressBar_49.setObjectName(u"progressBar_49")
        self.progressBar_49.setMaximumSize(QSize(16777215, 60))
        self.progressBar_49.setFont(font2)
        self.progressBar_49.setValue(80)
        self.progressBar_49.setAlignment(Qt.AlignCenter)
        self.progressBar_49.setOrientation(Qt.Horizontal)
        self.progressBar_49.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_40.addWidget(self.progressBar_49)

        self.progressBar_50 = QProgressBar(self.frame_60)
        self.progressBar_50.setObjectName(u"progressBar_50")
        self.progressBar_50.setMaximumSize(QSize(16777215, 60))
        self.progressBar_50.setFont(font2)
        self.progressBar_50.setValue(90)
        self.progressBar_50.setAlignment(Qt.AlignCenter)
        self.progressBar_50.setOrientation(Qt.Horizontal)

        self.horizontalLayout_40.addWidget(self.progressBar_50)

        self.progressBar_51 = QProgressBar(self.frame_60)
        self.progressBar_51.setObjectName(u"progressBar_51")
        self.progressBar_51.setMaximumSize(QSize(16777215, 60))
        self.progressBar_51.setFont(font2)
        self.progressBar_51.setStyleSheet(u"border-color: rgb(255, 0, 0);")
        self.progressBar_51.setValue(50)
        self.progressBar_51.setAlignment(Qt.AlignCenter)
        self.progressBar_51.setOrientation(Qt.Horizontal)

        self.horizontalLayout_40.addWidget(self.progressBar_51)


        self.verticalLayout_35.addWidget(self.frame_60)


        self.horizontalLayout_38.addWidget(self.frame_57)

        self.frame_61 = QFrame(self.frame_40)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setMinimumSize(QSize(361, 171))
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_61)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.frame_62 = QFrame(self.frame_61)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setMinimumSize(QSize(351, 50))
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_62)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.label_88 = QLabel(self.frame_62)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setMinimumSize(QSize(117, 40))
        self.label_88.setTextFormat(Qt.RichText)

        self.horizontalLayout_41.addWidget(self.label_88)

        self.label_42 = QLabel(self.frame_62)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(234, 45))
        self.label_42.setTextFormat(Qt.RichText)

        self.horizontalLayout_41.addWidget(self.label_42)


        self.verticalLayout_37.addWidget(self.frame_62)

        self.frame_63 = QFrame(self.frame_61)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setMinimumSize(QSize(351, 40))
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_63)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.label_43 = QLabel(self.frame_63)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(351, 40))

        self.verticalLayout_38.addWidget(self.label_43)


        self.verticalLayout_37.addWidget(self.frame_63)

        self.frame_64 = QFrame(self.frame_61)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setMinimumSize(QSize(351, 60))
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_64)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.progressBar_52 = QProgressBar(self.frame_64)
        self.progressBar_52.setObjectName(u"progressBar_52")
        self.progressBar_52.setMaximumSize(QSize(16777215, 60))
        self.progressBar_52.setFont(font2)
        self.progressBar_52.setValue(80)
        self.progressBar_52.setAlignment(Qt.AlignCenter)
        self.progressBar_52.setOrientation(Qt.Horizontal)
        self.progressBar_52.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_42.addWidget(self.progressBar_52)

        self.progressBar_53 = QProgressBar(self.frame_64)
        self.progressBar_53.setObjectName(u"progressBar_53")
        self.progressBar_53.setMaximumSize(QSize(16777215, 60))
        self.progressBar_53.setFont(font2)
        self.progressBar_53.setValue(90)
        self.progressBar_53.setAlignment(Qt.AlignCenter)
        self.progressBar_53.setOrientation(Qt.Horizontal)

        self.horizontalLayout_42.addWidget(self.progressBar_53)

        self.progressBar_54 = QProgressBar(self.frame_64)
        self.progressBar_54.setObjectName(u"progressBar_54")
        self.progressBar_54.setMaximumSize(QSize(16777215, 60))
        self.progressBar_54.setFont(font2)
        self.progressBar_54.setStyleSheet(u"border-color: rgb(255, 0, 0);")
        self.progressBar_54.setValue(50)
        self.progressBar_54.setAlignment(Qt.AlignCenter)
        self.progressBar_54.setOrientation(Qt.Horizontal)

        self.horizontalLayout_42.addWidget(self.progressBar_54)


        self.verticalLayout_37.addWidget(self.frame_64)


        self.horizontalLayout_38.addWidget(self.frame_61)

        self.frame_65 = QFrame(self.frame_40)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setMinimumSize(QSize(361, 171))
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_65)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.frame_66 = QFrame(self.frame_65)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setMinimumSize(QSize(351, 50))
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_66)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.label_89 = QLabel(self.frame_66)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setMinimumSize(QSize(117, 40))
        self.label_89.setTextFormat(Qt.RichText)

        self.horizontalLayout_43.addWidget(self.label_89)

        self.label_44 = QLabel(self.frame_66)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(234, 45))
        self.label_44.setTextFormat(Qt.RichText)

        self.horizontalLayout_43.addWidget(self.label_44)


        self.verticalLayout_39.addWidget(self.frame_66)

        self.frame_67 = QFrame(self.frame_65)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setMinimumSize(QSize(351, 40))
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_67)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.label_45 = QLabel(self.frame_67)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(351, 40))

        self.verticalLayout_40.addWidget(self.label_45)


        self.verticalLayout_39.addWidget(self.frame_67)

        self.frame_68 = QFrame(self.frame_65)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setMinimumSize(QSize(351, 60))
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_68)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.progressBar_55 = QProgressBar(self.frame_68)
        self.progressBar_55.setObjectName(u"progressBar_55")
        self.progressBar_55.setMaximumSize(QSize(16777215, 60))
        self.progressBar_55.setFont(font2)
        self.progressBar_55.setValue(80)
        self.progressBar_55.setAlignment(Qt.AlignCenter)
        self.progressBar_55.setOrientation(Qt.Horizontal)
        self.progressBar_55.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_44.addWidget(self.progressBar_55)

        self.progressBar_56 = QProgressBar(self.frame_68)
        self.progressBar_56.setObjectName(u"progressBar_56")
        self.progressBar_56.setMaximumSize(QSize(16777215, 60))
        self.progressBar_56.setFont(font2)
        self.progressBar_56.setValue(90)
        self.progressBar_56.setAlignment(Qt.AlignCenter)
        self.progressBar_56.setOrientation(Qt.Horizontal)

        self.horizontalLayout_44.addWidget(self.progressBar_56)

        self.progressBar_57 = QProgressBar(self.frame_68)
        self.progressBar_57.setObjectName(u"progressBar_57")
        self.progressBar_57.setMaximumSize(QSize(16777215, 60))
        self.progressBar_57.setFont(font2)
        self.progressBar_57.setStyleSheet(u"border-color: rgb(255, 0, 0);")
        self.progressBar_57.setValue(50)
        self.progressBar_57.setAlignment(Qt.AlignCenter)
        self.progressBar_57.setOrientation(Qt.Horizontal)

        self.horizontalLayout_44.addWidget(self.progressBar_57)


        self.verticalLayout_39.addWidget(self.frame_68)


        self.horizontalLayout_38.addWidget(self.frame_65)

        self.frame_69 = QFrame(self.frame_40)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setMinimumSize(QSize(361, 171))
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_69)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.frame_70 = QFrame(self.frame_69)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setMinimumSize(QSize(351, 50))
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_70)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.label_90 = QLabel(self.frame_70)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setMinimumSize(QSize(117, 40))
        self.label_90.setTextFormat(Qt.RichText)

        self.horizontalLayout_45.addWidget(self.label_90)

        self.label_46 = QLabel(self.frame_70)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(234, 45))
        self.label_46.setTextFormat(Qt.RichText)

        self.horizontalLayout_45.addWidget(self.label_46)


        self.verticalLayout_41.addWidget(self.frame_70)

        self.frame_71 = QFrame(self.frame_69)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setMinimumSize(QSize(351, 40))
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_71)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.label_47 = QLabel(self.frame_71)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMinimumSize(QSize(351, 40))

        self.verticalLayout_42.addWidget(self.label_47)


        self.verticalLayout_41.addWidget(self.frame_71)

        self.frame_72 = QFrame(self.frame_69)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setMinimumSize(QSize(351, 60))
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_72)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.progressBar_58 = QProgressBar(self.frame_72)
        self.progressBar_58.setObjectName(u"progressBar_58")
        self.progressBar_58.setMaximumSize(QSize(16777215, 60))
        self.progressBar_58.setFont(font2)
        self.progressBar_58.setValue(80)
        self.progressBar_58.setAlignment(Qt.AlignCenter)
        self.progressBar_58.setOrientation(Qt.Horizontal)
        self.progressBar_58.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_46.addWidget(self.progressBar_58)

        self.progressBar_59 = QProgressBar(self.frame_72)
        self.progressBar_59.setObjectName(u"progressBar_59")
        self.progressBar_59.setMaximumSize(QSize(16777215, 60))
        self.progressBar_59.setFont(font2)
        self.progressBar_59.setValue(90)
        self.progressBar_59.setAlignment(Qt.AlignCenter)
        self.progressBar_59.setOrientation(Qt.Horizontal)

        self.horizontalLayout_46.addWidget(self.progressBar_59)

        self.progressBar_60 = QProgressBar(self.frame_72)
        self.progressBar_60.setObjectName(u"progressBar_60")
        self.progressBar_60.setMaximumSize(QSize(16777215, 60))
        self.progressBar_60.setFont(font2)
        self.progressBar_60.setStyleSheet(u"border-color: rgb(255, 0, 0);")
        self.progressBar_60.setValue(50)
        self.progressBar_60.setAlignment(Qt.AlignCenter)
        self.progressBar_60.setOrientation(Qt.Horizontal)

        self.horizontalLayout_46.addWidget(self.progressBar_60)


        self.verticalLayout_41.addWidget(self.frame_72)


        self.horizontalLayout_38.addWidget(self.frame_69)


        self.verticalLayout_63.addWidget(self.frame_40)


        self.verticalLayout_14.addWidget(self.main_items_cont)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_4.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.main_body_widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"VEI PRODUCTION MONITOR", None))
        self.minimize.setText("")
        self.restore.setText("")
        self.close.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">SMT - PRODUCTION STATUS </span></p></body></html>", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">SMT-02</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">RUNNING</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">PROD:  HDSAFKASDF</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">SHIFT -A OEE %</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">SHIFT -B OEE %</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">SHIFT -C OEE %</span></p></body></html>", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">SMT-03</span></p></body></html>", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">CORRECTIVE</span></p></body></html>", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\"></span></p></body></html>", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">SHIFT -A OEE %</span></p></body></html>", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">SHIFT -B OEE %</span></p></body></html>", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">SHIFT -C OEE %</span></p></body></html>", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">SMT-04</span></p></body></html>", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">RUNNING</span></p></body></html>", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\"></span></p></body></html>", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">SHIFT -A OEE %</span></p></body></html>", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">SHIFT -B OEE %</span></p></body></html>", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">SHIFT -C OEE %</span></p></body></html>", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">SMT-05</span></p></body></html>", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">RUNNING</span></p></body></html>", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\"></span></p></body></html>", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">SHIFT -A OEE %</span></p></body></html>", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">SHIFT -B OEE %</span></p></body></html>", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">SHIFT -C OEE %</span></p></body></html>", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">SMT-06</span></p></body></html>", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">RUNNING</span></p></body></html>", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\"></span></p></body></html>", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">SHIFT -A EFF %</span></p></body></html>", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">SHIFT -B EFF %</span></p></body></html>", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">SHIFT -C EFF %</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">FA - PRODUCTION STATUS</span></p></body></html>", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">FA-01</span></p></body></html>", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">RUNNING</span></p></body></html>", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\"></span></p></body></html>", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">FA-02</span></p></body></html>", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">RUNNING</span></p></body></html>", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\"></span></p></body></html>", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">FA-03</span></p></body></html>", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">CHANGEOVER</span></p></body></html>", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\"></span></p></body></html>", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">FA-04</span></p></body></html>", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">RUNNING</span></p></body></html>", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\"></span></p></body></html>", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">FA-05</span></p></body></html>", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">RUNNING</span></p></body></html>", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\"></span></p></body></html>", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">FA-06</span></p></body></html>", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">RUNNING</span></p></body></html>", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\"></span></p></body></html>", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">FA-07</span></p></body></html>", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">RUNNING</span></p></body></html>", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\"></span></p></body></html>", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">FA-08</span></p></body></html>", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">RUNNING</span></p></body></html>", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\"></span></p></body></html>", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">FA-09</span></p></body></html>", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">RUNNING</span></p></body></html>", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\"></span></p></body></html>", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">FA-10</span></p></body></html>", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">RUNNING</span></p></body></html>", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\"></span></p></body></html>", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">FA-11</span></p></body></html>", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">RUNNING</span></p></body></html>", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\"></span></p></body></html>", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">FA-12</span></p></body></html>", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">RUNNING</span></p></body></html>", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\"></span></p></body></html>", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">FA-13</span></p></body></html>", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">RUNNING</span></p></body></html>", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\"></span></p></body></html>", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">FA-14</span></p></body></html>", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">RUNNING</span></p></body></html>", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\"></span></p></body></html>", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">FA-15</span></p></body></html>", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">RUNNING</span></p></body></html>", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\"></span></p></body></html>", None))
    # retranslateUi

