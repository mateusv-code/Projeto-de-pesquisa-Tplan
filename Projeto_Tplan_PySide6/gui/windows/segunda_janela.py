from qt_core import *

class SegundaJanela(QMainWindow):
    def __init__(self, linhas=None, volume_aterro_secoes = [], volume_corte_secoes = []):
        super().__init__()
        self.setWindowTitle('Resumo de Volumes')
        self.resize(500,200)
        icon_path = "gui/img/IMG_TPLAN.png"
        self.setWindowIcon(QIcon(icon_path))

        #Criando a tabela
        self.table = QTableWidget()
        self.table.setRowCount(linhas+1)     # Número de linhas
        self.table.setColumnCount(4)  # Número de colunas
        self.table.setHorizontalHeaderLabels(["Secões","(-) Aterro", "(+) Corte", "Soma"])

        for i in range(linhas):
            self.tabela_generica = QTableWidgetItem()
            self.table.setItem(i,1,self.tabela_generica)
            self.tabela_generica.setText(f'- {round(volume_aterro_secoes[i],4)} m³')

        for i in range(linhas):
            self.tabela_generica = QTableWidgetItem()
            self.table.setItem(i,2,self.tabela_generica)
            self.tabela_generica.setText(f' {round(volume_corte_secoes[i],4)} m³')

        for i in range(linhas):
            self.tabela_generica = QTableWidgetItem()
            self.table.setItem(i,0,self.tabela_generica)
            self.tabela_generica.setText(f' seção {i+1}')

        self.tabela_soma = QTableWidgetItem('soma =')
        self.table.setItem(linhas,0, self.tabela_soma)

        for i in range(linhas):
            self.tabela_generica = QTableWidgetItem()
            self.table.setItem(i,3,self.tabela_generica)
            self.tabela_generica.setText(f' {round(volume_corte_secoes[i] - volume_aterro_secoes[i],2)} m³')

        self.tabela_soma = QTableWidgetItem(f'{round(sum(volume_corte_secoes)-sum(volume_aterro_secoes),4)}')
        self.table.setItem(linhas,3, self.tabela_soma)




        # Inserindo dados na tabela
        # Create the QTableWidgetItem for the first cell

        # Set the text for volume_aterro if it's provided
        self.tabela_3_1 =  QTableWidgetItem()
        self.table.setItem(linhas, 1, self.tabela_3_1)
        self.tabela_3_1.setText(f'- {round(sum(volume_aterro_secoes),4)} m³') # Set text on the item

        # Now, set the item in the table
        

        self.table_2_2 = QTableWidgetItem()
        self.table.setItem(linhas, 2,self.table_2_2)
        self.table_2_2.setText(f'{round(sum(volume_corte_secoes),4)} m³')

        # Layout para exibir a tabela
        layout = QVBoxLayout()
        layout.addWidget(self.table)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    