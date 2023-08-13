# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'second.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_second_window(object):
    def setupUi(self, second_window):
        if not second_window.objectName():
            second_window.setObjectName(u"second_window")
        second_window.resize(437, 381)
        self.centralwidget = QWidget(second_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.s_button = QPushButton(self.centralwidget)
        self.s_button.setObjectName(u"s_button")
        self.s_button.setGeometry(QRect(100, 290, 211, 41))
        second_window.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(second_window)
        self.statusbar.setObjectName(u"statusbar")
        second_window.setStatusBar(self.statusbar)

        self.retranslateUi(second_window)

        QMetaObject.connectSlotsByName(second_window)
    # setupUi

    def retranslateUi(self, second_window):
        second_window.setWindowTitle(QCoreApplication.translate("second_window", u"MainWindow", None))
        self.s_button.setText(QCoreApplication.translate("second_window", u"to page 1", None))
    # retranslateUi

