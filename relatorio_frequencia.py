from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from database import listar_frequencias_por_turma_ano
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
        self.turma_selection = QtWidgets.QComboBox(parent=self.centralwidget)
        self.turma_selection.setGeometry(QtCore.QRect(70, 50, 291, 41))
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
        self.turma_selection.addItem("01. Berçário I")
        self.turma_selection.addItem("02. Berçário II")
        self.turma_selection.addItem("03. Maternal I")
        self.turma_selection.addItem("04. Maternal II")
        self.turma_selection.addItem("05. Jardim I")
        self.turma_selection.addItem("06. Jardim II")
        self.turma_selection.addItem("07. Ciclo I - 1° Ano")
        self.turma_selection.addItem("08. Ciclo I - 2° Ano")
        self.turma_selection.addItem("09. Ciclo I - 3° Ano")
        self.turma_selection.addItem("10. Ciclo II - 1° Ano")
        self.turma_selection.addItem("11. Ciclo II - 2° Ano")
        self.turma_selection.addItem("12. Ciclo III - 1° Ano")
        self.turma_selection.addItem("13. Ciclo III - 2° Ano")
        self.turma_selection.addItem("14. Ciclo IV - 1° Ano")
        self.turma_selection.addItem("15. Ciclo IV - 2° Ano")
        self.turma_selection.addItem("16. 1ª Totalidade")
        self.turma_selection.addItem("17.  2ª Totalidade")
        self.turma_selection.addItem("18.  3ª Etapa")
        self.turma_selection.addItem("19.  4ª Etapa")
        self.turma_selection.addItem("20. 1° Ano")
        self.turma_selection.addItem("21. 2° Ano")
        self.turma_selection.addItem("22. 3° Ano")
        self.turma_selection.addItem("23. 4° Ano")
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
        self.tableWidget.setColumnCount(13)
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
        self.tableWidget.setItem(0, 0, item)
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
        self.refresh_button = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda: self.atualizar_tabela())
        self.refresh_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))        
        self.refresh_button.setGeometry(QtCore.QRect(220, 90, 136, 41))
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
        frequencias = listar_frequencias_por_turma_ano(codigo_serie, ano_selecionado)
        #print("Dados retornados:", frequencias)
        self.tableWidget.setRowCount(len(frequencias))
        self.tableWidget.setColumnCount(14) 

        headers = ["Nome Aluno", "Matrícula"] + [f"{mes}" for mes in ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "St", "Out", "Nov", "Dez"]]
        self.tableWidget.setHorizontalHeaderLabels(headers)

        for row, freq in enumerate(frequencias):
                # freq[0] = nome do aluno, freq[1] = matrícula, freq[2:] = faltas por mês
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(freq[0])))  # nome
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(freq[1])))  # matricula
                for col in range(2, 14):
                        if col-2 < len(freq[2:]):
                                self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str(freq[col])))
                        else:
                                self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem("N/A"))

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

    #endregion