import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLineEdit, QLabel

class MainJanela(QMainWindow):
    def __init__(self):
        super().__init__()

 
        self.setWindowTitle("Janela Principal")
        self.setGeometry(100, 100, 400, 200)


        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)


        self.result_label = QLabel("Mensagem e Nome aparecerão aqui")
        layout.addWidget(self.result_label)


        self.open_input_button = QPushButton("Abrir Janela de Entrada")
        layout.addWidget(self.open_input_button)

        self.open_input_button.clicked.connect(self.abrir_janela_entrada)


        self.janela_entrada = None

    def abrir_janela_entrada(self):
        if not self.janela_entrada:
            self.janela_entrada = JanelaEntrada(self)
        self.janela_entrada.show()

    def exibir_mensagem(self, mensagem, nome):

        self.result_label.setText(f"Nome: {nome}\nMensagem: {mensagem}")

class JanelaEntrada(QWidget):
    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window


        self.setWindowTitle("Janela de Entrada")
        self.setGeometry(200, 200, 300, 150)

a
        layout = QVBoxLayout(self)

        self.nome_input = QLineEdit(self)
        self.nome_input.setPlaceholderText("Digite seu nome")
        layout.addWidget(self.nome_input)

        self.mensagem_input = QLineEdit(self)
        self.mensagem_input.setPlaceholderText("Digite sua mensagem")
        layout.addWidget(self.mensagem_input)

        enviar_button = QPushButton("Enviar", self)
        layout.addWidget(enviar_button)


        enviar_button.clicked.connect(self.enviar_mensagem)

    def enviar_mensagem(self):
        
        nome = self.nome_input.text()
        mensagem = self.mensagem_input.text()

        
        self.main_window.exibir_mensagem(mensagem, nome)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainJanela()
    main_window.show()
    sys.exit(app.exec_())
