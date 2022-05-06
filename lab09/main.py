import sys
from PyQt6.QtWidgets import QApplication, QDialog
from form import Ui_Widget


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QDialog()
    ui = Ui_Widget()
    ui.setupUi(window)

    window.show()
    sys.exit(app.exec())
