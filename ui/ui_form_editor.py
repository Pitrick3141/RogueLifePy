# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormEditor.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_FormEditor(object):
    def setupUi(self, FormEditor):
        if not FormEditor.objectName():
            FormEditor.setObjectName(u"FormEditor")
        FormEditor.resize(1440, 900)
        self.centralwidget = QWidget(FormEditor)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 1441, 851))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 0, 5, 0)
        self.gridLayoutList = QGridLayout()
        self.gridLayoutList.setSpacing(10)
        self.gridLayoutList.setObjectName(u"gridLayoutList")
        self.gridLayoutList.setContentsMargins(5, 0, 5, 0)
        self.groupActions = QGroupBox(self.horizontalLayoutWidget)
        self.groupActions.setObjectName(u"groupActions")
        self.listActions = QListWidget(self.groupActions)
        self.listActions.setObjectName(u"listActions")
        self.listActions.setGeometry(QRect(10, 20, 331, 391))

        self.gridLayoutList.addWidget(self.groupActions, 1, 1, 1, 1)

        self.groupEvents = QGroupBox(self.horizontalLayoutWidget)
        self.groupEvents.setObjectName(u"groupEvents")
        self.listEvents = QListWidget(self.groupEvents)
        self.listEvents.setObjectName(u"listEvents")
        self.listEvents.setGeometry(QRect(10, 20, 331, 391))

        self.gridLayoutList.addWidget(self.groupEvents, 1, 0, 1, 1)

        self.groupChallenges = QGroupBox(self.horizontalLayoutWidget)
        self.groupChallenges.setObjectName(u"groupChallenges")
        self.listChallenges = QListWidget(self.groupChallenges)
        self.listChallenges.setObjectName(u"listChallenges")
        self.listChallenges.setGeometry(QRect(10, 20, 331, 391))

        self.gridLayoutList.addWidget(self.groupChallenges, 0, 1, 1, 1)

        self.groupItems = QGroupBox(self.horizontalLayoutWidget)
        self.groupItems.setObjectName(u"groupItems")
        self.listItems = QListWidget(self.groupItems)
        self.listItems.setObjectName(u"listItems")
        self.listItems.setGeometry(QRect(10, 20, 331, 391))

        self.gridLayoutList.addWidget(self.groupItems, 0, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayoutList)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, -1, 10, -1)
        self.groupEdit = QGroupBox(self.horizontalLayoutWidget)
        self.groupEdit.setObjectName(u"groupEdit")
        self.tabEdit = QTabWidget(self.groupEdit)
        self.tabEdit.setObjectName(u"tabEdit")
        self.tabEdit.setGeometry(QRect(0, 20, 681, 401))
        self.tabBasic = QWidget()
        self.tabBasic.setObjectName(u"tabBasic")
        self.frameIndex = QFrame(self.tabBasic)
        self.frameIndex.setObjectName(u"frameIndex")
        self.frameIndex.setGeometry(QRect(0, 10, 200, 50))
        self.frameIndex.setFrameShape(QFrame.StyledPanel)
        self.frameIndex.setFrameShadow(QFrame.Raised)
        self.labelIndex = QLabel(self.frameIndex)
        self.labelIndex.setObjectName(u"labelIndex")
        self.labelIndex.setGeometry(QRect(10, 10, 54, 16))
        self.lineIndex = QLineEdit(self.frameIndex)
        self.lineIndex.setObjectName(u"lineIndex")
        self.lineIndex.setGeometry(QRect(50, 10, 131, 20))
        self.frameName = QFrame(self.tabBasic)
        self.frameName.setObjectName(u"frameName")
        self.frameName.setGeometry(QRect(0, 60, 200, 50))
        self.frameName.setFrameShape(QFrame.StyledPanel)
        self.frameName.setFrameShadow(QFrame.Raised)
        self.labelName = QLabel(self.frameName)
        self.labelName.setObjectName(u"labelName")
        self.labelName.setGeometry(QRect(10, 10, 54, 16))
        self.lineName = QLineEdit(self.frameName)
        self.lineName.setObjectName(u"lineName")
        self.lineName.setGeometry(QRect(50, 10, 131, 20))
        self.frame_2 = QFrame(self.tabBasic)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(420, 10, 251, 361))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.tabEdit.addTab(self.tabBasic, "")
        self.tabText = QWidget()
        self.tabText.setObjectName(u"tabText")
        self.frameDes = QFrame(self.tabText)
        self.frameDes.setObjectName(u"frameDes")
        self.frameDes.setGeometry(QRect(0, 150, 671, 221))
        self.frameDes.setFrameShape(QFrame.StyledPanel)
        self.frameDes.setFrameShadow(QFrame.Raised)
        self.labelDes = QLabel(self.frameDes)
        self.labelDes.setObjectName(u"labelDes")
        self.labelDes.setGeometry(QRect(10, 10, 54, 16))
        self.textDes = QPlainTextEdit(self.frameDes)
        self.textDes.setObjectName(u"textDes")
        self.textDes.setGeometry(QRect(10, 30, 661, 181))
        self.frameEff = QFrame(self.tabText)
        self.frameEff.setObjectName(u"frameEff")
        self.frameEff.setGeometry(QRect(0, 0, 671, 151))
        self.frameEff.setFrameShape(QFrame.StyledPanel)
        self.frameEff.setFrameShadow(QFrame.Raised)
        self.labelEff = QLabel(self.frameEff)
        self.labelEff.setObjectName(u"labelEff")
        self.labelEff.setGeometry(QRect(10, 10, 54, 16))
        self.textEff = QPlainTextEdit(self.frameEff)
        self.textEff.setObjectName(u"textEff")
        self.textEff.setGeometry(QRect(10, 30, 661, 111))
        self.tabEdit.addTab(self.tabText, "")
        self.tabResults = QWidget()
        self.tabResults.setObjectName(u"tabResults")
        self.frameDisplayGeneral = QFrame(self.tabResults)
        self.frameDisplayGeneral.setObjectName(u"frameDisplayGeneral")
        self.frameDisplayGeneral.setGeometry(QRect(0, 0, 671, 131))
        self.frameDisplayGeneral.setFrameShape(QFrame.StyledPanel)
        self.frameDisplayGeneral.setFrameShadow(QFrame.Raised)
        self.labelDisplayGeneral = QLabel(self.frameDisplayGeneral)
        self.labelDisplayGeneral.setObjectName(u"labelDisplayGeneral")
        self.labelDisplayGeneral.setGeometry(QRect(10, 10, 151, 16))
        self.textDisplayGeneral = QPlainTextEdit(self.frameDisplayGeneral)
        self.textDisplayGeneral.setObjectName(u"textDisplayGeneral")
        self.textDisplayGeneral.setGeometry(QRect(10, 30, 661, 91))
        self.frameDisplaySuccess = QFrame(self.tabResults)
        self.frameDisplaySuccess.setObjectName(u"frameDisplaySuccess")
        self.frameDisplaySuccess.setGeometry(QRect(0, 130, 671, 121))
        self.frameDisplaySuccess.setFrameShape(QFrame.StyledPanel)
        self.frameDisplaySuccess.setFrameShadow(QFrame.Raised)
        self.labelDisplaySuccess = QLabel(self.frameDisplaySuccess)
        self.labelDisplaySuccess.setObjectName(u"labelDisplaySuccess")
        self.labelDisplaySuccess.setGeometry(QRect(10, 10, 151, 16))
        self.textDisplaySuccess = QPlainTextEdit(self.frameDisplaySuccess)
        self.textDisplaySuccess.setObjectName(u"textDisplaySuccess")
        self.textDisplaySuccess.setGeometry(QRect(10, 30, 661, 81))
        self.frameDisplayFailure = QFrame(self.tabResults)
        self.frameDisplayFailure.setObjectName(u"frameDisplayFailure")
        self.frameDisplayFailure.setGeometry(QRect(0, 250, 671, 121))
        self.frameDisplayFailure.setFrameShape(QFrame.StyledPanel)
        self.frameDisplayFailure.setFrameShadow(QFrame.Raised)
        self.labelDisplayFailure = QLabel(self.frameDisplayFailure)
        self.labelDisplayFailure.setObjectName(u"labelDisplayFailure")
        self.labelDisplayFailure.setGeometry(QRect(10, 10, 151, 16))
        self.textDisplayFailure = QPlainTextEdit(self.frameDisplayFailure)
        self.textDisplayFailure.setObjectName(u"textDisplayFailure")
        self.textDisplayFailure.setGeometry(QRect(10, 30, 661, 81))
        self.tabEdit.addTab(self.tabResults, "")
        self.tabPossibility = QWidget()
        self.tabPossibility.setObjectName(u"tabPossibility")
        self.frameRequire = QFrame(self.tabPossibility)
        self.frameRequire.setObjectName(u"frameRequire")
        self.frameRequire.setGeometry(QRect(0, 50, 341, 321))
        self.frameRequire.setFrameShape(QFrame.StyledPanel)
        self.frameRequire.setFrameShadow(QFrame.Raised)
        self.labelRequire = QLabel(self.frameRequire)
        self.labelRequire.setObjectName(u"labelRequire")
        self.labelRequire.setGeometry(QRect(10, 10, 101, 16))
        self.listRequire = QListWidget(self.frameRequire)
        self.listRequire.setObjectName(u"listRequire")
        self.listRequire.setGeometry(QRect(10, 40, 241, 271))
        self.buttonAddRequire = QPushButton(self.frameRequire)
        self.buttonAddRequire.setObjectName(u"buttonAddRequire")
        self.buttonAddRequire.setGeometry(QRect(260, 40, 75, 24))
        self.buttonRemoveRequire = QPushButton(self.frameRequire)
        self.buttonRemoveRequire.setObjectName(u"buttonRemoveRequire")
        self.buttonRemoveRequire.setGeometry(QRect(260, 70, 75, 24))
        self.buttonClearRequire = QPushButton(self.frameRequire)
        self.buttonClearRequire.setObjectName(u"buttonClearRequire")
        self.buttonClearRequire.setGeometry(QRect(260, 100, 75, 24))
        self.lineRequire = QLineEdit(self.frameRequire)
        self.lineRequire.setObjectName(u"lineRequire")
        self.lineRequire.setGeometry(QRect(210, 10, 113, 20))
        self.frameExclude = QFrame(self.tabPossibility)
        self.frameExclude.setObjectName(u"frameExclude")
        self.frameExclude.setGeometry(QRect(340, 50, 341, 321))
        self.frameExclude.setFrameShape(QFrame.StyledPanel)
        self.frameExclude.setFrameShadow(QFrame.Raised)
        self.labelExclude = QLabel(self.frameExclude)
        self.labelExclude.setObjectName(u"labelExclude")
        self.labelExclude.setGeometry(QRect(10, 10, 101, 16))
        self.listExclude = QListWidget(self.frameExclude)
        self.listExclude.setObjectName(u"listExclude")
        self.listExclude.setGeometry(QRect(10, 40, 241, 271))
        self.buttonAddExclude = QPushButton(self.frameExclude)
        self.buttonAddExclude.setObjectName(u"buttonAddExclude")
        self.buttonAddExclude.setGeometry(QRect(260, 40, 75, 24))
        self.buttonRemoveExclude = QPushButton(self.frameExclude)
        self.buttonRemoveExclude.setObjectName(u"buttonRemoveExclude")
        self.buttonRemoveExclude.setGeometry(QRect(260, 70, 75, 24))
        self.buttonClearExclude = QPushButton(self.frameExclude)
        self.buttonClearExclude.setObjectName(u"buttonClearExclude")
        self.buttonClearExclude.setGeometry(QRect(260, 100, 75, 24))
        self.lineExclude = QLineEdit(self.frameExclude)
        self.lineExclude.setObjectName(u"lineExclude")
        self.lineExclude.setGeometry(QRect(210, 10, 113, 20))
        self.checkExcluisive = QCheckBox(self.tabPossibility)
        self.checkExcluisive.setObjectName(u"checkExcluisive")
        self.checkExcluisive.setGeometry(QRect(10, 10, 79, 20))
        self.labelPoss = QLabel(self.tabPossibility)
        self.labelPoss.setObjectName(u"labelPoss")
        self.labelPoss.setGeometry(QRect(160, 10, 54, 16))
        self.linePoss = QLineEdit(self.tabPossibility)
        self.linePoss.setObjectName(u"linePoss")
        self.linePoss.setGeometry(QRect(220, 10, 141, 20))
        self.tabEdit.addTab(self.tabPossibility, "")
        self.tabAdjustment = QWidget()
        self.tabAdjustment.setObjectName(u"tabAdjustment")
        self.frameAdjustment = QFrame(self.tabAdjustment)
        self.frameAdjustment.setObjectName(u"frameAdjustment")
        self.frameAdjustment.setGeometry(QRect(0, 0, 331, 371))
        self.frameAdjustment.setFrameShape(QFrame.StyledPanel)
        self.frameAdjustment.setFrameShadow(QFrame.Raised)
        self.labelAdjustment = QLabel(self.frameAdjustment)
        self.labelAdjustment.setObjectName(u"labelAdjustment")
        self.labelAdjustment.setGeometry(QRect(10, 10, 101, 16))
        self.listAdjustment = QListWidget(self.frameAdjustment)
        self.listAdjustment.setObjectName(u"listAdjustment")
        self.listAdjustment.setGeometry(QRect(10, 31, 201, 331))
        self.labelAdjustmentName = QLabel(self.frameAdjustment)
        self.labelAdjustmentName.setObjectName(u"labelAdjustmentName")
        self.labelAdjustmentName.setGeometry(QRect(220, 10, 54, 16))
        self.lineAdjustmentName = QLineEdit(self.frameAdjustment)
        self.lineAdjustmentName.setObjectName(u"lineAdjustmentName")
        self.lineAdjustmentName.setGeometry(QRect(220, 30, 101, 20))
        self.labelAdjustmentValue = QLabel(self.frameAdjustment)
        self.labelAdjustmentValue.setObjectName(u"labelAdjustmentValue")
        self.labelAdjustmentValue.setGeometry(QRect(220, 60, 54, 16))
        self.lineAdjustmentValue = QLineEdit(self.frameAdjustment)
        self.lineAdjustmentValue.setObjectName(u"lineAdjustmentValue")
        self.lineAdjustmentValue.setGeometry(QRect(220, 80, 101, 20))
        self.buttonAddAdjustment = QPushButton(self.frameAdjustment)
        self.buttonAddAdjustment.setObjectName(u"buttonAddAdjustment")
        self.buttonAddAdjustment.setGeometry(QRect(220, 110, 75, 24))
        self.buttonRemoveAdjustment = QPushButton(self.frameAdjustment)
        self.buttonRemoveAdjustment.setObjectName(u"buttonRemoveAdjustment")
        self.buttonRemoveAdjustment.setGeometry(QRect(220, 140, 75, 24))
        self.buttonClearAdjustment = QPushButton(self.frameAdjustment)
        self.buttonClearAdjustment.setObjectName(u"buttonClearAdjustment")
        self.buttonClearAdjustment.setGeometry(QRect(220, 170, 75, 24))
        self.frameRequiredAdjustment = QFrame(self.tabAdjustment)
        self.frameRequiredAdjustment.setObjectName(u"frameRequiredAdjustment")
        self.frameRequiredAdjustment.setGeometry(QRect(330, 0, 341, 371))
        self.frameRequiredAdjustment.setFrameShape(QFrame.StyledPanel)
        self.frameRequiredAdjustment.setFrameShadow(QFrame.Raised)
        self.labelRequiredAdjustment = QLabel(self.frameRequiredAdjustment)
        self.labelRequiredAdjustment.setObjectName(u"labelRequiredAdjustment")
        self.labelRequiredAdjustment.setGeometry(QRect(10, 10, 121, 16))
        self.listRequiredAdjustment = QListWidget(self.frameRequiredAdjustment)
        self.listRequiredAdjustment.setObjectName(u"listRequiredAdjustment")
        self.listRequiredAdjustment.setGeometry(QRect(10, 31, 201, 331))
        self.labelRequiredAdjustmentName = QLabel(self.frameRequiredAdjustment)
        self.labelRequiredAdjustmentName.setObjectName(u"labelRequiredAdjustmentName")
        self.labelRequiredAdjustmentName.setGeometry(QRect(220, 10, 54, 16))
        self.lineRequiredAdjustmentName = QLineEdit(self.frameRequiredAdjustment)
        self.lineRequiredAdjustmentName.setObjectName(u"lineRequiredAdjustmentName")
        self.lineRequiredAdjustmentName.setGeometry(QRect(220, 30, 111, 20))
        self.labelRequiredAdjustmentValue = QLabel(self.frameRequiredAdjustment)
        self.labelRequiredAdjustmentValue.setObjectName(u"labelRequiredAdjustmentValue")
        self.labelRequiredAdjustmentValue.setGeometry(QRect(220, 60, 54, 16))
        self.lineRequiredAdjustmentValue = QLineEdit(self.frameRequiredAdjustment)
        self.lineRequiredAdjustmentValue.setObjectName(u"lineRequiredAdjustmentValue")
        self.lineRequiredAdjustmentValue.setGeometry(QRect(220, 80, 111, 20))
        self.buttonAddRequiredAdjustment = QPushButton(self.frameRequiredAdjustment)
        self.buttonAddRequiredAdjustment.setObjectName(u"buttonAddRequiredAdjustment")
        self.buttonAddRequiredAdjustment.setGeometry(QRect(220, 110, 75, 24))
        self.buttonRemoveRequiredAdjustment = QPushButton(self.frameRequiredAdjustment)
        self.buttonRemoveRequiredAdjustment.setObjectName(u"buttonRemoveRequiredAdjustment")
        self.buttonRemoveRequiredAdjustment.setGeometry(QRect(220, 140, 75, 24))
        self.buttonClearRequiredAdjustment = QPushButton(self.frameRequiredAdjustment)
        self.buttonClearRequiredAdjustment.setObjectName(u"buttonClearRequiredAdjustment")
        self.buttonClearRequiredAdjustment.setGeometry(QRect(220, 170, 75, 24))
        self.tabEdit.addTab(self.tabAdjustment, "")
        self.tabBind = QWidget()
        self.tabBind.setObjectName(u"tabBind")
        self.frameBindChallenge = QFrame(self.tabBind)
        self.frameBindChallenge.setObjectName(u"frameBindChallenge")
        self.frameBindChallenge.setGeometry(QRect(0, 0, 341, 371))
        self.frameBindChallenge.setFrameShape(QFrame.StyledPanel)
        self.frameBindChallenge.setFrameShadow(QFrame.Raised)
        self.labelBindChallenge = QLabel(self.frameBindChallenge)
        self.labelBindChallenge.setObjectName(u"labelBindChallenge")
        self.labelBindChallenge.setGeometry(QRect(10, 10, 101, 16))
        self.listChallenge = QListWidget(self.frameBindChallenge)
        self.listChallenge.setObjectName(u"listChallenge")
        self.listChallenge.setGeometry(QRect(10, 40, 241, 321))
        self.buttonAddChallenge = QPushButton(self.frameBindChallenge)
        self.buttonAddChallenge.setObjectName(u"buttonAddChallenge")
        self.buttonAddChallenge.setGeometry(QRect(260, 40, 75, 24))
        self.buttonRemoveChallenge = QPushButton(self.frameBindChallenge)
        self.buttonRemoveChallenge.setObjectName(u"buttonRemoveChallenge")
        self.buttonRemoveChallenge.setGeometry(QRect(260, 70, 75, 24))
        self.buttonClearChallenge = QPushButton(self.frameBindChallenge)
        self.buttonClearChallenge.setObjectName(u"buttonClearChallenge")
        self.buttonClearChallenge.setGeometry(QRect(260, 100, 75, 24))
        self.lineChallenge = QLineEdit(self.frameBindChallenge)
        self.lineChallenge.setObjectName(u"lineChallenge")
        self.lineChallenge.setGeometry(QRect(210, 10, 113, 20))
        self.frameBindAction = QFrame(self.tabBind)
        self.frameBindAction.setObjectName(u"frameBindAction")
        self.frameBindAction.setGeometry(QRect(340, 0, 341, 371))
        self.frameBindAction.setFrameShape(QFrame.StyledPanel)
        self.frameBindAction.setFrameShadow(QFrame.Raised)
        self.labelBindAction = QLabel(self.frameBindAction)
        self.labelBindAction.setObjectName(u"labelBindAction")
        self.labelBindAction.setGeometry(QRect(10, 10, 101, 16))
        self.listAction = QListWidget(self.frameBindAction)
        self.listAction.setObjectName(u"listAction")
        self.listAction.setGeometry(QRect(10, 40, 241, 321))
        self.buttonAddAction = QPushButton(self.frameBindAction)
        self.buttonAddAction.setObjectName(u"buttonAddAction")
        self.buttonAddAction.setGeometry(QRect(260, 40, 75, 24))
        self.buttonRemoveAction = QPushButton(self.frameBindAction)
        self.buttonRemoveAction.setObjectName(u"buttonRemoveAction")
        self.buttonRemoveAction.setGeometry(QRect(260, 70, 75, 24))
        self.buttonClearAction = QPushButton(self.frameBindAction)
        self.buttonClearAction.setObjectName(u"buttonClearAction")
        self.buttonClearAction.setGeometry(QRect(260, 100, 75, 24))
        self.lineAction = QLineEdit(self.frameBindAction)
        self.lineAction.setObjectName(u"lineAction")
        self.lineAction.setGeometry(QRect(210, 10, 113, 20))
        self.tabEdit.addTab(self.tabBind, "")
        self.tabAction = QWidget()
        self.tabAction.setObjectName(u"tabAction")
        self.frameRequirePoint = QFrame(self.tabAction)
        self.frameRequirePoint.setObjectName(u"frameRequirePoint")
        self.frameRequirePoint.setGeometry(QRect(0, 0, 211, 50))
        self.frameRequirePoint.setFrameShape(QFrame.StyledPanel)
        self.frameRequirePoint.setFrameShadow(QFrame.Raised)
        self.labelRequirePoint = QLabel(self.frameRequirePoint)
        self.labelRequirePoint.setObjectName(u"labelRequirePoint")
        self.labelRequirePoint.setGeometry(QRect(10, 10, 81, 16))
        self.lineRequirePoint = QLineEdit(self.frameRequirePoint)
        self.lineRequirePoint.setObjectName(u"lineRequirePoint")
        self.lineRequirePoint.setGeometry(QRect(100, 10, 101, 20))
        self.frameSuccessEvent = QFrame(self.tabAction)
        self.frameSuccessEvent.setObjectName(u"frameSuccessEvent")
        self.frameSuccessEvent.setGeometry(QRect(0, 50, 231, 50))
        self.frameSuccessEvent.setFrameShape(QFrame.StyledPanel)
        self.frameSuccessEvent.setFrameShadow(QFrame.Raised)
        self.labelSuccessEvent = QLabel(self.frameSuccessEvent)
        self.labelSuccessEvent.setObjectName(u"labelSuccessEvent")
        self.labelSuccessEvent.setGeometry(QRect(10, 10, 81, 16))
        self.lineSuccessEvent = QLineEdit(self.frameSuccessEvent)
        self.lineSuccessEvent.setObjectName(u"lineSuccessEvent")
        self.lineSuccessEvent.setGeometry(QRect(90, 10, 131, 20))
        self.frameFailureEvent = QFrame(self.tabAction)
        self.frameFailureEvent.setObjectName(u"frameFailureEvent")
        self.frameFailureEvent.setGeometry(QRect(0, 100, 231, 50))
        self.frameFailureEvent.setFrameShape(QFrame.StyledPanel)
        self.frameFailureEvent.setFrameShadow(QFrame.Raised)
        self.labelFailureEvent = QLabel(self.frameFailureEvent)
        self.labelFailureEvent.setObjectName(u"labelFailureEvent")
        self.labelFailureEvent.setGeometry(QRect(10, 10, 81, 16))
        self.lineFailureEvent = QLineEdit(self.frameFailureEvent)
        self.lineFailureEvent.setObjectName(u"lineFailureEvent")
        self.lineFailureEvent.setGeometry(QRect(90, 10, 131, 20))
        self.frameBigSuccessEvent = QFrame(self.tabAction)
        self.frameBigSuccessEvent.setObjectName(u"frameBigSuccessEvent")
        self.frameBigSuccessEvent.setGeometry(QRect(0, 150, 261, 50))
        self.frameBigSuccessEvent.setFrameShape(QFrame.StyledPanel)
        self.frameBigSuccessEvent.setFrameShadow(QFrame.Raised)
        self.labelBigSuccessEvent = QLabel(self.frameBigSuccessEvent)
        self.labelBigSuccessEvent.setObjectName(u"labelBigSuccessEvent")
        self.labelBigSuccessEvent.setGeometry(QRect(10, 10, 91, 16))
        self.lineBigSuccessEvent = QLineEdit(self.frameBigSuccessEvent)
        self.lineBigSuccessEvent.setObjectName(u"lineBigSuccessEvent")
        self.lineBigSuccessEvent.setGeometry(QRect(110, 10, 141, 20))
        self.frameBigFailureEvent = QFrame(self.tabAction)
        self.frameBigFailureEvent.setObjectName(u"frameBigFailureEvent")
        self.frameBigFailureEvent.setGeometry(QRect(0, 200, 261, 50))
        self.frameBigFailureEvent.setFrameShape(QFrame.StyledPanel)
        self.frameBigFailureEvent.setFrameShadow(QFrame.Raised)
        self.labelBigFailureEvent = QLabel(self.frameBigFailureEvent)
        self.labelBigFailureEvent.setObjectName(u"labelBigFailureEvent")
        self.labelBigFailureEvent.setGeometry(QRect(10, 10, 91, 16))
        self.lineBigFailureEvent = QLineEdit(self.frameBigFailureEvent)
        self.lineBigFailureEvent.setObjectName(u"lineBigFailureEvent")
        self.lineBigFailureEvent.setGeometry(QRect(110, 10, 141, 20))
        self.frameConvertAdjustment = QFrame(self.tabAction)
        self.frameConvertAdjustment.setObjectName(u"frameConvertAdjustment")
        self.frameConvertAdjustment.setGeometry(QRect(330, 0, 341, 371))
        self.frameConvertAdjustment.setFrameShape(QFrame.StyledPanel)
        self.frameConvertAdjustment.setFrameShadow(QFrame.Raised)
        self.labelConvertAdjustment = QLabel(self.frameConvertAdjustment)
        self.labelConvertAdjustment.setObjectName(u"labelConvertAdjustment")
        self.labelConvertAdjustment.setGeometry(QRect(10, 10, 141, 16))
        self.listConvertAdjustment = QListWidget(self.frameConvertAdjustment)
        self.listConvertAdjustment.setObjectName(u"listConvertAdjustment")
        self.listConvertAdjustment.setGeometry(QRect(10, 31, 201, 331))
        self.labelConvertAdjustmentName = QLabel(self.frameConvertAdjustment)
        self.labelConvertAdjustmentName.setObjectName(u"labelConvertAdjustmentName")
        self.labelConvertAdjustmentName.setGeometry(QRect(220, 10, 54, 16))
        self.lineConvertAdjustmentName = QLineEdit(self.frameConvertAdjustment)
        self.lineConvertAdjustmentName.setObjectName(u"lineConvertAdjustmentName")
        self.lineConvertAdjustmentName.setGeometry(QRect(220, 30, 111, 20))
        self.labelConvertAdjustmentCoef = QLabel(self.frameConvertAdjustment)
        self.labelConvertAdjustmentCoef.setObjectName(u"labelConvertAdjustmentCoef")
        self.labelConvertAdjustmentCoef.setGeometry(QRect(220, 60, 54, 16))
        self.lineConvertAdjustmentCoef = QLineEdit(self.frameConvertAdjustment)
        self.lineConvertAdjustmentCoef.setObjectName(u"lineConvertAdjustmentCoef")
        self.lineConvertAdjustmentCoef.setGeometry(QRect(220, 80, 111, 20))
        self.buttonAddConvertAdjustment = QPushButton(self.frameConvertAdjustment)
        self.buttonAddConvertAdjustment.setObjectName(u"buttonAddConvertAdjustment")
        self.buttonAddConvertAdjustment.setGeometry(QRect(220, 110, 75, 24))
        self.buttonRemoveConvertAdjustment = QPushButton(self.frameConvertAdjustment)
        self.buttonRemoveConvertAdjustment.setObjectName(u"buttonRemoveConvertAdjustment")
        self.buttonRemoveConvertAdjustment.setGeometry(QRect(220, 140, 75, 24))
        self.buttonClearConvertAdjustment = QPushButton(self.frameConvertAdjustment)
        self.buttonClearConvertAdjustment.setObjectName(u"buttonClearConvertAdjustment")
        self.buttonClearConvertAdjustment.setGeometry(QRect(220, 170, 75, 24))
        self.tabEdit.addTab(self.tabAction, "")

        self.verticalLayout.addWidget(self.groupEdit)

        self.groupOperation = QGroupBox(self.horizontalLayoutWidget)
        self.groupOperation.setObjectName(u"groupOperation")
        self.gridLayoutWidget_2 = QWidget(self.groupOperation)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 20, 681, 391))
        self.gridLayoutOperations = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayoutOperations.setSpacing(10)
        self.gridLayoutOperations.setObjectName(u"gridLayoutOperations")
        self.gridLayoutOperations.setContentsMargins(10, 10, 10, 10)
        self.buttonQuit = QPushButton(self.gridLayoutWidget_2)
        self.buttonQuit.setObjectName(u"buttonQuit")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonQuit.sizePolicy().hasHeightForWidth())
        self.buttonQuit.setSizePolicy(sizePolicy)

        self.gridLayoutOperations.addWidget(self.buttonQuit, 2, 1, 1, 1)

        self.buttonRefresh = QPushButton(self.gridLayoutWidget_2)
        self.buttonRefresh.setObjectName(u"buttonRefresh")
        sizePolicy.setHeightForWidth(self.buttonRefresh.sizePolicy().hasHeightForWidth())
        self.buttonRefresh.setSizePolicy(sizePolicy)

        self.gridLayoutOperations.addWidget(self.buttonRefresh, 1, 0, 1, 1)

        self.buttonJson = QPushButton(self.gridLayoutWidget_2)
        self.buttonJson.setObjectName(u"buttonJson")
        sizePolicy.setHeightForWidth(self.buttonJson.sizePolicy().hasHeightForWidth())
        self.buttonJson.setSizePolicy(sizePolicy)

        self.gridLayoutOperations.addWidget(self.buttonJson, 1, 1, 1, 1)

        self.buttonSave = QPushButton(self.gridLayoutWidget_2)
        self.buttonSave.setObjectName(u"buttonSave")
        sizePolicy.setHeightForWidth(self.buttonSave.sizePolicy().hasHeightForWidth())
        self.buttonSave.setSizePolicy(sizePolicy)

        self.gridLayoutOperations.addWidget(self.buttonSave, 2, 0, 1, 1)

        self.buttonEdit = QPushButton(self.gridLayoutWidget_2)
        self.buttonEdit.setObjectName(u"buttonEdit")
        sizePolicy.setHeightForWidth(self.buttonEdit.sizePolicy().hasHeightForWidth())
        self.buttonEdit.setSizePolicy(sizePolicy)

        self.gridLayoutOperations.addWidget(self.buttonEdit, 0, 0, 1, 1)

        self.buttonClear = QPushButton(self.gridLayoutWidget_2)
        self.buttonClear.setObjectName(u"buttonClear")
        sizePolicy.setHeightForWidth(self.buttonClear.sizePolicy().hasHeightForWidth())
        self.buttonClear.setSizePolicy(sizePolicy)

        self.gridLayoutOperations.addWidget(self.buttonClear, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupOperation)


        self.horizontalLayout.addLayout(self.verticalLayout)

        FormEditor.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(FormEditor)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1440, 22))
        FormEditor.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(FormEditor)
        self.statusbar.setObjectName(u"statusbar")
        FormEditor.setStatusBar(self.statusbar)

        self.retranslateUi(FormEditor)

        self.tabEdit.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(FormEditor)
    # setupUi

    def retranslateUi(self, FormEditor):
        FormEditor.setWindowTitle(QCoreApplication.translate("FormEditor", u"RogueLife\u7f16\u8f91\u5668", None))
        self.groupActions.setTitle(QCoreApplication.translate("FormEditor", u"\u884c\u52a8\u5217\u8868", None))
        self.groupEvents.setTitle(QCoreApplication.translate("FormEditor", u"\u4e8b\u4ef6\u5217\u8868", None))
        self.groupChallenges.setTitle(QCoreApplication.translate("FormEditor", u"\u6311\u6218\u5217\u8868", None))
        self.groupItems.setTitle(QCoreApplication.translate("FormEditor", u"\u85cf\u54c1\u5217\u8868", None))
        self.groupEdit.setTitle(QCoreApplication.translate("FormEditor", u"\u7f16\u8f91\u533a", None))
        self.labelIndex.setText(QCoreApplication.translate("FormEditor", u"\u7f16\u53f7", None))
        self.labelName.setText(QCoreApplication.translate("FormEditor", u"\u540d\u79f0", None))
        self.tabEdit.setTabText(self.tabEdit.indexOf(self.tabBasic), QCoreApplication.translate("FormEditor", u"\u7f16\u8f91\u57fa\u7840\u4fe1\u606f", None))
        self.labelDes.setText(QCoreApplication.translate("FormEditor", u"\u63cf\u8ff0\u6587\u672c", None))
        self.labelEff.setText(QCoreApplication.translate("FormEditor", u"\u6548\u679c\u4ecb\u7ecd", None))
        self.tabEdit.setTabText(self.tabEdit.indexOf(self.tabText), QCoreApplication.translate("FormEditor", u"\u7f16\u8f91\u6587\u672c", None))
        self.labelDisplayGeneral.setText(QCoreApplication.translate("FormEditor", u"\u901a\u7528\u6587\u672c(\u663e\u793a\u5728\u68c0\u5b9a\u4e4b\u524d)", None))
        self.labelDisplaySuccess.setText(QCoreApplication.translate("FormEditor", u"\u6210\u529f\u6587\u672c(\u68c0\u5b9a\u6210\u529f\u663e\u793a)", None))
        self.labelDisplayFailure.setText(QCoreApplication.translate("FormEditor", u"\u5931\u8d25\u6587\u672c(\u68c0\u5b9a\u5931\u8d25\u663e\u793a)", None))
        self.tabEdit.setTabText(self.tabEdit.indexOf(self.tabResults), QCoreApplication.translate("FormEditor", u"\u7f16\u8f91\u7ed3\u679c\u6587\u672c", None))
        self.labelRequire.setText(QCoreApplication.translate("FormEditor", u"\u524d\u63d0\u6761\u4ef6\u5173\u7cfb", None))
        self.buttonAddRequire.setText(QCoreApplication.translate("FormEditor", u"\u6dfb\u52a0", None))
        self.buttonRemoveRequire.setText(QCoreApplication.translate("FormEditor", u"\u79fb\u9664", None))
        self.buttonClearRequire.setText(QCoreApplication.translate("FormEditor", u"\u6e05\u7a7a", None))
        self.labelExclude.setText(QCoreApplication.translate("FormEditor", u"\u65e0\u6cd5\u5171\u5b58\u5173\u7cfb", None))
        self.buttonAddExclude.setText(QCoreApplication.translate("FormEditor", u"\u6dfb\u52a0", None))
        self.buttonRemoveExclude.setText(QCoreApplication.translate("FormEditor", u"\u79fb\u9664", None))
        self.buttonClearExclude.setText(QCoreApplication.translate("FormEditor", u"\u6e05\u7a7a", None))
        self.checkExcluisive.setText(QCoreApplication.translate("FormEditor", u"\u53ef\u4ee5\u62bd\u53d6", None))
        self.labelPoss.setText(QCoreApplication.translate("FormEditor", u"\u62bd\u53d6\u6982\u7387", None))
        self.tabEdit.setTabText(self.tabEdit.indexOf(self.tabPossibility), QCoreApplication.translate("FormEditor", u"\u7f16\u8f91\u62bd\u53d6\u6982\u7387", None))
        self.labelAdjustment.setText(QCoreApplication.translate("FormEditor", u"\u8d60\u4e0e\u7684\u4fee\u6b63\u5217\u8868", None))
        self.labelAdjustmentName.setText(QCoreApplication.translate("FormEditor", u"\u4fee\u6b63\u540d\u79f0", None))
        self.labelAdjustmentValue.setText(QCoreApplication.translate("FormEditor", u"\u4fee\u6b63\u503c", None))
        self.buttonAddAdjustment.setText(QCoreApplication.translate("FormEditor", u"\u6dfb\u52a0\u4fee\u6b63", None))
        self.buttonRemoveAdjustment.setText(QCoreApplication.translate("FormEditor", u"\u79fb\u9664\u4fee\u6b63", None))
        self.buttonClearAdjustment.setText(QCoreApplication.translate("FormEditor", u"\u6e05\u7a7a\u4fee\u6b63", None))
        self.labelRequiredAdjustment.setText(QCoreApplication.translate("FormEditor", u"\u6311\u6218\u9700\u6c42\u7684\u4fee\u6b63\u5217\u8868", None))
        self.labelRequiredAdjustmentName.setText(QCoreApplication.translate("FormEditor", u"\u4fee\u6b63\u540d\u79f0", None))
        self.labelRequiredAdjustmentValue.setText(QCoreApplication.translate("FormEditor", u"\u4fee\u6b63\u503c", None))
        self.buttonAddRequiredAdjustment.setText(QCoreApplication.translate("FormEditor", u"\u6dfb\u52a0\u4fee\u6b63", None))
        self.buttonRemoveRequiredAdjustment.setText(QCoreApplication.translate("FormEditor", u"\u79fb\u9664\u4fee\u6b63", None))
        self.buttonClearRequiredAdjustment.setText(QCoreApplication.translate("FormEditor", u"\u6e05\u7a7a\u4fee\u6b63", None))
        self.tabEdit.setTabText(self.tabEdit.indexOf(self.tabAdjustment), QCoreApplication.translate("FormEditor", u"\u7f16\u8f91\u4fee\u6b63", None))
        self.labelBindChallenge.setText(QCoreApplication.translate("FormEditor", u"\u7ed1\u5b9a\u7684\u6311\u6218\u5217\u8868", None))
        self.buttonAddChallenge.setText(QCoreApplication.translate("FormEditor", u"\u6dfb\u52a0", None))
        self.buttonRemoveChallenge.setText(QCoreApplication.translate("FormEditor", u"\u79fb\u9664", None))
        self.buttonClearChallenge.setText(QCoreApplication.translate("FormEditor", u"\u6e05\u7a7a", None))
        self.labelBindAction.setText(QCoreApplication.translate("FormEditor", u"\u7ed1\u5b9a\u7684\u884c\u52a8\u5217\u8868", None))
        self.buttonAddAction.setText(QCoreApplication.translate("FormEditor", u"\u6dfb\u52a0", None))
        self.buttonRemoveAction.setText(QCoreApplication.translate("FormEditor", u"\u79fb\u9664", None))
        self.buttonClearAction.setText(QCoreApplication.translate("FormEditor", u"\u6e05\u7a7a", None))
        self.tabEdit.setTabText(self.tabEdit.indexOf(self.tabBind), QCoreApplication.translate("FormEditor", u"\u7ed1\u5b9a\u6311\u6218\u4e0e\u884c\u52a8", None))
        self.labelRequirePoint.setText(QCoreApplication.translate("FormEditor", u"\u6210\u529f\u9700\u8981\u70b9\u6570", None))
        self.labelSuccessEvent.setText(QCoreApplication.translate("FormEditor", u"\u6210\u529f\u89e6\u53d1\u4e8b\u4ef6", None))
        self.labelFailureEvent.setText(QCoreApplication.translate("FormEditor", u"\u5931\u8d25\u89e6\u53d1\u4e8b\u4ef6", None))
        self.labelBigSuccessEvent.setText(QCoreApplication.translate("FormEditor", u"\u5927\u6210\u529f\u89e6\u53d1\u4e8b\u4ef6", None))
        self.labelBigFailureEvent.setText(QCoreApplication.translate("FormEditor", u"\u5927\u5931\u8d25\u89e6\u53d1\u4e8b\u4ef6", None))
        self.labelConvertAdjustment.setText(QCoreApplication.translate("FormEditor", u"\u53ef\u4ee5\u8f6c\u6362\u70b9\u6570\u7684\u4fee\u6b63\u5217\u8868", None))
        self.labelConvertAdjustmentName.setText(QCoreApplication.translate("FormEditor", u"\u4fee\u6b63\u540d\u79f0", None))
        self.labelConvertAdjustmentCoef.setText(QCoreApplication.translate("FormEditor", u"\u8f6c\u6362\u7cfb\u6570", None))
        self.buttonAddConvertAdjustment.setText(QCoreApplication.translate("FormEditor", u"\u6dfb\u52a0\u4fee\u6b63", None))
        self.buttonRemoveConvertAdjustment.setText(QCoreApplication.translate("FormEditor", u"\u79fb\u9664\u4fee\u6b63", None))
        self.buttonClearConvertAdjustment.setText(QCoreApplication.translate("FormEditor", u"\u6e05\u7a7a\u4fee\u6b63", None))
        self.tabEdit.setTabText(self.tabEdit.indexOf(self.tabAction), QCoreApplication.translate("FormEditor", u"\u7f16\u8f91\u884c\u52a8", None))
        self.groupOperation.setTitle(QCoreApplication.translate("FormEditor", u"\u63a7\u5236\u533a", None))
        self.buttonQuit.setText(QCoreApplication.translate("FormEditor", u"\u9000\u51fa", None))
        self.buttonRefresh.setText(QCoreApplication.translate("FormEditor", u"\u5237\u65b0", None))
        self.buttonJson.setText(QCoreApplication.translate("FormEditor", u"\u751f\u6210json", None))
        self.buttonSave.setText(QCoreApplication.translate("FormEditor", u"\u4fdd\u5b58\u66f4\u6539", None))
        self.buttonEdit.setText(QCoreApplication.translate("FormEditor", u"\u7f16\u8f91\u9009\u4e2d\u9879", None))
        self.buttonClear.setText(QCoreApplication.translate("FormEditor", u"\u6e05\u7a7a\u7f16\u8f91\u533a", None))
    # retranslateUi

