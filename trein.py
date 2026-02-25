import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QGridLayout, QMessageBox, QGroupBox
)


class ReducaoVolumetricaApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Módulo de Redução Volumétrica do Solo")
        self.setFixedSize(480, 520)

        layout = QGridLayout(self)

        # ===== GRUPO: ENTRADAS =====
        grupo_entrada = QGroupBox("Dados de Entrada")
        layout_entrada = QGridLayout()

        self.vs = QLineEdit()
        self.gd_solto = QLineEdit()
        self.gd_max = QLineEdit()
        self.gc = QLineEdit()
        self.w_otima = QLineEdit()
        self.w_campo = QLineEdit()

        entradas = [
            ("Volume do solo solto (m³)", self.vs),
            ("Peso esp. seco do solo solto (g/cm³)", self.gd_solto),
            ("Peso esp. seco máx. – Proctor (g/cm³)", self.gd_max),
            ("Grau de compactação (%)", self.gc),
            ("Umidade ótima (%)", self.w_otima),
            ("Umidade de campo (%) [opcional]", self.w_campo),
        ]

        for i, (texto, campo) in enumerate(entradas):
            layout_entrada.addWidget(QLabel(texto), i, 0)
            layout_entrada.addWidget(campo, i, 1)

        grupo_entrada.setLayout(layout_entrada)
        layout.addWidget(grupo_entrada, 0, 0)

        # ===== BOTÃO =====
        self.botao = QPushButton("CALCULAR")
        self.botao.clicked.connect(self.calcular)
        layout.addWidget(self.botao, 1, 0)

        # ===== GRUPO: RESULTADOS =====
        grupo_saida = QGroupBox("Resultados")
        layout_saida = QGridLayout()

        self.frv = QLabel("-")
        self.gd_aterro = QLabel("-")
        self.vc = QLabel("-")
        self.reducao = QLabel("-")
        self.status_umidade = QLabel("-")

        saidas = [
            ("Fator de redução volumétrico: ", self.frv),
            ("Peso esp. seco no aterro (g/cm³): ", self.gd_aterro),
            ("Volume compactado (m³): ", self.vc),
            ("Redução volumétrica (%): ", self.reducao),
            ("Status da umidade: ", self.status_umidade),
        ]

        for i, (texto, campo) in enumerate(saidas):
            layout_saida.addWidget(QLabel(texto), i, 0)
            layout_saida.addWidget(campo, i, 1)

        grupo_saida.setLayout(layout_saida)
        layout.addWidget(grupo_saida, 2, 0)

    def calcular(self):
        try:
            Vs = float(self.vs.text())
            gd_solto = float(self.gd_solto.text())
            gd_max = float(self.gd_max.text())
            GC = float(self.gc.text()) / 100


            # Peso específico seco no aterro
            gd_aterro = gd_max * GC

            # Fator de redução volumétrico
            frv = gd_solto/gd_aterro

            # Volume compactado
            Vc = frv*Vs

            # Redução volumétrica
            reducao = ((Vs - Vc) / Vs) * 100

            # Resultados
            self.frv.setText(f"{frv:.2f}")
            self.gd_aterro.setText(f"{gd_aterro:.2f}")
            self.vc.setText(f"{Vc:.2f}")
            self.reducao.setText(f"{reducao:.2f}")

            # Avaliação da umidade
            if self.w_campo.text():
                w = float(self.w_campo.text())
                w_ot = float(self.w_otima.text())

                if abs(w - w_ot) <= 2:
                    self.status_umidade.setText("Dentro da umidade ótima ✔")
                elif w < w_ot:
                    self.status_umidade.setText("Abaixo da umidade ótima ⚠")
                else:
                    self.status_umidade.setText("Acima da umidade ótima ⚠")
            else:
                self.status_umidade.setText("Não informada")

        except ValueError:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos obrigatórios corretamente.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = ReducaoVolumetricaApp()
    janela.show()
    sys.exit(app.exec())