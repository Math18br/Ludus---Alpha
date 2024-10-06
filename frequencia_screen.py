from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QIcon
from database import *
from criar_excel import adicionar_dados_excel
from datetime import date


class UI_FrequenciaWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(1280, 720)
        MainWindow.setMaximumSize(1280, 720)
        MainWindow.setWindowFlags(MainWindow.windowFlags() & ~Qt.WindowType.WindowMaximizeButtonHint)
        MainWindow.setStyleSheet("background-color: rgb(243, 230, 213);\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setWindowIcon(QIcon('imagens\\1.png'))
        MainWindow.setStyleSheet("background-color: rgb(243, 230, 213);")
        
        self.lista_freq = QtWidgets.QListWidget(parent=self.centralwidget)
        self.lista_freq.setGeometry(QtCore.QRect(40, 150, 550, 530))
        self.lista_freq.setStyleSheet("background-color: rgb(243, 230, 213);\n"
                                        "border-style: outset;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 10px;\n"
                                        "border-color: black;\n"
                                        "font:bold 24px\"Inter Medium\" ;\n"
                                        "min-width: 5em;\n"
                                        "padding: 6px;\n"
                                        "color: rgb(131, 3, 2);")
        self.lista_freq.setObjectName("lista_freq")
        
        self.obs_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.obs_label.setGeometry(QtCore.QRect(600, 380, 640, 42))
        font = QtGui.QFont()
        font.setFamily("Trend Slab Four")
        font.setPointSize(48)
        self.obs_label.setFont(font)
        self.obs_label.setStyleSheet("color: rgb(130, 3, 0);")
        self.obs_label.setObjectName("obs_label")
        
        self.obs_text = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.obs_text.setGeometry(QtCore.QRect(600, 428, 640, 252))
        self.obs_text.setStyleSheet("background-color: rgb(243, 230, 213);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font:bold 14px\"Inter Medium\" ;\n"
"padding: 6px;\n"
"color: rgb(131, 3, 2);")
        self.obs_text.setObjectName("obs_text")
        
        self.confirm_button = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda: self.confirmar_frequencia())
        self.confirm_button.setGeometry(QtCore.QRect(1104, 50, 136, 71))
        self.confirm_button.setStyleSheet("background-color: rgb(131, 3, 2);;\n"
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
        self.confirm_button.setText("Confirmar")
        self.confirm_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        
        
        self.cancel_button = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda: self.voltar_menu())
        self.cancel_button.setGeometry(QtCore.QRect(958, 50, 136, 71))
        self.cancel_button.setStyleSheet("background-color: rgb(243, 230, 213);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font:bold 20px \"Inter Black\" ;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"color: rgb(131, 3, 2);")
        self.cancel_button.setObjectName("cancel_button")
        self.cancel_button.setText("Cancelar")
        self.cancel_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        
        self.just_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.just_label.setGeometry(QtCore.QRect(600, 150, 640, 42))
        font = QtGui.QFont()
        font.setFamily("Trend Slab Four")
        font.setPointSize(48)
        self.just_label.setFont(font)
        self.just_label.setStyleSheet("color: rgb(130, 3, 0);")
        self.just_label.setWordWrap(True)
        self.just_label.setObjectName("just_label")
        
        self.just_caixa = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.just_caixa.setGeometry(QtCore.QRect(600, 197, 640, 168))
        self.just_caixa.setStyleSheet("background-color: rgb(243, 230, 213);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font:bold 14px\"Inter Medium\" ;\n"
"QTextBrowser QScrollBar::handle { border-color: 1px outset rgb(131, 3, 2);}"
"padding: 6px;\n"
"color: rgb(131, 3, 2);")
        self.just_caixa.setObjectName("just_caixa")
        
        self.title_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(410, 30, 513, 84))
        font = QtGui.QFont()
        font.setFamily("Trend Slab Four")
        font.setPointSize(48)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("color: rgb(130, 3, 0);")
        self.title_label.setObjectName("title_label")
        self.date_selection = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.date_selection.setDate(date.today())
        self.date_selection.setGeometry(QtCore.QRect(80, 90, 151, 41))
        
        font = QtGui.QFont()        
        font.setFamily("Inter Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.date_selection.setFont(font)
        self.date_selection.setStyleSheet("background-color:rgb(243, 230, 213);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font:bold 20px  \"Inter Black\" ;\n"
"min-width: 2em;\n"
"color: rgb(130, 3, 0);\n"
"alternate-background-color:rgb(243, 230, 213);")
        self.date_selection.setWrapping(False)
        self.date_selection.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.date_selection.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.date_selection.setCalendarPopup(True)
        self.date_selection.setObjectName("date_selection")
        
        self.turma_selection = QtWidgets.QComboBox(parent=self.centralwidget)
        self.turma_selection.setGeometry(QtCore.QRect(80, 40, 291, 41))
        self.turma_selection.setStyleSheet("background-color:rgb(243, 230, 213);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font:bold 20px  \"Inter Black\" ;\n"
"padding: 6px;\n"
"color: rgb(130, 3, 0);\n"
"alternate-background-color:rgb(243, 230, 213);")
        self.turma_selection.setEditable(True)
        self.turma_selection.setObjectName("turma_selection")
        self.turma_selection.addItem("01. Jardim I")
        self.turma_selection.addItem("02. Jardim II")
        self.turma_selection.addItem("03. 1° Ano")
        self.turma_selection.addItem("04. 2° Ano")
        self.turma_selection.addItem("05. 3° Ano")
        self.turma_selection.addItem("06. 4° Ano")
        self.turma_selection.addItem("07. 5° Ano")
        
        self.refresh_button = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda: self.atualizar_lista_de_frequencia())
        self.refresh_button.setGeometry(QtCore.QRect(240, 90, 136, 41))
        self.refresh_button.setStyleSheet("background-color: rgb(131, 3, 2);;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font:bold 20px \"Inter Black\" ;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"color: rgb(243, 230, 213);\n"
"")
        self.refresh_button.setObjectName("refresh_button")
        self.refresh_button.setText("Atualizar")
        self.refresh_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.atualizar_lista_de_frequencia()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Frequência"))
        self.obs_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">observações</span></p></body></html>"))
        self.just_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Justificativa de faltas</span></p></body></html>"))
        self.title_label.setText(_translate("MainWindow", "<html><head/><body><p>frequencia</p></body></html>"))
        self.date_selection.setDisplayFormat(_translate("MainWindow", "d/M/yyyy"))


