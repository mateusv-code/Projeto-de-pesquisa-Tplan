import sys
import os
from qt_core import *
from gui.windows.main_window.ui_main_window import ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tplan')
        icon_path = self.resource_path("gui/img/IMG_TPLAN.png")
        self.setWindowIcon(QIcon(icon_path))
        
        self.ui = ui_MainWindow()
        self.ui.setup_ui(self)
    def resource_path(self,relative_path):
        """ Retorna o caminho absoluto para o recurso, funcionando tanto em dev quanto no PyInstaller """
        try:
            # O PyInstaller cria uma pasta temporária e armazena o caminho em _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
    
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())




