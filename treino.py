import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel


# Janela Secundária
class SegundaJanela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Segunda Janela")
        self.resize(300, 200)

        # Conteúdo da janela
        label = QLabel("Essa é a segunda janela!", self)
        label.move(50, 80)


# Janela Principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")
        self.resize(400, 300)

        # Botão
        self.botao = QPushButton("Abrir nova janela")
        self.botao.clicked.connect(self.abrir_janela)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.botao)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Criar referência para a outra janela
        self.segunda_janela = None

    def abrir_janela(self):
        if self.segunda_janela is None:
            self.segunda_janela = SegundaJanela()
        self.segunda_janela.show()  # Mostra a nova janela


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
