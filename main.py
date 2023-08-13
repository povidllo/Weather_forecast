from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtWidgets
from first import Ui_first_window
from second import Ui_second_window
import cities
import sys

class f_window(QMainWindow):
    def __init__(self):
        super(f_window,self).__init__()
        self.ui = Ui_first_window()
        self.ui.setupUi(self)
        self.ui.f_button.clicked.connect(self.gotoWindow2)
        for i in cities.get_city():
            self.ui.f_coutry.addItems([i])
        self.ui.f_coutry.currentIndexChanged.connect(self.update_city)
        self.ui.f_button.pressed.connect(self.pressed)

    def gotoWindow2(self):
        wiget.setCurrentIndex(wiget.currentIndex()+1)

    def pressed(self):
        print(self.ui.f_coutry.currentText())

    def update_city(self):
        country = self.ui.f_coutry.currentText()

        if country == 'Russia':
            self.ui.f_city.clear()
            self.ui.f_city.addItems(['Moscow', 'St. Petersburg', 'Novosibirsk'])
        elif country == 'Canada':
            self.ui.f_city.clear()
            self.ui.f_city.addItems(['Toronto', 'Vancouver'])

class s_window(QMainWindow):
    def __init__(self):
        super(s_window,self).__init__()
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
