import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget

import cities
import get_weather
from first import Ui_first_window
from second import Ui_second_window

from PySide6.QtGui import QPixmap


class f_window(QMainWindow):  # first screen (choosing country and city)
    def __init__(self):
        super(f_window, self).__init__()
        self.ui = Ui_first_window()
        self.ui.setupUi(self)
        for i in cities.get_city():
            self.ui.f_country.addItems([i])
        self.ui.f_country.currentIndexChanged.connect(self.update_city)
        self.ui.weather_button.pressed.connect(self.pressed)



    def pressed(self):  # Implementation of first page button press and get country and city
        if self.ui.weather_button.isDown():
            city = self.ui.f_city.currentText()
            country = self.ui.f_country.currentText()
            second = s_window(city, country)
            widget.addWidget(second)
            widget.setCurrentIndex(widget.currentIndex() + 1)

    def update_city(self):  # Implementation of choosing a country and updating the city list
        country = self.ui.f_country.currentText()
        for i in cities.get_city():
            if country == i:
                self.ui.f_city.clear()
                self.ui.f_city.addItems(cities.get_city()[i])
            elif country == 'Select country':
                self.ui.f_city.clear()
                self.ui.f_city.addItem('Select city')


class s_window(QMainWindow):  # Second screen
    def __init__(self, city, country):
        super(s_window, self).__init__()
        self.ui = Ui_second_window()
        self.ui.setupUi(self)
        self.ui.country_name.setText(country)
        self.ui.city_name.setText(city)
        for i in cities.get_city():
            self.ui.country.addItems([i])
        self.ui.country.currentIndexChanged.connect(self.update_city)
        self.ui.back_button.clicked.connect(self.refresh)
        min, max, temp = get_weather.weather(city, 0)

        self.ui.degree.setDigitCount(3) #колличество цифр
        self.ui.max_degree.setDigitCount(3)
        self.ui.min_degree.setDigitCount(3)
        self.ui.degree.display(temp)
        self.ui.min_degree.display(min)
        self.ui.max_degree.display(temp)


    def refresh(self):
        city = self.ui.city.currentText()
        country = self.ui.country.currentText()
        self.ui.country_name.setText(country)
        self.ui.city_name.setText(city)
        min, max, temp = get_weather.weather(city, 0)
        self.ui.degree.display(temp)
        self.ui.min_degree.display(min)
        self.ui.max_degree.display(temp)



    def update_city(self):  # Implementation of choosing a country and updating the city list
        country = self.ui.country.currentText()
        for i in cities.get_city():
            if country == i:
                self.ui.city.clear()
                self.ui.city.addItems(cities.get_city()[i])
            elif country == 'Select country':
                self.ui.city.clear()
                self.ui.city.addItem('Select city')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget=QtWidgets.QStackedWidget()
    main_window = f_window()
    widget.addWidget(main_window)
    widget.setFixedHeight(680)
    widget.setFixedWidth(440)
    widget.show()

    sys.exit(app.exec())