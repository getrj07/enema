# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Projects\enema\gui\main\main.ui'
#
# Created: Wed Apr 11 13:40:38 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName(_fromUtf8("MainForm"))
        MainForm.resize(1121, 624)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainForm.sizePolicy().hasHeightForWidth())
        MainForm.setSizePolicy(sizePolicy)
        MainForm.setMinimumSize(QtCore.QSize(591, 624))
        MainForm.setMaximumSize(QtCore.QSize(1121, 624))
        MainForm.setBaseSize(QtCore.QSize(0, 0))
        MainForm.setWindowTitle(_fromUtf8("Enema"))
        MainForm.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        MainForm.setDocumentMode(False)
        MainForm.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(MainForm)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabs = QtGui.QTabWidget(self.centralwidget)
        self.tabs.setEnabled(True)
        self.tabs.setGeometry(QtCore.QRect(0, 0, 591, 661))
        self.tabs.setMinimumSize(QtCore.QSize(1, 1))
        self.tabs.setMaximumSize(QtCore.QSize(1112, 661))
        self.tabs.setDocumentMode(True)
        self.tabs.setObjectName(_fromUtf8("tabs"))
        self.db_structureTab = QtGui.QWidget()
        self.db_structureTab.setObjectName(_fromUtf8("db_structureTab"))
        self.comboBox = QtGui.QComboBox(self.db_structureTab)
        self.comboBox.setGeometry(QtCore.QRect(520, 10, 61, 21))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.lineUrl = QtGui.QLineEdit(self.db_structureTab)
        self.lineUrl.setGeometry(QtCore.QRect(40, 10, 471, 20))
        self.lineUrl.setObjectName(_fromUtf8("lineUrl"))
        self.label_4 = QtGui.QLabel(self.db_structureTab)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 31, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.textData = QtGui.QTextEdit(self.db_structureTab)
        self.textData.setEnabled(False)
        self.textData.setGeometry(QtCore.QRect(10, 50, 571, 101))
        self.textData.setAcceptDrops(False)
        self.textData.setAcceptRichText(False)
        self.textData.setObjectName(_fromUtf8("textData"))
        self.label_15 = QtGui.QLabel(self.db_structureTab)
        self.label_15.setGeometry(QtCore.QRect(10, 30, 51, 21))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.groupBox_2 = QtGui.QGroupBox(self.db_structureTab)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 160, 411, 381))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.dbListComboBox = QtGui.QComboBox(self.groupBox_2)
        self.dbListComboBox.setGeometry(QtCore.QRect(70, 350, 131, 20))
        self.dbListComboBox.setObjectName(_fromUtf8("dbListComboBox"))
        self.listOfTables = QtGui.QListWidget(self.groupBox_2)
        self.listOfTables.setGeometry(QtCore.QRect(10, 50, 191, 291))
        self.listOfTables.setDragEnabled(True)
        self.listOfTables.setDragDropMode(QtGui.QAbstractItemView.DragOnly)
        self.listOfTables.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.listOfTables.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.listOfTables.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.listOfTables.setObjectName(_fromUtf8("listOfTables"))
        self.treeOfTables = QtGui.QTreeWidget(self.groupBox_2)
        self.treeOfTables.setEnabled(False)
        self.treeOfTables.setGeometry(QtCore.QRect(210, 50, 191, 291))
        self.treeOfTables.setAcceptDrops(True)
        self.treeOfTables.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeOfTables.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.treeOfTables.setDragDropOverwriteMode(True)
        self.treeOfTables.setDragDropMode(QtGui.QAbstractItemView.DropOnly)
        self.treeOfTables.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.treeOfTables.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.treeOfTables.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.treeOfTables.setIndentation(20)
        self.treeOfTables.setRootIsDecorated(True)
        self.treeOfTables.setUniformRowHeights(False)
        self.treeOfTables.setItemsExpandable(True)
        self.treeOfTables.setAnimated(True)
        self.treeOfTables.setWordWrap(False)
        self.treeOfTables.setColumnCount(1)
        self.treeOfTables.setObjectName(_fromUtf8("treeOfTables"))
        self.treeOfTables.header().setVisible(False)
        self.treeOfTables.header().setCascadingSectionResizes(False)
        self.treeOfTables.header().setHighlightSections(False)
        self.radioTables = QtGui.QRadioButton(self.groupBox_2)
        self.radioTables.setGeometry(QtCore.QRect(20, 20, 61, 17))
        self.radioTables.setChecked(True)
        self.radioTables.setObjectName(_fromUtf8("radioTables"))
        self.radioColumns = QtGui.QRadioButton(self.groupBox_2)
        self.radioColumns.setGeometry(QtCore.QRect(90, 20, 71, 17))
        self.radioColumns.setObjectName(_fromUtf8("radioColumns"))
        self.radioBases = QtGui.QRadioButton(self.groupBox_2)
        self.radioBases.setGeometry(QtCore.QRect(170, 20, 61, 17))
        self.radioBases.setObjectName(_fromUtf8("radioBases"))
        self.runButton = QtGui.QPushButton(self.groupBox_2)
        self.runButton.setGeometry(QtCore.QRect(260, 20, 91, 23))
        self.runButton.setObjectName(_fromUtf8("runButton"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 350, 61, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.cleanColumnsButton = QtGui.QToolButton(self.groupBox_2)
        self.cleanColumnsButton.setGeometry(QtCore.QRect(260, 350, 91, 23))
        self.cleanColumnsButton.setObjectName(_fromUtf8("cleanColumnsButton"))
        self.groupBox = QtGui.QGroupBox(self.db_structureTab)
        self.groupBox.setGeometry(QtCore.QRect(430, 160, 151, 201))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radioOrdinalPosition = QtGui.QRadioButton(self.groupBox)
        self.radioOrdinalPosition.setGeometry(QtCore.QRect(30, 170, 111, 16))
        self.radioOrdinalPosition.setObjectName(_fromUtf8("radioOrdinalPosition"))
        self.radioNotInArray = QtGui.QRadioButton(self.groupBox)
        self.radioNotInArray.setGeometry(QtCore.QRect(30, 110, 111, 17))
        self.radioNotInArray.setChecked(False)
        self.radioNotInArray.setObjectName(_fromUtf8("radioNotInArray"))
        self.radioNotInSubstring = QtGui.QRadioButton(self.groupBox)
        self.radioNotInSubstring.setGeometry(QtCore.QRect(30, 130, 111, 17))
        self.radioNotInSubstring.setChecked(True)
        self.radioNotInSubstring.setObjectName(_fromUtf8("radioNotInSubstring"))
        self.dbTypeBox = QtGui.QComboBox(self.groupBox)
        self.dbTypeBox.setGeometry(QtCore.QRect(20, 20, 111, 21))
        self.dbTypeBox.setObjectName(_fromUtf8("dbTypeBox"))
        self.dbTypeBox.addItem(_fromUtf8(""))
        self.dbTypeBox.addItem(_fromUtf8(""))
        self.comboInjType = QtGui.QComboBox(self.groupBox)
        self.comboInjType.setGeometry(QtCore.QRect(20, 50, 111, 21))
        self.comboInjType.setObjectName(_fromUtf8("comboInjType"))
        self.comboInjType.addItem(_fromUtf8(""))
        self.comboInjType.addItem(_fromUtf8(""))
        self.radioLimit = QtGui.QRadioButton(self.groupBox)
        self.radioLimit.setEnabled(False)
        self.radioLimit.setGeometry(QtCore.QRect(30, 150, 101, 17))
        self.radioLimit.setChecked(False)
        self.radioLimit.setObjectName(_fromUtf8("radioLimit"))
        self.headersButton = QtGui.QPushButton(self.groupBox)
        self.headersButton.setGeometry(QtCore.QRect(20, 80, 111, 23))
        self.headersButton.setObjectName(_fromUtf8("headersButton"))
        self.killButton = QtGui.QToolButton(self.db_structureTab)
        self.killButton.setGeometry(QtCore.QRect(460, 520, 91, 23))
        self.killButton.setObjectName(_fromUtf8("killButton"))
        self.logButton = QtGui.QToolButton(self.db_structureTab)
        self.logButton.setGeometry(QtCore.QRect(460, 490, 91, 21))
        self.logButton.setObjectName(_fromUtf8("logButton"))
        self.tabs.addTab(self.db_structureTab, _fromUtf8(""))
        self.queryTab = QtGui.QWidget()
        self.queryTab.setObjectName(_fromUtf8("queryTab"))
        self.groupBox_3 = QtGui.QGroupBox(self.queryTab)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 571, 201))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.queryText = QtGui.QTextEdit(self.groupBox_3)
        self.queryText.setGeometry(QtCore.QRect(10, 20, 551, 141))
        self.queryText.setDocumentTitle(_fromUtf8(""))
        self.queryText.setObjectName(_fromUtf8("queryText"))
        self.queryButton = QtGui.QPushButton(self.groupBox_3)
        self.queryButton.setGeometry(QtCore.QRect(490, 170, 71, 20))
        self.queryButton.setObjectName(_fromUtf8("queryButton"))
        self.blindMethodList = QtGui.QComboBox(self.groupBox_3)
        self.blindMethodList.setGeometry(QtCore.QRect(60, 170, 71, 20))
        self.blindMethodList.setObjectName(_fromUtf8("blindMethodList"))
        self.blindMethodList.addItem(_fromUtf8(""))
        self.blindMethodList.addItem(_fromUtf8(""))
        self.isStacked = QtGui.QCheckBox(self.groupBox_3)
        self.isStacked.setGeometry(QtCore.QRect(220, 170, 70, 20))
        self.isStacked.setObjectName(_fromUtf8("isStacked"))
        self.isHexed = QtGui.QCheckBox(self.groupBox_3)
        self.isHexed.setEnabled(True)
        self.isHexed.setGeometry(QtCore.QRect(290, 170, 51, 20))
        self.isHexed.setChecked(False)
        self.isHexed.setObjectName(_fromUtf8("isHexed"))
        self.methodLabel = QtGui.QLabel(self.groupBox_3)
        self.methodLabel.setGeometry(QtCore.QRect(10, 170, 41, 20))
        self.methodLabel.setObjectName(_fromUtf8("methodLabel"))
        self.resultGroup = QtGui.QGroupBox(self.queryTab)
        self.resultGroup.setGeometry(QtCore.QRect(10, 340, 571, 171))
        self.resultGroup.setObjectName(_fromUtf8("resultGroup"))
        self.queryOutput = QtGui.QTextEdit(self.resultGroup)
        self.queryOutput.setGeometry(QtCore.QRect(10, 20, 551, 141))
        self.queryOutput.setDocumentTitle(_fromUtf8(""))
        self.queryOutput.setReadOnly(True)
        self.queryOutput.setObjectName(_fromUtf8("queryOutput"))
        self.timeGroup = QtGui.QGroupBox(self.queryTab)
        self.timeGroup.setGeometry(QtCore.QRect(10, 220, 571, 51))
        self.timeGroup.setObjectName(_fromUtf8("timeGroup"))
        self.delayLabel = QtGui.QLabel(self.timeGroup)
        self.delayLabel.setGeometry(QtCore.QRect(10, 20, 41, 20))
        self.delayLabel.setObjectName(_fromUtf8("delayLabel"))
        self.delayBox = QtGui.QSpinBox(self.timeGroup)
        self.delayBox.setGeometry(QtCore.QRect(50, 20, 42, 20))
        self.delayBox.setMinimum(1)
        self.delayBox.setMaximum(59)
        self.delayBox.setProperty("value", 2)
        self.delayBox.setObjectName(_fromUtf8("delayBox"))
        self.trueTimeBox = QtGui.QDoubleSpinBox(self.timeGroup)
        self.trueTimeBox.setEnabled(False)
        self.trueTimeBox.setGeometry(QtCore.QRect(420, 20, 51, 20))
        self.trueTimeBox.setDecimals(2)
        self.trueTimeBox.setMaximum(59.0)
        self.trueTimeBox.setSingleStep(0.1)
        self.trueTimeBox.setProperty("value", 0.0)
        self.trueTimeBox.setObjectName(_fromUtf8("trueTimeBox"))
        self.trueTimeLabel = QtGui.QLabel(self.timeGroup)
        self.trueTimeLabel.setGeometry(QtCore.QRect(360, 20, 61, 20))
        self.trueTimeLabel.setObjectName(_fromUtf8("trueTimeLabel"))
        self.isAuto = QtGui.QCheckBox(self.timeGroup)
        self.isAuto.setGeometry(QtCore.QRect(480, 20, 81, 20))
        self.isAuto.setChecked(True)
        self.isAuto.setObjectName(_fromUtf8("isAuto"))
        self.lagLabel = QtGui.QLabel(self.timeGroup)
        self.lagLabel.setGeometry(QtCore.QRect(210, 20, 91, 20))
        self.lagLabel.setObjectName(_fromUtf8("lagLabel"))
        self.testButton = QtGui.QPushButton(self.timeGroup)
        self.testButton.setGeometry(QtCore.QRect(100, 20, 101, 20))
        self.testButton.setObjectName(_fromUtf8("testButton"))
        self.lagBox = QtGui.QDoubleSpinBox(self.timeGroup)
        self.lagBox.setGeometry(QtCore.QRect(300, 20, 51, 20))
        self.lagBox.setDecimals(2)
        self.lagBox.setMaximum(59.0)
        self.lagBox.setSingleStep(0.1)
        self.lagBox.setProperty("value", 5.0)
        self.lagBox.setObjectName(_fromUtf8("lagBox"))
        self.booleanGroup = QtGui.QGroupBox(self.queryTab)
        self.booleanGroup.setGeometry(QtCore.QRect(10, 280, 571, 51))
        self.booleanGroup.setObjectName(_fromUtf8("booleanGroup"))
        self.lineTruePattern = QtGui.QLineEdit(self.booleanGroup)
        self.lineTruePattern.setGeometry(QtCore.QRect(80, 20, 231, 20))
        self.lineTruePattern.setObjectName(_fromUtf8("lineTruePattern"))
        self.Label_2 = QtGui.QLabel(self.booleanGroup)
        self.Label_2.setGeometry(QtCore.QRect(10, 20, 81, 20))
        self.Label_2.setObjectName(_fromUtf8("Label_2"))
        self.tabs.addTab(self.queryTab, _fromUtf8(""))
        self.dumpTab = QtGui.QWidget()
        self.dumpTab.setObjectName(_fromUtf8("dumpTab"))
        self.label_18 = QtGui.QLabel(self.dumpTab)
        self.label_18.setGeometry(QtCore.QRect(200, 10, 71, 20))
        self.label_18.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.dumpTab)
        self.label_19.setGeometry(QtCore.QRect(10, 40, 71, 20))
        self.label_19.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_20 = QtGui.QLabel(self.dumpTab)
        self.label_20.setGeometry(QtCore.QRect(270, 40, 31, 20))
        self.label_20.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(self.dumpTab)
        self.label_21.setEnabled(True)
        self.label_21.setGeometry(QtCore.QRect(140, 40, 41, 20))
        self.label_21.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.lineTable = QtGui.QLineEdit(self.dumpTab)
        self.lineTable.setGeometry(QtCore.QRect(50, 10, 141, 20))
        self.lineTable.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.lineTable.setObjectName(_fromUtf8("lineTable"))
        self.lineTo = QtGui.QLineEdit(self.dumpTab)
        self.lineTo.setGeometry(QtCore.QRect(310, 40, 71, 20))
        self.lineTo.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.lineTo.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineTo.setObjectName(_fromUtf8("lineTo"))
        self.lineColumns = QtGui.QLineEdit(self.dumpTab)
        self.lineColumns.setGeometry(QtCore.QRect(260, 10, 321, 20))
        self.lineColumns.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.lineColumns.setObjectName(_fromUtf8("lineColumns"))
        self.lineFrom = QtGui.QLineEdit(self.dumpTab)
        self.lineFrom.setEnabled(True)
        self.lineFrom.setGeometry(QtCore.QRect(180, 40, 71, 20))
        self.lineFrom.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.lineFrom.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineFrom.setObjectName(_fromUtf8("lineFrom"))
        self.lineKey = QtGui.QLineEdit(self.dumpTab)
        self.lineKey.setGeometry(QtCore.QRect(80, 40, 41, 20))
        self.lineKey.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.lineKey.setObjectName(_fromUtf8("lineKey"))
        self.label_2 = QtGui.QLabel(self.dumpTab)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 51, 20))
        self.label_2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tableWidget = QtGui.QTableWidget(self.dumpTab)
        self.tableWidget.setGeometry(QtCore.QRect(10, 70, 571, 481))
        self.tableWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget.verticalHeader().setDefaultSectionSize(20)
        self.dmpButton = QtGui.QPushButton(self.dumpTab)
        self.dmpButton.setGeometry(QtCore.QRect(400, 40, 91, 23))
        self.dmpButton.setObjectName(_fromUtf8("dmpButton"))
        self.tabs.addTab(self.dumpTab, _fromUtf8(""))
        self.clearLogButton = QtGui.QToolButton(self.centralwidget)
        self.clearLogButton.setGeometry(QtCore.QRect(810, 570, 81, 21))
        self.clearLogButton.setObjectName(_fromUtf8("clearLogButton"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(10, 580, 571, 16))
        self.progressBar.setAcceptDrops(False)
        self.progressBar.setToolTip(_fromUtf8(""))
        self.progressBar.setStatusTip(_fromUtf8(""))
        self.progressBar.setMaximum(0)
        self.progressBar.setProperty("value", 83210)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setTextDirection(QtGui.QProgressBar.BottomToTop)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.logTxtEdit = QtGui.QTextEdit(self.centralwidget)
        self.logTxtEdit.setGeometry(QtCore.QRect(600, 10, 511, 551))
        self.logTxtEdit.setReadOnly(True)
        self.logTxtEdit.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.logTxtEdit.setObjectName(_fromUtf8("logTxtEdit"))
        MainForm.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1121, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSave = QtGui.QMenu(self.menubar)
        self.menuSave.setObjectName(_fromUtf8("menuSave"))
        self.menuLoad = QtGui.QMenu(self.menubar)
        self.menuLoad.setObjectName(_fromUtf8("menuLoad"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuPlugins = QtGui.QMenu(self.menubar)
        self.menuPlugins.setObjectName(_fromUtf8("menuPlugins"))
        self.menuMssql = QtGui.QMenu(self.menuPlugins)
        self.menuMssql.setObjectName(_fromUtf8("menuMssql"))
        MainForm.setMenuBar(self.menubar)
        self.saveTables = QtGui.QAction(MainForm)
        self.saveTables.setObjectName(_fromUtf8("saveTables"))
        self.saveColumns = QtGui.QAction(MainForm)
        self.saveColumns.setObjectName(_fromUtf8("saveColumns"))
        self.loadTables = QtGui.QAction(MainForm)
        self.loadTables.setObjectName(_fromUtf8("loadTables"))
        self.menuEncoder = QtGui.QAction(MainForm)
        self.menuEncoder.setObjectName(_fromUtf8("menuEncoder"))
        self.saveBases = QtGui.QAction(MainForm)
        self.saveBases.setObjectName(_fromUtf8("saveBases"))
        self.loadBases = QtGui.QAction(MainForm)
        self.loadBases.setObjectName(_fromUtf8("loadBases"))
        self.menuAbout = QtGui.QAction(MainForm)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.csvExport = QtGui.QAction(MainForm)
        self.csvExport.setObjectName(_fromUtf8("csvExport"))
        self.ssSettings = QtGui.QAction(MainForm)
        self.ssSettings.setObjectName(_fromUtf8("ssSettings"))
        self.lsSettings = QtGui.QAction(MainForm)
        self.lsSettings.setObjectName(_fromUtf8("lsSettings"))
        self.qEditor = QtGui.QAction(MainForm)
        self.qEditor.setObjectName(_fromUtf8("qEditor"))
        self.actionFtp = QtGui.QAction(MainForm)
        self.actionFtp.setObjectName(_fromUtf8("actionFtp"))
        self.actionAdd_user = QtGui.QAction(MainForm)
        self.actionAdd_user.setObjectName(_fromUtf8("actionAdd_user"))
        self.actionOpenrowset = QtGui.QAction(MainForm)
        self.actionOpenrowset.setObjectName(_fromUtf8("actionOpenrowset"))
        self.actionXp_cmdshell = QtGui.QAction(MainForm)
        self.actionXp_cmdshell.setObjectName(_fromUtf8("actionXp_cmdshell"))
        self.actionPreferences = QtGui.QAction(MainForm)
        self.actionPreferences.setObjectName(_fromUtf8("actionPreferences"))
        self.actionManual = QtGui.QAction(MainForm)
        self.actionManual.setObjectName(_fromUtf8("actionManual"))
        self.menuSave.addAction(self.saveTables)
        self.menuSave.addAction(self.saveColumns)
        self.menuSave.addAction(self.saveBases)
        self.menuSave.addAction(self.csvExport)
        self.menuSave.addSeparator()
        self.menuSave.addAction(self.ssSettings)
        self.menuLoad.addAction(self.loadTables)
        self.menuLoad.addAction(self.loadBases)
        self.menuLoad.addSeparator()
        self.menuLoad.addAction(self.lsSettings)
        self.menuTools.addAction(self.menuEncoder)
        self.menuTools.addAction(self.qEditor)
        self.menuTools.addAction(self.actionPreferences)
        self.menuHelp.addAction(self.actionManual)
        self.menuHelp.addAction(self.menuAbout)
        self.menuMssql.addAction(self.actionFtp)
        self.menuMssql.addAction(self.actionAdd_user)
        self.menuMssql.addAction(self.actionOpenrowset)
        self.menuMssql.addAction(self.actionXp_cmdshell)
        self.menuPlugins.addAction(self.menuMssql.menuAction())
        self.menubar.addAction(self.menuSave.menuAction())
        self.menubar.addAction(self.menuLoad.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuPlugins.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainForm)
        self.tabs.setCurrentIndex(0)
        self.comboBox.setCurrentIndex(0)
        self.dbTypeBox.setCurrentIndex(0)
        self.comboInjType.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        self.comboBox.setItemText(0, QtGui.QApplication.translate("MainForm", "GET", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("MainForm", "POST", None, QtGui.QApplication.UnicodeUTF8))
        self.lineUrl.setText(QtGui.QApplication.translate("MainForm", "http://192.168.1.53/?db=mssql&id=-1\' or 1=[sub];[cmd]--", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainForm", "URL:", None, QtGui.QApplication.UnicodeUTF8))
        self.textData.setHtml(QtGui.QApplication.translate("MainForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("MainForm", "Data:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainForm", "Task", None, QtGui.QApplication.UnicodeUTF8))
        self.treeOfTables.setSortingEnabled(False)
        self.treeOfTables.headerItem().setText(0, QtGui.QApplication.translate("MainForm", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.radioTables.setText(QtGui.QApplication.translate("MainForm", "Tables", None, QtGui.QApplication.UnicodeUTF8))
        self.radioColumns.setText(QtGui.QApplication.translate("MainForm", "Columns", None, QtGui.QApplication.UnicodeUTF8))
        self.radioBases.setText(QtGui.QApplication.translate("MainForm", "Bases", None, QtGui.QApplication.UnicodeUTF8))
        self.runButton.setText(QtGui.QApplication.translate("MainForm", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainForm", "Database:", None, QtGui.QApplication.UnicodeUTF8))
        self.cleanColumnsButton.setText(QtGui.QApplication.translate("MainForm", "Clean", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainForm", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.radioOrdinalPosition.setText(QtGui.QApplication.translate("MainForm", "ordinal_position", None, QtGui.QApplication.UnicodeUTF8))
        self.radioNotInArray.setText(QtGui.QApplication.translate("MainForm", "not in(array)", None, QtGui.QApplication.UnicodeUTF8))
        self.radioNotInSubstring.setText(QtGui.QApplication.translate("MainForm", "not in(substring)", None, QtGui.QApplication.UnicodeUTF8))
        self.dbTypeBox.setItemText(0, QtGui.QApplication.translate("MainForm", "MSSQL", None, QtGui.QApplication.UnicodeUTF8))
        self.dbTypeBox.setItemText(1, QtGui.QApplication.translate("MainForm", "MySQL", None, QtGui.QApplication.UnicodeUTF8))
        self.comboInjType.setItemText(0, QtGui.QApplication.translate("MainForm", "ERROR-BASED", None, QtGui.QApplication.UnicodeUTF8))
        self.comboInjType.setItemText(1, QtGui.QApplication.translate("MainForm", "UNION-BASED", None, QtGui.QApplication.UnicodeUTF8))
        self.radioLimit.setText(QtGui.QApplication.translate("MainForm", "LIMIT", None, QtGui.QApplication.UnicodeUTF8))
        self.headersButton.setText(QtGui.QApplication.translate("MainForm", "Headers", None, QtGui.QApplication.UnicodeUTF8))
        self.killButton.setText(QtGui.QApplication.translate("MainForm", "Kill all", None, QtGui.QApplication.UnicodeUTF8))
        self.logButton.setText(QtGui.QApplication.translate("MainForm", "Show log", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.db_structureTab), QtGui.QApplication.translate("MainForm", "Structure", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainForm", "Query", None, QtGui.QApplication.UnicodeUTF8))
        self.queryButton.setText(QtGui.QApplication.translate("MainForm", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.blindMethodList.setItemText(0, QtGui.QApplication.translate("MainForm", "Time", None, QtGui.QApplication.UnicodeUTF8))
        self.blindMethodList.setItemText(1, QtGui.QApplication.translate("MainForm", "Boolean", None, QtGui.QApplication.UnicodeUTF8))
        self.isStacked.setText(QtGui.QApplication.translate("MainForm", "Stacked", None, QtGui.QApplication.UnicodeUTF8))
        self.isHexed.setText(QtGui.QApplication.translate("MainForm", "Hex", None, QtGui.QApplication.UnicodeUTF8))
        self.methodLabel.setText(QtGui.QApplication.translate("MainForm", "Method:", None, QtGui.QApplication.UnicodeUTF8))
        self.resultGroup.setTitle(QtGui.QApplication.translate("MainForm", "Result", None, QtGui.QApplication.UnicodeUTF8))
        self.timeGroup.setTitle(QtGui.QApplication.translate("MainForm", "Time-based options", None, QtGui.QApplication.UnicodeUTF8))
        self.delayLabel.setText(QtGui.QApplication.translate("MainForm", "Delay:", None, QtGui.QApplication.UnicodeUTF8))
        self.trueTimeLabel.setText(QtGui.QApplication.translate("MainForm", "\'True\' time:", None, QtGui.QApplication.UnicodeUTF8))
        self.isAuto.setText(QtGui.QApplication.translate("MainForm", "Autodetect", None, QtGui.QApplication.UnicodeUTF8))
        self.lagLabel.setText(QtGui.QApplication.translate("MainForm", "Max lag time (+):", None, QtGui.QApplication.UnicodeUTF8))
        self.testButton.setText(QtGui.QApplication.translate("MainForm", "Test", None, QtGui.QApplication.UnicodeUTF8))
        self.booleanGroup.setTitle(QtGui.QApplication.translate("MainForm", "Boolean-based options", None, QtGui.QApplication.UnicodeUTF8))
        self.Label_2.setText(QtGui.QApplication.translate("MainForm", "\'True\' pattern:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.queryTab), QtGui.QApplication.translate("MainForm", "Query", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("MainForm", "Columns:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("MainForm", "Primary key:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("MainForm", "To:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("MainForm", "From:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineTable.setText(QtGui.QApplication.translate("MainForm", "customers", None, QtGui.QApplication.UnicodeUTF8))
        self.lineTo.setText(QtGui.QApplication.translate("MainForm", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.lineColumns.setText(QtGui.QApplication.translate("MainForm", "id;username;password;email", None, QtGui.QApplication.UnicodeUTF8))
        self.lineFrom.setText(QtGui.QApplication.translate("MainForm", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.lineKey.setText(QtGui.QApplication.translate("MainForm", "id", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainForm", "Table:", None, QtGui.QApplication.UnicodeUTF8))
        self.dmpButton.setText(QtGui.QApplication.translate("MainForm", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.dumpTab), QtGui.QApplication.translate("MainForm", "Dump", None, QtGui.QApplication.UnicodeUTF8))
        self.clearLogButton.setText(QtGui.QApplication.translate("MainForm", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.progressBar.setFormat(QtGui.QApplication.translate("MainForm", "%p%", None, QtGui.QApplication.UnicodeUTF8))
        self.logTxtEdit.setHtml(QtGui.QApplication.translate("MainForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSave.setTitle(QtGui.QApplication.translate("MainForm", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.menuLoad.setTitle(QtGui.QApplication.translate("MainForm", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTools.setTitle(QtGui.QApplication.translate("MainForm", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainForm", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuPlugins.setTitle(QtGui.QApplication.translate("MainForm", "Plugins", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMssql.setTitle(QtGui.QApplication.translate("MainForm", "mssql", None, QtGui.QApplication.UnicodeUTF8))
        self.saveTables.setText(QtGui.QApplication.translate("MainForm", "Tables", None, QtGui.QApplication.UnicodeUTF8))
        self.saveColumns.setText(QtGui.QApplication.translate("MainForm", "Columns", None, QtGui.QApplication.UnicodeUTF8))
        self.loadTables.setText(QtGui.QApplication.translate("MainForm", "Tables", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEncoder.setText(QtGui.QApplication.translate("MainForm", "Encoder", None, QtGui.QApplication.UnicodeUTF8))
        self.saveBases.setText(QtGui.QApplication.translate("MainForm", "Bases", None, QtGui.QApplication.UnicodeUTF8))
        self.loadBases.setText(QtGui.QApplication.translate("MainForm", "Bases", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setText(QtGui.QApplication.translate("MainForm", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.csvExport.setText(QtGui.QApplication.translate("MainForm", "Dump to csv", None, QtGui.QApplication.UnicodeUTF8))
        self.ssSettings.setText(QtGui.QApplication.translate("MainForm", "Site settings", None, QtGui.QApplication.UnicodeUTF8))
        self.ssSettings.setShortcut(QtGui.QApplication.translate("MainForm", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.lsSettings.setText(QtGui.QApplication.translate("MainForm", "Site settings", None, QtGui.QApplication.UnicodeUTF8))
        self.lsSettings.setShortcut(QtGui.QApplication.translate("MainForm", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.qEditor.setText(QtGui.QApplication.translate("MainForm", "Query editor", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFtp.setText(QtGui.QApplication.translate("MainForm", "ftp", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_user.setText(QtGui.QApplication.translate("MainForm", "add_user", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpenrowset.setText(QtGui.QApplication.translate("MainForm", "openrowset", None, QtGui.QApplication.UnicodeUTF8))
        self.actionXp_cmdshell.setText(QtGui.QApplication.translate("MainForm", "xp_cmdshell", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate("MainForm", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionManual.setText(QtGui.QApplication.translate("MainForm", "Manual", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainForm = QtGui.QMainWindow()
    ui = Ui_MainForm()
    ui.setupUi(MainForm)
    MainForm.show()
    sys.exit(app.exec_())

