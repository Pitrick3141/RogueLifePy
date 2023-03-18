# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormMain.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_FormMain(object):
    def setupUi(self, FormMain):
        if not FormMain.objectName():
            FormMain.setObjectName(u"FormMain")
        FormMain.resize(800, 520)
        FormMain.setMinimumSize(QSize(800, 520))
        FormMain.setMaximumSize(QSize(800, 520))
        icon = QIcon()
        icon.addFile(u"../../../.designer/backup/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        FormMain.setWindowIcon(icon)
        self.centralwidget = QWidget(FormMain)
        self.centralwidget.setObjectName(u"centralwidget")
        self.buttonStart = QPushButton(self.centralwidget)
        self.buttonStart.setObjectName(u"buttonStart")
        self.buttonStart.setGeometry(QRect(590, 90, 180, 71))
        self.buttonRecord = QPushButton(self.centralwidget)
        self.buttonRecord.setObjectName(u"buttonRecord")
        self.buttonRecord.setGeometry(QRect(590, 170, 180, 71))
        self.buttonMenu = QPushButton(self.centralwidget)
        self.buttonMenu.setObjectName(u"buttonMenu")
        self.buttonMenu.setGeometry(QRect(590, 250, 180, 71))
        self.buttonQuit = QPushButton(self.centralwidget)
        self.buttonQuit.setObjectName(u"buttonQuit")
        self.buttonQuit.setGeometry(QRect(659, 420, 111, 51))
        self.labelTitle = QLabel(self.centralwidget)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setGeometry(QRect(30, 20, 251, 61))
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(24)
        font.setBold(True)
        self.labelTitle.setFont(font)
        self.buttonEggs = QPushButton(self.centralwidget)
        self.buttonEggs.setObjectName(u"buttonEggs")
        self.buttonEggs.setEnabled(True)
        self.buttonEggs.setGeometry(QRect(20, 380, 161, 71))
        icon1 = QIcon()
        icon1.addFile(u"icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonEggs.setIcon(icon1)
        self.buttonEggs.setIconSize(QSize(32, 32))
        self.buttonEggs.setCheckable(False)
        self.buttonEggs.setChecked(False)
        self.buttonAbout = QPushButton(self.centralwidget)
        self.buttonAbout.setObjectName(u"buttonAbout")
        self.buttonAbout.setGeometry(QRect(589, 420, 61, 51))
        self.buttonAbout.setIconSize(QSize(32, 32))
        FormMain.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(FormMain)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        FormMain.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(FormMain)
        self.statusbar.setObjectName(u"statusbar")
        FormMain.setStatusBar(self.statusbar)

        self.retranslateUi(FormMain)

        QMetaObject.connectSlotsByName(FormMain)
    # setupUi

    def retranslateUi(self, FormMain):
        FormMain.setWindowTitle(QCoreApplication.translate("FormMain", u"MyRogueLife2", None))
        self.buttonStart.setText(QCoreApplication.translate("FormMain", u"\u5f00\u59cb\u65c5\u7a0b", None))
        self.buttonRecord.setText(QCoreApplication.translate("FormMain", u"\u65c5\u7a0b\u65e5\u8bb0", None))
        self.buttonMenu.setText(QCoreApplication.translate("FormMain", u"\u6e38\u620f\u83dc\u5355", None))
        self.buttonQuit.setText(QCoreApplication.translate("FormMain", u"\u9000\u51fa\u6e38\u620f", None))
        self.labelTitle.setText(QCoreApplication.translate("FormMain", u"MyRogueLife2", None))
        self.buttonEggs.setText(QCoreApplication.translate("FormMain", u"\u5df2\u53d1\u73b0\u5f69\u86cb: 0", None))
        self.buttonAbout.setText(QCoreApplication.translate("FormMain", u"\u5173\u4e8e", None))
    # retranslateUi

