from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import QRegularExpression, Qt
from PyQt6.QtGui import QIcon, QRegularExpressionValidator

from criar_excel import adicionar_dados_excel
from database import connect_db, insert_identificacao_aluno,insert_saude,insert_endereco,insert_dados_pais_responsavel,insert_informacoes_matricula,insert_saude,insert_certidao,checa_matricula

class UI_MatriculaWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 659)
        MainWindow.setMinimumSize(QtCore.QSize(750, 659))
        MainWindow.setMaximumSize(QtCore.QSize(750, 659))
        MainWindow.setWindowFlags(MainWindow.windowFlags() & ~Qt.WindowType.WindowMaximizeButtonHint)
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(243, 230, 213);")
        MainWindow.setWindowIcon(QIcon('imagens\\4.png'))
        MainWindow.setStyleSheet("background-color: rgb(243, 230, 213);")
        MainWindow.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 100, 721, 521))
        self.scrollArea.setStyleSheet("QScrollBar{ background-color: rgb(45, 84, 60);\n"
"color: rgb(243, 230, 213);\n"
"} ")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 702, 1268))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        # ID ALUNO

        self.id_aluno = QtWidgets.QGroupBox(parent=self.scrollAreaWidgetContents_2)
        self.id_aluno.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(12)
        self.id_aluno.setFont(font)
        self.id_aluno.setObjectName("id_aluno")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.id_aluno)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        # NOME ALUNO

        self.nome_aluno = QtWidgets.QLineEdit(parent=self.id_aluno)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.nome_aluno.setFont(font)
        self.nome_aluno.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);\n"
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

        # NIS

        self.codigo_NIS = QtWidgets.QLineEdit(parent=self.id_aluno)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.codigo_NIS.setFont(font)
        self.codigo_NIS.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.codigo_NIS.setMaxLength(255)
        self.codigo_NIS.setClearButtonEnabled(True)
        self.codigo_NIS.setObjectName("codigo_NIS")
        self.codigo_NIS.setValidator(validador)
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
        "border-color:  rgb(45, 84, 60);\n"
        "font: 12px \"Inter Medium\" ;\n"
        "color: black;")
        self.codigo_INEP.setMaxLength(12) 
        self.codigo_INEP.setClearButtonEnabled(True)
        self.codigo_INEP.setObjectName("codigo_INEP")

        validator = QtGui.QRegularExpressionValidator(QtCore.QRegularExpression("[0-9]{11}"), self.codigo_INEP)
        self.codigo_INEP.setValidator(validator)
        self.codigo_INEP.setPlaceholderText("Digite o ID do aluno INEP")

        self.verticalLayout_3.addWidget(self.codigo_INEP)

        # RAÇA

        self.label_id_racial = QtWidgets.QLabel(parent=self.id_aluno)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_id_racial.setFont(font)
        self.label_id_racial.setStyleSheet("color: rgb(45, 84, 60);\n"
"font: 57 10pt \"Inter Medium\";")
        self.label_id_racial.setObjectName("label_id_racial")
        self.verticalLayout_3.addWidget(self.label_id_racial)
        
        self.sel_id_racial = QtWidgets.QComboBox(parent=self.id_aluno)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sel_id_racial.setFont(font)
        self.sel_id_racial.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);\n"
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

        # SEXO
        
        self.label_sexo = QtWidgets.QLabel(parent=self.id_aluno)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_sexo.setFont(font)
        self.label_sexo.setStyleSheet("color: rgb(45, 84, 60);\n"
"font: 57 10pt \"Inter Medium\";")
        self.label_sexo.setObjectName("label_sexo")
        self.verticalLayout_3.addWidget(self.label_sexo)

        self.sel_sexo = QtWidgets.QComboBox(parent=self.id_aluno)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sel_sexo.setFont(font)
        self.sel_sexo.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.sel_sexo.setObjectName("sel_sexo")
        self.sel_sexo.addItem("")
        self.sel_sexo.addItem("")
        self.sel_sexo.addItem("")
        self.verticalLayout_3.addWidget(self.sel_sexo)
        
        # NASCIMENTO - DATA

        self.nascimento_uf = QtWidgets.QLineEdit(parent=self.id_aluno)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.nascimento_uf.setFont(font)
        self.nascimento_uf.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.nascimento_uf.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhUppercaseOnly)
        self.nascimento_uf.setText("")
        self.nascimento_uf.setMaxLength(2)
        self.nascimento_uf.setClearButtonEnabled(False)
        self.nascimento_uf.setObjectName("nascimento_uf")
        self.verticalLayout_3.addWidget(self.nascimento_uf)
        self.nascimento_municipio = QtWidgets.QLineEdit(parent=self.id_aluno)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.nascimento_municipio.setFont(font)
        self.nascimento_municipio.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);\n"
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
        "border-color:  rgb(45, 84, 60);\n"
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
        "border-color:  rgb(45, 84, 60);\n"
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
        self.label_data_nascimento.setStyleSheet("color: rgb(45, 84, 60);\n"
"font: 57 10pt \"Inter Medium\";")
        self.label_data_nascimento.setObjectName("label_data_nascimento")
        self.verticalLayout_3.addWidget(self.label_data_nascimento)

        self.data_nascimento = QtWidgets.QDateEdit(parent=self.id_aluno)
        self.data_nascimento.setFont(font)
        self.data_nascimento.setStyleSheet("background-color: rgb(243, 230, 213); \n"
                                        "border-style: outset;\n"
                                        "border-width: 1px;\n"
                                        "border-radius: 2px;\n"
                                        "border-color: rgb(45, 84, 60);\n"
                                        "font: 12px \"Inter Medium\" ;\n"
                                        "color: black\n"
                                        "\n"
                                        "")
        self.data_nascimento.setCalendarPopup(True)
        self.data_nascimento.setDate(QtCore.QDate.currentDate())
        self.data_nascimento.setObjectName("data_nascimento")
        self.verticalLayout_3.addWidget(self.data_nascimento)

        # Certidao

        self.label_certidao_civil = QtWidgets.QLabel(parent=self.id_aluno)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_certidao_civil.setFont(font)
        self.label_certidao_civil.setStyleSheet("color: rgb(45, 84, 60);\n"
"font: 57 10pt \"Inter Medium\";")
        self.label_certidao_civil.setObjectName("label_certidao_civil")
        self.verticalLayout_3.addWidget(self.label_certidao_civil)
        self.sel_certidao_civil = QtWidgets.QComboBox(parent=self.id_aluno)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        self.sel_certidao_civil.setFont(font)
        self.sel_certidao_civil.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);")
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
"border-color:  rgb(45, 84, 60);\n"
"color: black")
        self.numero_termo.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.numero_termo.setMaxLength(8)
        self.numero_termo.setClearButtonEnabled(False)
        self.numero_termo.setObjectName("numero_termo")
        self.horizontalLayout_5.addWidget(self.numero_termo)
        self.numero_termo.setValidator(validador)
        self.livro = QtWidgets.QLineEdit(parent=self.certidao_antiga)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        self.livro.setFont(font)
        self.livro.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);\n"
