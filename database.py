from dotenv import load_dotenv
import psycopg2
import os
from datetime import date

load_dotenv()


def connect_db():
    try:
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            port=os.getenv('DB_PORT')
        )
        return conn
    except psycopg2.OperationalError as e:
        print(f"Falha ao conectar ao banco de dados: {e}")
    except Exception as e:
        print(f"Um erro inesperado ocorreu: {e}")


def last_id():
    conn = connect_db()
    try:
        cur = conn.cursor()

        query = "SELECT id_aluno FROM identificacao_aluno ORDER BY id_aluno DESC LIMIT 1;"
        cur.execute(query)

        result = cur.fetchone()
        last_id_aluno = result[0] if result is not None else 0

        cur.close()
        conn.close()

        return last_id_aluno

    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None


def checa_matricula(matricula):
    query = """
        SELECT matricula
        FROM informacoes_matricula
        WHERE matricula = %s
    """
    parametros = (matricula,)
    resultado = executar_query_matricula(query, parametros)
    return bool(resultado)


def porcentagem(presencas, mes):

    if mes == 13:
        print(f'total dias = {obter_total_dias()}')
        print(f'presenças = {presencas}')
        porcent = (int(presencas) * 100) / obter_total_dias()
        return porcent
    elif obter_total_dias_mes(mes) != 0 and obter_total_dias_mes(mes) < 13:
        porcent = (int(presencas)*100)/obter_total_dias_mes(mes)
        return porcent
    elif obter_total_dias_mes(mes) == 0:
        porcent = 0
        return porcent
    else:
        print("total dias não é um numero")

#region EXECUTAR
def executar_query(conn, query, parametros):
    try:
        with conn.cursor() as cur:
            cur.execute(query, parametros)
            return True
    except psycopg2.Error as e:
        print(f"Falha ao executar query: {str(e)}")
        return False


def executar_query_realiza_freq(query, parametros):
    conn = connect_db()
    if conn is not None:
        try:
            with conn.cursor() as cur:
                cur.execute(query, parametros)
                conn.commit()
                return "Dados inseridos com sucesso"
        except psycopg2.Error as e:
            conn.rollback()
            return f"Falha ao inserir dados: {str(e)}"
        finally:
            conn.close()
    else:
        return "Conexão com o banco de dados não foi estabelecida."


def executar_query_freq(query, parametros):
    conn = connect_db()
    try:
        cur = conn.cursor()
        cur.execute(query, parametros)
        if query.strip().upper().startswith('SELECT'):
            resultados = cur.fetchall() 
            return resultados
        else:
            conn.commit()
            return cur.rowcount
    except Exception as e:
        print(f"Erro ao executar query: {e}")
        conn.rollback()
        return []
    finally:
        cur.close()
        conn.close()


def executar_query_matricula(query, parametros):
    conn = connect_db()
    try:
        cur = conn.cursor()
        cur.execute(query, parametros)
        if query.strip().upper().startswith('SELECT'):
            return cur.fetchall()
        else:
            conn.commit()
            return cur.rowcount
    except Exception as e:
        print(f"Erro ao executar query: {e}")
        conn.rollback()
        return None
    finally:
        cur.close()
        conn.close()

def executar_query_diarioClasse(query, parametros):
    conn = connect_db()
    try:
        with conn.cursor() as cur:
            cur.execute(query, (parametros,))
            result = cur.fetchall()
            return result
    except psycopg2.Error as e:
        print(f"Falha ao executar query: {str(e)}")
        return None
    finally:
        conn.close()
    
def atualizar_diario_classe(data):
    query = """
    SELECT 
        string_agg(justificativa, ', ') AS justificativas,
        string_agg(observacoes, ', ') AS observacoes 
    FROM 
        frequencia 
    WHERE 
        data_presenca = %s
    """

    resultados = executar_query_diarioClasse(query, (data,))

    if resultados and resultados[0]:
        justificativas, observacoes = resultados[0]
        return f"Justificativas: {justificativas}\nObservações: {observacoes}"
    else:
        return "Nenhum dado encontrado para a data selecionada."


#endregion

#region INSERTS
def insert_cadastro_sistema(login,nome_prof,senha):

    #print(login)
    #print(nome_prof)
    #print(senha)

    query = """INSERT INTO usuarios (login, nome_professor, senha) VALUES (%s, %s, %s)"""

    parametros = (login, nome_prof, senha)
    return executar_query_freq(query, parametros)


