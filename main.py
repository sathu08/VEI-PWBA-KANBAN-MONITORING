import math
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import openpyxl
import datetime
import calendar

from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile

import time

# from matplotlib.backends.backend_qt5agg import (
#         FigureCanvas, NavigationToolbar2QT as NavigationToolbar)

from matplotlib.figure import Figure

import numpy as np
import random

# from marketplace.ui_functions import UIFunctions
from ui_functions import *
## ==> GLOBALS
counter = 0
from ui_splash_screen import Ui_SplashScreen

# GUI FILE

from ui_main import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *
import webbrowser

from threads import *
import serial
import time
import datetime
from datetime import datetime, timedelta

import serial
import time
import pandas as pd
import numpy as np
import sys, argparse, csv
import matplotlib.pyplot as plt
# from ui_error import Ui_Error

import os
import sqlite3
import json
from pickle import FALSE
from telnetlib import STATUS

import warnings
import pandas as pd
from openpyxl import load_workbook

warnings.filterwarnings("ignore")
from threads import *
import io
import base64

import winsound
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


def search_excel_value(file_path, search_value, sheet_name, search_column, return_columns):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    result = df[df[search_column] == search_value]
    if not result.empty:
        return result[return_columns].values.tolist()
    else:
        return "Value not found."


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.file = None
        self.file1 = None
        self.file2 = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # UIFunctions.initStackTab(self)
        # MOVE WINDOW
        def moveWindow(event):
            # RESTORE BEFORE MOVE
            if UIFunctions.returnStatus() == 1:
                UIFunctions.maximize_restore(self)

            # IF LEFT CLICK MOVE WINDOW

        # SET TITLE BAR
        # self.ui.header_widget.mouseMoveEvent = moveWindow
        ## ==> SET UI DEFINITIONS background
        UIFunctions.uiDefinitions(self)
        self.show()
        UIFunctions.maximize_restore(self)
        self.ui.comboBox.currentIndexChanged.connect(self.get_data_and_plot)
        self.readpath()

    def readpath(self):
        try:
            with open("path.txt") as f:
                path = f.read()

            self.file = path + "WAREInventory.xlsx"

            self.get_data_and_plot()

        except Exception as e:
            print(e)

    def get_data_and_plot(self):
        input_val = self.ui.comboBox.currentText()
        print(input_val)
        self.update_graph(input_val)

    def update_graph(self, input_val):

        self.ui.MplWidget.ax.clear()
        all_data = []
        Storage_Area = input_val
        print(Storage_Area)
        file_path = 'WAREInventory.xlsx'
        search_value = Storage_Area
        search_column = "StorageArea"
        return_columns = ['PartNumber', 'TotQty']
        sheet_name = 'WAREInventory'
        results = search_excel_value(file_path, search_value, sheet_name, search_column, return_columns)
        # print(results)
        for result in results:
            file_path_sup = 'new.xlsx'
            search_value_sup = result[0]  # Using the "PART NO" from the first result
            search_column_sup = "PartNumber"
            return_columns_sup = ['BOX TY', 'R', 'Y', 'G']
            sheet_name_sup = 'Sheet3'
            results_sup = search_excel_value(file_path_sup, search_value_sup, sheet_name_sup, search_column_sup,
                                             return_columns_sup)
            if results_sup != "Value not found.":
                for result_sup in results_sup:
                    data = {
                        "PART NO": result[0],
                        "QTY IN HAND": result[1],
                        "BOX TY": result_sup[0],
                        "R": result_sup[1],
                        "Y": result_sup[2],
                        "G": result_sup[3]
                    }
                    all_data.append(data)
        df2 = pd.DataFrame(all_data)
        with pd.ExcelWriter('full_details.xlsx', engine='xlsxwriter') as writer:
            df2.to_excel(writer, sheet_name='Sheet1', index=False)
        try:
            df = pd.read_excel('full_details.xlsx', sheet_name='Sheet1')
            df_all_filled = df.dropna(subset=['R', 'Y', 'G'])
            df_empty_values = [df[['R', 'Y', 'G']].isnull().any(axis=1)]
            if True in df_empty_values[0].tolist():
                model = df_all_filled['PART NO'].tolist()
                qty_hand = df_all_filled['QTY IN HAND'].tolist()
                box_ty = df_all_filled['BOX TY'].tolist()
                R = df_all_filled['R'].tolist()
                Y = df_all_filled['Y'].tolist()
                G = df_all_filled['G'].tolist()
            else:
                model = df['PART NO'].tolist()
                qty_hand = df['QTY IN HAND'].tolist()
                box_ty = df['BOX TY'].tolist()
                R = df['R'].tolist()
                Y = df['Y'].tolist()
                G = df['G'].tolist()
            # values = np.array(qty_hand) / np.array(box_ty)
            box_values = np.array(qty_hand) / np.array(box_ty)
            col_red = np.array(qty_hand) / np.array(R)

            values = []
            for i in box_values:
                rounded_value = math.ceil(i)
                values.append(rounded_value)

            bars = []
            bar_width = 0.9
            for i, (model, value, qty, box, r, y, g) in enumerate(zip(model, values, qty_hand, box_ty, R, Y, G)):
                bin_red = r / box
                bin_red = math.ceil(bin_red)
                bin_yellow = (y - r) / box
                bin_yellow = math.ceil(bin_yellow)
                bin_green = (g - y) / box
                bin_green = math.ceil(bin_green)
                bin_blue = (qty - g) / box
                bin_blue = math.ceil(bin_blue)
                # print("red:", bin_red, "yellow:", bin_yellow, "green:", bin_green, "blue:", bin_blue)
                lit_col = ["#f5d3d3", "#ffffb3", "#e6fce6", '#add8e6']
                col = ["red", "#ffcc00", "green", "blue"]
                overall_total = bin_red + bin_yellow + bin_green
                for j in range(0, int(overall_total + bin_blue)):
                    if j < bin_red:
                        self.ui.MplWidget.ax.barh(model, 1, height=bar_width, color=lit_col[0], edgecolor='black',
                                                  left=j)
                    else:
                        self.ui.MplWidget.ax.barh(model, 1, height=bar_width, color=lit_col[3], edgecolor='black',
                                                  left=j)
                for j in range(0, int(overall_total)):
                    if j <= bin_red:
                        self.ui.MplWidget.ax.barh(model, 1, height=bar_width, color=lit_col[0], edgecolor='black',
                                                  left=j)
                    elif j <= bin_yellow + bin_red:
                        self.ui.MplWidget.ax.barh(model, 1, height=bar_width, color=lit_col[1], edgecolor='black',
                                                  left=j)
                    elif j <= bin_yellow + bin_red + bin_green:
                        self.ui.MplWidget.ax.barh(model, 1, height=bar_width, color=lit_col[2], edgecolor='black',
                                                  left=j)
                    if j == 1:
                        self.ui.MplWidget.ax.text(overall_total + 1, model, f"{g}", fontsize=20, ha='left', va='center',
                                                  color="black")
                #
                if 0 < bin_blue:
                    self.ui.MplWidget.ax.barh(model, 1, height=bar_width, color=col[3], edgecolor='black', left=
                                              overall_total + bin_blue-1)
                elif (overall_total + bin_blue) > (overall_total-bin_green):
                    self.ui.MplWidget.ax.barh(model, 1, height=bar_width, color=col[2], edgecolor='black', left=
                                              overall_total + bin_blue-1)
                    print(overall_total + bin_blue)
                elif (overall_total + bin_blue) > (overall_total-(bin_green + bin_yellow)):
                    self.ui.MplWidget.ax.barh(model, 1, height=bar_width, color=col[1], edgecolor='black', left=
                                              overall_total + bin_blue-1)
                else:
                    self.ui.MplWidget.ax.barh(model, 1, height=bar_width, color=col[0], edgecolor='black', left=
                                              overall_total + bin_blue-1)

                for j in range(0, int(overall_total + bin_blue)):
                    # if j < bin_red:
                    #     self.ui.MplWidget.ax.barh(model, 1, height=bar_width, color=col[0], edgecolor='black', left=j)
                    # elif j < bin_yellow + bin_red:
                    #     self.ui.MplWidget.ax.barh(model, 1, height=bar_width, color=col[1], edgecolor='black', left=j)
                    # elif j < bin_yellow + bin_red + bin_green:
                    #     self.ui.MplWidget.ax.barh(model, 1, height=bar_width, color=col[2], edgecolor='black', left=j)
                    # else:
                    #     self.ui.MplWidget.ax.barh(model, 1, height=bar_width, color=col[3], edgecolor='black', left=j)
                    if j == 1:
                        self.ui.MplWidget.ax.text(0, model, f"{qty}", fontsize=20, ha='left', va='center',
                                                  color="white")

                self.ui.MplWidget.canvas.figure.tight_layout()
                self.ui.MplWidget.ax.tick_params(axis="y", labelsize=11)
                self.ui.MplWidget.ax.xaxis.set_visible(False)
                self.ui.MplWidget.ax.set_facecolor("lightgray")
                self.ui.MplWidget.canvas.draw()

                ############## table view#############

                df_empty_data = df[df[['R', 'Y', 'G']].isnull().any(axis=1)]
                df2 = df_empty_data.drop(['BOX TY', 'R', 'Y', 'G'], axis=1)

                self.ui.tableWidget.setRowCount(len(df2.axes[0]))
                self.ui.tableWidget.setRowCount(len(df2.axes[0]))
                self.ui.tableWidget.setColumnCount(len(df2.axes[1]))
                list_values = [df2.columns.values.tolist()] + df2.values.tolist()
                # (list_values)
                # self.ui.tableWidget.setStyleSheet(u"background-color: rgb(140, 140, 140);")

                self.ui.tableWidget.setHorizontalHeaderLabels(list_values[0])

                row_index = 0
                for value_tuple in list_values[1:]:
                    col_index = 0
                    for value1 in value_tuple:
                        self.ui.tableWidget.setItem(row_index, col_index, QTableWidgetItem(str(value1)))
                        col_index += 1
                    row_index += 1
            QtCore.QTimer.singleShot(60000, self.update_graph)

        except Exception as e:
            print(e)

    ## APP event updation ###############################

    # plt.ylabel("Model")
    # plt.xlabel("Value (Qty IN HAND / BOX TY)")
    # plt.title("Bar Chart")
    # # ax.set_xticks(range(0, int(max(values)) + 5, 5))
    # # ax.yaxis.set_visible(False)
    # plt.xlim(0, int(max(values) + 5))
    # grp_img_buf = io.BytesIO()
    # plt.savefig(grp_img_buf, format='png')
    # grp_img_buf.seek(0)
    # grp_img_buf = base64.b64encode(grp_img_buf.read()).decode()

    ########################################################################


class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(600)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>WELCOME...</strong>")

        # Change Texts

        QtCore.QTimer.singleShot(2000, lambda: self.ui.label_description.setText(
            "<strong>Next Moment Arises out of Present Moment</strong> -Budha"))
        QtCore.QTimer.singleShot(40000,
                                 lambda: self.ui.label_description.setText("<strong></strong>Getting things ready!! "))
        QtCore.QTimer.singleShot(50000, lambda: self.ui.label_description.setText(
            "<strong>Loading</strong> user interface...."))
        QtCore.QTimer.singleShot(30000, lambda: self.ui.label_description.setText(
            "<strong>What gets Measured gets improved</strong> "))

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):
        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
