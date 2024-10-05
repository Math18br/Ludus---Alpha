from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSettings, Qt
from PyQt6.QtGui import QIcon


from matricula_screen import *
from frequencia_screen import *
from relatorio_frequencia import *
from editar_matricula1 import *

class Ui_MainWindow(object):
    def __init__(self):
        self.username = ""

    def setupUi(self, MainWindow, username=""):
        settings = QSettings()
        username = settings.value("username", "Usuário Não Encontrado")
        self.username = username
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setMinimumSize(640, 480)
        MainWindow.setMaximumSize(640, 480)
        MainWindow.setWindowFlags(MainWindow.windowFlags() & ~Qt.WindowType.WindowMaximizeButtonHint)
        MainWindow.setStyleSheet("background-color: rgb(243, 230, 213);")
        MainWindow.setWindowTitle(f"Bem-vindo ao LUDUS - Usuário: {username}")
        MainWindow.setWindowIcon(QIcon('imagens\\5.png'))
        MainWindow.setStyleSheet("background-color: rgb(243, 230, 213);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(108, 50, 423, 381))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")

        self.aluno_button = QtWidgets.QPushButton(parent=self.frame, clicked= lambda: self.abrir_tela_alunos())
        self.aluno_button.setGeometry(QtCore.QRect(210, 290, 196, 75))
        self.aluno_button.setMinimumSize(QtCore.QSize(196, 75))
        self.aluno_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.aluno_button.setStyleSheet("background-color: rgb(229, 149, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font:bold 14px \"Inter Black\" ;\n"
"min-width: 180px;\n"
"padding: 6px;\n"
"color: rgb(22, 22, 29)\n"
"")
        self.aluno_button.setObjectName("aluno_button")

        self.bemvindo = QtWidgets.QLabel(parent=self.frame)
        self.bemvindo.setGeometry(QtCore.QRect(10, 120, 400, 80))
        font = QtGui.QFont()
        font.setFamily("Trend Slab Four")
        font.setPointSize(15)
        self.bemvindo.setFont(font)
        self.bemvindo.setStyleSheet("color: rgb(130, 3, 0);")
        self.bemvindo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.bemvindo.setObjectName("bemvindo")
        self.bemvindo.setText(f"BEM VINDO PROFESSOR(A): {self.username}")

        self.ficha_button = QtWidgets.QPushButton(parent=self.frame, clicked= lambda: self.abrir_tela_relatorio_frequencia())
        self.ficha_button.setGeometry(QtCore.QRect(9, 290, 196, 75))
        self.ficha_button.setMinimumSize(QtCore.QSize(196, 75))
        self.ficha_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ficha_button.setStyleSheet("background-color: rgb(44, 46, 89);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font:bold 14px \"Inter Black\" ;\n"
"min-width: 180px;\n"
"padding: 6px;\n"
"color: rgb(243, 230, 213);\n"
"")
        self.ficha_button.setObjectName("ficha_button")
        self.matricula_button = QtWidgets.QPushButton(parent=self.frame, clicked = lambda: self.abrir_tela_cadastro())
        self.matricula_button.setGeometry(QtCore.QRect(210, 210, 196, 75))
        self.matricula_button.setMinimumSize(QtCore.QSize(196, 75))
        self.matricula_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.matricula_button.setStyleSheet("background-color: rgb(45, 84, 60);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font:bold 14px \"Inter Black\" ;\n"
"min-width: 180px;\n"
"padding: 6px;\n"
"color: rgb(243, 230, 213);")
        self.matricula_button.setCheckable(False)
        self.matricula_button.setObjectName("matricula_button")

        self.LUDUS_logo = QtWidgets.QLabel(parent=self.frame)
        self.LUDUS_logo.setGeometry(QtCore.QRect(9, -8, 405, 120))
        font = QtGui.QFont()
        font.setFamily("Trend Slab Four")
        font.setPointSize(48)
        self.LUDUS_logo.setFont(font)
        self.LUDUS_logo.setStyleSheet("color: rgb(130, 3, 0);")
        self.LUDUS_logo.setObjectName("LUDUS_logo")
        self.frequencia_button = QtWidgets.QPushButton(parent=self.frame, clicked = lambda: self.abrir_tela_frequencia())
        self.frequencia_button.setGeometry(QtCore.QRect(9, 210, 196, 75))
        self.frequencia_button.setMinimumSize(QtCore.QSize(196, 75))
        self.frequencia_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.frequencia_button.setStyleSheet("background-color: rgb(131, 3, 2);;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font:bold 14px \"Inter Black\" ;\n"
"min-width: 180px;\n"
"padding: 6px;\n"
"color: rgb(243, 230, 213);\n"
"")
        self.frequencia_button.setObjectName("frequencia_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.logOut_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.logOut_button.setGeometry(QtCore.QRect(10, 10, 100, 50))  # Tamanho reduzido
        self.logOut_button.setStyleSheet("background-color: rgb(131, 3, 2);\n"
                                         "border-style: outset;\n"
                                         "border-width: 2px;\n"
                                         "border-radius: 10px;\n"
                                         "border-color: black;\n"
                                         "font:bold 14px \"Inter Black\" ;\n"
                                         "color: rgb(243, 230, 213);\n")
        self.logOut_button.setText("Sair")
        self.logOut_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.logOut_button.setObjectName("logOut_button")
        self.logOut_button.clicked.connect(self.logout)

        self.register_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.register_button.setGeometry(QtCore.QRect(120, 10, 100, 50))  # Logo abaixo do botão de Sair
        self.register_button.setStyleSheet("background-color: rgb(45, 84, 60);\n"
                                           "border-style: outset;\n"
                                           "border-width: 2px;\n"
                                           "border-radius: 10px;\n"
                                           "border-color: black;\n"
                                           "font:bold 14px \"Inter Black\" ;\n"
                                           "color: rgb(243, 230, 213);\n")
        self.register_button.setText("Registrar")
        self.register_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.register_button.setObjectName("register_button")
        self.register_button.clicked.connect(self.abrir_tela_registro)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        #MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.aluno_button.setToolTip(_translate("MainWindow", "Consulta, alteração e remoção de matriculas existentes"))
        self.aluno_button.setText(_translate("MainWindow", "Alunos"))
        self.bemvindo.setText(f"BEM VINDO PROFESSOR(A):\n{self.username}")
        self.ficha_button.setToolTip(_translate("MainWindow", "Perfis individuais de alunos para exportação"))
        self.ficha_button.setText(_translate("MainWindow", "Fichas"))
        self.matricula_button.setToolTip(_translate("MainWindow", "Cadastro de novos alunos nas turmas"))
        self.matricula_button.setText(_translate("MainWindow", "Matricula"))
        self.LUDUS_logo.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt;\">LUDUS</span></p></body></html>"))
        self.frequencia_button.setToolTip(_translate("MainWindow", "Registros de frequências, justificativas e observações"))
        self.frequencia_button.setText(_translate("MainWindow", "Frequência"))

    def abrir_tela_cadastro(self):
        self.tela_cadastro = QtWidgets.QMainWindow()
        self.ui = UI_MatriculaWindow()           
        self.ui.setupUi(self.tela_cadastro)           
        self.tela_cadastro.show()                     
        QtWidgets.QApplication.instance().activeWindow().close()
        
    def abrir_tela_frequencia(self):
        self.tela_frequencia = QtWidgets.QMainWindow()
        self.ui = UI_FrequenciaWindow()           
        self.ui.setupUi(self.tela_frequencia)           
        self.tela_frequencia.show()                     
        QtWidgets.QApplication.instance().activeWindow().close()

    def abrir_tela_relatorio_frequencia(self):
        self.tela_relatorio = QtWidgets.QMainWindow()
        self.ui = Ui_RelatorioWindow()           
        self.ui.setupUi(self.tela_relatorio)           
        self.tela_relatorio.show()                     
        QtWidgets.QApplication.instance().activeWindow().close()

    def abrir_tela_alunos(self):
        self.tela_alunos = QtWidgets.QMainWindow()
        self.ui = Ui_Edit_1_Window()
        self.ui.setupUi(self.tela_alunos)
        self.tela_alunos.show()
        QtWidgets.QApplication.instance().activeWindow().close()

    def logout(self):
        from main import Ui_LoginScreen
        self.tela_login = QtWidgets.QMainWindow()
        self.ui = Ui_LoginScreen()
        self.ui.setupUi(self.tela_login)
        self.tela_login.show()
        QtWidgets.QApplication.instance().activeWindow().close()

    def abrir_tela_registro(self):
        from register_screen import Ui_RegisterUserWindow
        self.tela_registro = QtWidgets.QMainWindow()
        self.ui = Ui_RegisterUserWindow()
        self.ui.setupUi(self.tela_registro)
        self.tela_registro.show()