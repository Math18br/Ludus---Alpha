from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import Qt
from database import insert_cadastro_sistema, verifica_login

class Ui_RegisterUserWindow():
    def setupUi(self, RegisterUserWindow):
        RegisterUserWindow.setObjectName("RegisterUserWindow")
        RegisterUserWindow.resize(467, 112)
        RegisterUserWindow.setMinimumSize(467, 112)
        RegisterUserWindow.setMaximumSize(467, 112)
        RegisterUserWindow.setWindowFlags(RegisterUserWindow.windowFlags() & ~Qt.WindowType.WindowMaximizeButtonHint)
        self.centralwidget = QtWidgets.QWidget(parent=RegisterUserWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nome_prof = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.nome_prof.setGeometry(QtCore.QRect(10, 10, 281, 17))
        self.nome_prof.setText("")
        self.nome_prof.setObjectName("nome_prof")
        
        self.username = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.username.setGeometry(QtCore.QRect(10, 30, 281, 17))
        self.username.setText("")
        self.username.setObjectName("username")
        
        self.senha = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.senha.setGeometry(QtCore.QRect(10, 50, 281, 17))
        self.senha.setText("")  
        self.senha.setObjectName("senha")
        self.senha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        
        self.confirmar_button = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda: self.cadastrar_sistema(RegisterUserWindow))
        self.confirmar_button.setGeometry(QtCore.QRect(330, 10, 75, 23))
        self.confirmar_button.setObjectName("confirmar_button")
        
        self.cancelar_button = QtWidgets.QPushButton(parent=self.centralwidget,clicked = lambda: RegisterUserWindow.close())
        self.cancelar_button.setGeometry(QtCore.QRect(330, 40, 75, 23))
        self.cancelar_button.setObjectName("cancelar_button")
        RegisterUserWindow.setCentralWidget(self.centralwidget)

        
        self.retranslateUi(RegisterUserWindow)
        QtCore.QMetaObject.connectSlotsByName(RegisterUserWindow)

    def retranslateUi(self, RegisterUserWindow):
        _translate = QtCore.QCoreApplication.translate
        RegisterUserWindow.setWindowTitle(_translate("RegisterUserWindow", "MainWindow"))
        self.nome_prof.setPlaceholderText(_translate("RegisterUserWindow", "Nome do Professor Responsavel"))
        self.username.setPlaceholderText(_translate("RegisterUserWindow", "Username"))
        self.senha.setPlaceholderText(_translate("RegisterUserWindow", "Senha"))
        self.confirmar_button.setText(_translate("RegisterUserWindow", "Confirmar"))
        self.cancelar_button.setText(_translate("RegisterUserWindow", "Voltar"))

    def cadastrar_sistema(self, RegisterUserWindow):
        login = self.username.text()
        senha = self.senha.text()
        nome_professor = self.nome_prof.text()

        if verifica_login(login):
            self.exibir_mensagem_erro()
        else:
            insert_cadastro_sistema(login, nome_professor, senha)
            self.exibir_mensagem_sucesso()
            RegisterUserWindow.close()
            

    def exibir_mensagem_sucesso(self):
        mensagem = QMessageBox()
        mensagem.setIcon(QMessageBox.Icon.Information)
        mensagem.setText("Cadastro realizado com sucesso!")
        mensagem.setWindowTitle("Confirmação de Cadastro")
        mensagem.setStandardButtons(QMessageBox.StandardButton.Ok)
        mensagem.exec()
    
    def exibir_mensagem_erro(self):
        mensagem = QMessageBox()
        mensagem.setIcon(QMessageBox.Icon.Information)
        mensagem.setText("Cadastro não foi realizado, usuário já existe! Tente novamente")
        mensagem.setWindowTitle("Confirmação de Cadastro ERRO")
        mensagem.setStandardButtons(QMessageBox.StandardButton.Ok)
        mensagem.exec()

   
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegisterUserWindow = QtWidgets.QMainWindow()
    ui = Ui_RegisterUserWindow()
    ui.setupUi(RegisterUserWindow)
    RegisterUserWindow.show()
    sys.exit(app.exec())
