# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormConsole.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_FormConsole(object):
    def setupUi(self, FormConsole):
        if not FormConsole.objectName():
            FormConsole.setObjectName(u"FormConsole")
        FormConsole.resize(510, 430)
        self.centralwidget = QWidget(FormConsole)
        self.centralwidget.setObjectName(u"centralwidget")
        self.labelCommand = QLabel(self.centralwidget)
        self.labelCommand.setObjectName(u"labelCommand")
        self.labelCommand.setGeometry(QRect(20, 10, 80, 15))
        self.buttonRun = QPushButton(self.centralwidget)
        self.buttonRun.setObjectName(u"buttonRun")
        self.buttonRun.setGeometry(QRect(320, 300, 171, 71))
        self.lineEditCoef1 = QLineEdit(self.centralwidget)
        self.lineEditCoef1.setObjectName(u"lineEditCoef1")
        self.lineEditCoef1.setGeometry(QRect(350, 40, 130, 20))
        self.labelCoef1 = QLabel(self.centralwidget)
        self.labelCoef1.setObjectName(u"labelCoef1")
        self.labelCoef1.setGeometry(QRect(290, 40, 54, 15))
        self.labelCoef = QLabel(self.centralwidget)
        self.labelCoef.setObjectName(u"labelCoef")
        self.labelCoef.setGeometry(QRect(290, 10, 80, 15))
        self.labelCoef2 = QLabel(self.centralwidget)
        self.labelCoef2.setObjectName(u"labelCoef2")
        self.labelCoef2.setGeometry(QRect(290, 70, 54, 15))
        self.lineEditCoef2 = QLineEdit(self.centralwidget)
        self.lineEditCoef2.setObjectName(u"lineEditCoef2")
        self.lineEditCoef2.setGeometry(QRect(350, 70, 130, 20))
        self.buttonDebug = QPushButton(self.centralwidget)
        self.buttonDebug.setObjectName(u"buttonDebug")
        self.buttonDebug.setGeometry(QRect(320, 220, 171, 71))
        self.listCommand = QListWidget(self.centralwidget)
        self.listCommand.setObjectName(u"listCommand")
        self.listCommand.setGeometry(QRect(10, 30, 256, 341))
        self.labelCoef3 = QLabel(self.centralwidget)
        self.labelCoef3.setObjectName(u"labelCoef3")
        self.labelCoef3.setGeometry(QRect(290, 100, 54, 15))
        self.lineEditCoef3 = QLineEdit(self.centralwidget)
        self.lineEditCoef3.setObjectName(u"lineEditCoef3")
        self.lineEditCoef3.setGeometry(QRect(350, 100, 130, 20))
        FormConsole.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(FormConsole)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 510, 26))
        FormConsole.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(FormConsole)
        self.statusbar.setObjectName(u"statusbar")
        FormConsole.setStatusBar(self.statusbar)

        self.retranslateUi(FormConsole)

        QMetaObject.connectSlotsByName(FormConsole)
    # setupUi

    def retranslateUi(self, FormConsole):
        FormConsole.setWindowTitle(QCoreApplication.translate("FormConsole", u"\u63a7\u5236\u53f0", None))
        self.labelCommand.setText(QCoreApplication.translate("FormConsole", u"\u547d\u4ee4\u5217\u8868", None))
        self.buttonRun.setText(QCoreApplication.translate("FormConsole", u"\u8fd0\u884c\u547d\u4ee4", None))
        self.labelCoef1.setText(QCoreApplication.translate("FormConsole", u"\u53c2\u65701", None))
        self.labelCoef.setText(QCoreApplication.translate("FormConsole", u"\u53c2\u6570\u5217\u8868", None))
        self.labelCoef2.setText(QCoreApplication.translate("FormConsole", u"\u53c2\u65702", None))
        self.buttonDebug.setText(QCoreApplication.translate("FormConsole", u"\u663e\u793a\u8c03\u8bd5\u8f93\u51fa", None))
        self.labelCoef3.setText(QCoreApplication.translate("FormConsole", u"\u53c2\u65703", None))
    # retranslateUi

