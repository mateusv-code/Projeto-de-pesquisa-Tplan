from qt_core import*
from gui.windows.segunda_janela import *
import numpy as np
from gui.gráficos.graficos import *

class ui_MainWindow(object):
    def setup_ui(self,parent):
        if not parent.objectName():
            parent.setObjectName('MainWindow')

            parent.resize(1455,705)
            parent.setMinimumSize(1455,705)
            self.central_frame = QFrame()
            parent.setCentralWidget(self.central_frame)

            self.lista_de_line_edits_matriz = [] # Crie a lista aqui

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
        pixmap1 = QPixmap("gui/img/IMG_IFMA.png").scaledToWidth(150, Qt.SmoothTransformation)
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
        self.pixmap_tplan = QPixmap("gui/img/IMG_TPLAN.png").scaledToWidth(450, Qt.SmoothTransformation)
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
        self.calcular_button = QPushButton("IMPORTAR .XLSX")
        self.center_panel_layout.addWidget(self.plataforma_button, 7, 1, alignment=Qt.AlignCenter)
        self.center_panel_layout.addWidget(self.calcular_button, 6, 1, alignment=Qt.AlignRight)
    
    def widgets_panel_3(self):
        self.right_panel_layout = QVBoxLayout(self.right_panel)
        self.right_panel_layout.setContentsMargins(0,10,0,0)
        self.right_panel_layout.setSpacing(5)

        self.logo2_label = QLabel()
        self.pixmap2 = QPixmap("gui/img/IMG_ENG_CIV.png").scaledToWidth(170, Qt.SmoothTransformation)
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
        self.importar_button = QPushButton("IMPORTAR .XLSX")
        self.calcular_button = QPushButton("CALCULAR")
        self.calcular_button.clicked.connect(self.calcular_volumes)
        self.relatorio_button = QPushButton('RELATÓRIO')
        self.resumo_button = QPushButton('RESUMO DE VOLUMES')
        self.resumo_button.clicked.connect(self.abrir_janela_resumo_volumes)
        self.layout_pos_inclinação.addWidget(self.importar_button, 4, 2, alignment=Qt.AlignRight)
        self.layout_pos_inclinação.addWidget(self.calcular_button, 5, 2, alignment=Qt.AlignCenter)
        self.layout_pos_inclinação.addWidget(self.relatorio_button, 6, 2, alignment=Qt.AlignRight)
        self.layout_pos_inclinação.addWidget(self.resumo_button, 7,2, alignment=Qt.AlignRight)

        self.spacer_item = QSpacerItem(20,75, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.right_panel_layout.addItem(self.spacer_item)

        self.segunda_janela = None

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
    
    def gerar_campos(self):
        # Limpe a lista antes de gerar os novos campos
        self.lista_de_line_edits_matriz.clear()

        try:
            self.linhas = int(self.secao_longitudinal.text())
            self.colunas = int(self.secao_transversal.text())
        except ValueError:
            QMessageBox.warning(None,'Error', 'Digite apenas números nos campos de seções!')
            print("Digite apenas números nos campos de seções!")
            return
        """Cria os QLineEdits de acordo com o número de linhas e colunas"""
        # Limpa os campos antigos

        # Remove existing tables if they exist
        if self.table:
            self.scroll_layout.removeWidget(self.table)
            self.table.deleteLater()

        # Create new tables
        self.table = QTableWidget(self.linhas, self.colunas)
        self.scroll_layout.addWidget(self.table)
        #self.scroll_layout.insertWidget(3, self.table)

        # Fill tables with empty items to allow input
        for i in range(self.linhas):
            for j in range(self.colunas):
                self.table.setItem(i, j, QTableWidgetItem("0"))

        # Remove existing tables if they exist
        if self.table_2:
            self.scroll_layout_2.removeWidget(self.table_2)
            self.table_2.deleteLater()

        # Create new tables
        self.table_2 = QTableWidget(1, self.colunas - 1)
        self.scroll_layout_2.addWidget(self.table_2)
        #self.scroll_layout_2.insertWidget(3 , self.table_2)

        # Fill tables with empty items to allow input
        for j in range(self.colunas-1):
            self.table_2.setItem(0, j, QTableWidgetItem("0"))

    def plataforma(self):

        self.mat_cotas = np.zeros((self.linhas,self.colunas))
        for i in range(self.linhas):
            for j in range(self.colunas):
                item = self.table.item(i,j)
                if item and item.text():
                    try:
                        self.mat_cotas[i,j] = float(item.text())
                    except ValueError:
                        QMessageBox.warning(None, "Error",f"Erro: O valor '{item.text()}' não é um número válido. Verifique os campos." )
                        print(f"Erro: O valor '{item.text()}' não é um número válido. Verifique os campos.")
                        return
        print(self.mat_cotas)

        # --- calcula a cota de plataforma plana (média ponderada) ---
        soma_cotas_x_pesos = 0.0
        soma_pesos = 0.0

        for i in range(self.linhas):
            for j in range(self.colunas):
                cota = self.mat_cotas[i,j]
                if (i == 0 and j == 0) or (i == 0 and j == self.colunas - 1) or \
                (i == self.linhas - 1 and j == 0) or (i == self.linhas - 1 and j == self.colunas - 1):
                    peso = 1
                elif i == 0 or i == self.linhas - 1 or j == 0 or j == self.colunas - 1:
                    peso = 2
                else:
                    peso = 4
                soma_cotas_x_pesos += cota * peso
                soma_pesos += peso

        if soma_pesos == 0:
            print("Erro: A soma dos pesos é zero. Não foi possível calcular a cota de plataforma.")
            return

        self.cota_plataforma = round(soma_cotas_x_pesos / soma_pesos,10)
        self.label_calculada.setText(f'{self.cota_plataforma:.2f}')
        print(self.cota_plataforma)

        self.entry_adotada.setText(f'{self.cota_plataforma}')

       
    
    def calcular_volumes(self):

        val_inclinacao = np.zeros(self.colunas - 1)
        for j in range(self.colunas - 1):
            item = self.table_2.item(0,j)
            if item and item.text():
                try:
                    val_inclinacao[j] = float(item.text())
                except ValueError:
                    QMessageBox.warning(None, "Error",f"Erro: O valor '{item.text()}' não é um número válido. Verifique os campos." )
                    print(f"Erro: O valor '{item.text()}' não é um número válido. Verifique os campos.")
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
            print("Erro: Digite dimensões válidas.")
            return

        # --- Gera a matriz cotas_plataforma_mista centralizada (igual TPlan) ---
        self.cotas_plataforma_mista = np.zeros((self.linhas, self.colunas))

        # Caso especial: só 1 coluna (nenhuma inclinação entre colunas)
        if self.colunas == 1:
            self.cotas_plataforma_mista[:] = self.cota_adotada
            print("Plataforma mista gerada (1 coluna) como NumPy array.")
            # Removi o return para manter o fluxo, ajuste se necessário no seu métodoforma mista gerada (1 coluna).")
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

        # Aqui está o "pulo do gato" do NumPy: 
        # Atribuímos a 'linha_base' calculada para TODAS as linhas da matriz de uma vez
        self.cotas_plataforma_mista[:, :] = linha_base

        print("Matriz NumPy gerada com sucesso.", self.cotas_plataforma_mista)
        #comecou aqui
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

        print(f'Corte por seção: {self.volumes_de_corte_secoes}')
        print(f'Aterro por seção: {self.volumes_de_aterro_secoes}')

       
        graficos(dx=dx, colunas= self.colunas, cotas_plataforma_mista= self.cotas_plataforma_mista,mat_cotas=self.mat_cotas, cota_adotada=self.cota_adotada)

    


    def abrir_janela_resumo_volumes(self):
        #if self.segunda_janela is None:
        self.segunda_janela = SegundaJanela(linhas= self.linhas, volume_aterro_secoes=self.volumes_de_aterro_secoes, volume_corte_secoes=self.volumes_de_corte_secoes)
        self.segunda_janela.show()
