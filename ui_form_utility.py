# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormUtility.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget)

class Ui_FormUtility(object):
    def setupUi(self, FormUtility):
        if not FormUtility.objectName():
            FormUtility.setObjectName(u"FormUtility")
        FormUtility.resize(400, 250)
        FormUtility.setMinimumSize(QSize(400, 250))
        FormUtility.setMaximumSize(QSize(400, 250))
        self.buttonImportDataFile = QPushButton(FormUtility)
        self.buttonImportDataFile.setObjectName(u"buttonImportDataFile")
        self.buttonImportDataFile.setGeometry(QRect(10, 70, 151, 51))
        self.buttonCheckUpdate = QPushButton(FormUtility)
        self.buttonCheckUpdate.setObjectName(u"buttonCheckUpdate")
        self.buttonCheckUpdate.setGeometry(QRect(230, 70, 151, 51))
        self.buttonConsole = QPushButton(FormUtility)
        self.buttonConsole.setObjectName(u"buttonConsole")
        self.buttonConsole.setGeometry(QRect(230, 190, 151, 51))
        self.buttonCustomDataFile = QPushButton(FormUtility)
        self.buttonCustomDataFile.setObjectName(u"buttonCustomDataFile")
        self.buttonCustomDataFile.setGeometry(QRect(10, 130, 151, 51))
        self.buttonDebug = QPushButton(FormUtility)
        self.buttonDebug.setObjectName(u"buttonDebug")
        self.buttonDebug.setGeometry(QRect(10, 190, 151, 51))
        self.buttonOpenDataFilesDir = QPushButton(FormUtility)
        self.buttonOpenDataFilesDir.setObjectName(u"buttonOpenDataFilesDir")
        self.buttonOpenDataFilesDir.setGeometry(QRect(10, 10, 151, 51))
        self.buttonSyncDataFiles = QPushButton(FormUtility)
        self.buttonSyncDataFiles.setObjectName(u"buttonSyncDataFiles")
        self.buttonSyncDataFiles.setGeometry(QRect(230, 10, 151, 51))

        self.retranslateUi(FormUtility)

        QMetaObject.connectSlotsByName(FormUtility)
    # setupUi

    def retranslateUi(self, FormUtility):
        FormUtility.setWindowTitle(QCoreApplication.translate("FormUtility", u"\u529f\u80fd\u83dc\u5355", None))
        self.buttonImportDataFile.setText(QCoreApplication.translate("FormUtility", u"\u5bfc\u5165\u81ea\u5b9a\u4e49\u6570\u636e\u6587\u4ef6", None))
        self.buttonCheckUpdate.setText(QCoreApplication.translate("FormUtility", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.buttonConsole.setText(QCoreApplication.translate("FormUtility", u"\u6253\u5f00\u63a7\u5236\u53f0", None))
        self.buttonCustomDataFile.setText(QCoreApplication.translate("FormUtility", u"\u7f16\u8f91\u81ea\u5b9a\u4e49\u6570\u636e\u6587\u4ef6", None))
        self.buttonDebug.setText(QCoreApplication.translate("FormUtility", u"\u6253\u5f00\u8c03\u8bd5\u8f93\u51fa", None))
        self.buttonOpenDataFilesDir.setText(QCoreApplication.translate("FormUtility", u"\u6253\u5f00\u6570\u636e\u6587\u4ef6\u76ee\u5f55", None))
        self.buttonSyncDataFiles.setText(QCoreApplication.translate("FormUtility", u"\u4ece\u4e91\u7aef\u540c\u6b65\u6570\u636e\u6587\u4ef6", None))
    # retranslateUi

