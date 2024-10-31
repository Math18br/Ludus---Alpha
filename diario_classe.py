from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from database import * 
import sys
import os

class Ui_DiarioWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(243, 230, 213);")

        def resource_path(relative_path):
            """ Obtém o caminho absoluto para o arquivo (funciona tanto para .exe quanto para o script). """
            base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
            return os.path.join(base_path, relative_path)

        MainWindow.setWindowIcon(QIcon(resource_path('imagens\\3.png')))

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: rgb(243, 230, 213);")

        # Título
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(250, 10, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Trend Slab Four")
        font.setPointSize(20)
        self.title_label.setFont(font)
        self.title_label.setText("Diário de Classe")
        self.title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title_label.setStyleSheet("color: rgb(44, 46, 89);")

        # Data
        self.date_selection = QtWidgets.QDateEdit(self.centralwidget)
        self.date_selection.setGeometry(QtCore.QRect(50, 100, 300, 40))
        self.date_selection.setCalendarPopup(True)
        self.date_selection.setDate(QtCore.QDate.currentDate())
        self.date_selection.setStyleSheet("""
    background-color: rgb(243, 230, 213);  /* Cor de fundo igual ao botão */
    border-style: outset;
    border-width: 2px;
    border-radius: 10px;
    border-color: black;
    font: bold 20px "Inter Black";  /* Tamanho e estilo da fonte */
    min-width: 2em;
    color: rgb(44, 46, 89);  /* Cor do texto igual ao botão */
""")

        # Justificativas
        self.text_area = QtWidgets.QTextEdit(self.centralwidget)
        self.text_area.setGeometry(QtCore.QRect(50, 200, 700, 300))
        self.text_area.setReadOnly(True)
        self.text_area.setStyleSheet("""
    background-color: rgb(255, 255, 255); 
    border: 2px solid black; 
    font: bold 18px 'Inter Medium';  /* Fonte semelhante à do QTableWidget */
    color: rgb(44, 46, 89);  /* Cor do texto */
""")

        # Atualizar
        self.atualizar_button = QtWidgets.QPushButton(self.centralwidget, clicked=self.receber_diario)
        self.atualizar_button.setGeometry(QtCore.QRect(620, 100, 130, 40))
        self.atualizar_button.setText("Atualizar")
        self.atualizar_button.setStyleSheet("background-color: rgb(44, 46, 89);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font:bold 20px \"Inter Black\" ;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"color: rgb(243, 230, 213);")

        # Retornar
        self.retornar_button = QtWidgets.QPushButton(self.centralwidget)
        self.retornar_button.setGeometry(QtCore.QRect(50, 520, 130, 40))
        self.retornar_button.setText("Retornar")
        self.retornar_button.clicked.connect(MainWindow.close)
        self.retornar_button.setStyleSheet("background-color:rgb(44, 46, 89);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font:bold 20px \"Inter Black\" ;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"color: rgb(243, 230, 213);\n"
"")

        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowTitle("Diário de Classe")

    
    def receber_diario(self):
        data = self.date_selection.date().toString("yyyy-MM-dd")

        resultado = atualizar_diario_classe(data)
        print(resultado)
        self.text_area.setText(resultado)
