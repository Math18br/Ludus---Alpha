from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QRegularExpression, QDate, Qt
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QIcon, QRegularExpressionValidator
from database import *
import pickle, os
class Ui_Edit_2_Window(object):
    
    def __init__(self):
        self.importar_dados()

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 747)
        MainWindow.setMinimumSize(750, 747)
        MainWindow.setWindowFlags(MainWindow.windowFlags() & ~Qt.WindowType.WindowMaximizeButtonHint)
        MainWindow.setWindowIcon(QIcon('imagens\\2.png'))
        MainWindow.setMaximumSize(QtCore.QSize(750, 747))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(243, 230, 213);")
        MainWindow.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 100, 721, 521))
        self.scrollArea.setStyleSheet("QScrollBar{ background-color: rgb(203, 132, 0);; \n"
        "color: rgb(243, 230, 213);\n"
        "} ")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 702, 1271))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.id_aluno = QtWidgets.QGroupBox(parent=self.scrollAreaWidgetContents_2)
        self.id_aluno.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(12)
        self.id_aluno.setFont(font)
        self.id_aluno.setStyleSheet("color: rgb(203, 132, 0);")
        self.id_aluno.setObjectName("id_aluno")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.id_aluno)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.nome_aluno = QtWidgets.QLineEdit(parent=self.id_aluno)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.nome_aluno.setFont(font)
        self.nome_aluno.setStyleSheet("background-color: rgb(243, 230, 213); \n"
                                        "border-style: outset;\n"
                                        "border-width: 1px;\n"
                                        "border-radius: 2px;\n"
                                        "border-color: rgb(203, 132, 0);\n"
                                        "font: 14px \"Inter Medium\" ;\n"
                                        "color: black\n"
                                        "\n"
                                        "")
        self.nome_aluno.setMaxLength(255)
        self.nome_aluno.setClearButtonEnabled(True)
        self.nome_aluno.setObjectName("nome_aluno")
        self.verticalLayout_3.addWidget(self.nome_aluno)

        validador = QtGui.QIntValidator()
        cpf_regex = QRegularExpression("^\\d{11}$")
        cpf_validador = QRegularExpressionValidator(cpf_regex)

        self.codigo_NIS = QtWidgets.QLineEdit(parent=self.id_aluno)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.codigo_NIS.setFont(font)
        self.codigo_NIS.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(203, 132, 0);\n"