#region FUNÇÕES

    def atualizar_lista_de_frequencia(self):
        alunos = self.listar_alunos()
        self.listaFreqRefresh(alunos)

    def listar_alunos(self):
         turma = self.turma_selection.currentText()

         resultado = listar_alunos_por_turma(turma)
         return resultado

    def listaFreqRefresh(self, alunos):
        self.lista_freq.clear()
        for aluno in alunos:
                nome_aluno, matricula = aluno
                item = QtWidgets.QListWidgetItem()
                item.setCheckState(QtCore.Qt.CheckState.Unchecked)
                item.setText(f"{matricula} - {nome_aluno}")
                self.lista_freq.addItem(item)

    def confirmar_frequencia(self):
        data_presenca = self.date_selection.date().toString("yyyy-MM-dd")
        mes = self.date_selection.date().month()
        ano = self.date_selection.date().year()
        justificativa = self.just_caixa.toPlainText()
        observacoes = self.obs_text.toPlainText()
        sucesso = True

        for index in range(self.lista_freq.count()):
                item = self.lista_freq.item(index)
                matricula, nome_aluno = item.text().split(' - ')
                id_aluno = obter_id_aluno_por_matricula(matricula)
                total = obter_total_dias_mes(mes)
                if id_aluno:
                        estado_presenca = 'P' if item.checkState() == Qt.CheckState.Checked else 'A'
                        realiza_freq(id_aluno, nome_aluno, matricula, data_presenca, estado_presenca, justificativa, observacoes)

                        informacoes_frequencia = {
                                "MATRÍCULA": matricula,
                                "NOME ALUNO": nome_aluno,
                                "DATA": data_presenca,
                                "PRESSENÇA": estado_presenca,
                                "JUSTIFICATIVA": justificativa,
                                "OBSERVAÇÕES": observacoes
                        }
                        adicionar_dados_excel('base_dados_frequencia.xlsx', informacoes_frequencia)

                        novo_total = total + 1  # Adiciona 1 ao total de dias letivos toda vez que realiza a frequencia
                        print(novo_total)
                        update_controle(novo_total, mes, ano)
                else:
                        sucesso = False
                        print(f"Não foi possível encontrar o ID para a matrícula {matricula}")
        if sucesso:

                self.atualizar_lista_de_frequencia()
                self.exibir_mensagem_sucesso()
        else:
                self.exibir_mensagem_erro()

    def exibir_mensagem_sucesso(self):
        data_presenca = self.date_selection.date().toString("yyyy-MM-dd")
        turma = self.turma_selection.currentText()
        mensagem = QMessageBox()
        mensagem.setIcon(QMessageBox.Icon.Information)
        mensagem.setText(f"Frequência do dia {data_presenca} para a turma {turma} realizado com sucesso!")
        mensagem.setWindowTitle("Confirmação de frequência")
        mensagem.setStandardButtons(QMessageBox.StandardButton.Ok)
        mensagem.exec()
    
    def exibir_mensagem_erro(self):
        mensagem = QMessageBox()
        mensagem.setIcon(QMessageBox.Icon.Information)
        mensagem.setText("Ocorreu um erro ao realizar a frequência, tente novamente.")
        mensagem.setWindowTitle("Confirmação de frequência ERRO")
        mensagem.setStandardButtons(QMessageBox.StandardButton.Ok)
        mensagem.exec()

    def bool_para_sim_nao(self,valor):
        return "SIM" if valor else "NÃO"

    def voltar_menu(self):
        from home_screen import Ui_MainWindow
        self.tela_principal = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()           
        self.ui.setupUi(self.tela_principal)           
        self.tela_principal.show()                     
        QtWidgets.QApplication.instance().activeWindow().close()


    #endregion