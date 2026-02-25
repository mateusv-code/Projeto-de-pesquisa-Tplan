from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class JanelaEmpolamento(QMainWindow):
    def __init__(self, volume_corte_secoes = []):
        super().__init__()
        self.setWindowTitle('Empolamento & Redução')
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

        # 1. Criar o Widget de Abas
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.aba1 = QWidget()
        self.main_layout_vertical = QVBoxLayout(self.aba1)       
        

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

        #aqui
        self.aba2 = QWidget()
        layout = QGridLayout(self.aba2)

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
        self.botao.clicked.connect(self.calcular2)
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

        # 4. Adicionar as abas ao QTabWidget
        self.tabs.addTab(self.aba1, "Empolamento")
        self.tabs.addTab(self.aba2, "Redução Volumétrica")

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

    def calcular2(self):
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

