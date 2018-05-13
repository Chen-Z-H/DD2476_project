import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from se_gui import Ui_MainWindow


def show_window():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    se_ui = Ui_MainWindow()
    se_ui.iniWindow(MainWindow)

    MainWindow.show()
    # app.exec_()
    sys.exit(app.exec_())


show_window()

