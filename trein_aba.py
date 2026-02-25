import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QPushButton

class MinhaJanela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemplo de Abas - PySide6")
        self.resize(400, 300)

        # 1. Criar o Widget de Abas
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # 2. Criar a primeira aba
        self.aba1 = QWidget()
        layout1 = QVBoxLayout()
        layout1.addWidget(QLabel("Esta é a página inicial"))
        layout1.addWidget(QPushButton("Botão na Aba 1"))
        self.aba1.setLayout(layout1)

        # 3. Criar a segunda aba
        self.aba2 = QWidget()
        layout2 = QVBoxLayout()
        layout2.addWidget(QLabel("Configurações e Opções"))
        self.aba2.setLayout(layout2)

        # 4. Adicionar as abas ao QTabWidget
        self.tabs.addTab(self.aba1, "Home")
        self.tabs.addTab(self.aba2, "Configurações")

        # Opcional: Adicionar ícones ou tornar as abas fecháveis
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.fechar_aba)

    def fechar_aba(self, index):
        self.tabs.removeTab(index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MinhaJanela()
    janela.show()
    sys.exit(app.exec())