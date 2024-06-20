# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'marketplacenKviST.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import ( NavigationToolbar2QT as NavigationToolbar)

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from matplotlib.figure import Figure

import numpy as np
import random

#import resources_rc

# ------------------ MplWidget ------------------
class MplWidget(QWidget):

        def __init__(self, parent=None, width=5, height=4, dpi=100):
                super().__init__()
                self.figure, self.ax = plt.subplots()
                self.cmap = plt.get_cmap("viridis")
                #plt.style.use('_mpl-gallery')
                self.canvas = FigureCanvas(self.figure)
                layout = QVBoxLayout()
                layout.addWidget(self.canvas)
                self.setStyleSheet("background-color: lightgray")

               # layout.addWidget(NavigationToolbar(self.canvas, self))
                self.setLayout(layout)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1197, 719)
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
"}\n"
"\n"
"QLCDNumber{\n"
"border-right:2px solid;\n"
"border-left: 2px solid;\n"
"border-color:  #0cbaba;\n"
"border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #646464;\n"
"    padding: 4px;\n"
"    border: 1px solid #fffff8;\n"
"    font-size: 14pt;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    gridline-color: #fffff8;\n"
"    font-size: 12pt;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: #646464;\n"
"    border: 1px solid #fffff8;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_widget = QWidget(self.centralwidget)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setMaximumSize(QSize(16777215, 50))
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
        self.label_113 = QLabel(self.header_title)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setMinimumSize(QSize(220, 0))
        self.label_113.setMaximumSize(QSize(150, 220))
        self.label_113.setPixmap(QPixmap(u"icons/vist_trans.png"))
        self.label_113.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_113)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label = QLabel(self.header_title)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignLeft)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.comboBox = QComboBox(self.header_title)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(250, 50))
        self.comboBox.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setWeight(75)
        self.comboBox.setFont(font1)
        self.comboBox.setLayoutDirection(Qt.LeftToRight)
        self.comboBox.setAutoFillBackground(False)

        self.horizontalLayout_3.addWidget(self.comboBox)


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
        icon.addFile(u"icons/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize.setIcon(icon)
        self.minimize.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.minimize)

        self.restore = QPushButton(self.header_nav)
        self.restore.setObjectName(u"restore")
        icon1 = QIcon()
        icon1.addFile(u"icons/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore.setIcon(icon1)
        self.restore.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.restore)

        self.close = QPushButton(self.header_nav)
        self.close.setObjectName(u"close")
        icon2 = QIcon()
        icon2.addFile(u"icons/close.svg", QSize(), QIcon.Normal, QIcon.Off)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1197, 669))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 10, 0, 10)
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.MplWidget = MplWidget(self.frame)
        self.MplWidget.setObjectName(u"MplWidget")

        self.horizontalLayout_5.addWidget(self.MplWidget)

        self.tableWidget = QTableWidget(self.frame)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        if (self.tableWidget.rowCount() < 2):
            self.tableWidget.setRowCount(2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(400, 0))
        self.tableWidget.setMaximumSize(QSize(400, 16777215))
        font2 = QFont()
        font2.setPointSize(12)
        self.tableWidget.setFont(font2)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setRowCount(2)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(170)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(170)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setHighlightSections(False)

        self.horizontalLayout_5.addWidget(self.tableWidget)


        self.verticalLayout_14.addWidget(self.frame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_4.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.main_body_widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_113.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">VEI -  PWBA   KANBAN   MONITORING </span></p></body></html>", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"MARKET PLACE LINE 2", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"MARKET PLACE LINE 3", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"MARKET PLACE LINE 4", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"MARKET PLACE LINE 5", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"MARKET PLACE LINE 6", None))
        self.comboBox.setItemText(5, "")

        self.minimize.setText("")
        self.restore.setText("")
        self.close.setText("")
    # retranslateUi