"font: 14px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.codigo_NIS.setMaxLength(255)
        self.codigo_NIS.setClearButtonEnabled(True)
        self.codigo_NIS.setObjectName("codigo_NIS")
        self.verticalLayout_3.addWidget(self.codigo_NIS)

        # ID do aluno INEP

        self.codigo_INEP = QtWidgets.QLineEdit(parent=self.id_aluno)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.codigo_INEP.setFont(font)
        self.codigo_INEP.setStyleSheet("background-color: rgb(243, 230, 213); \n"
                                       "border-style: outset;\n"
                                       "border-width: 1px;\n"
                                       "border-radius: 2px;\n"
                                       "border-color:  rgb(203, 132, 0);\n"
                                       "font: 12px \"Inter Medium\" ;\n"
                                       "color: black;")
        self.codigo_INEP.setMaxLength(12)
        self.codigo_INEP.setClearButtonEnabled(True)
        self.codigo_INEP.setObjectName("codigo_INEP")

        validator = QtGui.QRegularExpressionValidator(QtCore.QRegularExpression("[0-9]{11}"), self.codigo_INEP)
        self.codigo_INEP.setValidator(validator)
        self.codigo_INEP.setPlaceholderText("Digite o ID do aluno INEP")

        self.verticalLayout_3.addWidget(self.codigo_INEP)

        self.label_id_racial = QtWidgets.QLabel(parent=self.id_aluno)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_id_racial.setFont(font)
        self.label_id_racial.setStyleSheet("color: rgb(203, 132, 0);\n"
"font: 57 10pt \"Inter Medium\";")
        self.label_id_racial.setObjectName("label_id_racial")
        self.verticalLayout_3.addWidget(self.label_id_racial)
        self.sel_id_racial = QtWidgets.QComboBox(parent=self.id_aluno)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sel_id_racial.setFont(font)
        self.sel_id_racial.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(203, 132, 0);\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.sel_id_racial.setObjectName("sel_id_racial")
        self.sel_id_racial.addItem("")
        self.sel_id_racial.addItem("")
        self.sel_id_racial.addItem("")
        self.sel_id_racial.addItem("")
        self.sel_id_racial.addItem("")
        self.sel_id_racial.addItem("")
        self.verticalLayout_3.addWidget(self.sel_id_racial)
        self.label_sexo = QtWidgets.QLabel(parent=self.id_aluno)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_sexo.setFont(font)
        self.label_sexo.setStyleSheet("color: rgb(203, 132, 0);font: 57 10pt \"Inter Medium\";")
        self.label_sexo.setObjectName("label_sexo")
        self.verticalLayout_3.addWidget(self.label_sexo)
        self.sel_sexo = QtWidgets.QComboBox(parent=self.id_aluno)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sel_sexo.setFont(font)
        self.sel_sexo.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(203, 132, 0);\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.sel_sexo.setObjectName("sel_sexo")
        self.sel_sexo.addItem("")
        self.sel_sexo.addItem("")
        self.sel_sexo.addItem("")
        self.verticalLayout_3.addWidget(self.sel_sexo)
        self.nascimento_uf = QtWidgets.QLineEdit(parent=self.id_aluno)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.nascimento_uf.setFont(font)
        self.nascimento_uf.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(203, 132, 0);\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.nascimento_uf.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhUppercaseOnly)
        self.nascimento_uf.setText(str(self.imported_uf))
        self.nascimento_uf.setMaxLength(2)
        self.nascimento_uf.setClearButtonEnabled(False)
        self.nascimento_uf.setObjectName("nascimento_uf")
        self.verticalLayout_3.addWidget(self.nascimento_uf)
        self.nascimento_municipio = QtWidgets.QLineEdit(parent=self.id_aluno)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.nascimento_municipio.setFont(font)
        self.nascimento_municipio.setStyleSheet("background-color: rgb(243, 230, 213); \n"
                                                "border-style: outset;\n"
                                                "border-width: 1px;\n"
                                                "border-radius: 2px;\n"
                                                "border-color: rgb(203, 132, 0);\n"
                                                "font: 12px \"Inter Medium\" ;\n"
                                                "color: black\n"
                                                "\n"
                                                "")
        self.nascimento_municipio.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.nascimento_municipio.setText("")
        self.nascimento_municipio.setMaxLength(30)
        self.nascimento_municipio.setClearButtonEnabled(False)
        self.nascimento_municipio.setObjectName("nascimento_municipio")
        self.verticalLayout_3.addWidget(self.nascimento_municipio)

        # Campo para Nacionalidade

        self.nacionalidade = QtWidgets.QLineEdit(parent=self.id_aluno)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.nacionalidade.setFont(font)
        self.nacionalidade.setStyleSheet("background-color: rgb(243, 230, 213); \n"
                                         "border-style: outset;\n"
                                         "border-width: 1px;\n"
                                         "border-radius: 2px;\n"
                                         "border-color:  rgb(203, 132, 0);\n"
                                         "font: 12px \"Inter Medium\" ;\n"
                                         "color: black\n"
                                         "\n"
                                         "")
        self.nacionalidade.setMaxLength(30)
        self.nacionalidade.setClearButtonEnabled(False)
        self.nacionalidade.setPlaceholderText("Nacionalidade")
        self.nacionalidade.setObjectName("nacionalidade")
        self.verticalLayout_3.addWidget(self.nacionalidade)

        # Campo para Tipo de Nascimento

        self.tipo_nascimento = QtWidgets.QLineEdit(parent=self.id_aluno)
        self.tipo_nascimento.setFont(font)
        self.tipo_nascimento.setStyleSheet("background-color: rgb(243, 230, 213); \n"
                                           "border-style: outset;\n"
                                           "border-width: 1px;\n"
                                           "border-radius: 2px;\n"
                                           "border-color:  rgb(203, 132, 0);\n"
                                           "font: 12px \"Inter Medium\" ;\n"
                                           "color: black\n"
                                           "\n"
                                           "")
        self.tipo_nascimento.setMaxLength(2)
        self.tipo_nascimento.setClearButtonEnabled(False)
        self.tipo_nascimento.setPlaceholderText("Tipo de Nascimento")
        self.tipo_nascimento.setObjectName("tipo_nascimento")
        self.verticalLayout_3.addWidget(self.tipo_nascimento)

        # Data de Nascimento

        self.label_data_nascimento = QtWidgets.QLabel("Data de Nascimento:", parent=self.id_aluno)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_data_nascimento.setFont(font)
        self.label_data_nascimento.setStyleSheet("color: rgb(203, 132, 0);\n"
                                                 "font: 57 10pt \"Inter Medium\";")
        self.label_data_nascimento.setObjectName("label_data_nascimento")
        self.verticalLayout_3.addWidget(self.label_data_nascimento)

        self.data_nascimento = QtWidgets.QDateEdit(parent=self.id_aluno)
        self.data_nascimento.setFont(font)
        self.data_nascimento.setStyleSheet("background-color: rgb(243, 230, 213); \n"
                                           "border-style: outset;\n"
                                           "border-width: 1px;\n"
                                           "border-radius: 2px;\n"
                                           "border-color: rgb(203, 132, 0);\n"
                                           "font: 12px \"Inter Medium\" ;\n"
                                           "color: black\n"
                                           "\n"
                                           "")
        self.data_nascimento.setCalendarPopup(True)
        self.data_nascimento.setDate(QtCore.QDate.currentDate())
        self.data_nascimento.setObjectName("data_nascimento")
        self.verticalLayout_3.addWidget(self.data_nascimento)

        self.label_certidao_civil = QtWidgets.QLabel(parent=self.id_aluno)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_certidao_civil.setFont(font)
        self.label_certidao_civil.setStyleSheet("color: rgb(203, 132, 0);\n"
                                                "font: 57 10pt \"Inter Medium\";")
        self.label_certidao_civil.setObjectName("label_certidao_civil")
        self.verticalLayout_3.addWidget(self.label_certidao_civil)
        self.sel_certidao_civil = QtWidgets.QComboBox(parent=self.id_aluno)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sel_certidao_civil.setFont(font)
        self.sel_certidao_civil.setStyleSheet("background-color: rgb(243, 230, 213); \n"
                                                "border-style: outset;\n"
                                                "border-width: 1px;\n"
                                                "border-radius: 2px;\n"
                                                "border-color: rgb(203, 132, 0);\n"
                                                "font: 12px \"Inter Medium\" ;\n"
                                                "color: black\n"
                                                "\n"
                                                "")
        self.sel_certidao_civil.setObjectName("sel_certidao_civil")
        self.sel_certidao_civil.addItem("")
        self.sel_certidao_civil.addItem("")
        self.sel_certidao_civil.addItem("")
        self.verticalLayout_3.addWidget(self.sel_certidao_civil)
        self.certidao_antiga = QtWidgets.QGroupBox(parent=self.id_aluno)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(10)
        self.certidao_antiga.setFont(font)
        self.certidao_antiga.setObjectName("certidao_antiga")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.certidao_antiga)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.numero_termo = QtWidgets.QLineEdit(parent=self.certidao_antiga)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        self.numero_termo.setFont(font)
        self.numero_termo.setStyleSheet("background-color: rgb(243, 230, 213); \n"
                                        "border-style: outset;\n"
                                        "border-width: 1px;\n"
                                        "border-radius: 2px;\n"
                                        "border-color: rgb(203, 132, 0);\n"
                                        "color: black\n"
                                        "\n"
                                        "")
        self.numero_termo.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.numero_termo.setMaxLength(8)
        self.numero_termo.setClearButtonEnabled(False)
        self.numero_termo.setObjectName("numero_termo")
        self.horizontalLayout_5.addWidget(self.numero_termo)
        self.livro = QtWidgets.QLineEdit(parent=self.certidao_antiga)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        self.livro.setFont(font)
        self.livro.setStyleSheet("background-color: rgb(243, 230, 213); \n"
                                "border-style: outset;\n"
                                "border-width: 1px;\n"
                                "border-radius: 2px;\n"
                                "border-color: rgb(203, 132, 0);\n"
                                "color: black\n"
                                "\n"
                                "")
        self.livro.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.livro.setMaxLength(8)
        self.livro.setClearButtonEnabled(False)
        self.livro.setObjectName("livro")
        self.horizontalLayout_5.addWidget(self.livro)
        self.folha = QtWidgets.QLineEdit(parent=self.certidao_antiga)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        self.folha.setFont(font)
        self.folha.setStyleSheet("background-color: rgb(243, 230, 213); \n"
                                "border-style: outset;\n"
                                "border-width: 1px;\n"
                                "border-radius: 2px;\n"
                                "border-color: rgb(203, 132, 0);\n"
                                "color: black\n"
                                "\n"
                                "")
        self.folha.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.folha.setMaxLength(4)
        self.folha.setClearButtonEnabled(False)
        self.folha.setObjectName("folha")
        self.horizontalLayout_5.addWidget(self.folha)
        self.label_data_exp_certidao = QtWidgets.QLabel(parent=self.certidao_antiga)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(10)
        self.label_data_exp_certidao.setFont(font)
        self.label_data_exp_certidao.setStyleSheet("color: rgb(203, 132, 0);")
        self.label_data_exp_certidao.setWordWrap(True)
        self.label_data_exp_certidao.setObjectName("label_data_exp_certidao")
        self.horizontalLayout_5.addWidget(self.label_data_exp_certidao)
        self.data_expedicao = QtWidgets.QDateEdit(parent=self.certidao_antiga)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(12)
        self.data_expedicao.setFont(font)
        self.data_expedicao.setStyleSheet("background-color: rgb(243, 230, 213); \n"
                                        "border-style: outset;\n"
                                        "border-width: 1px;\n"
                                        "border-radius: 2px;\n"
                                        "border-color: rgb(203, 132, 0);\n"
                                        "color: black\n"
                                        "\n"
                                        "")
        self.data_expedicao.setCalendarPopup(True)
        self.data_expedicao.setObjectName("data_expedicao")
        self.horizontalLayout_5.addWidget(self.data_expedicao)
        self.verticalLayout_3.addWidget(self.certidao_antiga)
        self.certidao_nova = QtWidgets.QGroupBox(parent=self.id_aluno)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(10)
        self.certidao_nova.setFont(font)
        self.certidao_nova.setObjectName("certidao_nova")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.certidao_nova)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.numero_registro_civil = QtWidgets.QLineEdit(parent=self.certidao_nova)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        self.numero_registro_civil.setFont(font)
        self.numero_registro_civil.setStyleSheet("background-color: rgb(243, 230, 213); \n"
                                                "border-style: outset;\n"
                                                "border-width: 1px;\n"
                                                "border-radius: 2px;\n"
                                                "border-color: rgb(203, 132, 0);\n"
                                                "color: black\n"
                                                "\n"
                                                "")
        self.numero_registro_civil.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.numero_registro_civil.setMaxLength(255)
        self.numero_registro_civil.setCursorPosition(0)
        self.numero_registro_civil.setClearButtonEnabled(False)
        self.numero_registro_civil.setObjectName("numero_registro_civil")
        self.horizontalLayout_6.addWidget(self.numero_registro_civil)
        self.verticalLayout_3.addWidget(self.certidao_nova)
        self.info_documentos = QtWidgets.QGroupBox(parent=self.id_aluno)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(10)
        self.info_documentos.setFont(font)
        self.info_documentos.setStyleSheet("")
        self.info_documentos.setObjectName("info_documentos")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.info_documentos)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_data_exp_info_doc = QtWidgets.QLabel(parent=self.info_documentos)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(12)
        self.label_data_exp_info_doc.setFont(font)
        self.label_data_exp_info_doc.setStyleSheet("color: rgb(203, 132, 0);\n"
                                                "")
        self.label_data_exp_info_doc.setWordWrap(True)
        self.label_data_exp_info_doc.setObjectName("label_data_exp_info_doc")
        self.gridLayout_4.addWidget(self.label_data_exp_info_doc, 3, 1, 1, 1)
        self.cpf_aluno = QtWidgets.QLineEdit(parent=self.info_documentos)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cpf_aluno.setFont(font)
        self.cpf_aluno.setStyleSheet("background-color: rgb(243, 230, 213); \n"
                                        "border-style: outset;\n"
                                        "border-width: 1px;\n"
                                        "border-radius: 2px;\n"
                                        "border-color: rgb(203, 132, 0);\n"
                                        "font: 12px \"Inter Medium\" ;\n"
                                        "color: black\n"
                                        "\n"
                                        "")
        self.cpf_aluno.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhUppercaseOnly)
        self.cpf_aluno.setText("")
        self.cpf_aluno.setMaxLength(15)
        self.cpf_aluno.setClearButtonEnabled(False)
        self.cpf_aluno.setObjectName("cpf_aluno")
        self.gridLayout_4.addWidget(self.cpf_aluno, 4, 0, 1, 1)
        self.documento_tipo = QtWidgets.QLineEdit(parent=self.info_documentos)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.documento_tipo.setFont(font)
        self.documento_tipo.setStyleSheet("background-color: rgb(243, 230, 213); \n"
                                        "border-style: outset;\n"
                                        "border-width: 1px;\n"
                                        "border-radius: 2px;\n"
                                        "border-color: rgb(203, 132, 0);\n"
                                        "font: 12px \"Inter Medium\" ;\n"
                                        "color: black\n"
                                        "\n"
                                        "")
        self.documento_tipo.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.documento_tipo.setText("")
        self.documento_tipo.setMaxLength(30)
        self.documento_tipo.setClearButtonEnabled(False)
        self.documento_tipo.setObjectName("documento_tipo")
        self.gridLayout_4.addWidget(self.documento_tipo, 3, 0, 1, 1)
        self.data_exp = QtWidgets.QDateEdit(parent=self.info_documentos)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(12)
        self.data_exp.setFont(font)
        self.data_exp.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(203, 132, 0);\n"
