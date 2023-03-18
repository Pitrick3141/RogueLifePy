# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormUpdate.ui'
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
from PySide6.QtWidgets import (QApplication, QProgressBar, QPushButton, QSizePolicy,
    QTextBrowser, QWidget)

class Ui_FormUpdate(object):
    def setupUi(self, FormUpdate):
        if not FormUpdate.objectName():
            FormUpdate.setObjectName(u"FormUpdate")
        FormUpdate.resize(455, 350)
        FormUpdate.setMinimumSize(QSize(455, 350))
        FormUpdate.setMaximumSize(QSize(455, 350))
        self.textInfo = QTextBrowser(FormUpdate)
        self.textInfo.setObjectName(u"textInfo")
        self.textInfo.setGeometry(QRect(10, 10, 431, 231))
        self.progressBar = QProgressBar(FormUpdate)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 252, 431, 41))
        self.progressBar.setValue(0)
        self.buttonWeb = QPushButton(FormUpdate)
        self.buttonWeb.setObjectName(u"buttonWeb")
        self.buttonWeb.setGeometry(QRect(110, 300, 91, 41))
        self.buttonDownload = QPushButton(FormUpdate)
        self.buttonDownload.setObjectName(u"buttonDownload")
        self.buttonDownload.setGeometry(QRect(10, 300, 91, 41))
        self.buttonCancel = QPushButton(FormUpdate)
        self.buttonCancel.setObjectName(u"buttonCancel")
        self.buttonCancel.setGeometry(QRect(280, 300, 75, 41))
        self.buttonIgnore = QPushButton(FormUpdate)
        self.buttonIgnore.setObjectName(u"buttonIgnore")
        self.buttonIgnore.setGeometry(QRect(360, 300, 75, 41))

        self.retranslateUi(FormUpdate)

        QMetaObject.connectSlotsByName(FormUpdate)
    # setupUi

    def retranslateUi(self, FormUpdate):
        FormUpdate.setWindowTitle(QCoreApplication.translate("FormUpdate", u"\u53d1\u73b0\u65b0\u7248\u672c", None))
        self.buttonWeb.setText(QCoreApplication.translate("FormUpdate", u"\u6253\u5f00\u53d1\u5e03\u9875\u9762", None))
        self.buttonDownload.setText(QCoreApplication.translate("FormUpdate", u"\u4e0b\u8f7d\u66f4\u65b0", None))
        self.buttonCancel.setText(QCoreApplication.translate("FormUpdate", u"\u53d6\u6d88", None))
        self.buttonIgnore.setText(QCoreApplication.translate("FormUpdate", u"\u5ffd\u7565\u6b64\u7248\u672c", None))
    # retranslateUi

