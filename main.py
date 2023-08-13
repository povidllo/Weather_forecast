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
        self.ui.f_button.clicked.connect(self.gotoWindow2)
        for i in cities.get_city():
            self.ui.f_country.addItems([i])
        self.ui.f_country.currentIndexChanged.connect(self.update_city)
        self.ui.f_button.pressed.connect(self.pressed)

    def gotoWindow2(self):  # Implementation screens
        wiget.setCurrentIndex(wiget.currentIndex() + 1)

    def pressed(self):  # Implementation of first page button press and get country and city
        self.country = self.ui.f_country.currentText()
        self.city = self.ui.f_city.currentText()
        print(self.country, self.city)

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
    def __init__(self):
        super(s_window, self).__init__()
        self.ui = Ui_second_window()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wiget = QtWidgets.QStackedWidget()

    main_window = f_window()
    window2 = s_window()

    wiget.addWidget(main_window)
    wiget.addWidget(window2)

    wiget.setFixedWidth(500)
    wiget.setFixedHeight(500)

    # main_window.show()
    wiget.show()
    sys.exit(app.exec())
