



## ==> GUI FILE
from main import *
from ui_main import Ui_MainWindow
## ==> GLOBALS

GLOBAL_STATE = 0
GLOBAL_TITLE_BAR = True
init = False

class TableModel(QtCore.QAbstractTableModel):

    def __init__(self,data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):


        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]
        if role == Qt.TextAlignmentRole:
            value = self._data[index.row()][index.column()]

            if isinstance(value, int) or isinstance(value, float):
                # Align right, vertical middle.
                return Qt.AlignVCenter

        if role == Qt.BackgroundRole:
            value = self._data[index.row()][index.column()]
            for nos in list:
                if value == nos:
                    return QtGui.QColor("red")



    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])
class UIFunctions(MainWindow):

    def initStackTab(self):
        global init
        if init == True:
            self.ui.container.setCurrentIndex(0)
            #self.ui.lab_tab.setText("Home")
            #self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)")
            init = True

    ## ==> MAXIMIZE RESTORE FUNCTION
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        # IF NOT MAXIMIZED
        if status == 0:
            self.showMaximized()

            # SET GLOBAL TO 1
            GLOBAL_STATE = 1

            # IF MAXIMIZED REMOVE MARGINS AND BORDER RADIUS
            #self.ui.frame_8.setContentsMargins(0, 0, 0, 0)
           # self.ui.frame_8.setStyleSheet(self)
            self.ui.restore.setToolTip("Restore")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            #self.ui.frame_8.setContentsMargins(10, 10, 10, 10)
           # self.ui.drop_shadow_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255)); border-radius: 10px;")
            self.ui.restore.setToolTip("Maximize")

    ## ==> UI DEFINITIONS
    def uiDefinitions(self):

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # SET DROPSHADOW WINDOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        # APPLY DROPSHADOW TO FRAME
        #self.ui.frame_3.setGraphicsEffect(self.shadow)
        #self.ui.frame_8.setGraphicsEffect(self.shadow)

        self.showNormal()


        # MAXIMIZE / RESTORE 
        self.ui.restore.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # MINIMIZE
        self.ui.minimize.clicked.connect(lambda: self.showMinimized())

        # CLOSE
        self.ui.close.clicked.connect(lambda: self.close())

        ## ==> CREATE SIZE GRIP TO RESIZE WINDOW
        #self.sizegrip = QSizeGrip(self.ui.size_grip)
        #self.sizegrip.setStyleSheet("QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(50, 42, 94) }")
        #self.sizegrip.setToolTip("Resize Window")



    ## RETURN STATUS IF WINDOWS IS MAXIMIZE OR RESTAURED
    def returnStatus():

        return GLOBAL_STATE
    def setStatus(status):
        global GLOBAL_STATE
        GLOBAL_STATE = status


    def toodleMenu(self, maxWidth, clicked):

        print("INtoodle")


        if clicked:
            self.ui.left_menu_frame.setMaximumSize(QSize(0, 16777215))
            currentWidth = self.ui.left_menu_frame.width()
            print(currentWidth)
            minWidth = 0
            if currentWidth == 150:
                print("if")
                extend = minWidth
                self.ui.stackedWidget.setCurrentWidget(self.ui.overview)


                #self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_home)
                #self.ui.lab_tab.setText("About > Home")
                #self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)")
            else:
                print("esle")
                extend = maxWidth

                # self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
                # self.ui.lab_tab.setText("Home")
                # self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)")

            self.animation = QPropertyAnimation(self.ui.left_menu_frame, b"minimumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(minWidth)
            self.animation.setEndValue(extend)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def buttonPressed(self, buttonName):

        index = self.ui.stackedWidget.currentIndex()

        # ------> THIS LINE CLEARS THE BG OF PREVIOUS TABS I.E. FROM THE LITER COLOR TO THE SAME BG COLOR I.E. TO CHANGE THE HIGHLIGHT.

        if buttonName == 'overview':

                self.ui.stackedWidget.setCurrentWidget(self.ui.overview)
                #self.ui.lab_tab.setText("Home")
                #self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)")  # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

        elif buttonName == "ame":
            self.ui.stackedWidget.setCurrentWidget(self.ui.ame)

        elif buttonName == "operations":
            self.ui.stackedWidget.setCurrentWidget(self.ui.operations)
        elif buttonName == "quality":
            self.ui.stackedWidget.setCurrentWidget(self.ui.quality)
        elif buttonName == "ame":
            self.ui.stackedWidget.setCurrentWidget(self.ui.ame)
        elif buttonName == "finance":
            self.ui.stackedWidget.setCurrentWidget(self.ui.finance)


    

            
           
           

       

