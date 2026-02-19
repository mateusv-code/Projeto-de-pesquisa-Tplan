from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class JanelaEmpolamento(QMainWindow):
    def __init__(self, volume_corte_secoes = []):
        super().__init__()
        self.setWindowTitle('Calculadora de Empolamento Profissional')
        self.resize(450,400)
        incon_path = 'gui/img/IMG_TPLAN.png'
        self.setWindowIcon(QIcon(incon_path))
        
        volume_corte = round(sum(volume_corte_secoes),4)
        
        self.dados_solos = {
            'Solos argilosos': 40,
            'Terra comum seca': 25,
            'Terra comum úmida': 25,
            'Solo arenoso seco': 12,
            "Personalizado": 0
        }

        widget_central = QWidget()
        self.setCentralWidget(widget_central)
        self.main_layout_vertical = QVBoxLayout(widget_central)

        self.label_title = QLabel('Dimencionamento de Empolamento')
        self.label_title.setStyleSheet('font_size: 18px; font-weight: bold; color: #2c3e50')
        self.label_title.setAlignment(Qt.AlignCenter)
        self.main_layout_vertical.addWidget(self.label_title)

        self.main_layout_vertical.addWidget(QLabel('Volume corte(m³): '))
        self.input_v_corte = QLineEdit()
        self.input_v_corte.setPlaceholderText('Ex: 100 ')
        self.input_v_corte.setText(f'{volume_corte}')
        self.main_layout_vertical.addWidget(self.input_v_corte)

        self.main_layout_vertical.addWidget(QLabel('Tipo de Solo'))
        self.combo_solo = QComboBox()
        self.combo_solo.addItems(self.dados_solos.keys())
        self.combo_solo.currentIndexChanged.connect(self.atualizar_estado_campo)
        self.main_layout_vertical.addWidget(self.combo_solo)

        # Taxa de Empolamento (f%)
        self.main_layout_vertical.addWidget(QLabel("Taxa de Empolamento (%):"))
        self.input_taxa = QLineEdit()
        self.input_taxa.setText("40")  # Valor inicial do primeiro item
        self.input_taxa.setReadOnly(True) # Começa travado
        self.input_taxa.setStyleSheet("background-color: #f0f0f0;")
        self.main_layout_vertical.addWidget(self.input_taxa)

        # --- Ações e Resultados ---
        self.btn_calcular = QPushButton("CALCULAR VOLUME SOLTO")
        self.btn_calcular.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                font-weight: bold;
                padding: 12px;
                border-radius: 5px;
                margin-top: 10px;
            }
            QPushButton:hover { background-color: #219150; }
        """)
        self.btn_calcular.clicked.connect(self.calcular)
        self.main_layout_vertical.addWidget(self.btn_calcular)

        # Resultado
        self.frame_res = QFrame()
        self.frame_res.setFrameShape(QFrame.StyledPanel)
        self.res_layout = QVBoxLayout(self.frame_res)
        self.resultado_label = QLabel("Volume Final: ---")
        self.resultado_label.setAlignment(Qt.AlignCenter)
        self.resultado_label.setStyleSheet("font-size: 16px; color: #2c3e50; font-weight: bold;")
        self.res_layout.addWidget(self.resultado_label)
        self.main_layout_vertical.addWidget(self.frame_res)

    def atualizar_estado_campo(self):
        escolha = self.combo_solo.currentText()
        valor = self.dados_solos[escolha]
        
        if escolha == "Personalizado":
            self.input_taxa.setReadOnly(False)
            self.input_taxa.clear()
            self.input_taxa.setPlaceholderText("Digite o valor")
            self.input_taxa.setStyleSheet("background-color: white;")
            self.input_taxa.setFocus()
        else:
            self.input_taxa.setReadOnly(True)
            self.input_taxa.setText(str(valor))
            self.input_taxa.setStyleSheet("background-color: #f0f0f0;")

    def calcular(self):
        try:
            v_corte = float(self.input_v_corte.text().replace(',', '.'))
            taxa = float(self.input_taxa.text().replace(',', '.'))
            
            v_solto = v_corte * (1 + (taxa / 100))
            
            self.resultado_label.setText(f"Volume Final Solto: {v_solto:.2f} m³")
            self.resultado_label.setStyleSheet("font-size: 16px; color: #27ae60; font-weight: bold;")
        except ValueError:
            self.resultado_label.setText("Erro: Preencha os valores corretamente")
            self.resultado_label.setStyleSheet("color: #e74c3c; font-weight: bold;")