"color: black")
        self.livro.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.livro.setMaxLength(8)
        self.livro.setClearButtonEnabled(False)
        self.livro.setObjectName("livro")
        self.livro.setValidator(validador)
        self.horizontalLayout_5.addWidget(self.livro)
        self.folha = QtWidgets.QLineEdit(parent=self.certidao_antiga)
        self.folha.setValidator(validador)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        self.folha.setFont(font)
        self.folha.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);\n"
"color: black")
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
        self.label_data_exp_certidao.setStyleSheet("color: rgb(45, 84, 60);")
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
"border-color:  rgb(45, 84, 60);\n"
"color: black;")
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
"border-color:  rgb(45, 84, 60);\n"
"color: black;")
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
        self.label_data_exp_info_doc.setStyleSheet("color: rgb(45, 84, 60);")
        self.label_data_exp_info_doc.setWordWrap(True)
        self.label_data_exp_info_doc.setObjectName("label_data_exp_info_doc")
        self.gridLayout_4.addWidget(self.label_data_exp_info_doc, 3, 1, 1, 1)
        self.cpf_aluno = QtWidgets.QLineEdit(parent=self.info_documentos)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cpf_aluno.setFont(font)
        self.cpf_aluno.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.cpf_aluno.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhUppercaseOnly)
        self.cpf_aluno.setText("")
        self.cpf_aluno.setMaxLength(15)
        self.cpf_aluno.setClearButtonEnabled(False)
        self.cpf_aluno.setObjectName("cpf_aluno")
        self.cpf_aluno.setValidator(cpf_validador)
        self.gridLayout_4.addWidget(self.cpf_aluno, 4, 0, 1, 1)
        self.documento_tipo = QtWidgets.QLineEdit(parent=self.info_documentos)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.documento_tipo.setFont(font)
        self.documento_tipo.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);\n"
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
"border-color:  rgb(45, 84, 60);\n"
"color: rgb(45, 84, 60);")
        self.data_exp.setCalendarPopup(True)
        self.data_exp.setObjectName("data_exp")
        self.gridLayout_4.addWidget(self.data_exp, 4, 1, 1, 1)
        self.cartorio_nome = QtWidgets.QLineEdit(parent=self.info_documentos)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cartorio_nome.setFont(font)
        self.cartorio_nome.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);\n"
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
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cartorio_uf.setFont(font)
        self.cartorio_uf.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);\n"
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
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.documento_orgao_emissor.setFont(font)
        self.documento_orgao_emissor.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);\n"
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
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cartorio_municipio.setFont(font)
        self.cartorio_municipio.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);\n"
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
        self.InformacoesdeMatricula.setObjectName("InformacoesdeMatricula")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.InformacoesdeMatricula)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.nome_escola = QtWidgets.QLineEdit(parent=self.InformacoesdeMatricula)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.nome_escola.setFont(font)
        self.nome_escola.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);\n"
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
        self.serie_label.setStyleSheet("color: rgb(45, 84, 60);")
        self.serie_label.setObjectName("serie_label")
        self.gridLayout_5.addWidget(self.serie_label, 4, 1, 1, 1)
        self.procedencia_label = QtWidgets.QLabel(parent=self.InformacoesdeMatricula)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(10)
        self.procedencia_label.setFont(font)
        self.procedencia_label.setStyleSheet("color: rgb(45, 84, 60);")
        self.procedencia_label.setObjectName("procedencia_label")
        self.gridLayout_5.addWidget(self.procedencia_label, 4, 2, 1, 1)
        self.bolsa_familia = QtWidgets.QCheckBox(parent=self.InformacoesdeMatricula)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
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
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sel_serie.setFont(font)
        self.sel_serie.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);\n"
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
        self.turno_label.setStyleSheet("color: rgb(45, 84, 60);")
        self.turno_label.setObjectName("turno_label")
        self.gridLayout_5.addWidget(self.turno_label, 4, 0, 1, 1)
        self.transporte = QtWidgets.QCheckBox(parent=self.InformacoesdeMatricula)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
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
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sel_turno.setFont(font)
        self.sel_turno.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);\n"
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
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sel_procedencia.setFont(font)
        self.sel_procedencia.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);\n"
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
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.codigo_inep.setFont(font)
        self.codigo_inep.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);\n"
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
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.codigo_turma.setFont(font)
        self.codigo_turma.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);\n"
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
        self.codigo_turma.setValidator(validador)
        self.data_ingresso_escola = QtWidgets.QDateEdit(parent=self.InformacoesdeMatricula)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.data_ingresso_escola.setFont(font)
        self.data_ingresso_escola.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);\n"
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
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ano_letivo.setFont(font)
        self.ano_letivo.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.ano_letivo.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhFormattedNumbersOnly)
        self.ano_letivo.setText("")
        self.ano_letivo.setMaxLength(4)
        self.ano_letivo.setClearButtonEnabled(False)
        self.ano_letivo.setObjectName("ano_letivo")
        self.ano_letivo.setValidator(validador)
        self.gridLayout_5.addWidget(self.ano_letivo, 2, 7, 1, 1)
        self.data_matricula = QtWidgets.QDateEdit(parent=self.InformacoesdeMatricula)
        self.data_matricula.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.data_matricula.setFont(font)
        self.data_matricula.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);\n"
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
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.matricula.setFont(font)
        self.matricula.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);\n"
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
        self.matricula.setValidator(validador)
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
                                        "border-color: rgb(45, 84, 60);\n"
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

        # pai

        self.nome_pai = QtWidgets.QLineEdit(parent=self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.nome_pai.setFont(font)
        self.nome_pai.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);\n"
