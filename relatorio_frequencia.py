from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from database import * #listar_frequencias_por_turma_ano, porcentagem, obter_id_aluno_por_matricula, obter_frequencias_por_aluno
import csv
import os


class Ui_RelatorioWindow(object):
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
        self.title_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(400, 0, 513, 161))
        font = QtGui.QFont()
        font.setFamily("Trend Slab Four")
        font.setPointSize(48)
        self.title_label.setFont(font)
        #self.title_label.setStyleSheet("color: rgb(44, 46, 89);\n"
#"text-stroke: 4px black;")
        MainWindow.setWindowIcon(QIcon('imagens\\3.png'))
        MainWindow.setStyleSheet("background-color: rgb(243, 230, 213);")
        self.title_label.setWordWrap(True)
        self.title_label.setObjectName("title_label")

        # turma
        self.turma_selection = QtWidgets.QComboBox(parent=self.centralwidget)
        self.turma_selection.setGeometry(QtCore.QRect(70, 10, 291, 41))
        self.turma_selection.setStyleSheet("background-color:rgb(243, 230, 213);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font:bold 20px  \"Inter Black\" ;\n"
"padding: 6px;\n"
"color:  rgb(44, 46, 89);\n"
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

        # botao confirmar
        self.confirm_button = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda: self.voltar_menu())
        self.confirm_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.confirm_button.setGeometry(QtCore.QRect(1076, 20, 136, 71))
        self.confirm_button.setStyleSheet("background-color:rgb(44, 46, 89);\n"
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

        #table
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(60, 160, 1161, 531))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet("background-color: rgb(243, 230, 213);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font:bold 12px\"Inter Medium\" ;\n"
"min-width: 1em;\n"
"color: rgb(44, 46, 89);\n"
"")
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(14)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        for row in range(self.tableWidget.rowCount()):
                self.tableWidget.setRowHeight(row, 30)

        for col in range(self.tableWidget.columnCount()):
                self.tableWidget.setColumnWidth(col, 70)

        #data
        self.date_selection = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.date_selection.setGeometry(QtCore.QRect(70, 90, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Inter Black")
        font.setPointSize(1)
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
"min-width: 5em;\n"
"padding: 6px;\n"
"color: rgb(44, 46, 89);\n"
"alternate-background-color:rgb(243, 230, 213);")
        self.date_selection.setWrapping(False)
        self.date_selection.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.date_selection.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.date_selection.setCalendarPopup(False)
        self.date_selection.setDate(QtCore.QDate(2024, 1, 1))
        self.date_selection.setObjectName("date_selection")
        self.date_selection.setGeometry(QtCore.QRect(70, 110, 136, 41))

        # att
        self.refresh_button = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda: self.atualizar_tabela())
        self.refresh_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))        
        self.refresh_button.setGeometry(QtCore.QRect(240, 110, 136, 41))
        self.refresh_button.setStyleSheet("background-color: rgb(44, 46, 89);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font:bold 20px \"Inter Black\" ;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"color: rgb(243, 230, 213);")
        self.refresh_button.setObjectName("refresh_button")
        self.cancel_button = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda: self.voltar_menu())
        self.refresh_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))  

        # mes
        self.month_selection = QtWidgets.QComboBox(parent=self.centralwidget)
        self.month_selection.setGeometry(QtCore.QRect(70, 60, 151, 41))
        self.month_selection.setStyleSheet("background-color:rgb(243, 230, 213);\n"
                                           "border-style: outset;\n"
                                           "border-width: 2px;\n"
                                           "border-radius: 10px;\n"
                                           "border-color: black;\n"
                                           "font:bold 20px  \"Inter Black\" ;\n"
                                           "color: rgb(44, 46, 89);")
        self.month_selection.setObjectName("month_selection")
        self.month_selection.addItems(["Anual", "Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"])

        # cancelar
        self.cancel_button.setGeometry(QtCore.QRect(930, 20, 136, 71))
        self.cancel_button.setStyleSheet("background-color: rgb(243, 230, 213);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font:bold 20px \"Inter Black\" ;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"color: rgb(44, 46, 89);")
        self.cancel_button.setObjectName("cancel_button")
        self.cancel_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.refresh_button_2 = QtWidgets.QPushButton(parent=self.centralwidget, clicked=self.exportar_para_csv)
        self.refresh_button_2.setGeometry(QtCore.QRect(930, 100, 281, 41))
        self.refresh_button_2.setStyleSheet("background-color: rgb(44, 46, 89);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font:bold 20px \"Inter Black\" ;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"color: rgb(243, 230, 213);")
        self.refresh_button_2.setObjectName("refresh_button_2")
        self.refresh_button_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.atualizar_tabela()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Relatorio das Frequências"))
        self.title_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Relatorio de classe</p></body></html>"))

        self.confirm_button.setText(_translate("MainWindow", "Confirmar"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "NOME"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "JAN"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "FEV"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "MAR"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "ABR"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "MAI"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "JUN"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "JUL"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "AGO"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "SET"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "OUT"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "NOV"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "DEZ"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Porcentagem de Faltas"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.date_selection.setDisplayFormat(_translate("MainWindow", "yyyy"))
        self.refresh_button.setText(_translate("MainWindow", "Atualizar"))
        self.cancel_button.setText(_translate("MainWindow", "Cancelar"))
        self.refresh_button_2.setText(_translate("MainWindow", "EXPORTAR"))

#region FUNÇÕES

    def voltar_menu(self):
        from home_screen import Ui_MainWindow
        self.tela_principal = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()           
        self.ui.setupUi(self.tela_principal)           
        self.tela_principal.show()                     
        QtWidgets.QApplication.instance().activeWindow().close()

    def atualizar_tabela(self):
        codigo_serie = self.turma_selection.currentText()
        ano_selecionado = self.date_selection.date().year()
        mes_selecionado = self.month_selection.currentText()

        frequencias = listar_frequencias_por_turma_ano(codigo_serie, ano_selecionado)
        
        if mes_selecionado == "Anual":
                self.tableWidget.setRowCount(len(frequencias))
                self.tableWidget.setColumnCount(14) 

                headers = ["Aluno", "Matrícula"] + [f"{mes}" for mes in ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]] + ["Total", "%"]
                self.tableWidget.setHorizontalHeaderLabels(headers)

                for row, freq in enumerate(frequencias):
                        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(freq[0])))  # nome
                        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(freq[1])))  # matricula

                        total_faltas = 0
                        for mes in range(1, 13):
                                faltas_mes = freq[mes + 1] if len(freq) > mes + 1 else 0
                                self.tableWidget.setItem(row, mes + 1, QtWidgets.QTableWidgetItem(str(faltas_mes)))
                                total_faltas += faltas_mes
                        
                        self.tableWidget.setItem(row, 13, QtWidgets.QTableWidgetItem(str(total_faltas)))
                
                        matricula = self.tableWidget.item(row, 1).text()
                        porcentagem = self.porcentagem_mensal(ano_selecionado, matricula)
                        self.tableWidget.setItem(row, 14, QtWidgets.QTableWidgetItem(porcentagem[0]))

        else:
                mes_selecionado_index = self.month_selection.currentIndex()

                self.tableWidget.setRowCount(len(frequencias))
                self.tableWidget.setColumnCount(4)

                headers = ["Aluno", "Matrícula", "Faltas", "%"]
                self.tableWidget.setHorizontalHeaderLabels(headers)

                for row, freq in enumerate(frequencias):
                        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(freq[0])))  # nome
                        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(freq[1])))  # matricula

                        matricula = self.tableWidget.item(row, 1).text()
                        faltas_mes = freq[mes_selecionado_index ] if len(freq) > mes_selecionado_index + 1 else 0
                        porcentagem = self.porcentagem_mensal(ano_selecionado, matricula)[mes_selecionado_index - 1]

                        self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(faltas_mes)))
                        self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(porcentagem))


    def porcentagem_mensal(self, ano_selecionado, matricula):
        id_aluno = obter_id_aluno_por_matricula(matricula)
        lista_porcentagens = []

        for i in range(1, 13):
            frequencia = obter_frequencias_por_aluno(id_aluno, ano_selecionado, i)
            lista_porcentagens.append(f"{porcentagem(frequencia, i)}%")
        return lista_porcentagens

    def exportar_para_csv(self):
          nome_arquivo = 'base_relatório.csv'
          caminho_arquivo = os.path.join(os.getcwd(),nome_arquivo)
          headers = ["Nome Aluno", "Matricula"] + [f"{mes}" for mes in ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]]

          try:
                modo = 'a' if os.path.exists(caminho_arquivo) else 'w'
                with open(caminho_arquivo, modo, newline='',encoding='utf-8') as arquivo:
                      escritor = csv.writer(arquivo)
                      if modo == 'w':
                            escritor.writerow(headers)
                      for row in range(self.tableWidget.rowCount()):
                            linha = []
                            for col in range(self.tableWidget.columnCount()):
                                  item = self.tableWidget.item(row, col)
                                  if item is not None:
                                   linha.append(item.text())
                                  else:
                                        linha.append('')
                            escritor.writerow(linha)
                self.mostrar_mensagem_sucesso('Dados exportados com sucesso para CSV')
          except Exception as e:
                self.mostrar_mensagem_erro(f"Erro ao exportar dados: {e}")
     
    def mostrar_mensagem_sucesso(self, mensagem):
                alerta = QMessageBox()
                alerta.setWindowTitle("Sucesso")
                alerta.setText(mensagem)
                alerta.setIcon(QMessageBox.Icon.Information)
                alerta.setStandardButtons(QMessageBox.StandardButton.Ok)
                alerta.exec()

    def mostrar_mensagem_erro(self, mensagem):
        alerta = QMessageBox()
        alerta.setWindowTitle("Erro")
        alerta.setText(mensagem)
        alerta.setIcon(QMessageBox.Icon.Critical)
        alerta.setStandardButtons(QMessageBox.StandardButton.Ok)
        alerta.exec()
