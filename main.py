from PySide6.QtWidgets import QApplication

from src.views.main_window_view import MainWindow

import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec())
    