"color: black\n"
"\n"
"")
        self.data_exp.setCalendarPopup(True)
        self.data_exp.setObjectName("data_exp")
        self.gridLayout_4.addWidget(self.data_exp, 4, 1, 1, 1)
        self.cartorio_nome = QtWidgets.QLineEdit(parent=self.info_documentos)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cartorio_nome.setFont(font)
        self.cartorio_nome.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(203, 132, 0);\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.cartorio_nome.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.cartorio_nome.setText("")
        self.cartorio_nome.setMaxLength(30)
        self.cartorio_nome.setClearButtonEnabled(False)
        self.cartorio_nome.setObjectName("cartorio_nome")
        self.gridLayout_4.addWidget(self.cartorio_nome, 2, 1, 1, 1)
        self.cartorio_uf = QtWidgets.QLineEdit(parent=self.info_documentos)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cartorio_uf.setFont(font)
        self.cartorio_uf.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(203, 132, 0);\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.cartorio_uf.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhUppercaseOnly)
        self.cartorio_uf.setText("")
        self.cartorio_uf.setMaxLength(2)
        self.cartorio_uf.setClearButtonEnabled(False)
        self.cartorio_uf.setObjectName("cartorio_uf")
        self.gridLayout_4.addWidget(self.cartorio_uf, 0, 0, 1, 1)
        self.documento_orgao_emissor = QtWidgets.QLineEdit(parent=self.info_documentos)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.documento_orgao_emissor.setFont(font)
        self.documento_orgao_emissor.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(203, 132, 0);\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.documento_orgao_emissor.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhUppercaseOnly)
        self.documento_orgao_emissor.setText("")
        self.documento_orgao_emissor.setMaxLength(2)
        self.documento_orgao_emissor.setClearButtonEnabled(False)
        self.documento_orgao_emissor.setObjectName("documento_orgao_emissor")
        self.gridLayout_4.addWidget(self.documento_orgao_emissor, 0, 1, 1, 1)
        self.cartorio_municipio = QtWidgets.QLineEdit(parent=self.info_documentos)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cartorio_municipio.setFont(font)
        self.cartorio_municipio.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(203, 132, 0);\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.cartorio_municipio.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.cartorio_municipio.setText("")
        self.cartorio_municipio.setMaxLength(30)
        self.cartorio_municipio.setClearButtonEnabled(False)
        self.cartorio_municipio.setObjectName("cartorio_municipio")
        self.gridLayout_4.addWidget(self.cartorio_municipio, 2, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.info_documentos)
        self.verticalLayout_4.addWidget(self.id_aluno)
        self.InformacoesdeMatricula = QtWidgets.QGroupBox(parent=self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(10)
        self.InformacoesdeMatricula.setFont(font)
        self.InformacoesdeMatricula.setStyleSheet("color: rgb(203, 132, 0);")
        self.InformacoesdeMatricula.setObjectName("InformacoesdeMatricula")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.InformacoesdeMatricula)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.nome_escola = QtWidgets.QLineEdit(parent=self.InformacoesdeMatricula)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.nome_escola.setFont(font)
        self.nome_escola.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(203, 132, 0);\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.nome_escola.setMaxLength(255)
        self.nome_escola.setClearButtonEnabled(True)
        self.nome_escola.setObjectName("nome_escola")
        self.gridLayout_5.addWidget(self.nome_escola, 0, 0, 1, 8)
        self.serie_label = QtWidgets.QLabel(parent=self.InformacoesdeMatricula)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(10)
        self.serie_label.setFont(font)
        self.serie_label.setStyleSheet("color: rgb(203, 132, 0);")
        self.serie_label.setObjectName("serie_label")
        self.gridLayout_5.addWidget(self.serie_label, 4, 1, 1, 1)
        self.procedencia_label = QtWidgets.QLabel(parent=self.InformacoesdeMatricula)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(10)
        self.procedencia_label.setFont(font)
        self.procedencia_label.setStyleSheet("color: rgb(203, 132, 0);")
        self.procedencia_label.setObjectName("procedencia_label")
        self.gridLayout_5.addWidget(self.procedencia_label, 4, 2, 1, 1)
        self.bolsa_familia = QtWidgets.QCheckBox(parent=self.InformacoesdeMatricula)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.bolsa_familia.setFont(font)
        self.bolsa_familia.setStyleSheet("\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.bolsa_familia.setObjectName("bolsa_familia")
        self.gridLayout_5.addWidget(self.bolsa_familia, 4, 5, 1, 1)
        self.sel_serie = QtWidgets.QComboBox(parent=self.InformacoesdeMatricula)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sel_serie.setFont(font)
        self.sel_serie.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(203, 132, 0);\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.sel_serie.setObjectName("sel_serie")
        self.sel_serie.addItem("")
        self.sel_serie.addItem("")
        self.sel_serie.addItem("")
        self.sel_serie.addItem("")
        self.sel_serie.addItem("")
        self.sel_serie.addItem("")
        self.sel_serie.addItem("")
        self.gridLayout_5.addWidget(self.sel_serie, 5, 1, 1, 1)
        self.turno_label = QtWidgets.QLabel(parent=self.InformacoesdeMatricula)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(10)
        self.turno_label.setFont(font)
        self.turno_label.setStyleSheet("color: rgb(203, 132, 0);")
        self.turno_label.setObjectName("turno_label")
        self.gridLayout_5.addWidget(self.turno_label, 4, 0, 1, 1)
        self.transporte = QtWidgets.QCheckBox(parent=self.InformacoesdeMatricula)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.transporte.setFont(font)
        self.transporte.setStyleSheet("\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.transporte.setObjectName("transporte")
        self.gridLayout_5.addWidget(self.transporte, 5, 5, 1, 1)
        self.sel_turno = QtWidgets.QComboBox(parent=self.InformacoesdeMatricula)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sel_turno.setFont(font)
        self.sel_turno.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(203, 132, 0);\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.sel_turno.setObjectName("sel_turno")
        self.sel_turno.addItem("")
        self.sel_turno.addItem("")
        self.sel_turno.addItem("")
        self.sel_turno.addItem("")
        self.sel_turno.addItem("")
        self.gridLayout_5.addWidget(self.sel_turno, 5, 0, 1, 1)
        self.sel_procedencia = QtWidgets.QComboBox(parent=self.InformacoesdeMatricula)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sel_procedencia.setFont(font)
        self.sel_procedencia.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(203, 132, 0);\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.sel_procedencia.setObjectName("sel_procedencia")
        self.sel_procedencia.addItem("")
        self.sel_procedencia.addItem("")
        self.sel_procedencia.addItem("")
        self.sel_procedencia.addItem("")
        self.sel_procedencia.addItem("")
        self.sel_procedencia.addItem("")
        self.gridLayout_5.addWidget(self.sel_procedencia, 5, 2, 1, 3)

        self.codigo_inep = QtWidgets.QLineEdit(parent=self.InformacoesdeMatricula)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.codigo_inep.setFont(font)
        self.codigo_inep.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(203, 132, 0);\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.codigo_inep.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.codigo_inep.setText("")
        self.codigo_inep.setMaxLength(8)
        self.codigo_inep.setClearButtonEnabled(False)
        self.codigo_inep.setObjectName("codigo_inep")
        self.gridLayout_5.addWidget(self.codigo_inep, 2, 0, 1, 3)
        self.codigo_inep.setValidator(validador)
        self.codigo_turma = QtWidgets.QLineEdit(parent=self.InformacoesdeMatricula)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.codigo_turma.setFont(font)
        self.codigo_turma.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(203, 132, 0);\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.codigo_turma.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.codigo_turma.setText("")
        self.codigo_turma.setMaxLength(8)
        self.codigo_turma.setClearButtonEnabled(False)
        self.codigo_turma.setObjectName("codigo_turma")
        self.gridLayout_5.addWidget(self.codigo_turma, 2, 3, 1, 4)
        self.data_ingresso_escola = QtWidgets.QDateEdit(parent=self.InformacoesdeMatricula)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.data_ingresso_escola.setFont(font)
        self.data_ingresso_escola.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(203, 132, 0);\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.data_ingresso_escola.setCalendarPopup(True)
        self.data_ingresso_escola.setObjectName("data_ingresso_escola")
        self.gridLayout_5.addWidget(self.data_ingresso_escola, 1, 1, 1, 1)
        self.ano_letivo = QtWidgets.QLineEdit(parent=self.InformacoesdeMatricula)
        self.ano_letivo.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ano_letivo.setFont(font)
        self.ano_letivo.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(203, 132, 0);\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.ano_letivo.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhFormattedNumbersOnly)
        self.ano_letivo.setText("")
        self.ano_letivo.setMaxLength(4)
        self.ano_letivo.setClearButtonEnabled(False)
        self.ano_letivo.setObjectName("ano_letivo")
        self.gridLayout_5.addWidget(self.ano_letivo, 2, 7, 1, 1)
        self.data_matricula = QtWidgets.QDateEdit(parent=self.InformacoesdeMatricula)
        self.data_matricula.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.data_matricula.setFont(font)
        self.data_matricula.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(203, 132, 0);\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.data_matricula.setCalendarPopup(True)
        self.data_matricula.setObjectName("data_matricula")
        self.gridLayout_5.addWidget(self.data_matricula, 1, 4, 1, 2)
        self.matricula = QtWidgets.QLineEdit(parent=self.InformacoesdeMatricula)
        self.matricula.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.matricula.setFont(font)
        self.matricula.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(203, 132, 0);\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.matricula.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.matricula.setText("")
        self.matricula.setMaxLength(8)
        self.matricula.setClearButtonEnabled(False)
        self.matricula.setObjectName("matricula")
        self.gridLayout_5.addWidget(self.matricula, 1, 6, 1, 2)
        self.data_matricula_label = QtWidgets.QLabel(parent=self.InformacoesdeMatricula)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(10)
        self.data_matricula_label.setFont(font)
        self.data_matricula_label.setWordWrap(True)
        self.data_matricula_label.setObjectName("data_matricula_label")
        self.gridLayout_5.addWidget(self.data_matricula_label, 1, 2, 1, 2)
        self.data_ingresso_label = QtWidgets.QLabel(parent=self.InformacoesdeMatricula)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(10)
        self.data_ingresso_label.setFont(font)
        self.data_ingresso_label.setWordWrap(True)
        self.data_ingresso_label.setObjectName("data_ingresso_label")
        self.gridLayout_5.addWidget(self.data_ingresso_label, 1, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.InformacoesdeMatricula)
        self.verticalLayout_9.addLayout(self.verticalLayout_4)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox = QtWidgets.QGroupBox(parent=self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        # código do aluno

        self.codigo_aluno = QtWidgets.QLineEdit(parent=self.groupBox)
        self.codigo_aluno.setMinimumSize(QtCore.QSize(0, 0))
        self.codigo_aluno.setFont(font)
        self.codigo_aluno.setStyleSheet("background-color: rgb(243, 230, 213); \n"
                                        "border-style: outset;\n"
                                        "border-width: 1px;\n"
                                        "border-radius: 2px;\n"
                                        "border-color: rgb(203, 132, 0);\n"
                                        "font: 12px \"Inter Medium\" ;\n"
                                        "color: black;")
        self.codigo_aluno.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.codigo_aluno.setMaxLength(20)
        self.codigo_aluno.setClearButtonEnabled(True)
        self.codigo_aluno.setObjectName("codigo_aluno")
        self.codigo_aluno.setPlaceholderText("Código do Aluno")
        self.verticalLayout_5.addWidget(self.codigo_aluno)

        # Documento Pendente?
        self.checkbox_documento_pendente = QtWidgets.QCheckBox("Documento Pendente?", parent=self.groupBox)
        self.checkbox_documento_pendente.setObjectName("checkbox_documento_pendente")
        self.checkbox_documento_pendente.setStyleSheet("\n"
                                                       "font: 12px \"Inter Medium\" ;\n"
                                                       "color: black\n"
                                                       "\n"
                                                       "")
        self.verticalLayout_5.addWidget(self.checkbox_documento_pendente)

        self.gridLayout_5.addWidget(self.codigo_aluno, 6, 0, 1, 3)
        self.gridLayout_5.addWidget(self.checkbox_documento_pendente, 6, 5, 1, 1)

        self.nome_pai = QtWidgets.QLineEdit(parent=self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.nome_pai.setFont(font)
        self.nome_pai.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(203, 132, 0);\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.nome_pai.setMaxLength(255)
        self.nome_pai.setClearButtonEnabled(True)
        self.nome_pai.setObjectName("nome_pai")
        self.verticalLayout_5.addWidget(self.nome_pai)

        self.nome_mae = QtWidgets.QLineEdit(parent=self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.nome_mae.setFont(font)
        self.nome_mae.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(203, 132, 0);\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.nome_mae.setMaxLength(255)
        self.nome_mae.setClearButtonEnabled(True)
        self.nome_mae.setObjectName("nome_mae")
        self.verticalLayout_5.addWidget(self.nome_mae)

        # responsavel

        self.responsavel = QtWidgets.QLineEdit(parent=self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.responsavel.setFont(font)
        self.responsavel.setStyleSheet("background-color: rgb(243, 230, 213); \n"
                                       "border-style: outset;\n"
                                       "border-width: 1px;\n"
                                       "border-radius: 2px;\n"
                                       "border-color:  rgb(203, 132, 0);\n"
                                       "font: 12px \"Inter Medium\" ;\n"
                                       "color: black\n"
                                       "\n"
                                       "")
        self.responsavel.setMaxLength(255)
        self.responsavel.setClearButtonEnabled(True)
        self.responsavel.setObjectName("responsavel")
        self.responsavel.setPlaceholderText("Responsável")
        self.verticalLayout_5.addWidget(self.responsavel)

        self.verticalLayout_6.addWidget(self.groupBox)
        self.frame = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.transtorno_global_desenvolvimento = QtWidgets.QGroupBox(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.transtorno_global_desenvolvimento.setFont(font)
        self.transtorno_global_desenvolvimento.setStyleSheet("\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.transtorno_global_desenvolvimento.setObjectName("transtorno_global_desenvolvimento")
        self.layoutWidget_3 = QtWidgets.QWidget(parent=self.transtorno_global_desenvolvimento)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 25, 251, 96))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.layoutWidget_3.setFont(font)
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.def_autismo = QtWidgets.QCheckBox(parent=self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.def_autismo.setFont(font)
        self.def_autismo.setObjectName("def_autismo")
        self.verticalLayout_8.addWidget(self.def_autismo)
        self.def_rett = QtWidgets.QCheckBox(parent=self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.def_rett.setFont(font)
        self.def_rett.setObjectName("def_rett")
        self.verticalLayout_8.addWidget(self.def_rett)
        self.def_asperger = QtWidgets.QCheckBox(parent=self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.def_asperger.setFont(font)
        self.def_asperger.setObjectName("def_asperger")
        self.verticalLayout_8.addWidget(self.def_asperger)
        self.def_TDI = QtWidgets.QCheckBox(parent=self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.def_TDI.setFont(font)
        self.def_TDI.setObjectName("def_TDI")
        self.verticalLayout_8.addWidget(self.def_TDI)
        self.gridLayout_6.addWidget(self.transtorno_global_desenvolvimento, 0, 0, 1, 1)
        self.groupBox_8 = QtWidgets.QGroupBox(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setStyleSheet("\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.groupBox_8.setObjectName("groupBox_8")
        self.altas_habilidades = QtWidgets.QCheckBox(parent=self.groupBox_8)
        self.altas_habilidades.setGeometry(QtCore.QRect(10, 57, 216, 19))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.altas_habilidades.setFont(font)
        self.altas_habilidades.setObjectName("altas_habilidades")
        self.gridLayout_6.addWidget(self.groupBox_8, 1, 0, 1, 1)
        self.deficiencias = QtWidgets.QGroupBox(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.deficiencias.setFont(font)
        self.deficiencias.setStyleSheet("\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.deficiencias.setObjectName("deficiencias")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.deficiencias)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.def_baixa_visao = QtWidgets.QCheckBox(parent=self.deficiencias)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.def_baixa_visao.setFont(font)
        self.def_baixa_visao.setObjectName("def_baixa_visao")
        self.verticalLayout_7.addWidget(self.def_baixa_visao)
        self.def_cegueira = QtWidgets.QCheckBox(parent=self.deficiencias)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.def_cegueira.setFont(font)
        self.def_cegueira.setObjectName("def_cegueira")
        self.verticalLayout_7.addWidget(self.def_cegueira)
        self.def_auditiva = QtWidgets.QCheckBox(parent=self.deficiencias)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.def_auditiva.setFont(font)
        self.def_auditiva.setObjectName("def_auditiva")
        self.verticalLayout_7.addWidget(self.def_auditiva)
        self.def_intelectual = QtWidgets.QCheckBox(parent=self.deficiencias)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.def_intelectual.setFont(font)
        self.def_intelectual.setObjectName("def_intelectual")
        self.verticalLayout_7.addWidget(self.def_intelectual)
        self.def_fisica = QtWidgets.QCheckBox(parent=self.deficiencias)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.def_fisica.setFont(font)
        self.def_fisica.setObjectName("def_fisica")
        self.verticalLayout_7.addWidget(self.def_fisica)
        self.def_multipla = QtWidgets.QCheckBox(parent=self.deficiencias)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.def_multipla.setFont(font)
        self.def_multipla.setObjectName("def_multipla")
        self.verticalLayout_7.addWidget(self.def_multipla)
        self.def_down = QtWidgets.QCheckBox(parent=self.deficiencias)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.def_down.setFont(font)
        self.def_down.setObjectName("def_down")
        self.verticalLayout_7.addWidget(self.def_down)
        self.def_surdez = QtWidgets.QCheckBox(parent=self.deficiencias)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.def_surdez.setFont(font)
        self.def_surdez.setObjectName("def_surdez")
        self.verticalLayout_7.addWidget(self.def_surdez)
        self.def_surdocegueira = QtWidgets.QCheckBox(parent=self.deficiencias)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.def_surdocegueira.setFont(font)
        self.def_surdocegueira.setObjectName("def_surdocegueira")
        self.verticalLayout_7.addWidget(self.def_surdocegueira)
        self.gridLayout_6.addWidget(self.deficiencias, 0, 1, 2, 1)
        self.verticalLayout_6.addWidget(self.frame)
        self.caixa_endereco = QtWidgets.QGroupBox(parent=self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        self.caixa_endereco.setFont(font)
        self.caixa_endereco.setObjectName("caixa_endereco")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.caixa_endereco)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.CEP = QtWidgets.QLineEdit(parent=self.caixa_endereco)
        self.CEP.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.CEP.setFont(font)
        self.CEP.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(203, 132, 0);\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.CEP.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.CEP.setText("")
        self.CEP.setMaxLength(8)
        self.CEP.setClearButtonEnabled(False)
        self.CEP.setObjectName("CEP")
        self.gridLayout_7.addWidget(self.CEP, 1, 5, 1, 1)
        self.complemento = QtWidgets.QLineEdit(parent=self.caixa_endereco)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.complemento.setFont(font)
        self.complemento.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(203, 132, 0);\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.complemento.setMaxLength(200)
        self.complemento.setClearButtonEnabled(False)
        self.complemento.setObjectName("complemento")
        self.gridLayout_7.addWidget(self.complemento, 1, 3, 1, 1)
        self.lab_zona = QtWidgets.QLabel(parent=self.caixa_endereco)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        self.lab_zona.setFont(font)
        self.lab_zona.setObjectName("lab_zona")
        self.gridLayout_7.addWidget(self.lab_zona, 4, 0, 1, 1)
        self.numero = QtWidgets.QLineEdit(parent=self.caixa_endereco)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.numero.setFont(font)
        self.numero.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(203, 132, 0);\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.numero.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.numero.setText("")
        self.numero.setMaxLength(255)
        self.numero.setClearButtonEnabled(False)
        self.numero.setObjectName("numero")
        self.gridLayout_7.addWidget(self.numero, 1, 0, 1, 1)
        self.municipio_endereco = QtWidgets.QLineEdit(parent=self.caixa_endereco)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.municipio_endereco.setFont(font)
        self.municipio_endereco.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(203, 132, 0);\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.municipio_endereco.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.municipio_endereco.setText("")
        self.municipio_endereco.setMaxLength(30)
        self.municipio_endereco.setClearButtonEnabled(False)
        self.municipio_endereco.setObjectName("municipio_endereco")
        self.gridLayout_7.addWidget(self.municipio_endereco, 3, 0, 1, 3)
        self.bairro_endereco = QtWidgets.QLineEdit(parent=self.caixa_endereco)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.bairro_endereco.setFont(font)
        self.bairro_endereco.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(203, 132, 0);\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.bairro_endereco.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.bairro_endereco.setText("")
        self.bairro_endereco.setMaxLength(32)
        self.bairro_endereco.setClearButtonEnabled(False)
        self.bairro_endereco.setObjectName("bairro_endereco")
        self.gridLayout_7.addWidget(self.bairro_endereco, 3, 3, 1, 2)
        self.uf_endereco = QtWidgets.QLineEdit(parent=self.caixa_endereco)
        self.uf_endereco.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.uf_endereco.setFont(font)
        self.uf_endereco.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(203, 132, 0);\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.uf_endereco.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhUppercaseOnly)
        self.uf_endereco.setText("")
        self.uf_endereco.setMaxLength(2)
        self.uf_endereco.setClearButtonEnabled(False)
        self.uf_endereco.setObjectName("uf_endereco")
        self.gridLayout_7.addWidget(self.uf_endereco, 3, 5, 1, 1)
        self.endereco = QtWidgets.QLineEdit(parent=self.caixa_endereco)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.endereco.setFont(font)
        self.endereco.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(203, 132, 0);\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.endereco.setMaxLength(255)
        self.endereco.setClearButtonEnabled(True)
        self.endereco.setObjectName("endereco")
        self.gridLayout_7.addWidget(self.endereco, 0, 0, 1, 6)
        self.sel_zona = QtWidgets.QComboBox(parent=self.caixa_endereco)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sel_zona.setFont(font)
        self.sel_zona.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(203, 132, 0);\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.sel_zona.setObjectName("sel_zona")
        self.sel_zona.addItem("")
        self.sel_zona.addItem("")
        self.sel_zona.addItem("")
        self.gridLayout_7.addWidget(self.sel_zona, 5, 0, 1, 2)
        self.telefone = QtWidgets.QLineEdit(parent=self.caixa_endereco)
        self.telefone.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.telefone.setFont(font)
        self.telefone.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(203, 132, 0);\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.telefone.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly|QtCore.Qt.InputMethodHint.ImhPreferNumbers)
        self.telefone.setText("")
        self.telefone.setMaxLength(13)
        self.telefone.setClearButtonEnabled(False)
        self.telefone.setObjectName("telefone")
        self.gridLayout_7.addWidget(self.telefone, 5, 3, 1, 1)
        self.email = QtWidgets.QLineEdit(parent=self.caixa_endereco)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.email.setFont(font)
        self.email.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(203, 132, 0);\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.email.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhEmailCharactersOnly|QtCore.Qt.InputMethodHint.ImhPreferNumbers)
        self.email.setText("")
        self.email.setMaxLength(25)
        self.email.setClearButtonEnabled(False)
        self.email.setObjectName("email")
        self.gridLayout_7.addWidget(self.email, 5, 5, 1, 1)
        self.verticalLayout_6.addWidget(self.caixa_endereco)
        self.verticalLayout_9.addLayout(self.verticalLayout_6)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.confirm_button = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.atualiza_aluno())
        self.confirm_button.setGeometry(QtCore.QRect(580, 640, 136, 71))
        self.confirm_button.setStyleSheet("background-color: rgb(203, 132, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font:bold 20px \"Inter Black\" ;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"color: rgb(243, 230, 213);\n"
"")
        self.confirm_button.setObjectName("confirm_button")
        self.confirm_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.cancel_button = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.voltar_tela_editar_1())
        self.cancel_button.setGeometry(QtCore.QRect(440, 640, 136, 71))
        self.cancel_button.setStyleSheet("background-color: rgb(243, 230, 213);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font:bold 20px \"Inter Black\" ;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"color: rgb(203, 132, 0)")
        self.cancel_button.setObjectName("cancel_button")
        self.cancel_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 20, 621, 70))
        self.label.setStyleSheet("font: 57 40pt \"Trend Slab Four\";\n"
"color: rgb(203, 132, 0)")
        self.label.setObjectName("label")
        self.delete_button = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: (self.excluir_aluno())) #DELETE
        self.delete_button.setGeometry(QtCore.QRect(40, 640, 136, 71))
        self.delete_button.setStyleSheet("background-color: rgb(203, 132, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font:bold 20px \"Inter Black\" ;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"color: rgb(243, 230, 213);\n"
"")
        self.delete_button.setObjectName("delete_button")
        self.delete_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", f"Editar Matrícula do Aluno: {str(self.imported_nome_aluno)}"))
        self.id_aluno.setTitle(_translate("MainWindow", "Identificação do Aluno"))

        self.nome_aluno.setText(_translate("MainWindow", str(self.imported_nome_aluno)))
        self.nome_aluno.setPlaceholderText(_translate("MainWindow", "Nome do Aluno"))

        self.codigo_NIS.setText(_translate("MainWindow", str(self.imported_nis)))
        self.codigo_NIS.setPlaceholderText(_translate("MainWindow", "NIS"))

        self.codigo_INEP.setText(_translate("MainWindow", self.imported_codigo_inep))

        self.label_id_racial.setText(_translate("MainWindow", "Identidade Racial"))

        self.sel_id_racial.setItemText(0, _translate("MainWindow", "1- Branca"))
        self.sel_id_racial.setItemText(1, _translate("MainWindow", "2- Preta"))
        self.sel_id_racial.setItemText(2, _translate("MainWindow", "3- Parda"))
        self.sel_id_racial.setItemText(3, _translate("MainWindow", "4- Amarela"))
        self.sel_id_racial.setItemText(4, _translate("MainWindow", "5- Indígena"))
        self.sel_id_racial.setItemText(5, _translate("MainWindow", "N/A"))
        self.sel_id_racial.setCurrentIndex(self.imported_raca)

        self.label_sexo.setText(_translate("MainWindow", "Sexo*"))
        self.sel_sexo.setItemText(0, _translate("MainWindow", "Masculino"))
        self.sel_sexo.setItemText(1, _translate("MainWindow", "Feminino"))
        self.sel_sexo.setItemText(2, _translate("MainWindow", "N/A"))
        self.sel_sexo.setCurrentIndex(self.imported_sexo)

        self.nascimento_uf.setPlaceholderText(_translate("MainWindow", "UF*"))
        self.nascimento_uf.setText(str(self.imported_uf))

        self.nascimento_municipio.setPlaceholderText(_translate("MainWindow", "Município de nascimento*"))
        self.nascimento_municipio.setText(_translate("MainWindow", str(self.imported_local_nascimento_municipio)))

        self.nacionalidade.setText(_translate("MainWindow", self.imported_nacionalidade))

        self.tipo_nascimento.setText(_translate("MainWindow", self.imported_tipo_nasc))

        #data de nascimento
        self.data_nascimento.setDisplayFormat(_translate("MainWindow", "d/M/yyyy"))
        self.data_nascimento.setDate(QDate(int(self.ano_nasc), int(self.mes_nasc), int(self.dia_nasc)))

        self.label_certidao_civil.setText(_translate("MainWindow", "Tipo da Certidão Civil")) #Não inserido no banco
        self.sel_certidao_civil.setItemText(0, _translate("MainWindow", "Nascimento"))
        self.sel_certidao_civil.setItemText(1, _translate("MainWindow", "Casamento"))
        self.sel_certidao_civil.setItemText(2, _translate("MainWindow", "N/A"))
        self.sel_certidao_civil.setCurrentIndex(self.imported_tipo_certidao_civil)

        self.certidao_antiga.setTitle(_translate("MainWindow", "Certidão Modelo Antigo"))

        self.numero_termo.setPlaceholderText(_translate("MainWindow", "Numero Termo"))
        self.numero_termo.setText(_translate("MainWindow", self.imported_num_termo))

        self.livro.setPlaceholderText(_translate("MainWindow", "Livro"))
        self.livro.setText(_translate("MainWindow", self.imported_livro))

        self.folha.setPlaceholderText(_translate("MainWindow", "Folha"))
        self.folha.setText(_translate("MainWindow", self.imported_folha))

        self.label_data_exp_certidao.setText(_translate("MainWindow", "Data de Expedição Certidão"))
        self.data_expedicao.setDisplayFormat(_translate("MainWindow", "d/M/yyyy"))
        self.data_expedicao.setDate(QDate(int(self.ano_exp_cert), int(self.mes_exp_cert), int(self.dia_exp_cert)))

        self.certidao_nova.setTitle(_translate("MainWindow", "Certidão Modelo Novo"))
        self.numero_registro_civil.setPlaceholderText(_translate("MainWindow", "Numero de Matrícula (Registro Civil)"))
        self.numero_registro_civil.setText(_translate("MainWindow", self.imported_num_matricula_rc))

        self.info_documentos.setTitle(_translate("MainWindow", "Informações Documentadas"))

        self.label_data_exp_info_doc.setText(_translate("MainWindow", "Data de Expedição"))

        self.cpf_aluno.setPlaceholderText(_translate("MainWindow", "Cadastro de Pessoa Física (CPF)"))
        self.cpf_aluno.setText(_translate("MainWindow", self.imported_cpf))

        self.documento_tipo.setPlaceholderText(_translate("MainWindow", "Identidade, Documento Estrangerio ou Passaporte"))
        self.documento_tipo.setText(_translate("MainWindow", self.imported_identidade_doc_pass))

        self.data_exp.setDisplayFormat(_translate("MainWindow", "d/M/yyyy"))
        self.data_exp.setDate(QDate(int(self.ano_exp_id), int(self.mes_exp_id), int(self.dia_exp_id)))

        self.cartorio_nome.setPlaceholderText(_translate("MainWindow", "Nome do Cartório"))
        self.cartorio_nome.setText(_translate("MainWindow", str(self.imported_nome_cartorio)))

        self.cartorio_uf.setPlaceholderText(_translate("MainWindow", "UF - Cartório"))
        self.cartorio_uf.setText(_translate("MainWindow", str(self.imported_uf_cartorio)))

        self.documento_orgao_emissor.setPlaceholderText(_translate("MainWindow", "Orgão Emissor"))
        self.documento_orgao_emissor.setText(_translate("MainWindow", str(self.imported_orgao_emissor)))

        self.cartorio_municipio.setPlaceholderText(_translate("MainWindow", "Município do Cartório"))
        self.cartorio_municipio.setText(_translate("MainWindow", str(self.imported_municipio_cartorio)))

        self.InformacoesdeMatricula.setTitle(_translate("MainWindow", "Informações de Matricula"))

        self.nome_escola.setPlaceholderText(_translate("MainWindow", "Nome da Escola"))
        self.nome_escola.setText(_translate("MainWindow", self.imported_nome_escola))

        self.serie_label.setText(_translate("MainWindow", "Série*"))

        self.procedencia_label.setText(_translate("MainWindow", "Codigo de Procedência*"))

        self.bolsa_familia.setText(_translate("MainWindow", "Programa Bolsa Família"))
        self.bolsa_familia.setChecked(self.imported_participa_programa)

        self.checkbox_documento_pendente.setChecked(self.imported_doc_pendente)

        self.sel_serie.setItemText(0, _translate("MainWindow", "01. Jardim I"))
        self.sel_serie.setItemText(1, _translate("MainWindow", "02. Jardim II"))
        self.sel_serie.setItemText(2, _translate("MainWindow", "03. 1° Ano"))
        self.sel_serie.setItemText(3, _translate("MainWindow", "04. 2° Ano"))
        self.sel_serie.setItemText(4, _translate("MainWindow", "05. 3° Ano"))
        self.sel_serie.setItemText(5, _translate("MainWindow", "06. 4° Ano"))
        self.sel_serie.setItemText(6, _translate("MainWindow", "07. 5° Ano"))
        self.sel_serie.setCurrentIndex(self.imported_codigo_serie)

        self.turno_label.setText(_translate("MainWindow", "Turno*"))

        self.transporte.setText(_translate("MainWindow", "Transporte Escolar"))
        self.transporte.setChecked(self.imported_transporte_escola)

        self.sel_turno.setCurrentIndex(self.imported_turno)
        self.sel_turno.setItemText(0, _translate("MainWindow", "Manhã"))
        self.sel_turno.setItemText(1, _translate("MainWindow", "Intermediário"))
        self.sel_turno.setItemText(2, _translate("MainWindow", "Tarde"))
        self.sel_turno.setItemText(3, _translate("MainWindow", "Noite"))
        self.sel_turno.setItemText(4, _translate("MainWindow", "Tempo Integral"))


        self.sel_procedencia.setItemText(0, _translate("MainWindow", "01 - Do Lar"))
        self.sel_procedencia.setItemText(1, _translate("MainWindow", "02 - Escola Municipal"))
        self.sel_procedencia.setItemText(2, _translate("MainWindow", "03 - Escola Estadual"))
        self.sel_procedencia.setItemText(3, _translate("MainWindow", "04 - Escola Particular"))
        self.sel_procedencia.setItemText(4, _translate("MainWindow", "05 - Escola Federal"))
        self.sel_procedencia.setItemText(5, _translate("MainWindow", "06 - Escola Comunitária"))
        self.sel_procedencia.setCurrentIndex(self.imported_codigo_procedencia)

        self.codigo_aluno.setText(_translate("MainWindow", self.imported_codigo_aluno))

        self.codigo_inep.setPlaceholderText(_translate("MainWindow", "Codigo Senso Inep*"))
        self.codigo_inep.setText(_translate("MainWindow", self.imported_cod_censo))

        self.codigo_turma.setPlaceholderText(_translate("MainWindow", "Codigo Turma*"))
        self.codigo_turma.setText(_translate("MainWindow", self.imported_codigo_turma))

        self.data_ingresso_escola.setDisplayFormat(_translate("MainWindow", "d/M/yyyy"))

        self.ano_letivo.setPlaceholderText(_translate("MainWindow", "Ano Letivo*"))
        self.ano_letivo.setText(_translate("MainWindow", self.imported_ano_letivo))

        self.data_matricula.setDisplayFormat(_translate("MainWindow", "d/M/yyyy"))

        self.matricula.setPlaceholderText(_translate("MainWindow", "Matricula*"))
        self.matricula.setText(_translate("MainWindow", self.imported_matricula))

        self.data_matricula_label.setText(_translate("MainWindow", "Data de Matricula"))
        self.data_matricula.setDate(QDate(int(self.ano_matricula), int(self.mes_matricula), int(self.dia_matricula)))

        self.data_ingresso_label.setText(_translate("MainWindow", "Data de Ingresso"))
        self.data_ingresso_escola.setDate(QDate(int(self.ano_ingresso), int(self.mes_ingresso), int(self.dia_ingresso)))

        self.groupBox.setTitle(_translate("MainWindow", "Dados dos Pais/Responsáveis"))

        self.nome_pai.setPlaceholderText(_translate("MainWindow", "Nome do Pai"))
        self.nome_pai.setText(_translate("MainWindow", self.imported_nome_pai))

        self.nome_mae.setPlaceholderText(_translate("MainWindow", "Nome da Mãe"))
        self.nome_mae.setText(_translate("MainWindow", self.imported_nome_mae))

        self.responsavel.setText(_translate("MainWindow", self.imported_responsavel))

        self.transtorno_global_desenvolvimento.setTitle(_translate("MainWindow", "Transtorno Global do Desenvolvimento"))

        self.def_autismo.setText(_translate("MainWindow", "Autismo"))
        self.def_autismo.setChecked(self.imported_autismo)

        self.def_rett.setText(_translate("MainWindow", "Sindrome de Rett"))
        self.def_rett.setChecked(self.imported_rett)

        self.def_asperger.setText(_translate("MainWindow", "Sindrome de Asperger"))
        self.def_asperger.setChecked(self.imported_asperger)

        self.def_TDI.setText(_translate("MainWindow", "Transtorno desintegrativo da infância"))
        self.def_TDI.setChecked(self.imported_transtorno_desintegrativo)

        self.groupBox_8.setTitle(_translate("MainWindow", "Altas Habilidades / Superdotação"))

        self.altas_habilidades.setText(_translate("MainWindow", "Altas Habilidades / Superdotação"))
        self.altas_habilidades.setChecked(self.imported_altas_habilidades)

        self.deficiencias.setTitle(_translate("MainWindow", "Deficiências"))

        self.def_baixa_visao.setText(_translate("MainWindow", "Baixa Visão"))
        self.def_baixa_visao.setChecked(self.imported_baixa_visao)

        self.def_cegueira.setText(_translate("MainWindow", "Cegueira"))
        self.def_cegueira.setChecked(self.imported_cegueira)

        self.def_auditiva.setText(_translate("MainWindow", "Deficiência Auditiva"))
        self.def_auditiva.setChecked(self.imported_auditiva)

        self.def_intelectual.setText(_translate("MainWindow", "Deficiência Intelectual"))
        self.def_intelectual.setChecked(self.imported_intelectual)

        self.def_fisica.setText(_translate("MainWindow", "Deficiência Física"))
        self.def_fisica.setChecked(self.imported_fisica)

        self.def_multipla.setText(_translate("MainWindow", "Deficiência Múltipla"))
        self.def_multipla.setChecked(self.imported_multipla)

        self.def_down.setText(_translate("MainWindow", "Sindrome de Down"))
        self.def_down.setChecked(self.imported_sindrome_down)

        self.def_surdez.setText(_translate("MainWindow", "Surdez"))
        self.def_surdez.setChecked(self.imported_surdez)

        self.def_surdocegueira.setText(_translate("MainWindow", "Surdocegueira"))
        self.def_surdocegueira.setChecked(self.imported_surdocegueira)

        #endereco
        self.caixa_endereco.setTitle(_translate("MainWindow", "Endereço"))

        self.CEP.setPlaceholderText(_translate("MainWindow", "CEP*"))
        self.CEP.setText(_translate("MainWindow", self.imported_cep))

        self.complemento.setPlaceholderText(_translate("MainWindow", "Complemento"))
        self.complemento.setText(_translate("MainWindow", self.imported_complemento))

        self.lab_zona.setText(_translate("MainWindow", "Zona*"))

        self.numero.setPlaceholderText(_translate("MainWindow", "N°"))
        self.numero.setText(_translate("MainWindow", self.imported_num_endereco))

        self.municipio_endereco.setPlaceholderText(_translate("MainWindow", "Município*"))
        self.municipio_endereco.setText(_translate("MainWindow", self.imported_municipio_endereco))

        self.bairro_endereco.setPlaceholderText(_translate("MainWindow", "Bairro"))
        self.bairro_endereco.setText(_translate("MainWindow", self.imported_bairro))

        self.uf_endereco.setPlaceholderText(_translate("MainWindow", "UF"))
        self.uf_endereco.setText(_translate("MainWindow", self.imported_uf_endereco))

        self.endereco.setPlaceholderText(_translate("MainWindow", "Endereço"))
        self.endereco.setText(_translate("MainWindow", self.imported_endereco))

        self.sel_zona.setCurrentIndex(self.imported_zona)
        self.sel_zona.setItemText(0, _translate("MainWindow", "Rural"))
        self.sel_zona.setItemText(1, _translate("MainWindow", "Urbana"))
        self.sel_zona.setItemText(2, _translate("MainWindow", "N/A"))

        self.telefone.setPlaceholderText(_translate("MainWindow", "Telefone"))
        self.telefone.setText(_translate("MainWindow", self.imported_telefone))

        self.email.setPlaceholderText(_translate("MainWindow", "Email"))
        self.email.setText(_translate("MainWindow", self.imported_email))

        self.confirm_button.setText(_translate("MainWindow", "Confirmar"))
        self.cancel_button.setText(_translate("MainWindow", "Cancelar"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Atualizar perfil</p></body></html>"))
        self.delete_button.setText(_translate("MainWindow", "Excluir"))

    def importar_dados(self):
        if os.path.exists('dados_editar.pkl'):
            with open('dados_editar.pkl', 'rb') as arquivo:
                id_aluno = pickle.load(arquivo)

                nis = pickle.load(arquivo)
                nome_aluno = pickle.load(arquivo)
                sexo = pickle.load(arquivo)
                uf = pickle.load(arquivo)
                local_nascimento_municipio = pickle.load(arquivo)
                uf_cartorio = pickle.load(arquivo)
                municipio_cartorio = pickle.load(arquivo)
                nome_cartorio = pickle.load(arquivo)
                identidade_doc_pass = pickle.load(arquivo)
                data_expedicao_id = pickle.load(arquivo)
                orgao_emissor = pickle.load(arquivo)
                uf_identidade = pickle.load(arquivo)
                cpf = pickle.load(arquivo)
                raca = pickle.load(arquivo)
                data_nasc = pickle.load(arquivo)
                tipo_nasc = pickle.load(arquivo)
                nacionalidade = pickle.load(arquivo)
                codigo_inep = pickle.load(arquivo)

                num_matricula_rc = pickle.load(arquivo)
                num_termo = pickle.load(arquivo)
                livro = pickle.load(arquivo)
                folha = pickle.load(arquivo)
                data_expedicao_certidao = pickle.load(arquivo)
                tipo_certidao_civil = pickle.load(arquivo)

                nome_escola = pickle.load(arquivo)
                cod_censo = pickle.load(arquivo)
                data_ingresso_escola = pickle.load(arquivo)
                matricula = pickle.load(arquivo)
                data_matricula = pickle.load(arquivo)
                codigo_turma = pickle.load(arquivo)
                turno = pickle.load(arquivo)
                codigo_serie = pickle.load(arquivo)
                codigo_procedencia = pickle.load(arquivo)
                participa_programa = pickle.load(arquivo)
                transporte_escolar = pickle.load(arquivo)
                ano_letivo = pickle.load(arquivo)
                codigo_aluno = pickle.load(arquivo)
                doc_pendente = pickle.load(arquivo)

                nome_mae = pickle.load(arquivo)
                nome_pai = pickle.load(arquivo)
                responsavel = pickle.load(arquivo)

                autismo = pickle.load(arquivo)
                rett = pickle.load(arquivo)
                asperger = pickle.load(arquivo)
                transtorno_desintegrativo = pickle.load(arquivo)
                baixa_visao = pickle.load(arquivo)
                cegueira = pickle.load(arquivo)
                auditiva = pickle.load(arquivo)
                intelectual = pickle.load(arquivo)
                fisica = pickle.load(arquivo)
                multipla = pickle.load(arquivo)
                sindrome_down = pickle.load(arquivo)
                surdez = pickle.load(arquivo)
                surdocegueira = pickle.load(arquivo)
                altas_habilidades = pickle.load(arquivo)

                endereco = pickle.load(arquivo)
                complemento = pickle.load(arquivo)
                num_endereco = pickle.load(arquivo)
                municipio_endereco = pickle.load(arquivo)
                bairro = pickle.load(arquivo)
                cep = pickle.load(arquivo)
                zona = pickle.load(arquivo)
                telefone = pickle.load(arquivo)
                email = pickle.load(arquivo)
                uf_endereco = pickle.load(arquivo)


            if sexo == 'Masculino': sexo = 0
            elif sexo == 'Feminino': sexo = 1
            else: sexo = 3

            if raca == '1- Branca': raca = 0
            elif raca == '2- Preta': raca = 1
            elif raca == '3- Parda': raca = 2
            elif raca == '4- Amarela': raca = 3
            elif raca == '5- Indígena': raca = 4
            else: raca = 5

            if codigo_serie == '01. Jardim I': codigo_serie = 0
            elif codigo_serie == '02. Jardim II': codigo_serie = 1
            elif codigo_serie == '03. 1° Ano': codigo_serie = 2
            elif codigo_serie == '04. 2° Ano': codigo_serie = 3
            elif codigo_serie == '05. 3° Ano': codigo_serie = 4
            elif codigo_serie == '06. 4° Ano': codigo_serie = 5
            else: codigo_serie = 6

            if turno == 'Manhã': turno = 0
            elif turno == 'Intermediário': turno = 1
            elif turno == 'Tarde': turno = 2
            elif turno == 'Noite': turno = 3
            else: turno = 4

            if codigo_procedencia == '01 - Do Lar': codigo_procedencia = 0
            elif codigo_procedencia == '02 - Escola Municipal': codigo_procedencia = 1
            elif codigo_procedencia == '03 - Escola Estadual': codigo_procedencia = 2
            elif codigo_procedencia == '04 - Escola Particular': codigo_procedencia = 3
            elif codigo_procedencia == '05 - Escola Federal': codigo_procedencia = 4
            else: codigo_procedencia = 5

            if zona == 'Rural': zona = 0
            elif zona == 'Urbana': zona = 1
            else: zona = 2

            if tipo_certidao_civil == "Nascimento": tipo_certidao_civil = 0
            elif tipo_certidao_civil == "Casamento": tipo_certidao_civil = 1
            else: tipo_certidao_civil = 2

            #region IDENTIFICAÇÃO_ALUNO
            self.imported_id_aluno = id_aluno

            self.imported_nis = nis
            self.imported_nome_aluno = nome_aluno
            self.imported_sexo = sexo
            self.imported_uf = uf
            self.imported_local_nascimento_municipio = local_nascimento_municipio
            self.imported_uf_cartorio = uf_cartorio
            self.imported_municipio_cartorio = municipio_cartorio
            self.imported_nome_cartorio = nome_cartorio
            self.imported_identidade_doc_pass = identidade_doc_pass
            self.imported_data_expedicao_id = str(data_expedicao_id)
            self.imported_orgao_emissor = orgao_emissor
            self.imported_uf_identidade = uf_identidade
            self.imported_cpf = str(cpf)
            self.imported_raca = raca

            #NOVOS
            self.imported_data_nasc = str(data_nasc)
            self.imported_tipo_nasc = tipo_nasc
            self.imported_nacionalidade = nacionalidade
            self.imported_codigo_inep = str(codigo_inep)

            self.ano_nasc = self.imported_data_nasc.split("-")[0]
            self.mes_nasc = self.imported_data_nasc.split("-")[1]
            self.dia_nasc = self.imported_data_nasc.split("-")[2]

            self.ano_exp_id = self.imported_data_expedicao_id.split("-")[0]
            self.mes_exp_id = self.imported_data_expedicao_id.split("-")[1]
            self.dia_exp_id = self.imported_data_expedicao_id.split("-")[2]
            #endregion

            #region CERTIDAO
            self.imported_num_matricula_rc = num_matricula_rc
            self.imported_num_termo = num_termo
            self.imported_livro = str(livro)
            self.imported_folha = str(folha)
            self.imported_data_expedicao_certidao = str(data_expedicao_certidao)
            self.imported_tipo_certidao_civil = tipo_certidao_civil

            self.ano_exp_cert = self.imported_data_expedicao_certidao.split("-")[0]
            self.mes_exp_cert = self.imported_data_expedicao_certidao.split("-")[1]
            self.dia_exp_cert = self.imported_data_expedicao_certidao.split("-")[2]
            #endregion

            #region INFORMAÇÕES_MATRICULA
            self.imported_nome_escola = nome_escola
            self.imported_cod_censo = str(cod_censo)
            self.imported_data_ingresso_escola = str(data_ingresso_escola)
            self.imported_matricula = str(matricula)
            self.imported_data_matricula = str(data_matricula)
            self.imported_codigo_turma = str(codigo_turma)
            self.imported_turno = turno
            self.imported_codigo_serie = codigo_serie
            self.imported_codigo_procedencia = codigo_procedencia
            self.imported_participa_programa = participa_programa
            self.imported_transporte_escola = transporte_escolar
            self.imported_ano_letivo = str(ano_letivo)
            self.imported_codigo_aluno = str(codigo_aluno)
            self.imported_doc_pendente = doc_pendente

            self.ano_ingresso = self.imported_data_ingresso_escola.split("-")[0]
            self.mes_ingresso = self.imported_data_ingresso_escola.split("-")[1]
            self.dia_ingresso = self.imported_data_ingresso_escola.split("-")[2]

            self.ano_matricula = self.imported_data_matricula.split("-")[0]
            self.mes_matricula = self.imported_data_matricula.split("-")[1]
            self.dia_matricula = self.imported_data_matricula.split("-")[2]
            #endregion

            #region DADOS_PAIS_RESPONSAVEL
            self.imported_nome_mae = nome_mae
            self.imported_nome_pai = nome_pai

            self.imported_responsavel = responsavel
            #endregion

            #region SAUDE
            self.imported_autismo = autismo
            self.imported_rett = rett
            self.imported_asperger = asperger
            self.imported_transtorno_desintegrativo = transtorno_desintegrativo
            self.imported_baixa_visao = baixa_visao
            self.imported_cegueira = cegueira
            self.imported_auditiva = auditiva
            self.imported_intelectual = intelectual
            self.imported_fisica = fisica
            self.imported_multipla = multipla
            self.imported_sindrome_down = sindrome_down
            self.imported_surdez = surdez
            self.imported_surdocegueira = surdocegueira
            self.imported_altas_habilidades = altas_habilidades
            #endregion

            #region ENDERECO
            self.imported_endereco = endereco
            self.imported_complemento = complemento
            self.imported_num_endereco = str(num_endereco)
            self.imported_municipio_endereco = municipio_endereco
            self.imported_bairro = bairro
            self.imported_cep = str(cep)
            self.imported_zona = zona
            self.imported_telefone = str(telefone)
            self.imported_email = email
            self.imported_uf_endereco = uf_endereco
            #endregion

            print("Dados importados.")
        else:
            print("Arquivo 'dados_editar.pkl' não encontrado.")

    def voltar_tela_editar_1(self):
        from editar_matricula1 import Ui_Edit_1_Window
        self.tela_alunos = QtWidgets.QMainWindow()
        self.ui = Ui_Edit_1_Window()
        self.ui.setupUi(self.tela_alunos)
        self.tela_alunos.show()
        QtWidgets.QApplication.instance().activeWindow().close()

    def excluir_aluno(self):

        id_aluno = self.imported_id_aluno

        if id_aluno:

            executar_query_freq("DELETE FROM certidao WHERE id_aluno = %s",[id_aluno])
            executar_query_freq("DELETE FROM dados_pais_responsavel WHERE id_aluno = %s", [id_aluno])
            executar_query_freq("DELETE FROM endereco WHERE id_aluno = %s", [id_aluno])
            executar_query_freq("DELETE FROM informacoes_matricula WHERE id_aluno = %s", [id_aluno])
            executar_query_freq("DELETE FROM saude WHERE id_aluno = %s", [id_aluno])
            executar_query_freq("DELETE FROM identificacao_aluno WHERE id_aluno = %s", [id_aluno])

        print("Aluno excluido.")
        self.voltar_tela_editar_1()

# UPDATES
    def atualiza_aluno(self):
        try:
            resultado_identificacao = self.update_identificacao_aluno_ui()
            if not resultado_identificacao:
                raise Exception("Falha ao atualizar identificação do aluno")

            resultado_saude = self.update_saude_ui()
            if not resultado_saude:
                raise Exception("Falha ao atualizar informações de saúde")

            resultado_endereco = self.update_endereco_ui()
            if not resultado_endereco:
                raise Exception("Falha ao atualizar endereço")

            resultado_dados_pais = self.update_dados_pais_ui()
            if not resultado_dados_pais:
                raise Exception("Falha ao atualizar dados dos pais ou responsáveis")

            resultado_informacoes_matricula = self.update_informacoes_matricula_ui()
            if not resultado_informacoes_matricula:
                raise Exception("Falha ao atualizar informações da matrícula")

            resultado_certidao = self.update_certidao_ui()
            if not resultado_certidao:
                raise Exception("Falha ao atualizar certidão")


        except Exception as e:
            print(str(e))

        print("Aluno atualizado com sucesso")
        self.voltar_tela_editar_1()

    def update_identificacao_aluno_ui(self):
        try:
            nome_aluno = self.nome_aluno.text()
            codigo_NIS = self.codigo_NIS.text()
            raca_aluno = self.sel_id_racial.currentText()
            sexo_aluno = self.sel_sexo.currentText()
            nascimento_uf = self.nascimento_uf.text()
            nascimento_municipio = self.nascimento_municipio.text()
            cartorio_uf = self.cartorio_uf.text()
            nome_cartorio = self.cartorio_nome.text()
            id_doc_pass = self.documento_tipo.text()
            cartorio_municipio = self.cartorio_municipio.text()
            data_exp_identidade = self.data_exp.date().toString("yyyy-MM-dd")
            orgao_emissor = self.documento_orgao_emissor.text()
            uf_identidade = self.nascimento_uf.text()
            cpf = self.cpf_aluno.text()
            data_nascimento = self.data_nascimento.date().toString("yyyy-MM-dd")
            tipo_nascimento = self.tipo_nascimento.text()
            nacionalidade = self.nacionalidade.text()
            codigo_INEP = self.codigo_inep.text()

            if not all([nome_aluno, codigo_NIS, raca_aluno, sexo_aluno, nascimento_uf, nascimento_municipio,
                        cartorio_uf, nome_cartorio, id_doc_pass, cartorio_municipio, data_exp_identidade, orgao_emissor,
                        uf_identidade, cpf, data_nascimento, tipo_nascimento, nacionalidade, codigo_INEP]):
                QMessageBox(QMessageBox.Icon.Warning, "Erro", "Alguns campos do Identificação do Aluno estão vazios",
                            QMessageBox.StandardButton.Ok).exec()
                return False

            resultado = update_identificacao_aluno(codigo_NIS, nome_aluno,sexo_aluno, nascimento_uf, nascimento_municipio,cartorio_uf, nome_cartorio, id_doc_pass, cartorio_municipio, data_exp_identidade,orgao_emissor, uf_identidade, cpf, raca_aluno, data_nascimento, tipo_nascimento, nacionalidade, codigo_INEP, self.imported_id_aluno)

            return True if resultado else False
        except Exception as e:
            print(f"Erro ao inserir identificação do aluno: {e}")
            return False

    def update_saude_ui(self):
        try:
            autismo = self.def_autismo.isChecked()
            rett = self.def_rett.isChecked()
            asperger = self.def_asperger.isChecked()
            transtorno_desintegrativo = self.def_TDI.isChecked()
            baixa_visao = self.def_baixa_visao.isChecked()
            cegueira = self.def_cegueira.isChecked()
            auditiva = self.def_auditiva.isChecked()
            intelectual = self.def_intelectual.isChecked()
            fisica = self.def_fisica.isChecked()
            multipla = self.def_multipla.isChecked()
            sindrome_down = self.def_down.isChecked()
            surdez = self.def_surdez.isChecked()
            surdocegueira = self.def_surdocegueira.isChecked()
            altas_habilidades = self.altas_habilidades.isChecked()

            resultado = update_saude(autismo, rett, asperger, transtorno_desintegrativo,baixa_visao, cegueira, auditiva, intelectual, fisica,multipla, sindrome_down, surdez, surdocegueira, altas_habilidades, self.imported_id_aluno)

            return True if resultado else False
        except Exception as e:
            print(f"Erro ao inserir informações de saúde: {e}")
            return False

    def update_endereco_ui(self):
        try:
            endereco = self.endereco.text()
            complemento = self.complemento.text()
            numero_endereco = self.numero.text()
            municipio = self.municipio_endereco.text()
            bairro = self.bairro_endereco.text()
            cep = self.CEP.text()
            zona = self.sel_zona.currentText()
            telefone = self.telefone.text()
            email = self.email.text()
            uf = self.uf_endereco.text()

            resultado = update_endereco(endereco, complemento, numero_endereco, municipio, bairro, cep, zona, telefone, email, uf, self.imported_id_aluno)
            return True if resultado else False
        except Exception as e:
            print(f"Erro ao inserir endereço: {e}")
            return False

    def update_dados_pais_ui(self):
        try:
            nome_pai = self.nome_pai.text()
            nome_mae = self.nome_mae.text()
            responsavel = self.responsavel.text()

            if not all([nome_mae]):
                QMessageBox(QMessageBox.Icon.Warning, "Erro", "Alguns campos Dados dos Pais estão vazios",
                            QMessageBox.StandardButton.Ok).exec()
                return False

            resultado = update_dados_pais_responsavel(nome_mae, nome_pai, responsavel, self.imported_id_aluno)
            return True if resultado else False
        except Exception as e:
            print(f"Erro ao inserir dados dos pais ou responsáveis: {e}")
            return False

    def update_informacoes_matricula_ui(self):
        try:
            nome_escola = self.nome_escola.text()
            codigo_turma = self.codigo_turma.text()
            data_matricula = self.data_matricula.date().toString("yyyy-MM-dd")
            codigo_inep = self.codigo_inep.text()
            matricula = self.matricula.text()
            data_ingresso_escola = self.data_ingresso_escola.date().toString("yyyy-MM-dd")
            turno = self.sel_turno.currentText()
            serie = self.sel_serie.currentText()
            codigo_procedencia = self.sel_procedencia.currentText()
            programa_bolsa_familia = self.bolsa_familia.isChecked()
            transporte_escolar = self.transporte.isChecked()
            ano_letivo = self.ano_letivo.text()
            codigo_aluno = self.codigo_aluno.text()
            documento_pendente = self.checkbox_documento_pendente.isChecked()

            if not all([nome_escola, codigo_turma, data_matricula, codigo_inep, matricula, data_ingresso_escola,
                        turno, serie, codigo_procedencia, ano_letivo, codigo_aluno]):
                QMessageBox(QMessageBox.Icon.Warning, "Erro", "Alguns campos do Iformações da Matrícula estão vazios",
                            QMessageBox.StandardButton.Ok).exec()
                return False

            resultado = update_informacoes_matricula(nome_escola, codigo_inep, data_ingresso_escola, matricula, data_matricula, codigo_turma, programa_bolsa_familia, transporte_escolar, turno, serie, codigo_procedencia, ano_letivo, codigo_aluno, documento_pendente, self.imported_id_aluno)

            return True if resultado else False
        except Exception as e:
            print(f"Erro ao inserir informações da matrícula: {e}")
            return False

    def update_certidao_ui(self):
        try:
            num_matricula_registro_civil = self.numero_registro_civil.text()
            num_termo = self.numero_termo.text()
            livro = self.livro.text()
            folha = self.folha.text()
            data_expedicao_certidao = self.data_expedicao.date().toString("yyyy-MM-dd")
            tipo_certidao_civil = self.sel_certidao_civil.currentText()

            resultado = update_certidao(num_matricula_registro_civil, num_termo, livro, folha, data_expedicao_certidao, tipo_certidao_civil, self.imported_id_aluno)
            return True if resultado else False
        except Exception as e:
            print(f"Erro ao inserir certidão: {e}")
            return False


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Edit_2_Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
