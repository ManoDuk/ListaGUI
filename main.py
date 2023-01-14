from PyQt6.QtWidgets import QWidget,QApplication,QMainWindow, QListWidget,QVBoxLayout,QLineEdit,QPushButton
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(400,500) # Define o Tamanho FIXO da Janela
        self.setWindowTitle('Sistema de Lista') #Define o Titulo da Janela

        VBOX = QVBoxLayout() 
        self.setLayout(VBOX)

        self.list_widget = QListWidget() # Cria o Widget QListWidget
        self.line = QLineEdit() # Cria a Caixa de texto

        self.btn_add = QPushButton('Adicionar Item') # Cria o Botão "Adicionar"
        self.btn_rem = QPushButton('Remover Item') # Cria o Botão "Remover"

    #Função para clicar nos botões

        self.btn_add.clicked.connect(self.adicionar)
        self.btn_rem.clicked.connect(self.remover)
        self.line.editingFinished.connect(self.adicionar) # Ao Apertar ENTER, o item será adicionado
 
    #Adiciona os Widgets A Janela

        VBOX.addWidget(self.list_widget)
        VBOX.addWidget(self.line)
        VBOX.addWidget(self.btn_add)
        VBOX.addWidget(self.btn_rem)

    #Funções para os Botões

    def adicionar(self):

        if self.line.text() != '':
            self.item = self.line.text() # Recupera o texto digitado na Caixa de texto
            self.list_widget.insertItem(0,self.item) # Adiciona o Item a Lista
            self.line.setText('') # Após Adicionado, Define a caixa de texto como "Vazia"
        else:
            print('Preencha o Campo !')

    def remover(self):
        self.item = self.list_widget.currentItem() #Retorna o Item clicado
        self.line_row = self.list_widget.currentRow() #Retorna a linha em que o Item está
        self.list_widget.takeItem(self.line_row) # Remove O Item


app = QApplication(sys.argv)
MainWindow = Window()
MainWindow.show()
app.exec()