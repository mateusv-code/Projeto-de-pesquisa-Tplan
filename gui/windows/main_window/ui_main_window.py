from qt_core import*
from gui.windows.segunda_janela import *

class ui_MainWindow(object):
    def setup_ui(self,parent):
        if not parent.objectName():
            parent.setObjectName('MainWindow')

            parent.resize(1455,705)
            parent.setMinimumSize(1455,705)
            self.central_frame = QFrame()
            parent.setCentralWidget(self.central_frame)

            self.lista_de_line_edits_matriz = [] # Crie a lista aqui

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
                QLineEdit {
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
        self.scroll_layout = QGridLayout(self.scroll_widget)

        self.scroll_area_cota = QScrollArea()
        self.scroll_area_cota.setWidget(self.scroll_widget)
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

        self.spacer_item = QSpacerItem(20,75, QSizePolicy.Minimum)
        self.right_panel_layout.addItem(self.spacer_item)

        self.spacer_item = QSpacerItem(20,75, QSizePolicy.Minimum, QSizePolicy.Expanding)
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
        self.label_calculada.setStyleSheet('background-color: white')
        self.cota_layout.addWidget(self.label_calculada, 0, 1)
        
        self.cota_layout.addWidget(QLabel("Adotada"), 1, 0)
        self.entry_adotada =  QLineEdit()
        self.entry_adotada.setAlignment(Qt.AlignCenter)
        self.entry_adotada.setStyleSheet('border:  0.5px solid gray, background-color: white')
        self.cota_layout.addWidget(self.entry_adotada, 1, 1)  
        self.right_panel_layout.addWidget(self.cota_group, alignment= Qt.AlignCenter)

        self.spacer_item = QSpacerItem(20,10, QSizePolicy.Minimum)
        self.right_panel_layout.addItem(self.spacer_item)

        self.frame_pos_inclinacao = QFrame()
        self.right_panel_layout.addWidget(self.frame_pos_inclinacao)

        self.layout_pos_inclinação = QGridLayout(self.frame_pos_inclinacao)


        # "INCLINAÇÕES DE PROJETO (%)" GroupBox
        self.inclinacoes_group = QGroupBox("INCLINAÇÕES DE PROJETO (%)")
        self.inclinacoes_group.setMaximumHeight(100)
        self.inclinacoes_group.setMinimumHeight(100)
        self.inclinacoes_group.setMinimumWidth(450)
        self.inclinacoes_group.setMaximumWidth(450)
        self.inclinacoes_layout = QGridLayout(self.inclinacoes_group)

        self.scroll_widget_2 = QWidget()
        self.scroll_layout_2 = QGridLayout(self.scroll_widget_2)


        self.scroll_area_inclinacao = QScrollArea()
        self.scroll_area_inclinacao.setWidget(self.scroll_widget_2)
        self.scroll_area_inclinacao.setWidgetResizable(True)
        self.scroll_area_inclinacao.setStyleSheet("border: 0.5px solid gray")
        
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
        while self.scroll_layout.count():
            item = self.scroll_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        while self.scroll_layout_2.count():
            item = self.scroll_layout_2.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        # Cria novos QLineEdits
        for i in range(self.linhas):
            linha_atual = [] # Cria uma nova lista para cada linha
            for j in range(self.colunas):
                global line_edit
                line_edit = QLineEdit()
                line_edit.setAlignment(Qt.AlignCenter)
                self.scroll_layout.addWidget(line_edit,i,j)
                #self.line_edit.setStyleSheet('border: 1px solid black')
                linha_atual.append(line_edit)

                
            self.lista_de_line_edits_matriz.append(linha_atual)

        self.list_inclinacao = []
        for j in range(self.colunas-1):
            self.line_edit_inclinacao = QLineEdit()
            self.scroll_layout_2.addWidget(self.line_edit_inclinacao,1,j)
            self.list_inclinacao.append(self.line_edit_inclinacao)



    def plataforma(self):
        # --- lê a matriz de cotas da interface ---
        global valores_matriz
        valores_matriz = []
        for i in range(len(self.lista_de_line_edits_matriz)):
            linha_valores = []
            for j in range(len(self.lista_de_line_edits_matriz[i])):
                texto_cota = self.lista_de_line_edits_matriz[i][j].text()
                try:
                    cota = float(texto_cota)
                    linha_valores.append(cota)
                except ValueError:
                    QMessageBox.warning(None, "Error",f"Erro: O valor '{texto_cota}' não é um número válido. Verifique os campos." )
                    print(f"Erro: O valor '{texto_cota}' não é um número válido. Verifique os campos.")
                    return
            valores_matriz.append(linha_valores)

        if not valores_matriz:
            print("A matriz de cotas está vazia. Gere os campos e insira os valores primeiro.")
            return

        # --- calcula a cota de plataforma plana (média ponderada) ---
        soma_cotas_x_pesos = 0.0
        soma_pesos = 0.0

        linhas = len(valores_matriz)
        colunas = len(valores_matriz[0])

        for i in range(linhas):
            for j in range(colunas):
                cota = valores_matriz[i][j]
                if (i == 0 and j == 0) or (i == 0 and j == colunas - 1) or \
                (i == linhas - 1 and j == 0) or (i == linhas - 1 and j == colunas - 1):
                    peso = 1
                elif i == 0 or i == linhas - 1 or j == 0 or j == colunas - 1:
                    peso = 2
                else:
                    peso = 4
                soma_cotas_x_pesos += cota * peso
                soma_pesos += peso

        if soma_pesos == 0:
            print("Erro: A soma dos pesos é zero. Não foi possível calcular a cota de plataforma.")
            return

        cota_plataforma = round(soma_cotas_x_pesos / soma_pesos, 9)
        self.label_calculada.setText(f'{cota_plataforma:.2f}')


        self.entry_adotada.setText(f'{cota_plataforma:.2f}')

       
    
    def calcular_volumes(self):
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

        global valores_matriz, cota_plataforma
        self.linhas = len(valores_matriz)
        self.colunas = len(valores_matriz[0])

        #colei aqui@@@@@@@@@@@@@@@@

        # --- monta a lista 'inclinacoes' a partir dos QLineEdit (list_inclinacao) ---
        #espera-se len(inclinacoes) == colunas - 1 (inclinações entre colunas)
        inclinacoes = []
        if hasattr(self, 'list_inclinacao') and self.list_inclinacao:
            for le in self.list_inclinacao:
                s = le.text().strip()
                if s == '':
                    inclinacoes.append(0.0)
                else:
                    try:
                        inclinacoes.append(float(s))
                    except ValueError:
                        QMessageBox.warning(None, "Error", f"Erro: valor de inclinação inválido '{s}'." )
                        print(f"Erro: valor de inclinação inválido '{s}'.")
                        return
        # completa com zeros caso falte (ou trunca se tiver a mais)
        needed = max(0, self.colunas - 1)
        if len(inclinacoes) < needed:
            inclinacoes += [0.0] * (needed - len(inclinacoes))
        elif len(inclinacoes) > needed:
            inclinacoes = inclinacoes[:needed]

        # --- Gera a matriz cotas_plataforma_mista centralizada (igual TPlan) ---
        self.cotas_plataforma_mista = []

        # Caso especial: só 1 coluna (nenhuma inclinação entre colunas)
        if self.colunas == 1:
            for _ in range(self.linhas):
                self.cotas_plataforma_mista.append([self.cota_adotada])
            print("Plataforma mista gerada (1 coluna).")
            return

        meio = self.colunas // 2

        for i in range(self.linhas):
            linha_plataforma = [0.0] * self.colunas
            cota_base = self.cota_adotada

            if self.colunas % 2 == 0:
                # par: eixo entre meio-1 e meio (conforme MATLAB)
                # usamos inclinacoes[meio-1] para definir a meia diferença inicial
                linha_plataforma[meio - 1] = cota_base - (inclinacoes[meio - 1] / 100.0) * dx * 0.5
                linha_plataforma[meio] = cota_base + (inclinacoes[meio - 1] / 100.0) * dx * 0.5

                # expandir para a esquerda
                for j in range(meio - 2, -1, -1):
                    # inclinacoes[j] existe porque j em [0..colunas-2]
                    linha_plataforma[j] = linha_plataforma[j + 1] - (inclinacoes[j] / 100.0) * dx

                # expandir para a direita
                for j in range(meio + 1, self.colunas):
                    linha_plataforma[j] = linha_plataforma[j - 1] + (inclinacoes[j - 1] / 100.0) * dx

            else:
                # ímpar: eixo exatamente no meio
                linha_plataforma[meio] = cota_base

                # expandir para a esquerda
                for j in range(meio - 1, -1, -1):
                    linha_plataforma[j] = linha_plataforma[j + 1] - (inclinacoes[j] / 100.0) * dx

                # expandir para a direita
                for j in range(meio + 1, self.colunas):
                    linha_plataforma[j] = linha_plataforma[j - 1] + (inclinacoes[j - 1] / 100.0) * dx

            self.cotas_plataforma_mista.append(linha_plataforma)

        # debug opcional
        print(f"Gerado cotas_plataforma_mista: linhas={self.linhas}, colunas={self.colunas}, len(inclinacoes)={len(inclinacoes)}")
        for r in self.cotas_plataforma_mista:
            print(r)


        #terminei aqui@@@@@@@@@@@@@@@@@

        self.volumes_de_corte_secoes = []
        self.volumes_de_aterro_secoes = []

        for i in range(self.linhas):
            volume_corte_secao = 0
            volume_aterro_secao = 0
            
            # Inicialize as listas para as sub-áreas de corte e aterro desta seção AQUI
            

            # Fator de multiplicação (bordas usam metade)
            if i == 0 or i == self.linhas - 1:
                fator = dy / 2
            else:
                fator = dy

            for j in range(self.colunas - 1):
                # garante que a matriz de plataforma mista existe e tem o mesmo tamanho
                if not hasattr(self, 'cotas_plataforma_mista'):
                    print("Plataforma mista não calculada. Rode a função 'plataforma()' antes de calcular volumes.")
                    return

                # pega a cota de plataforma pontual (cada vértice)
                plat_h1 = self.cotas_plataforma_mista[i][j]
                plat_h2 = self.cotas_plataforma_mista[i][j+1]

                h1 = valores_matriz[i][j] - plat_h1
                h2 = valores_matriz[i][j+1] - plat_h2



                volume_corte = 0
                volume_aterro = 0

                if h1 >= 0 and h2 >= 0:
                    # Todo em corte
                    volume_corte = ((h1 + h2) / 2) * dx * fator

                elif h1 <= 0 and h2 <= 0:
                    # Todo em aterro
                    volume_aterro = ((abs(h1) + abs(h2)) / 2) * dx * fator

                else:
                    # Houve interseção com a plataforma
                    x_intersec = dx * (abs(h1) / (abs(h1) + abs(h2)))

                    if h1 > 0:
                        # ponto inicial em corte
                        volume_corte = (h1 * x_intersec) / 2 * fator
                        volume_aterro = (abs(h2) * (dx - x_intersec)) / 2 * fator
                    else:
                        # ponto inicial em aterro
                        volume_aterro = (abs(h1) * x_intersec) / 2 * fator
                        volume_corte = (h2 * (dx - x_intersec)) / 2 * fator

                volume_corte_secao += volume_corte
                volume_aterro_secao += volume_aterro
            self.volumes_de_corte_secoes.append(volume_corte_secao)
            self.volumes_de_aterro_secoes.append(volume_aterro_secao)
        
        print(f'{self.volumes_de_corte_secoes}')
        print(f'{ self.volumes_de_aterro_secoes}')


    def abrir_janela_resumo_volumes(self):
        #if self.segunda_janela is None:
        self.segunda_janela = SegundaJanela(linhas= self.linhas, volume_aterro_secoes=self.volumes_de_aterro_secoes, volume_corte_secoes=self.volumes_de_corte_secoes)
        self.segunda_janela.show()
