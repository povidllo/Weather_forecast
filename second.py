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
from PySide6.QtWidgets import (QApplication, QComboBox, QLCDNumber, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QWidget)
import resources_rc

class Ui_second_window(object):
    def setupUi(self, second_window):
        if not second_window.objectName():
            second_window.setObjectName(u"second_window")
        second_window.resize(440, 680)
        second_window.setMinimumSize(QSize(440, 680))
        second_window.setMaximumSize(QSize(440, 680))
        self.centralwidget = QWidget(second_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.back_button = QPushButton(self.centralwidget)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(290, 10, 147, 51))
        self.country_name = QLineEdit(self.centralwidget)
        self.country_name.setObjectName(u"country_name")
        self.country_name.setGeometry(QRect(240, 90, 181, 41))
        self.country_name.setAlignment(Qt.AlignCenter)
        self.country_name.setReadOnly(True)
        self.city_name = QLineEdit(self.centralwidget)
        self.city_name.setObjectName(u"city_name")
        self.city_name.setGeometry(QRect(50, 90, 171, 41))
        self.city_name.setAlignment(Qt.AlignCenter)
        self.city_name.setReadOnly(True)
        self.country = QComboBox(self.centralwidget)
        self.country.addItem("")
        self.country.setObjectName(u"country")
        self.country.setGeometry(QRect(10, 10, 128, 51))
        self.country.setMinimumSize(QSize(128, 0))
        self.city = QComboBox(self.centralwidget)
        self.city.addItem("")
        self.city.setObjectName(u"city")
        self.city.setGeometry(QRect(150, 10, 131, 51))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.city.sizePolicy().hasHeightForWidth())
        self.city.setSizePolicy(sizePolicy)
        self.degree = QLCDNumber(self.centralwidget)
        self.degree.setObjectName(u"degree")
        self.degree.setGeometry(QRect(20, 150, 201, 151))
        self.max_temp = QLineEdit(self.centralwidget)
        self.max_temp.setObjectName(u"max_temp")
        self.max_temp.setGeometry(QRect(290, 150, 51, 41))
        self.max_temp.setAlignment(Qt.AlignCenter)
        self.max_temp.setReadOnly(True)
        self.min_temp = QLineEdit(self.centralwidget)
        self.min_temp.setObjectName(u"min_temp")
        self.min_temp.setGeometry(QRect(290, 210, 51, 41))
        self.min_temp.setAlignment(Qt.AlignCenter)
        self.min_temp.setReadOnly(True)
        self.max_degree = QLCDNumber(self.centralwidget)
        self.max_degree.setObjectName(u"max_degree")
        self.max_degree.setGeometry(QRect(350, 150, 61, 41))
        self.min_degree = QLCDNumber(self.centralwidget)
        self.min_degree.setObjectName(u"min_degree")
        self.min_degree.setGeometry(QRect(350, 210, 61, 41))
        self.clouds = QLineEdit(self.centralwidget)
        self.clouds.setObjectName(u"clouds")
        self.clouds.setGeometry(QRect(230, 260, 201, 41))
        self.clouds.setAlignment(Qt.AlignCenter)
        self.clouds.setReadOnly(True)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(18, 95, 31, 31))
        self.label.setPixmap(QPixmap(u":/icons/icons/placeholder-filled-point.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(220, 160, 41, 91))
        self.label_2.setPixmap(QPixmap(u":/icons/icons/pngwing.com.png"))
        self.label_2.setScaledContents(True)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(410, 140, 31, 61))
        self.label_3.setPixmap(QPixmap(u":/icons/icons/pngwing.com.png"))
        self.label_3.setScaledContents(True)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(410, 200, 31, 61))
        self.label_4.setPixmap(QPixmap(u":/icons/icons/pngwing.com.png"))
        self.label_4.setScaledContents(True)
        second_window.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(second_window)
        self.statusbar.setObjectName(u"statusbar")
        second_window.setStatusBar(self.statusbar)

        self.retranslateUi(second_window)

        QMetaObject.connectSlotsByName(second_window)
    # setupUi

    def retranslateUi(self, second_window):
        second_window.setWindowTitle(QCoreApplication.translate("second_window", u"MainWindow", None))
        self.back_button.setText(QCoreApplication.translate("second_window", u"Enter another country/city", None))
        self.country_name.setText(QCoreApplication.translate("second_window", u"RU*'", None))
        self.city_name.setText(QCoreApplication.translate("second_window", u"Moscow*", None))
        self.country.setItemText(0, QCoreApplication.translate("second_window", u"Select country", None))

        self.city.setItemText(0, QCoreApplication.translate("second_window", u"Select city", None))

        self.max_temp.setText(QCoreApplication.translate("second_window", u"MAX: ", None))
        self.min_temp.setText(QCoreApplication.translate("second_window", u"MIN: ", None))
        self.clouds.setText(QCoreApplication.translate("second_window", u"Clouds*", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
    # retranslateUi

