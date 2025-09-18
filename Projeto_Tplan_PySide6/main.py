import sys
import os
from qt_core import *
from gui.windows.main_window.ui_main_window import ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tplan')
        icon_path = "gui/img/IMG_TPLAN.png"
        self.setWindowIcon(QIcon(icon_path))
        
        self.ui = ui_MainWindow()
        self.ui.setup_ui(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())




