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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QProgressBar,
    QSizePolicy, QTextBrowser, QWidget)

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
        self.buttonBox = QDialogButtonBox(FormUpdate)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 310, 431, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.NoButton)
        self.buttonBox.setCenterButtons(False)
        self.progressBar = QProgressBar(FormUpdate)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 252, 431, 41))
        self.progressBar.setValue(24)

        self.retranslateUi(FormUpdate)

        QMetaObject.connectSlotsByName(FormUpdate)
    # setupUi

    def retranslateUi(self, FormUpdate):
        FormUpdate.setWindowTitle(QCoreApplication.translate("FormUpdate", u"\u53d1\u73b0\u65b0\u7248\u672c", None))
    # retranslateUi

