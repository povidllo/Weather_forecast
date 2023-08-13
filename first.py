# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'first.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_first_window(object):
    def setupUi(self, first_window):
        if not first_window.objectName():
            first_window.setObjectName(u"first_window")
        first_window.resize(414, 401)
        self.centralwidget = QWidget(first_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.f_button = QPushButton(self.centralwidget)
        self.f_button.setObjectName(u"f_button")
        self.f_button.setGeometry(QRect(50, 240, 271, 111))
        self.f_country = QComboBox(self.centralwidget)
        self.f_country.addItem("")
        self.f_country.setObjectName(u"f_country")
        self.f_country.setGeometry(QRect(20, 80, 171, 81))
        self.f_city = QComboBox(self.centralwidget)
        self.f_city.addItem("")
        self.f_city.setObjectName(u"f_city")
        self.f_city.setGeometry(QRect(240, 80, 161, 81))
        first_window.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(first_window)
        self.statusbar.setObjectName(u"statusbar")
        first_window.setStatusBar(self.statusbar)

        self.retranslateUi(first_window)

        QMetaObject.connectSlotsByName(first_window)
    # setupUi

    def retranslateUi(self, first_window):
        first_window.setWindowTitle(QCoreApplication.translate("first_window", u"MainWindow", None))
        self.f_button.setText(QCoreApplication.translate("first_window", u"find out the weather forecast", None))
        self.f_country.setItemText(0, QCoreApplication.translate("first_window", u"Select country", None))

        self.f_city.setItemText(0, QCoreApplication.translate("first_window", u"Select city", None))

    # retranslateUi