def insert_identificacao_aluno(conn, nis, nome_aluno, sexo_aluno, nascimento_uf, nascimento_municipio,
                               cartorio_uf, nome_cartorio, id_doc_passaporte, data_exp_identidade,
                               orgao_emissor, uf_identidade, cpf, raca_aluno, municipio_cartorio):
    query = """
        INSERT INTO identificacao_aluno 
        (NIS, nome_aluno, sexo, UF, local_nascimento_municipio,
         uf_cartorio, nome_cartorio, identidade_docEstrangeiro_passaporte, data_expedicao_identidade,
         orgao_emissor, uf_identidade, cpf, aluno_raca, municipio_cartorio)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id_aluno;
    """
    parametros = (nis, nome_aluno, sexo_aluno, nascimento_uf, nascimento_municipio,
                  cartorio_uf, nome_cartorio, id_doc_passaporte, data_exp_identidade,
                  orgao_emissor, uf_identidade, cpf, raca_aluno, municipio_cartorio)
    
    cur = conn.cursor()
    cur.execute(query, parametros)
    id_aluno = cur.fetchone()[0]
    cur.close()
    return id_aluno


def insert_certidao(conn, id_aluno, num_matricula_registro_civil, num_termo, livro, folha, data_expedicao_certidao):
    query = """
        INSERT INTO certidao 
        (id_aluno, num_matricula_registro_civil, num_termo, livro, folha, data_expedicao_certidao)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    parametros = (id_aluno, num_matricula_registro_civil, num_termo, livro, folha, data_expedicao_certidao)
    return executar_query(conn, query, parametros)


def insert_saude(conn, id_aluno, autismo, rett, asperger, transtorno_desintegrativo,
                 baixa_visao, cegueira, auditiva, intelectual, fisica,
                 multipla, sindrome_down, surdez, surdocegueira, altas_habilidades):
    query = """
        INSERT INTO saude (id_aluno, autismo, rett, asperger, transtorno_desintegrativo,
                           baixa_visao, cegueira, auditiva, intelectual, fisica,
                           multipla, sindrome_down, surdez, surdocegueira, altas_habilidades)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    parametros = (id_aluno, autismo, rett, asperger, transtorno_desintegrativo,
                  baixa_visao, cegueira, auditiva, intelectual, fisica,
                  multipla, sindrome_down, surdez, surdocegueira, altas_habilidades)
    """
    print("Debugging insert_saude:", id_aluno, autismo, rett, asperger, transtorno_desintegrativo,
      baixa_visao, cegueira, auditiva, intelectual, fisica,
      multipla, sindrome_down, surdez, surdocegueira, altas_habilidades)
    """
    return executar_query(conn, query, parametros)


def insert_endereco(conn, id_aluno, endereco, complemento, numero_endereco, municipio, bairro, cep, zona, telefone, email, uf):
    query = """
        INSERT INTO endereco (id_aluno, endereco, complemento, numero_endereco, municipio, bairro, cep, zona, telefone, email, uf)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    parametros = (id_aluno, endereco, complemento, numero_endereco, municipio, bairro, cep, zona, telefone, email, uf)
    return executar_query(conn, query, parametros)


def insert_dados_pais_responsavel(conn, id_aluno, nome_mae, nome_pai):
    query = """
        INSERT INTO dados_pais_responsavel 
        (id_aluno, nome_mae, nome_pai)
        VALUES (%s, %s, %s)
    """
    parametros = (id_aluno, nome_mae, nome_pai)
    return executar_query(conn, query, parametros)


def insert_informacoes_matricula(conn, id_aluno, nome_escola, cod_censo, data_ingresso_escola, matricula, data_matricula,
                                 codigo_turma, participa_programa, transporte_escolar, turno, codigo_serie, codigo_procedencia, ano_letivo):
    query = """
        INSERT INTO informacoes_matricula
        (id_aluno, nome_escola, cod_censo_inep, data_ingresso_escola, matricula, data_matricula, codigo_turma, participa_programa, transporte_escolar, turno, codigo_serie, codigo_procedencia, ano_letivo)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    parametros = (id_aluno, nome_escola, cod_censo, data_ingresso_escola, matricula, data_matricula,
                  codigo_turma, participa_programa, transporte_escolar, turno, codigo_serie, codigo_procedencia, ano_letivo)
    
    return executar_query(conn, query, parametros)

