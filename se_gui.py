from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
import elasticioEx
from compareEx import Comparator

showtop = 20
reranktop = 50
userid = 5
alpha = 0.01


class Ui_MainWindow(object):

    def __init__(self):
        super().__init__()
        self.results = {}
        self.userprofile = {}
        self.comparator = Comparator(alpha)
        self.mode = 0   # 0 for content-based method, 1 for query based method, 2 for combined method
        self.currentquery = ""

    def iniWindow(self, MainWindow):
        self.setupUi(MainWindow)
        self.searchPushButton.clicked.connect(self.query)
        self.searchResultsTableWidget.cellClicked.connect(self.on_result_item_click)
        return 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
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
        self.searchResultsTableWidget.setGeometry(QtCore.QRect(10, 30, 501, 481))
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
        self.menuAlgorithm = QtWidgets.QMenu(self.menubar)
        self.menuAlgorithm.setObjectName("menuAlgorithm")
        MainWindow.setMenuBar(self.menubar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(QtWidgets.QApplication.quit)
        self.actionContent_Based = QtWidgets.QAction(MainWindow)
        self.actionContent_Based.setCheckable(True)
        self.actionContent_Based.setChecked(True)
        self.actionContent_Based.setObjectName("actionContent_Based")
        self.actionQuery_Based = QtWidgets.QAction(MainWindow)
        self.actionQuery_Based.setCheckable(True)
        self.actionQuery_Based.setObjectName("actionQuery_Based")
        self.actionContent_Query = QtWidgets.QAction(MainWindow)
        self.actionContent_Query.setCheckable(True)
        self.actionContent_Query.setObjectName("actionContent_Query")
        self.actionContent_Based.triggered.connect(self._setModeContent)
        self.actionQuery_Based.triggered.connect(self._setModeQuery)
        self.actionContent_Query.triggered.connect(self._setModeContentQuery)

        self.menuMenu.addAction(self.actionExit)
        self.menuAlgorithm.addAction(self.actionContent_Based)
        self.menuAlgorithm.addAction(self.actionQuery_Based)
        self.menuAlgorithm.addAction(self.actionContent_Query)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuAlgorithm.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "A very simple search engine"))
        self.groupBox.setTitle(_translate("MainWindow", "Search"))
        self.searchPushButton.setText(_translate("MainWindow", "Go"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Content"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Logs"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Results"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuAlgorithm.setTitle(_translate("MainWindow", "Algorithm"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionContent_Based.setText(_translate("MainWindow", "Content-Based"))
        self.actionQuery_Based.setText(_translate("MainWindow", "Query-Based"))
        self.actionContent_Query.setText(_translate("MainWindow", "Content+Query"))

    def query(self):
        query_words = self.queryLineEdit.text()
        if query_words == "" or query_words.isspace():
            self.addLog("Invalid query!", color="red")
        else:
            self.currentquery = query_words
            ret = elasticioEx.addQueryHistory(userid, query_words, "")
            if ret == 1:
                self.addLog("Query recorded", color="blue")
            else:
                self.addLog("Query adding failed!", color="red")
            '''
            Search here
            '''
            self.results, hits = elasticioEx.searchArticles(query_words)
            self.searchResultsTableWidget.clearContents()
            numShowResults = showtop if len(self.results) > showtop else len(self.results)  # num of results to display
            self.searchResultsTableWidget.setRowCount(numShowResults)

            if len(self.results) == 0:
                self.addLog("No results to display!", color="red")
                return

            self.rerank(query_words)    # rerank

            rank = 1
            # print(self.results)
            for k, v in self.results.items():
                newItem = QtWidgets.QTableWidgetItem(str(rank))
                newItem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                self.searchResultsTableWidget.setItem(rank-1, 0, newItem)

                newItem = QtWidgets.QTableWidgetItem(str(self.results[k]["title"]))
                newItem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                self.searchResultsTableWidget.setItem(rank-1, 1, newItem)
                rank = rank + 1
                if rank > numShowResults:
                    break
            self.addLog("User searched '%s'." % query_words)

    def rerank(self, query):
        '''
        Rerank the search results
        :return: reranked documents
        '''
        # self.userprofile = self.loadUserProfile(userid)
        self.userprofile = elasticioEx.getUserPreferences(userid)
        # print(self.userprofile)
        # full_clist = self.comparator.collect_categories(hits)
        #
        # user_cv = self.comparator.create_user_cv(self.userprofile, full_clist)
        # art_cvs = self.comparator.create_all_article_cvs(hits, full_clist)
        #
        # for k in self.results.keys():
        #     self.comparator.cosine_sim(user_cv, art_cvs[k])

        if self.mode == 0:
            # content-based
            self.results = self.comparator.rerank(self.results, self.userprofile)
            result_list = sorted(self.results.items(), key=lambda x: x[1]['score'], reverse=True)
            self.results = dict(result_list)
            self.addLog("Reranked by content-based method.", color="blue")
        elif self.mode == 1:
            # query-based
            sh = elasticioEx.getUserHistory(userid)
            self.results = self.comparator.LucBoost(self.results, query, sh)
            self.results = dict(self.results)
            self.addLog("Reranked by query-based method.", color="blue")
        else:
            # content+query
            self.results = self.comparator.rerank(self.results, self.userprofile)
            result_list = sorted(self.results.items(), key=lambda x: x[1]['score'], reverse=True)
            self.results = dict(result_list)
            sh = elasticioEx.getUserHistory(userid)
            self.results = self.comparator.LucBoost(self.results, query, sh)
            self.results = dict(self.results)
            self.addLog("Reranked by combined method.", color="blue")

    def on_result_item_click(self, row, col):
        # cell = self.searchResultsTableWidget.item(row, col)
        doc = list(self.results.values())[row]
        docid = list(self.results.keys())[row]
        ret = elasticioEx.addQueryHistory(userid, self.currentquery, docid)     # record the clickthrough of query here

        categories = doc["categories"]
        # print(doc)
        self.contentTextEdit.setText(self._formatString("Text:", color="blue"))
        self.addLog("User clicked '%s'." % doc["title"])
        self.updateUserProfile(userid, categories)  # Update user profile
        self.contentTextEdit.append(doc["text"])
        # print(doc["title"] + ": " + docid)
        self.contentTextEdit.append("\n")
        self.contentTextEdit.append(self._formatString("Categories:\n", color="blue"))
        self.contentTextEdit.append("\n".join(categories))

    def loadUserProfile(self, userid):
        '''
        Load the user profile based on user id
        :param userid:
        :return: user profile
        '''
        ret = elasticioEx.getUserPreferences(userid)
        return 0

    def updateUserProfile(self, userid, categories):
        '''
        Update the user's profile
        :param userid:
        :param categories:
        :return: whatever
        '''
        ret = elasticioEx.updateUserPreferences(userid, categories)
        if ret == 1:
            self.addLog("User preferences updated.", color="blue")
        else:
            self.addLog("User profile update failed!", color="red")

    def addLog(self, text, color="black", size="3"):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        content = self._formatString("%s: %s\n" % (now, text), color, size)
        self.logsTextEdit.append(content)

    def _formatString(self, text, color="black", size="3"):
        return "<font size=\"" + size + "\" " \
                    "color=\"" + color + "\">" + text + "</font>"

    def _setModeContent(self):
        self.mode = 0
        self.addLog("User set mode as 'content-based'.", color="green")
        self.actionContent_Based.setChecked(True)
        self.actionQuery_Based.setChecked(False)
        self.actionContent_Query.setChecked(False)

    def _setModeQuery(self):
        self.mode = 1
        self.addLog("User set mode as 'query-based'.", color="green")
        self.actionContent_Based.setChecked(False)
        self.actionQuery_Based.setChecked(True)
        self.actionContent_Query.setChecked(False)

    def _setModeContentQuery(self):
        self.mode = 2
        self.addLog("User set mode as 'content+query'.", color="green")
        self.actionContent_Based.setChecked(False)
        self.actionQuery_Based.setChecked(False)
        self.actionContent_Query.setChecked(True)