"font: 12px \"Inter Medium\" ;\n"
"color: black\n"
"\n"
"")
        self.nome_pai.setMaxLength(255)
        self.nome_pai.setClearButtonEnabled(True)
        self.nome_pai.setObjectName("nome_pai")
        self.verticalLayout_5.addWidget(self.nome_pai)

        # mae

        self.nome_mae = QtWidgets.QLineEdit(parent=self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.nome_mae.setFont(font)
        self.nome_mae.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);\n"
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
"border-color:  rgb(45, 84, 60);\n"
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
        font.setPointSize(11)
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
        font.setPointSize(11)
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
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.def_autismo.setFont(font)
        self.def_autismo.setObjectName("def_autismo")
        self.verticalLayout_8.addWidget(self.def_autismo)
        self.def_rett = QtWidgets.QCheckBox(parent=self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.def_rett.setFont(font)
        self.def_rett.setObjectName("def_rett")
        self.verticalLayout_8.addWidget(self.def_rett)
        self.def_asperger = QtWidgets.QCheckBox(parent=self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.def_asperger.setFont(font)
        self.def_asperger.setObjectName("def_asperger")
        self.verticalLayout_8.addWidget(self.def_asperger)
        self.def_TDI = QtWidgets.QCheckBox(parent=self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
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
        font.setPointSize(11)
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
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.altas_habilidades.setFont(font)
        self.altas_habilidades.setObjectName("altas_habilidades")
        self.gridLayout_6.addWidget(self.groupBox_8, 1, 0, 1, 1)
        self.deficiencias = QtWidgets.QGroupBox(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
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
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.def_baixa_visao.setFont(font)
        self.def_baixa_visao.setObjectName("def_baixa_visao")
        self.verticalLayout_7.addWidget(self.def_baixa_visao)
        self.def_cegueira = QtWidgets.QCheckBox(parent=self.deficiencias)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.def_cegueira.setFont(font)
        self.def_cegueira.setObjectName("def_cegueira")
        self.verticalLayout_7.addWidget(self.def_cegueira)
        self.def_auditiva = QtWidgets.QCheckBox(parent=self.deficiencias)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.def_auditiva.setFont(font)
        self.def_auditiva.setObjectName("def_auditiva")
        self.verticalLayout_7.addWidget(self.def_auditiva)
        self.def_intelectual = QtWidgets.QCheckBox(parent=self.deficiencias)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.def_intelectual.setFont(font)
        self.def_intelectual.setObjectName("def_intelectual")
        self.verticalLayout_7.addWidget(self.def_intelectual)
        self.def_fisica = QtWidgets.QCheckBox(parent=self.deficiencias)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.def_fisica.setFont(font)
        self.def_fisica.setObjectName("def_fisica")
        self.verticalLayout_7.addWidget(self.def_fisica)
        self.def_multipla = QtWidgets.QCheckBox(parent=self.deficiencias)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.def_multipla.setFont(font)
        self.def_multipla.setObjectName("def_multipla")
        self.verticalLayout_7.addWidget(self.def_multipla)
        self.def_down = QtWidgets.QCheckBox(parent=self.deficiencias)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.def_down.setFont(font)
        self.def_down.setObjectName("def_down")
        self.verticalLayout_7.addWidget(self.def_down)
        self.def_surdez = QtWidgets.QCheckBox(parent=self.deficiencias)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.def_surdez.setFont(font)
        self.def_surdez.setObjectName("def_surdez")
        self.verticalLayout_7.addWidget(self.def_surdez)
        self.def_surdocegueira = QtWidgets.QCheckBox(parent=self.deficiencias)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
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
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.CEP.setFont(font)
        self.CEP.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);\n"
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
        self.CEP.setValidator(validador)
        self.complemento = QtWidgets.QLineEdit(parent=self.caixa_endereco)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.complemento.setFont(font)
        self.complemento.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);\n"
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
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.numero.setFont(font)
        self.numero.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);\n"
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
        self.numero.setValidator(validador)
        self.municipio_endereco = QtWidgets.QLineEdit(parent=self.caixa_endereco)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.municipio_endereco.setFont(font)
        self.municipio_endereco.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);\n"
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
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.bairro_endereco.setFont(font)
        self.bairro_endereco.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);\n"
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
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.uf_endereco.setFont(font)
        self.uf_endereco.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);\n"
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
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.endereco.setFont(font)
        self.endereco.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);\n"
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
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sel_zona.setFont(font)
        self.sel_zona.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);\n"
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
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.telefone.setFont(font)
        self.telefone.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);\n"
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
        self.telefone.setValidator(validador)
        self.email = QtWidgets.QLineEdit(parent=self.caixa_endereco)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.email.setFont(font)
        self.email.setStyleSheet("background-color: rgb(243, 230, 213); \n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color:  rgb(45, 84, 60);\n"
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
        self.confirm_button = QtWidgets.QPushButton(parent=self.centralwidget,  clicked = lambda: self.matricula_aluno())
        self.confirm_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        
        self.confirm_button.setGeometry(QtCore.QRect(606, 20, 136, 71))
        self.confirm_button.setStyleSheet("background-color: rgb(45, 84, 60);\n"
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
        self.cancel_button = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda: self.voltar_menu())
        self.cancel_button.setGeometry(QtCore.QRect(460, 20, 136, 71))
        self.cancel_button.setStyleSheet("background-color: rgb(243, 230, 213);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font:bold 20px \"Inter Black\" ;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"color: rgb(45, 84, 60);")
        self.cancel_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))        
        self.cancel_button.setObjectName("cancel_button")
        
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 392, 75))
        self.label.setStyleSheet("font: 57 40pt \"Trend Slab Four\";\n"
"color:rgb(45, 84, 60)\n"
"")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Matrícula do Aluno"))
        self.id_aluno.setTitle(_translate("MainWindow", "Identificação do Aluno"))
        self.nome_aluno.setPlaceholderText(_translate("MainWindow", "Nome do Aluno"))
        self.codigo_NIS.setPlaceholderText(_translate("MainWindow", "NIS"))
        self.label_id_racial.setText(_translate("MainWindow", "Identidade Racial"))
        self.sel_id_racial.setItemText(0, _translate("MainWindow", "1- Branca"))
        self.sel_id_racial.setItemText(1, _translate("MainWindow", "2- Preta"))
        self.sel_id_racial.setItemText(2, _translate("MainWindow", "3- Parda"))
        self.sel_id_racial.setItemText(3, _translate("MainWindow", "4- Amarela"))
        self.sel_id_racial.setItemText(4, _translate("MainWindow", "5- Indígena"))
        self.sel_id_racial.setItemText(5, _translate("MainWindow", "N/A"))
        self.label_sexo.setText(_translate("MainWindow", "Sexo*"))
        self.sel_sexo.setItemText(0, _translate("MainWindow", "Masculino"))
        self.sel_sexo.setItemText(1, _translate("MainWindow", "Feminino"))
        self.sel_sexo.setItemText(2, _translate("MainWindow", "N/A"))
        self.nascimento_uf.setPlaceholderText(_translate("MainWindow", "UF*"))
        self.nascimento_municipio.setPlaceholderText(_translate("MainWindow", "Município de nascimento*"))
        self.label_certidao_civil.setText(_translate("MainWindow", "Tipo da Certidão Civil"))
        self.sel_certidao_civil.setItemText(0, _translate("MainWindow", "Nascimento"))
        self.sel_certidao_civil.setItemText(1, _translate("MainWindow", "Casamento"))
        self.sel_certidao_civil.setItemText(2, _translate("MainWindow", "N/A"))
        self.certidao_antiga.setTitle(_translate("MainWindow", "Certidão Modelo Antigo"))
        self.numero_termo.setPlaceholderText(_translate("MainWindow", "Numero Termo"))
        self.livro.setPlaceholderText(_translate("MainWindow", "Livro"))
        self.folha.setPlaceholderText(_translate("MainWindow", "Folha"))
        self.label_data_exp_certidao.setText(_translate("MainWindow", "Data de Expedição"))
        self.data_expedicao.setDisplayFormat(_translate("MainWindow", "d/M/yyyy"))
        self.certidao_nova.setTitle(_translate("MainWindow", "Certidão Modelo Novo"))
        self.numero_registro_civil.setPlaceholderText(_translate("MainWindow", "Numero de Matrícula (Registro Civil)"))
        self.info_documentos.setTitle(_translate("MainWindow", "Informações Documentadas"))
        self.label_data_exp_info_doc.setText(_translate("MainWindow", "Data de Expedição"))
        self.cpf_aluno.setPlaceholderText(_translate("MainWindow", "Cadastro de Pessoa Física (CPF)"))
        self.documento_tipo.setPlaceholderText(_translate("MainWindow", "Identidade, Documento Estrangerio ou Passaporte"))
        self.data_exp.setDisplayFormat(_translate("MainWindow", "d/M/yyyy"))
        self.cartorio_nome.setPlaceholderText(_translate("MainWindow", "Nome do Cartório"))
        self.cartorio_uf.setPlaceholderText(_translate("MainWindow", "UF - Cartório"))
        self.documento_orgao_emissor.setPlaceholderText(_translate("MainWindow", "Orgão Emissor"))
        self.cartorio_municipio.setPlaceholderText(_translate("MainWindow", "Município do Cartório"))
        self.InformacoesdeMatricula.setTitle(_translate("MainWindow", "Informações de Matricula"))
        self.nome_escola.setPlaceholderText(_translate("MainWindow", "Nome da Escola"))
        self.serie_label.setText(_translate("MainWindow", "Série*"))
        self.procedencia_label.setText(_translate("MainWindow", "Codigo de Procedência*"))
        self.bolsa_familia.setText(_translate("MainWindow", "Programa Bolsa Família"))

        self.sel_serie.setItemText(0, _translate("MainWindow", "01. Jardim I"))
        self.sel_serie.setItemText(1, _translate("MainWindow", "02. Jardim II"))
        self.sel_serie.setItemText(2, _translate("MainWindow", "03. 1° Ano"))
        self.sel_serie.setItemText(3, _translate("MainWindow", "04. 2° Ano"))
        self.sel_serie.setItemText(4, _translate("MainWindow", "05. 3° Ano"))
        self.sel_serie.setItemText(5, _translate("MainWindow", "06. 4° Ano"))
        self.sel_serie.setItemText(6, _translate("MainWindow", "07. 5° Ano"))

        self.turno_label.setText(_translate("MainWindow", "Turno*"))
        self.transporte.setText(_translate("MainWindow", "Transporte Escolar"))
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
        self.codigo_inep.setPlaceholderText(_translate("MainWindow", "Codigo Senso Inep*"))
        self.codigo_turma.setPlaceholderText(_translate("MainWindow", "Codigo Turma*"))
        self.data_ingresso_escola.setDisplayFormat(_translate("MainWindow", "d/M/yyyy"))
        self.ano_letivo.setPlaceholderText(_translate("MainWindow", "Ano Letivo*"))
        self.data_matricula.setDisplayFormat(_translate("MainWindow", "d/M/yyyy"))
        self.matricula.setPlaceholderText(_translate("MainWindow", "Matricula*"))
        self.data_matricula_label.setText(_translate("MainWindow", "Data de Matricula"))
        self.data_ingresso_label.setText(_translate("MainWindow", "Data de Ingresso"))
        self.groupBox.setTitle(_translate("MainWindow", "Dados dos Pais/Responsáveis"))
        self.nome_pai.setPlaceholderText(_translate("MainWindow", "Nome do Pai"))
        self.nome_mae.setPlaceholderText(_translate("MainWindow", "Nome da Mãe"))
        self.transtorno_global_desenvolvimento.setTitle(_translate("MainWindow", "Transtorno Global do Desenvolvimento"))
        self.def_autismo.setText(_translate("MainWindow", "Autismo"))
        self.def_rett.setText(_translate("MainWindow", "Sindrome de Rett"))
        self.def_asperger.setText(_translate("MainWindow", "Sindrome de Asperger"))
        self.def_TDI.setText(_translate("MainWindow", "Transtorno desintegrativo da infância"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Altas Habilidades / Superdotação"))
        self.altas_habilidades.setText(_translate("MainWindow", "Altas Habilidades / Superdotação"))
        self.deficiencias.setTitle(_translate("MainWindow", "Deficiências"))
        self.def_baixa_visao.setText(_translate("MainWindow", "Baixa Visão"))
        self.def_cegueira.setText(_translate("MainWindow", "Cegueira"))
        self.def_auditiva.setText(_translate("MainWindow", "Deficiência Auditiva"))
        self.def_intelectual.setText(_translate("MainWindow", "Deficiência Intelectual"))
        self.def_fisica.setText(_translate("MainWindow", "Deficiência Física"))
        self.def_multipla.setText(_translate("MainWindow", "Deficiência Múltipla"))
        self.def_down.setText(_translate("MainWindow", "Sindrome de Down"))
        self.def_surdez.setText(_translate("MainWindow", "Surdez"))
        self.def_surdocegueira.setText(_translate("MainWindow", "Surdocegueira"))
        self.caixa_endereco.setTitle(_translate("MainWindow", "Endereço"))
        self.CEP.setPlaceholderText(_translate("MainWindow", "CEP*"))
        self.complemento.setPlaceholderText(_translate("MainWindow", "Complemento"))
        self.lab_zona.setText(_translate("MainWindow", "Zona*"))
        self.numero.setPlaceholderText(_translate("MainWindow", "N°"))
        self.municipio_endereco.setPlaceholderText(_translate("MainWindow", "Município*"))
        self.bairro_endereco.setPlaceholderText(_translate("MainWindow", "Bairro"))
        self.uf_endereco.setPlaceholderText(_translate("MainWindow", "UF"))
        self.endereco.setPlaceholderText(_translate("MainWindow", "Endereço"))
        self.sel_zona.setItemText(0, _translate("MainWindow", "Rural"))
        self.sel_zona.setItemText(1, _translate("MainWindow", "Urbana"))
        self.sel_zona.setItemText(2, _translate("MainWindow", "N/A"))
        self.telefone.setPlaceholderText(_translate("MainWindow", "Telefone"))
        self.email.setPlaceholderText(_translate("MainWindow", "Email"))
        self.confirm_button.setText(_translate("MainWindow", "Confirmar"))
        self.cancel_button.setText(_translate("MainWindow", "Cancelar"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">MATRICULA</p></body></html>"))

    def matricula_aluno(self):
        conn = connect_db()
        if conn is not None:
                try:
                        conn.autocommit = False # inicio auto

                        # Insere a identificação do aluno
                        id_aluno = self.insert_identificacao_aluno_ui(conn)
                        print("ID Aluno:", id_aluno)
                        if id_aluno is None:
                                raise Exception("Falha ao inserir identificação do aluno")

                        # Insere as informações de saúde
                        if not self.insert_saude_ui(conn, id_aluno):
                                raise Exception("Falha ao inserir informações de saúde")

                        # Insere o endereço
                        if not self.insert_endereco_ui(conn, id_aluno):
                                raise Exception("Falha ao inserir endereço")

                        # Insere os dados dos pais ou responsáveis
                        if not self.insert_dados_pais_ui(conn, id_aluno):
                                raise Exception("Falha ao inserir dados dos pais ou responsáveis")

                        # Insere as informações da matrícula
                        if not self.insert_informacoes_matricula_ui(conn, id_aluno):
                                raise Exception("Falha ao inserir informações da matrícula")

                        # Insere a certidão
                        if not self.insert_certidao_ui(conn, id_aluno):
                                raise Exception("Falha ao inserir certidão")

                        # Se tudo estiver certo
                        conn.commit()

                        self.salvar_excel()

                        self.exibir_mensagem_sucesso()
                        print("Todos os dados foram inseridos com sucesso.")

                except Exception as e:
                        print(f"Erro durante a matrícula: {e}")

                        conn.rollback()

                        # controle de erro para os ids dos alunos
                        try:
                                if id_aluno is not None:
                                        with conn.cursor() as cur:
                                                cur.execute("DELETE FROM public.saude WHERE id_aluno = %s", (id_aluno,))
                                                cur.execute("DELETE FROM public.endereco WHERE id_aluno = %s", (id_aluno,))
                                                cur.execute("DELETE FROM public.dados_pais_responsavel WHERE id_aluno = %s", (id_aluno,))
                                                cur.execute("DELETE FROM public.informacoes_matricula WHERE id_aluno = %s", (id_aluno,))
                                                cur.execute("DELETE FROM public.certidao WHERE id_aluno = %s", (id_aluno,))
                                                cur.execute("DELETE FROM public.identificacao_aluno WHERE id_aluno = %s", (id_aluno,))
                                                cur.execute("DELETE FROM public.certidao WHERE id_aluno = %s", (id_aluno,))

                                                conn.commit()
                                                print(f"Aluno com ID {id_aluno} foi removido.")
                        except Exception as delete_error:
                                print(f"Erro ao tentar remover o aluno com ID {id_aluno}: {delete_error}")

                        self.exibir_mensagem_erro(str(e))

                finally:
                        conn.close()

        else:
                print("Não foi possível conectar ao banco de dados.")

    def insert_identificacao_aluno_ui(self, conn):
        try:
                nome_aluno = self.nome_aluno.text()
                codigo_NIS = self.codigo_NIS.text()
                raca_aluno = self.sel_id_racial.currentText()
                sexo_aluno = self.sel_sexo.currentText()
                nascimento_uf = self.nascimento_uf.text()
                nascimento_municipio = self.nascimento_municipio.text()
                cartorio_uf = self.cartorio_uf.text()
                nome_cartorio = self.cartorio_nome.text()
                cartorio_municipio = self.cartorio_municipio.text()
                data_exp_identidade = self.data_exp.date().toString("yyyy-MM-dd")
                orgao_emissor = self.documento_orgao_emissor.text()
                uf_identidade = self.nascimento_uf.text()
                cpf = self.cpf_aluno.text()
                info_documentos = self.documento_tipo.text()

                # Novos campos
                data_nascimento = self.data_nascimento.date().toString("yyyy-MM-dd")
                tipo_nascimento = self.tipo_nascimento.text()
                nacionalidade = self.nacionalidade.text()
                codigo_INEP = self.codigo_INEP.text()

                if len(cpf) != 11:
                        QMessageBox(QMessageBox.Icon.Warning, "Erro", "CPF INVÁLIDO", QMessageBox.StandardButton.Ok).exec()
                        return False  # Aqui pode ser a fonte do erro se n rolar alterar para `return None`.
                
                if not all([nome_aluno, raca_aluno, sexo_aluno, nascimento_uf, nascimento_municipio, data_exp_identidade, orgao_emissor, uf_identidade, cpf, data_nascimento, codigo_INEP]):
                        QMessageBox(QMessageBox.Icon.Warning, "Erro", "Alguns campos do Identificação do Aluno estão vazios", QMessageBox.StandardButton.Ok).exec()
                        return False  # Aqui tbm pode ser a fonte do erro se n rolar alterar para `return None`.

                id_aluno = insert_identificacao_aluno(conn, codigo_NIS, nome_aluno, sexo_aluno, nascimento_uf, nascimento_municipio,
                                              cartorio_uf, nome_cartorio, info_documentos, data_exp_identidade,
                                              orgao_emissor, uf_identidade, cpf, raca_aluno, cartorio_municipio,
                                              data_nascimento, tipo_nascimento, nacionalidade, codigo_INEP)
                
                return id_aluno 

        except Exception as e:
                print(f"Erro ao inserir identificação do aluno: {e}")
                return None

    def insert_saude_ui(self, conn, id_aluno):
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

                resultado = insert_saude(conn, id_aluno, autismo, rett, asperger, transtorno_desintegrativo,
                                 baixa_visao, cegueira, auditiva, intelectual, fisica,
                                 multipla, sindrome_down, surdez, surdocegueira, altas_habilidades)

                return True if resultado else False
        except Exception as e:
                print(f"Erro ao inserir informações de saúde: {e}")
                return False

    def insert_endereco_ui(self, conn, id_aluno):
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

                resultado = insert_endereco(conn, id_aluno, endereco, complemento, numero_endereco, municipio, bairro, cep, zona, telefone, email, uf)
                return True if resultado else False
        except Exception as e:
                print(f"Erro ao inserir endereço: {e}")
                return False

    def insert_dados_pais_ui(self, conn, id_aluno):
        try:
                nome_pai = self.nome_pai.text()
                nome_mae = self.nome_mae.text()
                responsavel = self.responsavel.text()

                if not nome_mae:
                        QMessageBox(QMessageBox.Icon.Warning, "Erro", "O campo nome da mãe está vazio", QMessageBox.StandardButton.Ok).exec()
                        return False
                if not responsavel:
                        QMessageBox(QMessageBox.Icon.Warning, "Erro", "O campo Responsável está vazio", QMessageBox.StandardButton.Ok).exec()
                        return False

                resultado = insert_dados_pais_responsavel(conn, id_aluno, nome_mae, nome_pai, responsavel)
                return True if resultado else False
        except Exception as e:
                print(f"Erro ao inserir dados dos pais ou responsáveis: {e}")
                return False

    def insert_informacoes_matricula_ui(self, conn, id_aluno):
        try:
                nome_escola = self.nome_escola.text()
                codigo_turma = self.codigo_turma.text()
                data_matricula = self.data_matricula.text()
                codigo_inep = self.codigo_inep.text()
                matricula = self.matricula.text()
                data_ingresso_escola = self.data_ingresso_escola.text()
                turno = self.sel_turno.currentText()
                serie = self.sel_serie.currentText() 
                codigo_procedencia = self.sel_procedencia.currentText()
                programa_bolsa_familia = self.bolsa_familia.isChecked()  
                transporte_escolar = self.transporte.isChecked()
                ano_letivo = self.ano_letivo.text()

                # Novos Campos
                codigo_aluno = self.codigo_aluno.text()
                documento_pendente = self.checkbox_documento_pendente.isChecked()

                if not all([nome_escola, codigo_turma, data_matricula, codigo_inep, matricula, data_ingresso_escola,
                        turno, serie, codigo_procedencia, ano_letivo, codigo_aluno]):
                        QMessageBox(QMessageBox.Icon.Warning, "Erro", "Alguns campos das Informações da Matrícula estão vazios", QMessageBox.StandardButton.Ok).exec()
                        return False

                if checa_matricula(matricula):
                        QMessageBox(QMessageBox.Icon.Warning, "Erro", "Matrícula já cadastrada", QMessageBox.StandardButton.Ok).exec()
                        return False

                resultado = insert_informacoes_matricula(conn, id_aluno, nome_escola, codigo_inep, data_ingresso_escola, matricula, data_matricula, codigo_turma, programa_bolsa_familia, transporte_escolar, turno, serie, codigo_procedencia, ano_letivo, codigo_aluno, documento_pendente)
                
                return True if resultado else False
        
        except Exception as e:
                print(f"Erro ao inserir informações da matrícula: {e}")
                return False

    def insert_certidao_ui(self, conn, id_aluno):
        try:
                num_matricula_registro_civil = self.numero_registro_civil.text()  
                num_termo = self.numero_termo.text()
                livro = self.livro.text()
                folha = self.folha.text()
                data_expedicao_certidao = self.data_expedicao.date().toString("yyyy-MM-dd")

                resultado = insert_certidao(conn, id_aluno, num_matricula_registro_civil, num_termo, livro, folha, data_expedicao_certidao)
                return True if resultado else False
        except Exception as e:
                print(f"Erro ao inserir certidão: {e}")
                return False

    def bool_para_sim_nao(self,valor):
        return "SIM" if valor else "NÃO"

    def salvar_excel(self):
        nome_arquivo = 'base_dados_alunos.xlsx'

        informacoes_aluno = {
            "MATRÍCULA": self.matricula.text(),
            "NOME ALUNO": self.nome_aluno.text(),
            "NIS": self.codigo_NIS.text(),
            "COD INEP": self.codigo_INEP.text(),
            "RAÇA ALUNO": self.sel_id_racial.currentText(),
            "DATA DE NASCIMENTO": self.data_nascimento.date().toString("yyyy-MM-dd"),
            "TIPO DE NASCIMENTO": self.tipo_nascimento.text(),
            "SEXO": self.sel_sexo.currentText(),
            "UF": self.nascimento_uf.text(),
            "NACIONALIDADE" : self.nacionalidade.text(),
            "MUNICÍPIO": self.nascimento_municipio.text(),
            "UF CARTÓRIO": self.cartorio_uf.text(),
            "NOME CARTÓRIO": self.cartorio_nome.text(),
            "MUNICÍPIO CARTÓRIO": self.cartorio_municipio.text(),
            "DATA EXP IDENTIDADE": self.data_expedicao.date().toString("yyyy-MM-dd"),
            "ÓRGÃO EMISSOR": self.documento_orgao_emissor.text(),
            "UF IDENTIDADE": self.nascimento_uf.text(),
            "CPF": self.cpf_aluno.text(),
            "AUTISMO": self.def_autismo.isChecked(),
            "RETT": self.def_rett.isChecked(),
            "ASPERGER": self.def_asperger.isChecked(),
            "TRANSTORNO DESINTEGRATIVO": self.def_TDI.isChecked(),
            "BAIXA VISÃO": self.def_baixa_visao.isChecked(),
            "CEGUEIRA": self.def_cegueira.isChecked(),
            "AUDITIVA": self.def_auditiva.isChecked(),
            "INTELECTUAL": self.def_intelectual.isChecked(),
            "FÍSICA": self.def_fisica.isChecked(),
            "MÚLTIPLA": self.def_multipla.isChecked(),
            "SÍNDROME DE DOWN": self.def_down.isChecked(),
            "SURDEZ": self.def_surdez.isChecked(),
            "SURDO E CEGO": self.def_surdocegueira.isChecked(),
            "ALTAS HABILIDADES": self.altas_habilidades.isChecked(),
            "ENDEREÇO": self.endereco.text(),
            "COMPLEMENTO": self.complemento.text(),
            "NÚMERO ENDEREÇO": self.numero.text(),
            "MUNICÍPIO": self.municipio_endereco.text(),
            "BAIRRO": self.bairro_endereco.text(),
            "CEP": self.CEP.text(),
            "ZONA": self.sel_zona.currentText(),
            "TELEFONE": self.telefone.text(),
            "EMAIL": self.email.text(),
            "UF": self.uf_endereco.text(),
            "NOME PAI": self.nome_pai.text(),
            "NOME MÃE": self.nome_mae.text(),
            "RESPONSÁVEL" : self.responsavel.text(),
            "NOME ESCOLA": self.nome_escola.text(),
            "CÓDIGO ALUNO": self.codigo_aluno.text(),
            "CÓDIGO TURMA": self.codigo_turma.text(),
            "DATA MATRÍCULA": self.data_matricula.text(),
            "COD INEP": self.codigo_inep.text(),
            "DATA INGRESSO ESCOLA": self.data_ingresso_escola.text(),
            "TURNO": self.sel_turno.currentText(),
            "SÉRIE": self.sel_serie.currentText(),
            "CÓDIGO PROCEDÊNCIA": self.sel_procedencia.currentText(),
            "BOLSA FAMÍLIA": self.bolsa_familia.isChecked(),
            "TRANSPORTE ESCOLAR": self.transporte.isChecked(),
            "DOCUMENTO PENDENTE": self.checkbox_documento_pendente.isChecked(),
            "TIPO DE CERTIDÃO": self.sel_certidao_civil.currentText(),
            "MATRÍCULA REGISTRO CIVIL": self.numero_registro_civil.text(),
            "NUM TERMO": self.numero_termo.text(),
            "LIVRO": self.livro.text(),
            "FOLHA": self.folha.text(),
            "DATA EXP CERTIDÃO": self.data_expedicao.date().toString("yyyy-MM-dd")
        }

        for chave, valor in informacoes_aluno.items():
            if isinstance(valor, bool):
                informacoes_aluno[chave] = self.bool_para_sim_nao(valor)

        adicionar_dados_excel(nome_arquivo, informacoes_aluno)

    def exibir_mensagem_sucesso(self):
        mensagem = QMessageBox()
        mensagem.setIcon(QMessageBox.Icon.Information)
        mensagem.setText(f"Aluno matriculado com sucesso!: {self.nome_aluno.text()}")
        mensagem.setWindowTitle("Confirmação de matricula")
        mensagem.setStandardButtons(QMessageBox.StandardButton.Ok)
        mensagem.exec()
    
    def exibir_mensagem_erro(self, erro="Ocorreu um erro ao matricular o aluno, tente novamente."):
        mensagem = QMessageBox()
        mensagem.setIcon(QMessageBox.Icon.Warning)
        mensagem.setText(f"Erro: {erro}")  # Mostra a mensagem de erro específica
        mensagem.setWindowTitle("Confirmação de matrícula - ERRO")
        mensagem.setStandardButtons(QMessageBox.StandardButton.Ok)
        mensagem.exec()

    def voltar_menu(self):
        from home_screen import Ui_MainWindow
        self.tela_principal = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()           
        self.ui.setupUi(self.tela_principal)           
        self.tela_principal.show()                     
        QtWidgets.QApplication.instance().activeWindow().close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UI_MatriculaWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
