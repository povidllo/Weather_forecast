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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QWidget)
import resources_rc

class Ui_first_window(object):
    def setupUi(self, first_window):
        if not first_window.objectName():
            first_window.setObjectName(u"first_window")
        first_window.resize(440, 680)
        first_window.setMinimumSize(QSize(440, 680))
        first_window.setMaximumSize(QSize(440, 680))
        first_window.setStyleSheet(u"QWidget {\n"
"	color: black;\n"
"	background:rgb(73, 203, 255);\n"
"	font-family: Verdana ;\n"
"	font-weight: 600;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border: 0px;\n"
"}\n"
"QPushButton {\n"
"	background-color:rgb(73, 203, 255);\n"
"	border: 4px solid rgb(91, 91, 91);\n"
"	border-radius: 20px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:rgb(66, 183, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #888 ;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border-radius: 20px; /* \u0417\u0434\u0435\u0441\u044c \u043c\u043e\u0436\u043d\u043e \u043d\u0430\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0440\u0430\u0434\u0438\u0443\u0441 \u0441\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u044f \u0443\u0433\u043b\u043e\u0432 */\n"
"\n"
"    border: 4px solid rgb(91, 91, 91);\n"
"}\n"
"\n"
"\n"
"QComboBox:hover {\n"
"    background-color:rgb(66, 183, 255); /* \u0418\u0437\u043c\u0435\u043d\u0438\u0442\u0435 \u043d\u0430 \u0436\u0435\u043b\u0430\u0435\u043c\u044b\u0439 \u0446\u0432\u0435\u0442 \u043f\u0440"
                        "\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"\n"
"QComboBox:drop-down{\n"
"	border: 0px;\n"
"	background-color:rgb(73, 203, 255);\n"
"	border-radius: 20px\n"
"}\n"
"QComboBox:down-arrow{\n"
"	image: url(:/icons/icons/expand_more_FILL0_wght400_GRAD0_opsz48.png);\n"
"	width:30px;\n"
"	height: 30px;\n"
"	margin-right: 15px;\n"
"}\n"
"\n"
"QComboBox QListView{\n"
"	border: 0px;\n"
"padding: 5px;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(first_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.weather_button = QPushButton(self.centralwidget)
        self.weather_button.setObjectName(u"weather_button")
        self.weather_button.setGeometry(QRect(10, 520, 420, 111))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(19)
        font.setBold(True)
        self.weather_button.setFont(font)
        self.f_country = QComboBox(self.centralwidget)
        self.f_country.addItem("")
        self.f_country.setObjectName(u"f_country")
        self.f_country.setGeometry(QRect(10, 340, 420, 71))
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.f_country.setFont(font1)
        self.f_country.setLayoutDirection(Qt.LeftToRight)
        self.f_city = QComboBox(self.centralwidget)
        self.f_city.addItem("")
        self.f_city.setObjectName(u"f_city")
        self.f_city.setGeometry(QRect(10, 430, 420, 71))
        self.f_city.setFont(font1)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(0, 0, 440, 91))
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(30)
        font2.setBold(True)
        self.lineEdit.setFont(font2)
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 90, 260, 241))
        self.label.setStyleSheet(u"")
        self.label.setPixmap(QPixmap(u":/icons/icons/8179067.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 49, 16))
        first_window.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(first_window)
        self.statusbar.setObjectName(u"statusbar")
        first_window.setStatusBar(self.statusbar)

        self.retranslateUi(first_window)

        QMetaObject.connectSlotsByName(first_window)
    # setupUi

    def retranslateUi(self, first_window):
        first_window.setWindowTitle(QCoreApplication.translate("first_window", u"MainWindow", None))
        self.weather_button.setText(QCoreApplication.translate("first_window", u"Find out the weather forecast", None))
        self.f_country.setItemText(0, QCoreApplication.translate("first_window", u"Select country", None))

        self.f_city.setItemText(0, QCoreApplication.translate("first_window", u"Select city", None))

        self.lineEdit.setText(QCoreApplication.translate("first_window", u"Weather Forecast", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("first_window", u"TextLabel", None))
    # retranslateUi

