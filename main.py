from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QCoreApplication, QSettings, Qt
from PyQt6.QtWidgets import QMessageBox
import sys
import os

from database import realiza_login, busca_nome_usuario
from home_screen import Ui_MainWindow

QCoreApplication.setOrganizationName("LUDUS")
QCoreApplication.setApplicationName("LUDUS-App")
settings = QSettings()

class Ui_LoginScreen(object):
    def setupUi(self, LoginScreen):
        LoginScreen.setObjectName("LoginScreen")
        LoginScreen.resize(640, 480)
        LoginScreen.setMinimumSize(640, 480)
        LoginScreen.setMaximumSize(640, 480)
        LoginScreen.setWindowFlags(LoginScreen.windowFlags() & ~Qt.WindowType.WindowMaximizeButtonHint)
        LoginScreen.setStyleSheet("background-color: rgb(243, 230, 213);")
        
        self.centralwidget = QtWidgets.QWidget(parent=LoginScreen)
        self.centralwidget.setObjectName("centralwidget")


        def resource_path(relative_path):
            """ Obtém o caminho absoluto para o arquivo (funciona tanto para .exe quanto para o script). """
            base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
            return os.path.join(base_path, relative_path)

        LoginScreen.setWindowIcon(QIcon(resource_path('imagens/7.png')))

        # Botão de Login
        self.login_button = QtWidgets.QPushButton(parent=self.centralwidget, clicked=self.logar)
        self.login_button.setGeometry(QtCore.QRect(270, 320, 106, 31))
        self.login_button.setStyleSheet("""
            QPushButton {
                background-color: rgb(131, 3, 2);
                border-width: 2px;
                border-radius: 10px;
                font: bold 14px "Inter Black";
                min-width: 90px;
                padding: 6px;
                color: rgb(243, 230, 213);                                  
            }
            QPushButton:hover {
                background-color: rgb(151, 23, 22);
            }
        """)
        self.login_button.setObjectName("login_button")
        self.login_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

        # Logo do LUDUS
        self.ludus_logo = QtWidgets.QLabel(parent=self.centralwidget)
        self.ludus_logo.setGeometry(QtCore.QRect(120, 110, 405, 120))
        font = QtGui.QFont()
        font.setFamily("Trend Slab Four")
        font.setPointSize(48)
        self.ludus_logo.setFont(font)
        self.ludus_logo.setStyleSheet("color: rgb(130, 3, 0);")
        self.ludus_logo.setObjectName("ludus_logo")

        # Campo de senha
        self.senha_input = QtWidgets.QLineEdit(self.centralwidget)
        self.senha_input.setGeometry(QtCore.QRect(170, 282, 281, 31))
        self.senha_input.setStyleSheet("""
            background-color: rgb(131, 3, 2);
            border-width: 2px;
            border-radius: 10px;
            font: bold 14px "Inter Black";
            padding: 6px;
            color: rgb(243, 230, 213);
        """)
        self.senha_input.setObjectName("senha_input")
        self.senha_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        # Campo de username
        self.username_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.username_input.setGeometry(QtCore.QRect(170, 246, 281, 31))
        self.username_input.setStyleSheet("""
            background-color: rgb(243, 230, 213);
            border-width: 1px;
            border-radius: 10px;
            font: bold 14px "Inter Black";
            padding: 6px;
            color: rgb(131, 3, 2);
        """)
        self.username_input.setObjectName("username_input")

        LoginScreen.setCentralWidget(self.centralwidget)
        self.retranslateUi(LoginScreen)
        QtCore.QMetaObject.connectSlotsByName(LoginScreen)

    def retranslateUi(self, LoginScreen):
        _translate = QtCore.QCoreApplication.translate
        LoginScreen.setWindowTitle(_translate("LoginScreen", "LUDUS - Login"))
        self.login_button.setText(_translate("LoginScreen", "Login"))
        self.ludus_logo.setText(_translate("LoginScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt;\">LUDUS</span></p></body></html>"))
        self.senha_input.setPlaceholderText(_translate("LoginScreen", "Senha"))
        self.username_input.setPlaceholderText(_translate("LoginScreen", "Username"))

    def logar(self):
        username = self.username_input.text()
        password = self.senha_input.text()

        if realiza_login(username, password):
            self.show_success_message(username)
            user_name = busca_nome_usuario(username)
            settings.setValue("username", user_name)
            self.open_main_window(user_name)
        else:
            self.show_error_message()

    def show_success_message(self, username):
        mensagem = QMessageBox()
        mensagem.setIcon(QMessageBox.Icon.Information)
        mensagem.setText(f"Login realizado com sucesso! Bem-vindo ao LUDUS, {username}")
        mensagem.setWindowTitle("Confirmação de Login")
        mensagem.setStandardButtons(QMessageBox.StandardButton.Ok)
        mensagem.exec()

    def show_error_message(self):
        mensagem = QMessageBox()
        mensagem.setIcon(QMessageBox.Icon.Information)
        mensagem.setText("Login não realizado! Usuário ou senha incorretos. Tente novamente.")
        mensagem.setWindowTitle("Erro de Login")
        mensagem.setStandardButtons(QMessageBox.StandardButton.Ok)
        mensagem.exec()

    def open_main_window(self, user_name):
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window, username=user_name)
        self.main_window.show()
        QtWidgets.QApplication.instance().activeWindow().close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginScreen = QtWidgets.QMainWindow()
    ui = Ui_LoginScreen()
    ui.setupUi(LoginScreen)
    LoginScreen.show()
    sys.exit(app.exec())
