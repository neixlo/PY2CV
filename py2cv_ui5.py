# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Admin\AppData\Local\Temp\tmplzpbx1xd'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(800, 696)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/opencv.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 2)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setSpacing(6)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.bOpenFile = QtWidgets.QPushButton(self.centralwidget)
        self.bOpenFile.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/icons8-full-image-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bOpenFile.setIcon(icon1)
        self.bOpenFile.setIconSize(QtCore.QSize(64, 64))
        self.bOpenFile.setObjectName("bOpenFile")
        self.horizontalLayout_16.addWidget(self.bOpenFile)
        self.bOpenCamera = QtWidgets.QPushButton(self.centralwidget)
        self.bOpenCamera.setEnabled(True)
        self.bOpenCamera.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/icons8-lens-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bOpenCamera.setIcon(icon2)
        self.bOpenCamera.setIconSize(QtCore.QSize(64, 64))
        self.bOpenCamera.setObjectName("bOpenCamera")
        self.horizontalLayout_16.addWidget(self.bOpenCamera)
        self.bAddLayout = QtWidgets.QPushButton(self.centralwidget)
        self.bAddLayout.setEnabled(False)
        self.bAddLayout.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/icons8-add-property-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bAddLayout.setIcon(icon3)
        self.bAddLayout.setIconSize(QtCore.QSize(64, 64))
        self.bAddLayout.setObjectName("bAddLayout")
        self.horizontalLayout_16.addWidget(self.bAddLayout)
        self.bExport = QtWidgets.QPushButton(self.centralwidget)
        self.bExport.setEnabled(False)
        self.bExport.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/icons8-send-file-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bExport.setIcon(icon4)
        self.bExport.setIconSize(QtCore.QSize(64, 64))
        self.bExport.setObjectName("bExport")
        self.horizontalLayout_16.addWidget(self.bExport)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_16)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.mytabWidget = QtWidgets.QTabWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mytabWidget.sizePolicy().hasHeightForWidth())
        self.mytabWidget.setSizePolicy(sizePolicy)
        self.mytabWidget.setMinimumSize(QtCore.QSize(250, 400))
        self.mytabWidget.setAutoFillBackground(False)
        self.mytabWidget.setObjectName("mytabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.blocksCollapsePushButton = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blocksCollapsePushButton.sizePolicy().hasHeightForWidth())
        self.blocksCollapsePushButton.setSizePolicy(sizePolicy)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/collapse-all.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.blocksCollapsePushButton.setIcon(icon5)
        self.blocksCollapsePushButton.setIconSize(QtCore.QSize(24, 24))
        self.blocksCollapsePushButton.setObjectName("blocksCollapsePushButton")
        self.horizontalLayout_5.addWidget(self.blocksCollapsePushButton)
        self.blocksExpandPushButton = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blocksExpandPushButton.sizePolicy().hasHeightForWidth())
        self.blocksExpandPushButton.setSizePolicy(sizePolicy)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/expand-all.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.blocksExpandPushButton.setIcon(icon6)
        self.blocksExpandPushButton.setIconSize(QtCore.QSize(24, 24))
        self.blocksExpandPushButton.setObjectName("blocksExpandPushButton")
        self.horizontalLayout_5.addWidget(self.blocksExpandPushButton)
        spacerItem1 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.layerCreatePushButton = QtWidgets.QPushButton(self.tab)
        self.layerCreatePushButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/list-add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.layerCreatePushButton.setIcon(icon7)
        self.layerCreatePushButton.setIconSize(QtCore.QSize(24, 24))
        self.layerCreatePushButton.setObjectName("layerCreatePushButton")
        self.horizontalLayout_5.addWidget(self.layerCreatePushButton)
        self.layerDeletePushButton = QtWidgets.QPushButton(self.tab)
        self.layerDeletePushButton.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/list-remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.layerDeletePushButton.setIcon(icon8)
        self.layerDeletePushButton.setIconSize(QtCore.QSize(24, 24))
        self.layerDeletePushButton.setObjectName("layerDeletePushButton")
        self.horizontalLayout_5.addWidget(self.layerDeletePushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.entitiesTreeView = TreeView(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entitiesTreeView.sizePolicy().hasHeightForWidth())
        self.entitiesTreeView.setSizePolicy(sizePolicy)
        self.entitiesTreeView.setObjectName("entitiesTreeView")
        self.verticalLayout_3.addWidget(self.entitiesTreeView)
        self.mytabWidget.addTab(self.tab, "")
        self.canvas = Canvas(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(7)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas.sizePolicy().hasHeightForWidth())
        self.canvas.setSizePolicy(sizePolicy)
        self.canvas.setMinimumSize(QtCore.QSize(400, 400))
        self.canvas.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.canvas.setObjectName("canvas")
        self.verticalLayout.addWidget(self.splitter)
        self.messageBox = MessageBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.messageBox.sizePolicy().hasHeightForWidth())
        self.messageBox.setSizePolicy(sizePolicy)
        self.messageBox.setMaximumSize(QtCore.QSize(16777215, 100))
        self.messageBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.messageBox.setObjectName("messageBox")
        self.verticalLayout.addWidget(self.messageBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuExport = QtWidgets.QMenu(self.menubar)
        self.menuExport.setEnabled(True)
        self.menuExport.setObjectName("menuExport")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon9)
        self.actionClose.setObjectName("actionClose")
        self.actionShowPathDirections = QtWidgets.QAction(MainWindow)
        self.actionShowPathDirections.setCheckable(True)
        self.actionShowPathDirections.setChecked(False)
        self.actionShowPathDirections.setEnabled(False)
        self.actionShowPathDirections.setObjectName("actionShowPathDirections")
        self.actionShowDisabledPaths = QtWidgets.QAction(MainWindow)
        self.actionShowDisabledPaths.setCheckable(True)
        self.actionShowDisabledPaths.setChecked(False)
        self.actionShowDisabledPaths.setEnabled(False)
        self.actionShowDisabledPaths.setObjectName("actionShowDisabledPaths")
        self.actionAutoscale = QtWidgets.QAction(MainWindow)
        self.actionAutoscale.setEnabled(False)
        self.actionAutoscale.setObjectName("actionAutoscale")
        self.actionDeleteG0Paths = QtWidgets.QAction(MainWindow)
        self.actionDeleteG0Paths.setEnabled(False)
        self.actionDeleteG0Paths.setObjectName("actionDeleteG0Paths")
        self.actionConfiguration = QtWidgets.QAction(MainWindow)
        self.actionConfiguration.setObjectName("actionConfiguration")
        self.actionConfigurationPostprocessor = QtWidgets.QAction(MainWindow)
        self.actionConfigurationPostprocessor.setObjectName("actionConfigurationPostprocessor")
        self.actionTolerances = QtWidgets.QAction(MainWindow)
        self.actionTolerances.setObjectName("actionTolerances")
        self.actionScaleAll = QtWidgets.QAction(MainWindow)
        self.actionScaleAll.setEnabled(False)
        self.actionScaleAll.setObjectName("actionScaleAll")
        self.actionRotateAll = QtWidgets.QAction(MainWindow)
        self.actionRotateAll.setEnabled(False)
        self.actionRotateAll.setObjectName("actionRotateAll")
        self.actionMoveWorkpieceZero = QtWidgets.QAction(MainWindow)
        self.actionMoveWorkpieceZero.setEnabled(False)
        self.actionMoveWorkpieceZero.setObjectName("actionMoveWorkpieceZero")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionOptimizePaths = QtWidgets.QAction(MainWindow)
        self.actionOptimizePaths.setEnabled(False)
        self.actionOptimizePaths.setObjectName("actionOptimizePaths")
        self.actionExportShapes = QtWidgets.QAction(MainWindow)
        self.actionExportShapes.setEnabled(False)
        self.actionExportShapes.setObjectName("actionExportShapes")
        self.actionOptimizeAndExportShapes = QtWidgets.QAction(MainWindow)
        self.actionOptimizeAndExportShapes.setEnabled(False)
        self.actionOptimizeAndExportShapes.setObjectName("actionOptimizeAndExportShapes")
        self.actionLiveUpdateExportRoute = QtWidgets.QAction(MainWindow)
        self.actionLiveUpdateExportRoute.setCheckable(True)
        self.actionLiveUpdateExportRoute.setEnabled(False)
        self.actionLiveUpdateExportRoute.setObjectName("actionLiveUpdateExportRoute")
        self.actionReload = QtWidgets.QAction(MainWindow)
        self.actionReload.setEnabled(False)
        self.actionReload.setObjectName("actionReload")
        self.actionSplitLineSegments = QtWidgets.QAction(MainWindow)
        self.actionSplitLineSegments.setCheckable(True)
        self.actionSplitLineSegments.setObjectName("actionSplitLineSegments")
        self.actionAutomaticCutterCompensation = QtWidgets.QAction(MainWindow)
        self.actionAutomaticCutterCompensation.setCheckable(True)
        self.actionAutomaticCutterCompensation.setEnabled(False)
        self.actionAutomaticCutterCompensation.setObjectName("actionAutomaticCutterCompensation")
        self.actionLaserCut = QtWidgets.QAction(MainWindow)
        self.actionLaserCut.setCheckable(True)
        self.actionLaserCut.setObjectName("actionLaserCut")
        self.actionMilling = QtWidgets.QAction(MainWindow)
        self.actionMilling.setCheckable(True)
        self.actionMilling.setObjectName("actionMilling")
        self.actionDragKnife = QtWidgets.QAction(MainWindow)
        self.actionDragKnife.setCheckable(True)
        self.actionDragKnife.setObjectName("actionDragKnife")
        self.actionLathe = QtWidgets.QAction(MainWindow)
        self.actionLathe.setCheckable(True)
        self.actionLathe.setObjectName("actionLathe")
        self.actionTopView = QtWidgets.QAction(MainWindow)
        self.actionTopView.setEnabled(False)
        self.actionTopView.setObjectName("actionTopView")
        self.actionIsometricView = QtWidgets.QAction(MainWindow)
        self.actionIsometricView.setEnabled(False)
        self.actionIsometricView.setObjectName("actionIsometricView")
        self.actionSaveProjectAs = QtWidgets.QAction(MainWindow)
        self.actionSaveProjectAs.setEnabled(False)
        self.actionSaveProjectAs.setObjectName("actionSaveProjectAs")
        self.actionMillimeters = QtWidgets.QAction(MainWindow)
        self.actionMillimeters.setCheckable(True)
        self.actionMillimeters.setEnabled(True)
        self.actionMillimeters.setObjectName("actionMillimeters")
        self.actionInches = QtWidgets.QAction(MainWindow)
        self.actionInches.setCheckable(True)
        self.actionInches.setObjectName("actionInches")
        self.actionOpenFile = QtWidgets.QAction(MainWindow)
        self.actionOpenFile.setObjectName("actionOpenFile")
        self.actionOpenFloder = QtWidgets.QAction(MainWindow)
        self.actionOpenFloder.setObjectName("actionOpenFloder")
        self.actionOpenCamera = QtWidgets.QAction(MainWindow)
        self.actionOpenCamera.setObjectName("actionOpenCamera")
        self.actionImageExport = QtWidgets.QAction(MainWindow)
        self.actionImageExport.setEnabled(False)
        self.actionImageExport.setShortcut("")
        self.actionImageExport.setObjectName("actionImageExport")
        self.menuFile.addAction(self.actionOpenFile)
        self.menuFile.addAction(self.actionOpenCamera)
        self.menuFile.addAction(self.actionReload)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSaveProjectAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addSeparator()
        self.menuView.addAction(self.actionAutoscale)
        self.menuOptions.addAction(self.actionConfiguration)
        self.menuOptions.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuExport.addAction(self.actionImageExport)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuExport.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.mytabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.mytabWidget, self.entitiesTreeView)
        MainWindow.setTabOrder(self.entitiesTreeView, self.blocksCollapsePushButton)
        MainWindow.setTabOrder(self.blocksCollapsePushButton, self.blocksExpandPushButton)
        MainWindow.setTabOrder(self.blocksExpandPushButton, self.canvas)
        MainWindow.setTabOrder(self.canvas, self.messageBox)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PY2CV"))
        self.bOpenFile.setToolTip(_translate("MainWindow", "Import File or Project"))
        self.bOpenCamera.setToolTip(_translate("MainWindow", "Open Camera"))
        self.bAddLayout.setToolTip(_translate("MainWindow", "Add Layer"))
        self.bExport.setToolTip(_translate("MainWindow", "Export"))
        self.blocksCollapsePushButton.setToolTip(_translate("MainWindow", "Collapse all items"))
        self.blocksExpandPushButton.setToolTip(_translate("MainWindow", "Expand all items"))
        self.mytabWidget.setTabText(self.mytabWidget.indexOf(self.tab), _translate("MainWindow", "Layout"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menuView.setTitle(_translate("MainWindow", "&View"))
        self.menuOptions.setTitle(_translate("MainWindow", "&Options"))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help"))
        self.menuExport.setStatusTip(_translate("MainWindow", "Export the current project to G-Code"))
        self.menuExport.setTitle(_translate("MainWindow", "&Export"))
        self.actionOpen.setText(_translate("MainWindow", "&Open..."))
        self.actionOpen.setStatusTip(_translate("MainWindow", "Load DXF or other supported document"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionClose.setText(_translate("MainWindow", "&Exit"))
        self.actionClose.setStatusTip(_translate("MainWindow", "Exit PY2CV and close window"))
        self.actionClose.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionShowPathDirections.setText(_translate("MainWindow", "&Show Path Directions"))
        self.actionShowPathDirections.setStatusTip(_translate("MainWindow", "Always shows the path direction in the plot (not only while selected)"))
        self.actionShowDisabledPaths.setText(_translate("MainWindow", "Show Disabled &Paths"))
        self.actionAutoscale.setText(_translate("MainWindow", "&Autoscale"))
        self.actionAutoscale.setShortcut(_translate("MainWindow", "Ctrl+Shift+V"))
        self.actionDeleteG0Paths.setText(_translate("MainWindow", "&Delete G0 Paths"))
        self.actionConfiguration.setText(_translate("MainWindow", "&Configuration..."))
        self.actionConfiguration.setShortcut(_translate("MainWindow", "Ctrl+Shift+C"))
        self.actionConfigurationPostprocessor.setText(_translate("MainWindow", "&Postprocessor configuration..."))
        self.actionConfigurationPostprocessor.setShortcut(_translate("MainWindow", "Ctrl+Shift+P"))
        self.actionTolerances.setText(_translate("MainWindow", "&Tolerances"))
        self.actionScaleAll.setText(_translate("MainWindow", "&Scale All"))
        self.actionRotateAll.setText(_translate("MainWindow", "&Rotate All"))
        self.actionMoveWorkpieceZero.setText(_translate("MainWindow", "&Move Workpiece Zero"))
        self.actionAbout.setText(_translate("MainWindow", "&About"))
        self.actionOptimizePaths.setText(_translate("MainWindow", "&Optimize Paths"))
        self.actionOptimizePaths.setShortcut(_translate("MainWindow", "Ctrl+Shift+O"))
        self.actionExportShapes.setText(_translate("MainWindow", "&Export Shapes"))
        self.actionExportShapes.setShortcut(_translate("MainWindow", "Ctrl+Shift+E"))
        self.actionOptimizeAndExportShapes.setText(_translate("MainWindow", "Optimize &and Export Shapes"))
        self.actionOptimizeAndExportShapes.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionLiveUpdateExportRoute.setText(_translate("MainWindow", "&Live Update Export Route"))
        self.actionReload.setText(_translate("MainWindow", "&Reload"))
        self.actionReload.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionSplitLineSegments.setText(_translate("MainWindow", "Split &Line Segments"))
        self.actionSplitLineSegments.setStatusTip(_translate("MainWindow", "Split line segments, e.g. can be used for compensation (G41/G42) in combination with EMC"))
        self.actionAutomaticCutterCompensation.setText(_translate("MainWindow", "&Automatic Cutter Compensation"))
        self.actionLaserCut.setText(_translate("MainWindow", "&LaserCut"))
        self.actionMilling.setText(_translate("MainWindow", "&Milling"))
        self.actionDragKnife.setText(_translate("MainWindow", "&Drag Knife"))
        self.actionLathe.setText(_translate("MainWindow", "&Lathe"))
        self.actionTopView.setText(_translate("MainWindow", "&Top View"))
        self.actionTopView.setShortcut(_translate("MainWindow", "Ctrl+V, T"))
        self.actionIsometricView.setText(_translate("MainWindow", "&Isometric View"))
        self.actionIsometricView.setShortcut(_translate("MainWindow", "Ctrl+V, I"))
        self.actionSaveProjectAs.setText(_translate("MainWindow", "&Save Project As..."))
        self.actionSaveProjectAs.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionMillimeters.setText(_translate("MainWindow", "&Millimeters"))
        self.actionInches.setText(_translate("MainWindow", "&Inches"))
        self.actionOpenFile.setText(_translate("MainWindow", "OpenFile..."))
        self.actionOpenFile.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionOpenFloder.setText(_translate("MainWindow", "OpenFloder..."))
        self.actionOpenCamera.setText(_translate("MainWindow", "OpenCamera"))
        self.actionOpenCamera.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionImageExport.setText(_translate("MainWindow", "Export Image"))
from py2cv.gui.canvas import Canvas
from py2cv.gui.messagebox import MessageBox
from py2cv.gui.treeview import TreeView
import py2cv_images5_rc
