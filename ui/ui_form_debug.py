# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormDebug.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QSizePolicy, QTextBrowser,
    QWidget)

class Ui_FormDebug(object):
    def setupUi(self, FormDebug):
        if not FormDebug.objectName():
            FormDebug.setObjectName(u"FormDebug")
        FormDebug.resize(520, 800)
        FormDebug.setMinimumSize(QSize(520, 800))
        FormDebug.setMaximumSize(QSize(520, 800))
        self.textDebug = QTextBrowser(FormDebug)
        self.textDebug.setObjectName(u"textDebug")
        self.textDebug.setGeometry(QRect(10, 10, 500, 780))
        self.textDebug.setMinimumSize(QSize(500, 780))
        self.textDebug.setMaximumSize(QSize(500, 780))

        self.retranslateUi(FormDebug)

        QMetaObject.connectSlotsByName(FormDebug)
    # setupUi

    def retranslateUi(self, FormDebug):
        FormDebug.setWindowTitle(QCoreApplication.translate("FormDebug", u"\u8c03\u8bd5\u4fe1\u606f", None))
    # retranslateUi

