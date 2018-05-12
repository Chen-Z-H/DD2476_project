from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import elasticioEx

top = 20
userid = 5


class Ui_MainWindow(object):

    def __init__(self):
        super().__init__()
        self.results = {}
        self.userprofile = self.loadUserProfile(userid)
        # self.client = client

    def iniWindow(self, MainWindow):
        self.setupUi(MainWindow)
        self.searchPushButton.clicked.connect(self.query)
        self.searchResultsTableWidget.cellClicked.connect(self.on_result_item_click)
        return 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("A very simple search engine")
        MainWindow.resize(1115, 690)
        MainWindow.setMinimumSize(QtCore.QSize(1115, 690))
        MainWindow.setMaximumSize(QtCore.QSize(1115, 690))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 521, 81))
        self.groupBox.setStyleSheet("font: 14pt \"18thCentury\";")
        self.groupBox.setObjectName("groupBox")
        self.searchPushButton = QtWidgets.QPushButton(self.groupBox)
        self.searchPushButton.setGeometry(QtCore.QRect(440, 25, 71, 41))
        self.searchPushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.searchPushButton.setStyleSheet("font: 75 12pt \"Arial\";")
        self.searchPushButton.setObjectName("searchPushButton")
        self.queryLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.queryLineEdit.setGeometry(QtCore.QRect(10, 25, 411, 41))
        self.queryLineEdit.setStyleSheet("font: 13pt \"Times New Roman\";")
        self.queryLineEdit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.queryLineEdit.setObjectName("queryLineEdit")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(560, 10, 541, 371))
        self.groupBox_2.setStyleSheet("font: 14pt \"18thCentury\";")
        self.groupBox_2.setObjectName("groupBox_2")
        self.contentTextEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.contentTextEdit.setGeometry(QtCore.QRect(10, 30, 521, 321))
        self.contentTextEdit.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.contentTextEdit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.contentTextEdit.setReadOnly(True)
        self.contentTextEdit.setObjectName("contentTextEdit")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(560, 390, 541, 241))
        self.groupBox_3.setStyleSheet("font: 14pt \"18thCentury\";")
        self.groupBox_3.setObjectName("groupBox_3")
        self.logsTextEdit = QtWidgets.QTextEdit(self.groupBox_3)
        self.logsTextEdit.setGeometry(QtCore.QRect(10, 30, 521, 201))
        self.logsTextEdit.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.logsTextEdit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.logsTextEdit.setReadOnly(True)
        self.logsTextEdit.setOverwriteMode(False)
        self.logsTextEdit.setObjectName("logsTextEdit")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 110, 521, 521))
        self.groupBox_4.setStyleSheet("font: 14pt \"18thCentury\";")
        self.groupBox_4.setObjectName("groupBox_4")
        self.searchResultsTableWidget = QtWidgets.QTableWidget(self.groupBox_4)
        self.searchResultsTableWidget.setGeometry(QtCore.QRect(10, 20, 501, 491))
        self.searchResultsTableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.searchResultsTableWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.searchResultsTableWidget.setObjectName("searchResultsTableWidget")
        self.searchResultsTableWidget.setColumnCount(2)
        self.searchResultsTableWidget.setRowCount(0)
        self.searchResultsTableWidget.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.searchResultsTableWidget.setHorizontalHeaderLabels(["Rank", "Title"])
        self.searchResultsTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.searchResultsTableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.searchResultsTableWidget.horizontalHeader().resizeSection(0, 145)
        self.searchResultsTableWidget.horizontalHeader().resizeSection(1, 345)
        self.searchResultsTableWidget.verticalHeader().setVisible(False)
        self.searchResultsTableWidget.horizontalHeader().setSectionsClickable(False)
        self.searchResultsTableWidget.horizontalHeader().setStyleSheet("font: 75 13pt \"Times New Roman\";")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1115, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuMenu.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Search"))
        self.searchPushButton.setText(_translate("MainWindow", "Go"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Content"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Logs"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Results"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

    def query(self):
        query_words = self.queryLineEdit.text()
        if query_words == "" or query_words.isspace():
            self.addLog("Invalid query!", color="red")
        else:
            '''
            Search here
            '''
            self.results = elasticioEx.searchArticles(query_words)
            self.searchResultsTableWidget.clearContents()
            numShowResults = top if len(self.results) > top else len(self.results)
            self.searchResultsTableWidget.setRowCount(numShowResults)
            rank = 1
            print(self.results)
            for k, v in self.results.items():
                newItem = QtWidgets.QTableWidgetItem(str(rank))
                newItem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                self.searchResultsTableWidget.setItem(rank-1, 0, newItem)

                newItem = QtWidgets.QTableWidgetItem(str(self.results[k]["title"]))
                newItem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                self.searchResultsTableWidget.setItem(rank-1, 1, newItem)
                rank = rank + 1
                if rank == numShowResults:
                    break
            self.addLog("User searched '%s'." % query_words)

    def on_result_item_click(self, row, col):
        # cell = self.searchResultsTableWidget.item(row, col)
        doc = list(self.results.values())[row]
        # print(doc)
        self.contentTextEdit.setText(doc["text"])
        self.addLog("User clicked '%s'." % doc["title"])
        categories = doc["categories"]
        self.updateUserProfile(userid, categories)  # Update user profile


    def updateUserProfile(self, userid, categories):
        '''
        Update the user's profile
        :param userid:
        :param categories:
        :return: whatever
        '''
        return 0

    def exit(self):
        return 0

    def addLog(self, text, color="black", size="3"):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        content = self._formatString("%s: %s\n" % (now, text), color, size)
        self.logsTextEdit.append(content)

    def _formatString(self, text, color, size):
        return "<font size=\"" + size + "\" " \
                    "color=\"" + color + "\">" + text + "</font>"


    def loadUserProfile(self, userid):
        '''
        Load the user profile based on user id
        :param userid:
        :return: user profile
        '''
        return 0

