import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow

import cities
from first import Ui_first_window
from second import Ui_second_window


class f_window(QMainWindow):  # first screen (choosing country and city)
    def __init__(self):
        super(f_window, self).__init__()
        self.ui = Ui_first_window()
        self.ui.setupUi(self)
        for i in cities.get_city():
            self.ui.f_country.addItems([i])
        self.ui.f_country.currentIndexChanged.connect(self.update_city)
        self.ui.f_button.pressed.connect(self.pressed)


    def pressed(self):  # Implementation of first page button press and get country and city
        city = self.ui.f_city.currentText()
        country = self.ui.f_country.currentText()
        global second_window
        second_window = s_window(city, country)
        main_window.close()
        second_window.show()

        def return_to_main():
            second_window.close()
            main_window.show()

        second_window.ui.s_button.clicked.connect(return_to_main)

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
        self.city = city
        self.country = country
        self.ui.lineEdit.setText(self.city)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = f_window()
    main_window.show()
    sys.exit(app.exec())
