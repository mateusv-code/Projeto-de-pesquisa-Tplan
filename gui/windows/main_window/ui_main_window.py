from qt_core import*
from gui.windows.segunda_janela import *
from gui.windows.janela_empolamento import *
import numpy as np 
from gui.gráficos.graficos import *
import pandas as pd
import sys
import os
from fpdf import FPDF

class ui_MainWindow(object):
    def setup_ui(self,parent):
        if not parent.objectName():
            parent.setObjectName('MainWindow')

            parent.resize(1455,705)
            parent.setMinimumSize(1455,705)
            self.central_frame = QFrame()
            parent.setCentralWidget(self.central_frame)

            self.lista_de_line_edits_matriz = [] 

            self.table = None
            self.table_2 = None

            self.volume_corte = 0
            self.volume_aterro = 0

            # CREATE MAIN LAYOUT

            self.main_vertical_layout = QVBoxLayout(self.central_frame)
            self.main_vertical_layout.setContentsMargins(0,0,0,0)
            self.main_vertical_layout.setSpacing(0)
            # TOP FRAME

            self.main_top_frame = QFrame()
            #self.main_top_frame.setStyleSheet('background-color: red')

            # BOTTOM FRAME

            self.main_bottom_frame = QFrame()
            self.main_bottom_frame.setMinimumHeight(100)
            self.main_bottom_frame.setMaximumHeight(100)
            

            # LAYOUT
            self.main_vertical_layout.addWidget(self.main_top_frame)
            self.main_vertical_layout.addWidget(self.main_bottom_frame)
            self.main_bottom_frame.setStyleSheet('background-color: #f0f0f0')

            self.fist_layout_horizontal()

            self.widgets_panel_1()

            self.widgets_panel_2()

            self.widgets_panel_3()

            self.descricao()

    def fist_layout_horizontal(self):
        # Create layout horizontal
        self.main_layout_horizontal = QHBoxLayout(self.main_top_frame)
        self.main_layout_horizontal.setContentsMargins(0,0,0,0)
        self.main_layout_horizontal.setSpacing(0)

        # Create left panel

        self.left_panel = QFrame()
        #self.left_panel.setStyleSheet('background-color: #f0f0f0')
        self.left_panel.setStyleSheet("""
                QFrame {
                    background-color: #f0f0f0;
                }
                QPushButton {
                    background-color: white; /* Cor cinza padrão do Qt */
                }
                QLineEdit {
                    background-color: white; /* Cor branca para os campos de texto */
                    border:  0.5px solid gray
                }              
            """)
        self.left_panel.setMaximumWidth(420)
        self.left_panel.setMinimumWidth(420)

        # Create central panel

        self.central_panel = QFrame()
        self.central_panel.setStyleSheet("""
                QFrame {
                    background-color: #f0f0f0;
                }
                QPushButton {
                    background-color: white; /* Cor cinza padrão do Qt */
                
            """)
        
        # Create right panel

        self.right_panel = QFrame()
        self.right_panel.setStyleSheet("""
                QFrame {
                    background-color: #f0f0f0;
                }
                QPushButton {
                    background-color: white; /* Cor cinza padrão do Qt */
                }
                QScrollArea {
                    background-color: white
                }
            """)
        self.right_panel.setMinimumWidth(522)
        self.right_panel.setMaximumWidth(522)

        # Layout
        self.main_layout_horizontal.addWidget(self.left_panel)
        self.main_layout_horizontal.addWidget(self.central_panel)
        self.main_layout_horizontal.addWidget(self.right_panel)


    def widgets_panel_1(self):

        self.left_vertical_layout = QVBoxLayout(self.left_panel)

        self.logo1_label = QLabel()
        # To add an image, use QPixmap:
        pixmap1 = QPixmap(self.resource_path("gui/img/IMG_IFMA.png")).scaledToWidth(150, Qt.SmoothTransformation)
        self.logo1_label.setPixmap(pixmap1)
        self.left_vertical_layout.addWidget(self.logo1_label, alignment=Qt.AlignCenter)

        self.spacer_item1 = QSpacerItem(20,40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.left_vertical_layout.addItem(self.spacer_item1)
        #Box Dimensoes da quadrícula

        self.dimensoes_group = QGroupBox("DIMENSÕES DA QUADRÍCULA")
        self.dimensoes_group.setMaximumHeight(125)
        self.dimensoes_group.setMaximumWidth(250)
        self.dimensoes_layout = QGridLayout(self.dimensoes_group)
        
        self.dimensoes_layout.addWidget(QLabel("Dimensão em X"), 0, 0)
        self.dimensao_X = QLineEdit()
        self.dimensao_X.setAlignment(Qt.AlignCenter)
        self.dimensoes_layout.addWidget(self.dimensao_X, 0, 1)
        self.dimensoes_layout.addWidget(QLabel("Dimensão em Y"), 1, 0)
        self.dimensao_Y = QLineEdit()
        self.dimensao_Y.setAlignment(Qt.AlignCenter)
        self.dimensoes_layout.addWidget(self.dimensao_Y, 1, 1)
        self.left_vertical_layout.addWidget(self.dimensoes_group, alignment= Qt.AlignCenter)

        self.spacer_item3 = QSpacerItem(20,20, QSizePolicy.Minimum)
        self.left_vertical_layout.addItem(self.spacer_item3)

        # Box Quadriculação

        self.quadriculacao_group = QGroupBox("QUADRICULAÇÃO")
        self.quadriculacao_group.setMaximumHeight(125)
        self.quadriculacao_group.setMaximumWidth(250)
        self.quadriculacao_layout = QGridLayout(self.quadriculacao_group)
        self.quadriculacao_layout.addWidget(QLabel("Nº de Seções Longitudinais"), 0, 0)
        self.secao_longitudinal = QLineEdit()
        self.secao_longitudinal.setAlignment(Qt.AlignCenter)
        self.quadriculacao_layout.addWidget(self.secao_longitudinal, 0, 1)
        self.quadriculacao_layout.addWidget(QLabel("Nº de Seções Transversais"), 1, 0)
        self.secao_transversal = QLineEdit()
        self.secao_transversal.setAlignment(Qt.AlignCenter)
        self.quadriculacao_layout.addWidget(self.secao_transversal, 1, 1)
        self.left_vertical_layout.addWidget(self.quadriculacao_group, alignment= Qt.AlignCenter)

                # "GERAR QUADRÍCULAS" Button
        self.gerar_button = QPushButton("GERAR QUADRÍCULAS")
        self.left_vertical_layout.addWidget(self.gerar_button, alignment= Qt.AlignCenter)
        self.gerar_button.clicked.connect(self.gerar_campos)

        self.spacer_item1 = QSpacerItem(20,100, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.left_vertical_layout.addItem(self.spacer_item1)

    def widgets_panel_2(self):
        self.center_panel_layout = QGridLayout(self.central_panel)
        self.center_panel_layout.setContentsMargins(0,0,0,0)
        self.center_panel_layout.setSpacing(0)

        self.tplan_logo_label = QLabel()
        self.pixmap_tplan = QPixmap(self.resource_path("gui/img/IMG_TPLAN.png")).scaledToWidth(450, Qt.SmoothTransformation)
        self.tplan_logo_label.setPixmap(self.pixmap_tplan)
        self.center_panel_layout.addWidget(self.tplan_logo_label, 0, 1, 1, 1, alignment=Qt.AlignCenter)

        self.spacer_item3 = QSpacerItem(20,40, QSizePolicy.Minimum)
        self.center_panel_layout.addItem(self.spacer_item3, 1,2)

          # "COTAS DO TERRENO NATURAL" Label
        self.cota_terreno_label = QLabel("COTAS DO TERRENO NATURAL")
        self.cota_terreno_label.setMaximumHeight(25)
        self.cota_terreno_label.setStyleSheet('font-size: 11pt; font-weight:bold')
        self.cota_terreno_label.setAlignment(Qt.AlignCenter)
        self.center_panel_layout.addWidget(self.cota_terreno_label, 2, 1)

        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)

        self.scroll_area_cota = QScrollArea()
        self.scroll_area_cota.setWidget(self.scroll_widget)
        self.scroll_area_cota.setMaximumHeight(260)
        self.scroll_area_cota.setWidgetResizable(True)
        self.scroll_area_cota.setStyleSheet("border: 0.5px solid gray; background-color: white")

        self.center_panel_layout.addWidget(self.scroll_area_cota, 3, 1, 3, 1)

        # "PLATAFORMA" and "CALCULAR" buttons
        self.plataforma_button = QPushButton("PLATAFORMA")
        self.plataforma_button.clicked.connect(self.plataforma)
        self.botao_importar_excel = QPushButton("IMPORTAR .XLSX")
        self.botao_importar_excel.clicked.connect(self.importar_excel)
        self.center_panel_layout.addWidget(self.plataforma_button, 7, 1, alignment=Qt.AlignCenter)
        self.center_panel_layout.addWidget(self.botao_importar_excel, 6, 1, alignment=Qt.AlignRight)
    
    def widgets_panel_3(self):
        self.right_panel_layout = QVBoxLayout(self.right_panel)
        self.right_panel_layout.setContentsMargins(0,10,0,0)
        self.right_panel_layout.setSpacing(5)

        self.logo2_label = QLabel()
        self.pixmap2 = QPixmap(self.resource_path("gui/img/IMG_ENG_CIV.png")).scaledToWidth(170, Qt.SmoothTransformation)
        self.logo2_label.setPixmap(self.pixmap2)
        self.right_panel_layout.addWidget(self.logo2_label, alignment=Qt.AlignCenter)

        self.spacer_item = QSpacerItem(20,55, QSizePolicy.Minimum)
        self.right_panel_layout.addItem(self.spacer_item)

        self.spacer_item = QSpacerItem(20,55, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.right_panel_layout.addItem(self.spacer_item)

        # "COTA DE PLATAFORMA" GroupBox
        self.cota_group = QGroupBox("COTA DE PLATAFORMA")
        self.cota_group.setMaximumWidth(250)
        self.cota_group.setMinimumWidth(250)
        self.cota_group.setMinimumHeight(80)
        self.cota_group.setMaximumHeight(80)
        self.cota_layout = QGridLayout(self.cota_group)
        self.cota_layout.addWidget(QLabel("Calculada"), 0, 0)
        self.label_calculada = QLabel()
        self.label_calculada.setAlignment(Qt.AlignCenter)
        self.label_calculada.setStyleSheet('border: 0.5px solid gray; background-color: white')
        self.cota_layout.addWidget(self.label_calculada, 0, 1)
        
        self.cota_layout.addWidget(QLabel("Adotada"), 1, 0)
        self.entry_adotada =  QLineEdit()
        self.entry_adotada.setAlignment(Qt.AlignCenter)
        self.entry_adotada.setStyleSheet('border: 0.5px solid gray; background-color: white')
        self.cota_layout.addWidget(self.entry_adotada, 1, 1)  
        self.right_panel_layout.addWidget(self.cota_group, alignment= Qt.AlignCenter)

        self.spacer_item = QSpacerItem(20,10, QSizePolicy.Minimum)
        self.right_panel_layout.addItem(self.spacer_item)

        self.frame_pos_inclinacao = QFrame()
        self.right_panel_layout.addWidget(self.frame_pos_inclinacao)

        self.layout_pos_inclinação = QGridLayout(self.frame_pos_inclinacao)


        # "INCLINAÇÕES DE PROJETO (%)" GroupBox
        self.inclinacoes_group = QGroupBox("INCLINAÇÕES DE PROJETO (%)")
        self.inclinacoes_group.setMaximumHeight(120)
        self.inclinacoes_group.setMinimumHeight(120)
        self.inclinacoes_group.setMinimumWidth(450)
        self.inclinacoes_group.setMaximumWidth(450)
        self.inclinacoes_layout = QGridLayout(self.inclinacoes_group)

        self.scroll_widget_2 = QWidget()
        self.scroll_layout_2 = QVBoxLayout(self.scroll_widget_2)


        self.scroll_area_inclinacao = QScrollArea()
        self.scroll_area_inclinacao.setWidget(self.scroll_widget_2)
        self.scroll_area_inclinacao.setWidgetResizable(True)
        self.scroll_area_inclinacao.setStyleSheet("border: 0.5px solid gray ; background-color: white")

        # ADICIONE OU ALTERE ESTA LINHA:
        #self.scroll_area_inclinacao.setMinimumHeight(80) # Define uma altura mínima maior
        #self.scroll_area_inclinacao.setMaximumHeight(80)
        
        self.inclinacoes_layout.addWidget(self.scroll_area_inclinacao, 0, 0, 1, 2)
        self.layout_pos_inclinação.addWidget(self.inclinacoes_group, 3, 2)

        # "RELATÓRIO" and "RESUMO DE VOLUMES" buttons
        self.importar_inclinacao_button = QPushButton("IMPORTAR .XLSX")
        self.importar_inclinacao_button.clicked.connect(self.importar_excel_inclinacao)
        self.calcular_button = QPushButton("CALCULAR")
        self.calcular_button.clicked.connect(self.calcular_volumes)
        self.calculadora_empolamento = QPushButton('EMPOLAMENTO E REDUÇÃO')
        self.calculadora_empolamento.clicked.connect(self.abrir_janela_empolamento)
        self.relatorio_button = QPushButton('RELATÓRIO')
        self.relatorio_button.clicked.connect(self.relatorio)
        self.resumo_button = QPushButton('RESUMO DE VOLUMES')
        self.resumo_button.clicked.connect(self.abrir_janela_resumo_volumes)
        self.layout_pos_inclinação.addWidget(self.importar_inclinacao_button, 5, 2, alignment=Qt.AlignRight)
        self.layout_pos_inclinação.addWidget(self.calcular_button, 5, 2, alignment=Qt.AlignCenter)
        self.layout_pos_inclinação.addWidget(self.relatorio_button, 6, 2, alignment=Qt.AlignRight)
        self.layout_pos_inclinação.addWidget(self.resumo_button, 7,2, alignment=Qt.AlignRight)
        self.layout_pos_inclinação.addWidget(self.calculadora_empolamento, 8,2, alignment=Qt.AlignRight)

        self.spacer_item = QSpacerItem(20,75, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.right_panel_layout.addItem(self.spacer_item)

        self.segunda_janela = None

    def resource_path(self,relative_path):
        """ Retorna o caminho absoluto para o recurso, funcionando tanto em dev quanto no PyInstaller """
        try:
            # O PyInstaller cria uma pasta temporária e armazena o caminho em _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def descricao(self):
        
        self.descricao_layout = QHBoxLayout(self.main_bottom_frame)
        self.descricao_layout.setContentsMargins(0,0,0,0)
        self.descricao_layout.setSpacing(0)

        self.descricao_group = QGroupBox('Descrição')
        self.descricao_group_layout = QGridLayout(self.descricao_group)
        # Description label
        self.bottom_info_label = QLabel(
            "<html>"
            "Programa de Terraplenagem apresentado ao Instituto Federal de Educação, Ciência e Tecnologia do Maranhão como requisito parcial para T<br>"
            "obtenção do título de Bacharel em Engenharia Civil. T<br>"
            "Desenvolvido por: <b> João Vitor Caldas Santos </b><br>"
            "Banca Avaliadora:<b> Prof. Dr. Antonio Jorge Parga da Silva; Prof. Msc. Andrey Sales Lopes; Prof. Dr. Luis Fernando Sampaio Soares <b>"
            "<html>"
        )
        self.bottom_info_label.setStyleSheet('line-height: 10%; font-size: 8pt')
        self.descricao_group_layout.addWidget(self.bottom_info_label)
        self.descricao_layout.addWidget(self.descricao_group, alignment=Qt.AlignRight)

    def relatorio(self):
        if not hasattr(self, 'mat_cotas') or not hasattr(self, 'volumes_de_corte_secoes'):
            QMessageBox.warning(None, "Atenção", "Execute o CALCULAR primeiro para gerar os dados.")
            return

        caminho_pdf = os.path.abspath("relatorio_detalhado.pdf")
        dx = float(self.dimensao_X.text())
        dy = float(self.dimensao_Y.text())

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        
        # Cabeçalho
        pdf.cell(190, 10, "RELATÓRIO DE MEMÓRIA DE CÁLCULO", ln=True, align="C")
        pdf.set_font("Arial", "", 10)
        pdf.cell(190, 5, "Sistema TPlan - Engenharia Civil", ln=True, align="C")
        pdf.ln(10)

        # --- 1. MEMORIAL DA COTA DE PLATAFORMA ---
        pdf.set_fill_color(200, 220, 255)
        pdf.set_font("Arial", "B", 12)
        pdf.cell(190, 8, "1. MEMORIAL DA COTA DE PLATAFORMA", ln=True, fill=True)
        pdf.ln(2)
        pdf.set_font("Courier", "", 9)

        # Lógica de separação dos pesos (simplificada para o PDF)
        txt_p1, txt_p2, txt_p4 = [], [], []
        s1, s2, s4 = 0, 0, 0
        for i in range(self.linhas):
            for j in range(self.colunas):
                c = self.mat_cotas[i, j]
                if (i == 0 and j == 0) or (i == 0 and j == self.colunas-1) or \
                (i == self.linhas-1 and j == 0) or (i == self.linhas-1 and j == self.colunas-1):
                    txt_p1.append(f"{c:.2f}"); s1 += c
                elif i == 0 or i == self.linhas-1 or j == 0 or j == self.colunas-1:
                    txt_p2.append(f"{c:.2f}"); s2 += c
                else:
                    txt_p4.append(f"{c:.2f}"); s4 += c

        pdf.multi_cell(190, 5, f"PESO 1 (Vértices): {' + '.join(txt_p1)} = {s1:.2f}")
        pdf.multi_cell(190, 5, f"PESO 2 (Bordas):   {' + '.join(txt_p2)} = {s2:.2f}")
        pdf.multi_cell(190, 5, f"PESO 4 (Internos): {' + '.join(txt_p4) if txt_p4 else '0.00'} = {s4:.2f}")
        
        pdf.set_font("Arial", "B", 10)
        somatoria_final = (s1*1 + s2*2 + s4*4)
        total_pesos = (1*len(txt_p1) + 2*len(txt_p2) + 4*len(txt_p4))
        pdf.ln(2)
        pdf.cell(190, 5, f"Somatória Final: {somatoria_final:.2f} / Total Pesos: {total_pesos}", ln=True)
        pdf.set_text_color(230, 126, 34)
        pdf.cell(190, 7, f"COTA ADOTADA: {self.cota_adotada:.6f}", ln=True)
        pdf.set_text_color(0, 0, 0)
        pdf.ln(5)

        # --- 2. MEMORIAL DE ÁREAS (TABELA) ---
        pdf.set_font("Arial", "B", 12)
        pdf.set_fill_color(200, 220, 255)
        pdf.cell(190, 8, "2. MEMORIAL DE CÁLCULO DAS ÁREAS (m2)", ln=True, fill=True)
        pdf.ln(2)
        
        # Cabeçalho da Tabela
        pdf.set_font("Arial", "B", 9)
        pdf.cell(30, 7, "Seção", 1, 0, "C")
        pdf.cell(120, 7, "Fórmula: [(h1 + h2) / 2] * dx", 1, 0, "C")
        pdf.cell(40, 7, "Resultado", 1, 1, "C")
        
        pdf.set_font("Courier", "", 8)
        # Mostra as primeiras seções para não estourar o PDF
        for i in range(min(self.linhas, 15)):
            for j in range(self.colunas - 1):
                h1 = self.mat_cotas[i, j] - self.cotas_plataforma_mista[i, j]
                h2 = self.mat_cotas[i, j+1] - self.cotas_plataforma_mista[i, j+1]
                area = ((h1 + h2) / 2) * dx
                pdf.cell(30, 6, f"S{i+1}-A{j+1}", 1, 0, "C")
                pdf.cell(120, 6, f"[({self.mat_cotas[i,j]:.2f}-{self.cotas_plataforma_mista[i,j]:.2f})+({self.mat_cotas[i,j+1]:.2f}-{self.cotas_plataforma_mista[i,j+1]:.2f})] * {dx/2}", 1, 0, "L")
                pdf.cell(40, 6, f"{area:.4f}", 1, 1, "C")

        pdf.ln(5)

        # --- 3. RESUMO DE VOLUMES ---
        pdf.set_font("Arial", "B", 12)
        pdf.set_fill_color(200, 220, 255)
        pdf.cell(190, 8, "3. RESUMO DE VOLUMES POR SEÇÃO", ln=True, fill=True)
        pdf.ln(2)

        pdf.set_font("Arial", "B", 9)
        pdf.cell(60, 7, "Seção Longitudinal", 1, 0, "C")
        pdf.cell(65, 7, "Volume Corte (m3)", 1, 0, "C")
        pdf.cell(65, 7, "Volume Aterro (m3)", 1, 1, "C")

        pdf.set_font("Arial", "", 9)
        for i in range(self.linhas):
            pdf.cell(60, 6, f"Seção {i+1}", 1, 0, "C")
            pdf.set_text_color(192, 57, 43) # Vermelho para corte
            pdf.cell(65, 6, f"{self.volumes_de_corte_secoes[i]:.2f}", 1, 0, "C")
            pdf.set_text_color(39, 174, 96) # Verde para aterro
            pdf.cell(65, 6, f"{self.volumes_de_aterro_secoes[i]:.2f}", 1, 1, "C")
            pdf.set_text_color(0, 0, 0)

        # Totais
        pdf.set_font("Arial", "B", 10)
        pdf.cell(60, 8, "TOTAIS FINAIS", 1, 0, "C", fill=True)
        pdf.cell(65, 8, f"{np.sum(self.volumes_de_corte_secoes):.2f} m3", 1, 0, "C")
        pdf.cell(65, 8, f"{np.sum(self.volumes_de_aterro_secoes):.2f} m3", 1, 1, "C")

        # Salvar e Abrir
        try:
            pdf.output(caminho_pdf)
            os.startfile(caminho_pdf) # Comando para abrir no Windows
        except Exception as e:
            QMessageBox.critical(None, "Erro", f"Não foi possível gerar o PDF: {str(e)}")

    
    def gerar_campos(self):
        try:
            self.linhas = int(self.secao_longitudinal.text())
            self.colunas = int(self.secao_transversal.text())
        except ValueError:
            QMessageBox.warning(None, 'Error', 'Digite apenas números nos campos de seções!')
            return


        # Só recria se o tamanho mudou ou se ela ainda não existe
        if not self.table or self.table.rowCount() != self.linhas or self.table.columnCount() != self.colunas:
            if self.table:
                self.scroll_layout.removeWidget(self.table)
                self.table.deleteLater()

            self.table = QTableWidget(self.linhas, self.colunas)
            self.scroll_layout.addWidget(self.table)
            for i in range(self.linhas):
                for j in range(self.colunas):
                    self.table.setItem(i, j, QTableWidgetItem("0"))

        # --- LÓGICA PARA A TABELA DE INCLINAÇÕES (table 2) ---
        novas_colunas_inc = self.colunas - 1
        if not self.table_2 or self.table_2.columnCount() != novas_colunas_inc:
            if self.table_2:
                self.scroll_layout_2.removeWidget(self.table_2)
                self.table_2.deleteLater()

            self.table_2 = QTableWidget(1, novas_colunas_inc)
            self.scroll_layout_2.addWidget(self.table_2)
            for j in range(novas_colunas_inc):
                self.table_2.setItem(0, j, QTableWidgetItem("0"))

    def importar_excel(self):
        # 1. Abrir seletor de arquivo
        caminho_arquivo, _ = QFileDialog.getOpenFileName(
            None, "Selecionar Planilha de Cotas", "", "Arquivos Excel (*.xlsx *.xls)"
        )

        if caminho_arquivo:
            try:
                # 2. Ler o Excel usando pandas
                # Considera que a planilha não tem cabeçalho ou o dado começa na célula A1
                df = pd.read_excel(caminho_arquivo, header=None)
                
                # 3. Pegar dimensões do arquivo
                n_linhas, n_colunas = df.shape

                # 4. Atualizar os campos de texto da interface
                self.secao_longitudinal.setText(str(n_linhas))
                self.secao_transversal.setText(str(n_colunas))

                # 5. Gerar a tabela na interface (reutiliza sua função existente)
                self.gerar_campos()

                # 6. Preencher a QTableWidget com os dados do Excel
                for i in range(n_linhas):
                    for j in range(n_colunas):
                        valor = df.iloc[i, j]
                        # Verifica se o valor é um número para evitar erros de exibição
                        valor_str = str(valor) if pd.notnull(valor) else "0"
                        self.table.setItem(i, j, QTableWidgetItem(valor_str))

                QMessageBox.information(None, "Sucesso", "Dados importados com sucesso!")

            except Exception as e:
                QMessageBox.critical(None, "Erro", f"Falha ao ler o arquivo: {str(e)}")

    def importar_excel_inclinacao(self):
        # 1. Abrir seletor de arquivo
        caminho_arquivo, _ = QFileDialog.getOpenFileName(
            None, "Selecionar Planilha de Inclinações", "", "Arquivos Excel (*.xlsx *.xls)"
        )

        if caminho_arquivo:
            try:
                # 2. Ler o Excel
                df = pd.read_excel(caminho_arquivo, header=None)
                
                # Converter para uma lista simples (achatar a matriz caso venha como linha ou coluna)
                dados = df.values.flatten()
                n_inclinações = len(dados)

                # 3. Validar se o número de inclinações bate com o número de seções transversais - 1
                # Se o usuário ainda não definiu as seções, o programa assume o valor do Excel
                if hasattr(self, 'colunas'):
                    if n_inclinações != (self.colunas - 1):
                        msg = f"Aviso: O Excel tem {n_inclinações} valores, mas o projeto espera {self.colunas - 1}.\nO projeto será ajustado."
                        QMessageBox.warning(None, "Ajuste de Projeto", msg)
                
                # Atualiza o campo de seções transversais para coincidir (n_inclinações + 1)
                self.secao_transversal.setText(str(n_inclinações + 1))
                
                # 4. Re-gerar campos para garantir que a table_2 exista com o tamanho correto
                self.gerar_campos()

                # 5. Preencher a table_2 (Inclinações)
                for j in range(n_inclinações):
                    valor = dados[j]
                    valor_str = str(valor) if pd.notnull(valor) else "0"
                    self.table_2.setItem(0, j, QTableWidgetItem(valor_str))

                QMessageBox.information(None, "Sucesso", "Inclinações importadas com sucesso!")

            except Exception as e:
                QMessageBox.critical(None, "Erro", f"Falha ao ler o arquivo de inclinações: {str(e)}")
        pass
    def plataforma(self):
        # 1. Obter matriz de cotas naturais
        self.mat_cotas = np.zeros((self.linhas, self.colunas))
        for i in range(self.linhas):
            for j in range(self.colunas):
                item = self.table.item(i, j)
                if item and item.text():
                    try:
                        self.mat_cotas[i, j] = float(item.text())
                    except ValueError:
                        QMessageBox.warning(None, "Error",f"Erro: O valor '{item.text()}' não é um número válido. Verifique os campos." )
                        return

        dx = float(self.dimensao_X.text())
        dy = float(self.dimensao_Y.text())
        
        # 2. Calcular o Volume do Terreno Natural (V_nat)
        # Aplicando os pesos: dy/2 nas bordas (i=0 e i=n) e dy no meio
        pesos_y = np.full(self.linhas, dy)
        pesos_y[0] = dy / 2
        pesos_y[-1] = dy / 2
        
        # Volume de cada ponto = Cota * Área de influência (dx * peso_y)
        # Nota: para as colunas das extremidades (j), o dx também deveria ser /2 se 
        # considerarmos a área total da malha.
        pesos_x = np.full(self.colunas, dx)
        pesos_x[0] = dx / 2
        pesos_x[-1] = dx / 2
        
        area_influencia = np.outer(pesos_y, pesos_x)
        v_natural = np.sum(self.mat_cotas * area_influencia)
        area_total = np.sum(area_influencia)

        # 3. Calcular a "Forma" da plataforma assimétrica (Delta H)
        # Geramos a plataforma com cota base = 0 para ver o volume relativo das inclinações
        val_inclinacao = np.zeros(self.colunas - 1)
        for j in range(self.colunas - 1):
            item = self.table_2.item(0, j)
            val_inclinacao[j] = float(item.text()) if item else 0

        # Lógica de deslocamento (sua lógica de plataforma centralizada)
        delta_h = np.zeros(self.colunas)
        meio = self.colunas // 2
        
        if self.colunas % 2 == 0:
            delta_h[meio - 1] = - (val_inclinacao[meio - 1] / 100.0) * dx * 0.5
            delta_h[meio] = (val_inclinacao[meio - 1] / 100.0) * dx * 0.5
            for j in range(meio - 2, -1, -1):
                delta_h[j] = delta_h[j + 1] - (val_inclinacao[j] / 100.0) * dx
            for j in range(meio + 1, self.colunas):
                delta_h[j] = delta_h[j - 1] + (val_inclinacao[j - 1] / 100.0) * dx
        else:
            delta_h[meio] = 0 # Cota base 0 no eixo
            for j in range(meio - 1, -1, -1):
                delta_h[j] = delta_h[j + 1] - (val_inclinacao[j] / 100.0) * dx
            for j in range(meio + 1, self.colunas):
                delta_h[j] = delta_h[j - 1] + (val_inclinacao[j - 1] / 100.0) * dx

        # Volume da "forma" da plataforma (V_forma)
        v_forma = np.sum(delta_h * np.sum(area_influencia, axis=0))

        # 4. A Cota de Equilíbrio (x)
        # V_nat = (x * Area_total) + V_forma  => x = (V_nat - V_forma) / Area_total
        cota_equilibrio = (v_natural - v_forma) / area_total

        # Atualizar Interface
        self.label_calculada.setText(f"{cota_equilibrio:.2f}")
        self.entry_adotada.setText(f"{cota_equilibrio:.6f}")

       
    
    def calcular_volumes(self):
        val_inclinacao = np.zeros(self.colunas - 1)
        for j in range(self.colunas - 1):
            item = self.table_2.item(0,j)
            if item and item.text():
                try:
                    val_inclinacao[j] = float(item.text())
                except ValueError:
                    QMessageBox.warning(None, "Error",f"Erro: O valor '{item.text()}' não é um número válido. Verifique os campos." )
                    return
        #self.plataforma()
        try:
            self.cota_adotada = float(self.entry_adotada.text())
        except ValueError:
            QMessageBox.warning(None, "Erro", "Digite um valor válido para a cota adotada.")
            return
        
        try:
            dx = float(self.dimensao_X.text())
            dy = float(self.dimensao_Y.text())
        except ValueError:
            QMessageBox.warning(None, 'Error', 'Digite dimensões válidas.')
            return

        # --- Gera a matriz cotas_plataforma_mista centralizada ---
        self.cotas_plataforma_mista = np.zeros((self.linhas, self.colunas))

        # Caso especial: só 1 coluna (nenhuma inclinação entre colunas)
        if self.colunas == 1:
            self.cotas_plataforma_mista[:] = self.cota_adotada
            return

        meio = self.colunas // 2

        cota_base = self.cota_adotada

        # Criamos uma única linha de base para os cálculos horizontais 
        # (já que a lógica parece se repetir para todas as linhas 'i')
        linha_base = np.zeros(self.colunas)

        if self.colunas % 2 == 0:
            # par: eixo entre meio-1 e meio
            linha_base[meio - 1] = cota_base - (val_inclinacao[meio - 1] / 100.0) * dx * 0.5
            linha_base[meio] = cota_base + (val_inclinacao[meio - 1] / 100.0) * dx * 0.5

            # expandir para a esquerda
            for j in range(meio - 2, -1, -1):
                linha_base[j] = linha_base[j + 1] - (val_inclinacao[j] / 100.0) * dx

            # expandir para a direita
            for j in range(meio + 1, self.colunas):
                linha_base[j] = linha_base[j - 1] + (val_inclinacao[j - 1] / 100.0) * dx

        else:
            # ímpar: eixo exatamente no meio
            linha_base[meio] = cota_base

            # expandir para a esquerda
            for j in range(meio - 1, -1, -1):
                linha_base[j] = linha_base[j + 1] - (val_inclinacao[j] / 100.0) * dx

            # expandir para a direita
            for j in range(meio + 1, self.colunas):
                linha_base[j] = linha_base[j - 1] + (val_inclinacao[j - 1] / 100.0) * dx

        # Atribuímos a 'linha_base' calculada para TODAS as linhas da matriz de uma vez
        self.cotas_plataforma_mista[:, :] = linha_base

        # 2. Calcular a diferença de alturas (H) para todos os pontos de uma vez
        # h > 0 significa Corte, h < 0 significa Aterro
        H = self.mat_cotas - self.cotas_plataforma_mista

        # 3. Preparar os deslocamentos para pegar (j) e (j+1) de forma vetorizada
        h1 = H[:, :-1]  # Todas as colunas exceto a última
        h2 = H[:, 1:]   # Todas as colunas exceto a primeira

        # 4. Criar o vetor de fatores (dy para o meio, dy/2 para as bordas)
        fator = np.full(self.linhas, dy)
        fator[0] = dy / 2
        fator[-1] = dy / 2
        # Ajustamos o fator para o formato da matriz (coluna vertical) para multiplicar corretamente
        fator = fator[:, np.newaxis] 

        # 5. Lógica de Cálculo Vetorizada
        vol_corte_matriz = np.zeros_like(h1)
        vol_aterro_matriz = np.zeros_like(h1)

        # Criamos uma matriz de fatores com o mesmo formato de h1 para evitar erros de dimensão
        # Isso repete o fator de cada linha para todas as colunas daquela linha
        fator_matriz = np.tile(fator, (1, h1.shape[1]))

        # --- Caso A: Todo em Corte (h1 >= 0 e h2 >= 0) ---
        mask_corte = (h1 >= 0) & (h2 >= 0)
        vol_corte_matriz[mask_corte] = ((h1[mask_corte] + h2[mask_corte]) / 2) * dx * fator_matriz[mask_corte]

        # --- Caso B: Todo em Aterro (h1 <= 0 e h2 <= 0) ---
        mask_aterro = (h1 <= 0) & (h2 <= 0)
        vol_aterro_matriz[mask_aterro] = ((np.abs(h1[mask_aterro]) + np.abs(h2[mask_aterro])) / 2) * dx * fator_matriz[mask_aterro]

        # --- Caso C: Interseção (Misto) ---
        mask_misto = ~mask_corte & ~mask_aterro
        if np.any(mask_misto):
            mh1 = h1[mask_misto]
            mh2 = h2[mask_misto]
            m_fator = fator_matriz[mask_misto]
            
            x_intersec = dx * (np.abs(mh1) / (np.abs(mh1) + np.abs(mh2)))
            
            # Usando np.where para decidir os volumes baseados no sinal de h1
            vol_corte_matriz[mask_misto] = np.where(mh1 > 0, 
                                                    (mh1 * x_intersec) / 2 * m_fator, 
                                                    (mh2 * (dx - x_intersec)) / 2 * m_fator)
            
            vol_aterro_matriz[mask_misto] = np.where(mh1 > 0, 
                                                     (np.abs(mh2) * (dx - x_intersec)) / 2 * m_fator, 
                                                     (np.abs(mh1) * x_intersec) / 2 * m_fator)

        # 6. Soma dos volumes por seção (linha)
        self.volumes_de_corte_secoes = np.sum(vol_corte_matriz, axis=1)
        self.volumes_de_aterro_secoes = np.sum(vol_aterro_matriz, axis=1)

       
        graficos(dx=dx, dy=dy, colunas= self.colunas, cotas_plataforma_mista= self.cotas_plataforma_mista,mat_cotas=self.mat_cotas, cota_adotada=self.cota_adotada)

        QMessageBox.information(None,'Sucesso', 'Operação concluida.\n' \
        ' verificar RESUMO DE VOLUMES.')

    def abrir_janela_resumo_volumes(self):
        # Primeiro, verificamos se o atributo existe e se tem valor
        if not hasattr(self, 'volumes_de_corte_secoes') or self.volumes_de_corte_secoes is None:
            # Se não existir, mostramos o aviso
            QMessageBox.warning(None, "Aviso", "ainda não é possível prosseguir!")
            return # Encerra a função aqui para não dar erro na linha de baixo
        #if self.segunda_janela is None:
        self.segunda_janela = SegundaJanela(linhas= self.linhas, volume_aterro_secoes=self.volumes_de_aterro_secoes, volume_corte_secoes=self.volumes_de_corte_secoes)
        self.segunda_janela.show()

    def abrir_janela_empolamento(self):
        # Primeiro, verificamos se o atributo existe e se tem valor
        if not hasattr(self, 'volumes_de_corte_secoes') or self.volumes_de_corte_secoes is None:
            # Se não existir, mostramos o aviso
            QMessageBox.warning(None, "Aviso", "Por favor, calcule o corte antes de prosseguir!")
            return # Encerra a função aqui para não dar erro na linha de baixo
        self.janela_empolamento = JanelaEmpolamento(volume_corte_secoes=self.volumes_de_corte_secoes)
        self.janela_empolamento.show()