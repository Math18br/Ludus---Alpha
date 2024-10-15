from PyQt6.QtCore import Qt
from database import *
from editar_matricula2 import *
from PyQt6.QtGui import QIcon

class Ui_Edit_1_Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(936, 750)
        MainWindow.setMinimumSize(936, 750)
        MainWindow.setMaximumSize(936, 750)
        MainWindow.setWindowFlags(MainWindow.windowFlags() & ~Qt.WindowType.WindowMaximizeButtonHint)
        MainWindow.setWindowIcon(QIcon('imagens\\2.png'))
        MainWindow.setStyleSheet("background-color: rgb(243, 230, 213);\n"
                                 "\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        """
        self.confirm_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.confirm_button.setGeometry(QtCore.QRect(676, 40, 136, 71))
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
        """
        self.cancel_button = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.voltar_menu())
        self.cancel_button.setGeometry(QtCore.QRect(530, 40, 136, 71))
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
        self.title_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(160, 30, 341, 101))
        font = QtGui.QFont()
        font.setFamily("Trend Slab Four")
        font.setPointSize(48)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("color: rgb(203, 132, 0)")
        self.title_label.setObjectName("title_label")
        self.refresh_button = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.atualizar_lista())
        self.refresh_button.setGeometry(QtCore.QRect(560, 150, 136, 41))
        self.refresh_button.setStyleSheet("background-color: rgb(203, 132, 0);\n"
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
        self.refresh_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        
        self.turma_selection = QtWidgets.QComboBox(parent=self.centralwidget)
        self.turma_selection.setGeometry(QtCore.QRect(290, 150, 261, 41))
        self.turma_selection.setStyleSheet("background-color:rgb(243, 230, 213);\n"
                                           "border-style: outset;\n"
                                           "border-width: 2px;\n"
                                           "border-radius: 10px;\n"
                                           "border-color: black;\n"
                                           "font:bold 20px  \"Inter Black\" ;\n"
                                           "padding: 6px;\n"
                                           "color: rgb(203, 132, 0);\n"
                                           "alternate-background-color:rgb(243, 230, 213);")
        self.turma_selection.setEditable(True)
        self.turma_selection.setObjectName("turma_selection")
        self.turma_selection.addItem("")
        self.turma_selection.addItem("")
        self.turma_selection.addItem("")
        self.turma_selection.addItem("")
        self.turma_selection.addItem("")
        self.turma_selection.addItem("")
        self.turma_selection.addItem("")

        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(130, 210, 721, 451))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 719, 449))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lista_alunos = QtWidgets.QListWidget(parent=self.scrollAreaWidgetContents)
        self.lista_alunos.setStyleSheet("color: rgb(203, 132, 0);\n"
                                        "font: 900 18pt \"Inter \";")
        self.lista_alunos.setObjectName("lista_alunos")
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.CheckState.Unchecked)
        self.lista_alunos.addItem(item)
        self.horizontalLayout.addWidget(self.lista_alunos)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.delete_button = QtWidgets.QPushButton(parent=self.centralwidget,clicked=lambda: (self.excluir_aluno()))  # EXCLUIR
        self.delete_button.setGeometry(QtCore.QRect(560, 670, 131, 61))
        self.delete_button.setStyleSheet("background-color: rgb(243, 230, 213);\n"
                                            "border-style: outset;\n"
                                            "border-width: 2px;\n"
                                            "border-radius: 10px;\n"
                                            "border-color: black;\n"
                                            "font:bold 20px \"Inter Black\" ;\n"
                                            "padding: 6px;\n"
                                            "color: rgb(203, 132, 0)")
        self.delete_button.setObjectName("delete_button")
        self.delete_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

        self.edit_button = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.editar_aluno())  # EDITAR
        self.edit_button.setGeometry(QtCore.QRect(710, 670, 136, 61))
        self.edit_button.setStyleSheet("background-color: rgb(203, 132, 0);\n"
                                            "border-style: outset;\n"
                                            "border-width: 2px;\n"
                                            "border-radius: 10px;\n"
                                            "border-color: black;\n"
                                            "font:bold 20px \"Inter Black\" ;\n"
                                            "min-width: 5em;\n"
                                            "padding: 6px;\n"
                                            "color: rgb(243, 230, 213);\n"
                                            "")
        self.edit_button.setObjectName("edit_button")
        self.edit_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Editar Matrícula do Aluno"))
        #self.confirm_button.setText(_translate("MainWindow", "Confirmar"))
        self.cancel_button.setText(_translate("MainWindow", "Cancelar"))
        self.title_label.setText(_translate("MainWindow", "<html><head/><body><p>alunos</p></body></html>"))
        self.refresh_button.setText(_translate("MainWindow", "Atualizar"))
        self.turma_selection.setItemText(0, _translate("MainWindow", "01. Jardim I"))
        self.turma_selection.setItemText(1, _translate("MainWindow", "02. Jardim II"))
        self.turma_selection.setItemText(2, _translate("MainWindow", "03. 1° Ano"))
        self.turma_selection.setItemText(3, _translate("MainWindow", "04. 2° Ano"))
        self.turma_selection.setItemText(4, _translate("MainWindow", "05. 3° Ano"))
        self.turma_selection.setItemText(5, _translate("MainWindow", "06. 4° Ano"))
        self.turma_selection.setItemText(6, _translate("MainWindow", "07. 5° Ano"))

        __sortingEnabled = self.lista_alunos.isSortingEnabled()
        self.lista_alunos.setSortingEnabled(False)
        self.lista_alunos.setSortingEnabled(__sortingEnabled)
        self.delete_button.setToolTip(_translate("MainWindow", "Excluir perfis selecionados"))
        self.delete_button.setText(_translate("MainWindow", "Excluir"))
        self.edit_button.setToolTip(_translate("MainWindow", "Editar perfil selecionado (Max 1)"))
        self.edit_button.setText(_translate("MainWindow", "Editar"))

        self.atualizar_lista()

    def executar_query(self, query, params):
        conn = connect_db()
        try:
            cur = conn.cursor()

            cur.execute(query, params)

        except Exception as e:
            print(f"Erro ao executar query: {e}")
            conn.rollback()
            return []
        finally:
            cur.close()
            conn.close()
            print("apagado")

    def voltar_menu(self):
        from home_screen import Ui_MainWindow
        self.tela_principal = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.tela_principal)
        self.tela_principal.show()
        QtWidgets.QApplication.instance().activeWindow().close()

    def atualizar_lista(self):
        alunos = self.listar_alunos()
        self.listaRefresh(alunos)

    def listar_alunos(self):
        turma = self.turma_selection.currentText()

        resultado = listar_alunos_por_turma(turma)
        return resultado

    def listaRefresh(self, alunos):
        self.lista_alunos.clear()
        for aluno in alunos:
            nome_aluno, matricula = aluno
            item = QtWidgets.QListWidgetItem()
            item.setCheckState(QtCore.Qt.CheckState.Unchecked)
            item.setText(f"{matricula} - {nome_aluno}")
            self.lista_alunos.addItem(item)

    def abrir_tela_editar_2(self):
        self.tela_alunos = QtWidgets.QMainWindow()
        self.ui = Ui_Edit_2_Window()
        self.ui.setupUi(self.tela_alunos)
        self.tela_alunos.show()
        QtWidgets.QApplication.instance().activeWindow().close()

    def armazenar_dados_matricula(self, id):
        conn = connect_db()
        try:
            cur = conn.cursor()

            #region IDENTIFICAÇÃO_ALUNO
            query = """
                SELECT * FROM identificacao_aluno
                WHERE id_aluno = %s
            """
            cur.execute(query, [id])
            tabela = cur.fetchone()

            id_aluno = tabela[0]

            nis = tabela[1]
            nome_aluno = tabela[2]
            sexo = tabela[3]
            uf = tabela[4]
            local_nascimento_municipio = tabela[5]
            uf_cartorio = tabela[6]
            municipio_cartorio = tabela[7]
            nome_cartorio = tabela[8]
            identidade_doc_pass = tabela[9]
            data_expedicao_id = tabela[10]
            orgao_emissor = tabela[11]
            uf_identidade = tabela[12]
            cpf = tabela[13]
            raca = tabela[14]

            data_nasc = tabela[15]
            tipo_nasc = tabela[16]
            nacionalidade = tabela[17]
            codigo_inep = tabela[18]
            #endregion

            #region CERTIDÃO
            query = """
                SELECT * FROM certidao
                WHERE id_aluno = %s
            """
            cur.execute(query, [id])
            tabela = cur.fetchone()

            num_matricula_rc = tabela[2]
            num_termo = tabela[3]
            livro = tabela[4]
            folha = tabela[5]
            data_expedicao_certidao = tabela[6]
            #endregion

            #region INFORMAÇÕES_MATRICULA
            query = """
                SELECT * FROM informacoes_matricula
                WHERE id_aluno = %s
            """
            cur.execute(query, [id])
            tabela = cur.fetchone()

            nome_escola = tabela[2]
            cod_censo = tabela[3]
            data_ingresso_escola = tabela[4]
            matricula = tabela[5]
            data_matricula = tabela[6]
            codigo_turma = tabela[7]
            turno = tabela[8]
            codigo_serie = tabela[9]
            codigo_procedencia = tabela[10]
            participa_programa = tabela[11]
            transporte_escolar = tabela[12]
            ano_letivo = tabela[13]

            codigo_aluno = tabela[14]
            doc_pendente = tabela[15]
            #endregion

            #region DADOS_PAIS_RESPONSAVEL
            query = """
                SELECT * FROM dados_pais_responsavel
                WHERE id_aluno = %s
            """
            cur.execute(query, [id])
            tabela = cur.fetchone()
            nome_mae = tabela[2]
            nome_pai = tabela[3]

            responsavel = tabela[4]

            #endregion

            #region SAUDE
            query = """
                SELECT * FROM saude
                WHERE id_aluno = %s
            """
            cur.execute(query, [id])
            tabela = cur.fetchone()

            autismo = tabela[2]
            rett = tabela[3]
            asperger = tabela[4]
            transtorno_desintegrativo = tabela[5]
            baixa_visao = tabela[6]
            cegueira = tabela[7]
            auditiva = tabela[8]
            intelectual = tabela[9]
            fisica = tabela[10]
            multipla = tabela[11]
            sindrome_down = tabela[12]
            surdez = tabela[13]
            surdocegueira = tabela[14]
            altas_habilidades = tabela[15]
            #endregion

            #region ENDERECO
            query = """
                SELECT * FROM endereco
                WHERE id_aluno = %s
            """
            cur.execute(query, [id])
            tabela = cur.fetchone()

            endereco = tabela[2]
            complemento = tabela[3]
            num_endereco = tabela[4]
            municipio_endereco = tabela[5]
            bairro = tabela[6]
            cep = tabela[7]
            zona = tabela[8]
            telefone = tabela[9]
            email = tabela[10]
            uf_endereco = tabela[11]
            #endregion

            with open('dados_editar.pkl', 'wb') as arquivo:
                #region IDENTIFICAÇÃO_ALUNO
                pickle.dump(id_aluno, arquivo)
                pickle.dump(nis, arquivo)
                pickle.dump(nome_aluno, arquivo)
                pickle.dump(sexo, arquivo)
                pickle.dump(uf, arquivo)
                pickle.dump(local_nascimento_municipio, arquivo)
                pickle.dump(uf_cartorio, arquivo)
                pickle.dump(municipio_cartorio, arquivo)
                pickle.dump(nome_cartorio, arquivo)
                pickle.dump(identidade_doc_pass, arquivo)
                pickle.dump(data_expedicao_id, arquivo)
                pickle.dump(orgao_emissor, arquivo)
                pickle.dump(uf_identidade, arquivo)
                pickle.dump(cpf, arquivo)
                pickle.dump(raca, arquivo)

                pickle.dump(data_nasc, arquivo)
                pickle.dump(tipo_nasc, arquivo)
                pickle.dump(nacionalidade, arquivo)
                pickle.dump(codigo_inep, arquivo)
                #endregion

                #region CERTIDÃO
                pickle.dump(num_matricula_rc, arquivo)
                pickle.dump(num_termo, arquivo)
                pickle.dump(livro, arquivo)
                pickle.dump(folha, arquivo)
                pickle.dump(data_expedicao_certidao, arquivo)
                #endregion

                #region INFORMAÇÕES_MATRICULA
                pickle.dump(nome_escola, arquivo)
                pickle.dump(cod_censo, arquivo)
                pickle.dump(data_ingresso_escola, arquivo)
                pickle.dump(matricula, arquivo)
                pickle.dump(data_matricula, arquivo)
                pickle.dump(codigo_turma, arquivo)
                pickle.dump(turno, arquivo)
                pickle.dump(codigo_serie, arquivo)
                pickle.dump(codigo_procedencia, arquivo)
                pickle.dump(participa_programa, arquivo)
                pickle.dump(transporte_escolar, arquivo)
                pickle.dump(ano_letivo, arquivo)

                pickle.dump(codigo_aluno, arquivo)
                pickle.dump(doc_pendente, arquivo)
                #endregion

                #region DADOS PAIS_RESPONSAVEL
                pickle.dump(nome_mae, arquivo)
                pickle.dump(nome_pai, arquivo)

                pickle.dump(responsavel, arquivo)
                #endregion

                #region SAUDE
                pickle.dump(autismo, arquivo)
                pickle.dump(rett, arquivo)
                pickle.dump(asperger, arquivo)
                pickle.dump(transtorno_desintegrativo, arquivo)
                pickle.dump(baixa_visao, arquivo)
                pickle.dump(cegueira, arquivo)
                pickle.dump(auditiva, arquivo)
                pickle.dump(intelectual, arquivo)
                pickle.dump(fisica, arquivo)
                pickle.dump(multipla, arquivo)
                pickle.dump(sindrome_down, arquivo)
                pickle.dump(surdez, arquivo)
                pickle.dump(surdocegueira, arquivo)
                pickle.dump(altas_habilidades, arquivo)
                #endregion

                #region ENDERECO
                pickle.dump(endereco, arquivo)
                pickle.dump(complemento, arquivo)
                pickle.dump(num_endereco, arquivo)
                pickle.dump(municipio_endereco, arquivo)
                pickle.dump(bairro, arquivo)
                pickle.dump(cep, arquivo)
                pickle.dump(zona, arquivo)
                pickle.dump(telefone, arquivo)
                pickle.dump(email, arquivo)
                pickle.dump(uf_endereco, arquivo)
                #endregion

        except Exception as e:
            print(f"Erro ao executar query: {e}")
            conn.rollback()
            return []
        finally:
            cur.close()
            conn.close()

    def editar_aluno(self):
        for index in range(self.lista_alunos.count()):
            item = self.lista_alunos.item(index)

           #print(item)

            if item.checkState() == Qt.CheckState.Checked:

                matricula, nome_aluno = item.text().split(' - ')
                id_aluno = obter_id_aluno_por_matricula(matricula)
                if id_aluno:
                    self.armazenar_dados_matricula(id_aluno)
                    self.abrir_tela_editar_2()
                    break
                else:
                    print(f"Não foi possível encontrar o ID para a matrícula {matricula}")

            else:
                print(f"Nenhum item selecionado")

    def excluir_aluno(self):
        for index in range(self.lista_alunos.count()):
            item = self.lista_alunos.item(index)

            if item.checkState() == Qt.CheckState.Checked:

                #print(item)

                matricula, nome_aluno = item.text().split(' - ')
                id_aluno = obter_id_aluno_por_matricula(matricula)

                if id_aluno:

                    executar_query_freq("DELETE FROM certidao WHERE id_aluno = %s",[id_aluno])
                    executar_query_freq("DELETE FROM dados_pais_responsavel WHERE id_aluno = %s", [id_aluno])
                    executar_query_freq("DELETE FROM endereco WHERE id_aluno = %s", [id_aluno])
                    executar_query_freq("DELETE FROM informacoes_matricula WHERE id_aluno = %s", [id_aluno])
                    executar_query_freq("DELETE FROM saude WHERE id_aluno = %s", [id_aluno])
                    executar_query_freq("DELETE FROM identificacao_aluno WHERE id_aluno = %s", [id_aluno])

                else:
                    print(f"Não foi possível encontrar o ID para a matrícula {matricula}")

            else:
                print(f"Item não selecionado")

        self.atualizar_lista()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Edit_1_Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