def insert_solicitacao_matricula(nome_aluno, matricula, codigo_turma, turno, codigo_serie, ano_letivo, documentos_pendentes):
    query = """
        INSERT INTO solicitacao_matricula
        (id_aluno, nome_aluno, matricula, codigo_turma, turno, codigo_serie, ano_letivo, documentos_pendentes)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    parametros = (last_id(), nome_aluno, matricula, codigo_turma, turno, codigo_serie, ano_letivo, documentos_pendentes)
    return executar_query_freq(query, parametros)

def insert_controle(ano):
    dia_zero = 0
    query = """
           INSERT INTO controle
           (ano, letivos_jan, letivos_fev, letivos_mar, letivos_abr, letivos_mai, letivos_jun, letivos_jul, letivos_ago, letivos_set, letivos_out, letivos_nov, letivos_dez)
           VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
       """
    parametros = (ano, dia_zero, dia_zero, dia_zero, dia_zero, dia_zero, dia_zero, dia_zero, dia_zero, dia_zero, dia_zero, dia_zero, dia_zero)
    return executar_query_freq(query, parametros)

#endregion

#region UPDATES

def update_controle(total_dias,mes,ano):

    if ano == int(obter_ano()):
        #print("ano igual")
        if mes == 1:
            #print(f"mes {mes}, dias letivos {total_dias}")
            query = "UPDATE controle SET letivos_jan = %s WHERE ano = %s"
            parametros = (total_dias, ano)
            return executar_query_freq(query, parametros)

        elif mes == 2:
            #print(f"mes {mes}, dias letivos {total_dias}")
            query = "UPDATE controle SET letivos_fev = %s WHERE ano = %s"
            parametros = (total_dias, ano)
            return executar_query_freq(query, parametros)

        elif mes == 3:
            #print(f"mes {mes}, dias letivos {total_dias}")
            query = "UPDATE controle SET letivos_mar = %s WHERE ano = %s"
            parametros = (total_dias, ano)
            return executar_query_freq(query, parametros)

        elif mes == 4:
            #print(f"mes {mes}, dias letivos {total_dias}")
            query = "UPDATE controle SET letivos_abr = %s WHERE ano = %s"
            parametros = (total_dias, ano)
            return executar_query_freq(query, parametros)

        elif mes == 5:
            #print(f"mes {mes}, dias letivos {total_dias}")
            query = "UPDATE controle SET letivos_mai = %s WHERE ano = %s"
            parametros = (total_dias, ano)
            return executar_query_freq(query, parametros)

        elif mes == 6:
            #print(f"mes {mes}, dias letivos {total_dias}")
            query = "UPDATE controle SET letivos_jun = %s WHERE ano = %s"
            parametros = (total_dias, ano)
            return executar_query_freq(query, parametros)

        elif mes == 7:
            #print(f"mes {mes}, dias letivos {total_dias}")
            query = "UPDATE controle SET letivos_jul = %s WHERE ano = %s"
            parametros = (total_dias, ano)
            return executar_query_freq(query, parametros)

        elif mes == 8:
            #print(f"mes {mes}, dias letivos {total_dias}")
            query = "UPDATE controle SET letivos_ago = %s WHERE ano = %s"
            parametros = (total_dias, ano)
            return executar_query_freq(query, parametros)

        elif mes == 9:
            #print(f"mes {mes}, dias letivos {total_dias}")
            query = "UPDATE controle SET letivos_set = %s WHERE ano = %s"
            parametros = (total_dias, ano)
            return executar_query_freq(query, parametros)

        elif mes == 10:
            #print(f"mes {mes}, dias letivos {total_dias}")
            query = "UPDATE controle SET letivos_out = %s WHERE ano = %s"
            parametros = (total_dias, ano)
            return executar_query_freq(query, parametros)

        elif mes == 11:
            #print(f"mes {mes}, dias letivos {total_dias}")
            query = "UPDATE controle SET letivos_nov = %s WHERE ano = %s"
            parametros = (total_dias, ano)
            return executar_query_freq(query, parametros)

        elif mes == 12:
            #print(f"mes {mes}, dias letivos {total_dias}")
            query = "UPDATE controle SET letivos_dez = %s WHERE ano = %s"
            parametros = (total_dias, ano)
            return executar_query_freq(query, parametros)

        else:
            print("Valor inválido")

    else:
        print("ano diferente")
        total_dias = 1
        insert_controle(ano)
        update_controle(total_dias, mes, obter_ano())


def update_identificacao_aluno(nis, nome_aluno, sexo_aluno, nascimento_uf, nascimento_municipio,cartorio_uf, nome_cartorio, cartorio_municipio, data_exp_identidade,orgao_emissor, uf_identidade, cpf, raca_aluno, id_aluno):

    query = """
        UPDATE identificacao_aluno 
        SET NIS = %s, nome_aluno = %s, sexo = %s, UF = %s, local_nascimento_municipio = %s, uf_cartorio = %s, nome_cartorio = %s, data_expedicao_identidade = %s, orgao_emissor = %s, uf_identidade = %s, cpf = %s, aluno_raca = %s, municipio_cartorio = %s
        WHERE id_aluno = %s
    """
    parametros = (nis, nome_aluno, sexo_aluno, nascimento_uf, nascimento_municipio,
              cartorio_uf, nome_cartorio, data_exp_identidade,
              orgao_emissor, uf_identidade, cpf, raca_aluno, cartorio_municipio,id_aluno)
    return executar_query_freq(query, parametros)

def update_certidao(num_matricula_registro_civil, num_termo, livro, folha, data_expedicao_certidao, id_aluno):

    query = """
        UPDATE certidao 
        SET num_matricula_registro_civil = %s, num_termo = %s, livro = %s, folha = %s, data_expedicao_certidao = %s
        WHERE id_aluno = %s
    """
    parametros = (num_matricula_registro_civil, num_termo, livro, folha, data_expedicao_certidao, id_aluno)
    return executar_query_freq(query, parametros)


def update_informacoes_matricula(nome_escola, cod_censo, data_ingresso_escola, matricula, data_matricula, codigo_turma, participa_programa, transporte_escolar, turno, codigo_serie, codigo_procedencia,id_aluno):
    query = """
        UPDATE informacoes_matricula
        SET nome_escola = %s, cod_censo_inep = %s, data_ingresso_escola = %s, matricula = %s, data_matricula = %s, codigo_turma = %s, participa_programa = %s, transporte_escolar = %s, turno = %s, codigo_serie = %s, codigo_procedencia = %s
        WHERE id_aluno = %s
    """
    parametros = (nome_escola, cod_censo, data_ingresso_escola, matricula, data_matricula,
                  codigo_turma, participa_programa, transporte_escolar, turno, codigo_serie, codigo_procedencia, id_aluno)

    return executar_query_freq(query, parametros)

def update_dados_pais_responsavel(nome_mae, nome_pai, id_aluno):
    query = """
        UPDATE dados_pais_responsavel 
        SET nome_mae = %s, nome_pai = %s
        WHERE id_aluno = %s
    """
    parametros = (nome_mae, nome_pai, id_aluno)
    return executar_query_freq(query, parametros)

def update_saude(autismo, rett, asperger, transtorno_desintegrativo, baixa_visao, cegueira, auditiva, intelectual, fisica, multipla, sindrome_down, surdez, surdocegueira, altas_habilidades, id_aluno):
    query = """
        UPDATE saude 
        SET autismo = %s, rett = %s, asperger = %s, transtorno_desintegrativo = %s, baixa_visao = %s, cegueira = %s, auditiva = %s, intelectual = %s, fisica = %s, multipla = %s, sindrome_down = %s, surdez = %s, surdocegueira = %s, altas_habilidades = %s
        WHERE id_aluno = %s
    """
    parametros = (autismo, rett, asperger, transtorno_desintegrativo, baixa_visao, cegueira, auditiva, intelectual, fisica, multipla, sindrome_down, surdez, surdocegueira, altas_habilidades, id_aluno)
    return executar_query_freq(query, parametros)

def update_endereco(endereco, complemento, numero_endereco, municipio, bairro, cep, zona, telefone, email, uf, id_aluno):

    query = """
        UPDATE endereco 
        SET endereco = %s, complemento = %s, numero_endereco = %s, municipio = %s, bairro = %s, cep = %s, telefone = %s, email = %s, uf = %s, zona = %s
        WHERE id_aluno = %s
    """
    parametros = (endereco, complemento, numero_endereco, municipio, bairro, cep, telefone, email, uf, zona, id_aluno)
    return executar_query_freq(query, parametros)

#endregion

def listar_alunos_por_turma(codigo_turma):
    query = """
        SELECT ia.nome_aluno, im.matricula
        FROM informacoes_matricula im
        JOIN identificacao_aluno ia ON im.id_aluno = ia.id_aluno
        WHERE im.codigo_serie = %s;
    """
    parametros = (codigo_turma,)
    
    alunos = executar_query_freq(query, parametros)
    
    return alunos

def listar_frequencias_por_turma_ano(codigo_serie, ano):
    query = """
    SELECT ia.nome_aluno, im.matricula,
       COALESCE(SUM(CASE WHEN EXTRACT(MONTH FROM f.data_presenca) = 1 AND EXTRACT(YEAR FROM f.data_presenca) = %s AND f.presenca = 'A' THEN 1 ELSE 0 END), 0) AS Jan,
       COALESCE(SUM(CASE WHEN EXTRACT(MONTH FROM f.data_presenca) = 2 AND EXTRACT(YEAR FROM f.data_presenca) = %s AND f.presenca = 'A' THEN 1 ELSE 0 END), 0) AS Feb,
       COALESCE(SUM(CASE WHEN EXTRACT(MONTH FROM f.data_presenca) = 3 AND EXTRACT(YEAR FROM f.data_presenca) = %s AND f.presenca = 'A' THEN 1 ELSE 0 END), 0) AS Mar,
       COALESCE(SUM(CASE WHEN EXTRACT(MONTH FROM f.data_presenca) = 4 AND EXTRACT(YEAR FROM f.data_presenca) = %s AND f.presenca = 'A' THEN 1 ELSE 0 END), 0) AS Apr,
       COALESCE(SUM(CASE WHEN EXTRACT(MONTH FROM f.data_presenca) = 5 AND EXTRACT(YEAR FROM f.data_presenca) = %s AND f.presenca = 'A' THEN 1 ELSE 0 END), 0) AS May,
       COALESCE(SUM(CASE WHEN EXTRACT(MONTH FROM f.data_presenca) = 6 AND EXTRACT(YEAR FROM f.data_presenca) = %s AND f.presenca = 'A' THEN 1 ELSE 0 END), 0) AS Jun,
       COALESCE(SUM(CASE WHEN EXTRACT(MONTH FROM f.data_presenca) = 7 AND EXTRACT(YEAR FROM f.data_presenca) = %s AND f.presenca = 'A' THEN 1 ELSE 0 END), 0) AS Jul,
       COALESCE(SUM(CASE WHEN EXTRACT(MONTH FROM f.data_presenca) = 8 AND EXTRACT(YEAR FROM f.data_presenca) = %s AND f.presenca = 'A' THEN 1 ELSE 0 END), 0) AS Aug,
       COALESCE(SUM(CASE WHEN EXTRACT(MONTH FROM f.data_presenca) = 9 AND EXTRACT(YEAR FROM f.data_presenca) = %s AND f.presenca = 'A' THEN 1 ELSE 0 END), 0) AS Sep,
       COALESCE(SUM(CASE WHEN EXTRACT(MONTH FROM f.data_presenca) = 10 AND EXTRACT(YEAR FROM f.data_presenca) = %s AND f.presenca = 'A' THEN 1 ELSE 0 END), 0) AS Oct,
       COALESCE(SUM(CASE WHEN EXTRACT(MONTH FROM f.data_presenca) = 11 AND EXTRACT(YEAR FROM f.data_presenca) = %s AND f.presenca = 'A' THEN 1 ELSE 0 END), 0) AS Nov,
       COALESCE(SUM(CASE WHEN EXTRACT(MONTH FROM f.data_presenca) = 12 AND EXTRACT(YEAR FROM f.data_presenca) = %s AND f.presenca = 'A' THEN 1 ELSE 0 END), 0) AS Dec
    FROM frequencia f
    JOIN identificacao_aluno ia ON f.id_aluno = ia.id_aluno
    JOIN informacoes_matricula im ON ia.id_aluno = im.id_aluno
    WHERE im.codigo_serie = %s AND EXTRACT(YEAR FROM f.data_presenca) = %s
    GROUP BY ia.nome_aluno, im.matricula;
    """
    parametros = (ano, ano, ano, ano, ano, ano, ano, ano, ano, ano, ano, ano, codigo_serie, ano)
    resultados = executar_query_freq(query, parametros)
    return resultados

def realiza_freq(id_aluno, nome_aluno, matricula, data_presenca, presenca, justificativa, observacoes):
    query= """
        INSERT INTO frequencia (id_aluno, nome_aluno, matricula, data_presenca, presenca, justificativa, observacoes)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
    """
    parametros = (id_aluno, nome_aluno, matricula, data_presenca, presenca, justificativa, observacoes)
    executar_query_realiza_freq(query, parametros)

def obter_frequencias_por_turma(codigo_serie):
    query = """
        SELECT ia.nome_aluno, f.data_presenca, f.presenca, im.codigo_serie
        FROM frequencia f
        INNER JOIN identificacao_aluno ia ON f.id_aluno = ia.id_aluno
        INNER JOIN informacoes_matricula im ON ia.id_aluno = im.id_aluno
        WHERE im.codigo_serie = %s;
    """

    parametros = (codigo_serie,)
    
    alunos = executar_query_freq(query, parametros)

    return alunos

def obter_frequencias_por_aluno(id_aluno, ano, mes):
    query =  """
        SELECT COUNT(*) 
        FROM frequencia 
        WHERE id_aluno = %s
        AND EXTRACT(YEAR FROM data_presenca) = %s
        AND EXTRACT(MONTH FROM data_presenca) = %s
        AND presenca = 'P'
    """

    parametros = (id_aluno, ano, mes)

    frequencia = executar_query_freq(query, parametros)

    #print(f"id aluno {id_aluno}, ano {ano}, mes {mes}, dias letivos {frequencia[0][0]}")

    return frequencia[0][0]

def obter_id_aluno_por_matricula(matricula):
    query = "SELECT id_aluno FROM informacoes_matricula WHERE matricula = %s;"
    parametros = (matricula,)
    conn = connect_db()
    try:
        cur = conn.cursor()
        cur.execute(query, parametros)
        result = cur.fetchone()
        if result:
            return result[0]
        else:
            return None
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def obter_total_dias_mes(mes):
    query = "SELECT * FROM controle"
    conn = connect_db()

    try:
        cur = conn.cursor()
        cur.execute(query)
        result = cur.fetchone()
        if result:
            total_dias_atual = result[mes]
            return total_dias_atual
        else:
            return None

    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def obter_total_dias():
    query = "SELECT * FROM controle"
    conn = connect_db()

    try:
        cur = conn.cursor()
        cur.execute(query)
        result = cur.fetchone()

        if result:
            total_dias = sum(result[1:13])
            return total_dias
        else:
            return None

    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def obter_ano():
    query = "SELECT ano FROM controle ORDER BY ano DESC LIMIT 1"
    conn = connect_db()

    try:
        cur = conn.cursor()
        cur.execute(query)
        result = cur.fetchone()
        if result:
            ano = result[0]
            return ano
        else:
            return None

    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def verifica_login(login):
    conn = connect_db()

    if conn is not None:
        try:
            with conn.cursor() as cur:
                query = "SELECT * FROM usuarios WHERE login = %s"
                cur.execute(query, (login,))
                dados = cur.fetchall()
                return len(dados) > 0
            
        except psycopg2.Error as e:
             print(f"Database error: {str(e)}")
             return False
        finally:
            conn.close()
    else:
        print("Conexão com o banco de dados não foi estabelecida.")
        return False

def realiza_login(login, senha):
    conn = connect_db()

    if conn is not None:
        try:
            with conn.cursor() as cur:
                query = "SELECT * FROM usuarios WHERE login = %s AND senha = %s"
                cur.execute(query, (login, senha))
                dados = cur.fetchall()

                return bool(dados)
            
        except psycopg2.Error as e:
             print(f"Database error: {str(e)}")
             return False
        finally:
            conn.close()
    else:
        print("Conexão com o banco de dados não foi estabelecida.")
        return False

def busca_nome_usuario(login):
    conn = connect_db()
    cur = conn.cursor()
    query = "SELECT nome_professor FROM usuarios WHERE login = %s"
    cur.execute(query, (login,))

    resultado = cur.fetchone()
    cur.close()
    conn.close()

    if resultado:
        return resultado[0] 
    else:
        return None