CREATE TABLE identificacao_aluno (
    id_aluno SERIAL PRIMARY KEY,
    NIS INT,
    nome_aluno VARCHAR(100),
    sexo VARCHAR(10),
    UF VARCHAR(2),
    local_nascimento_municipio VARCHAR(100),
    uf_cartorio VARCHAR(2),
    municipio_cartorio VARCHAR(100),
    nome_cartorio VARCHAR(100),
    identidade_docEstrangeiro_passaporte VARCHAR(100),
    data_expedicao_identidade DATE,
    orgao_emissor VARCHAR(2),
    uf_identidade VARCHAR(2),
    cpf VARCHAR(11),
	aluno_raca varchar(50)
);

CREATE TABLE certidao (
	id_certidao SERIAL PRIMARY KEY,
    id_aluno INT,
    num_matricula_registro_civil VARCHAR(100), -- certidão nova
    num_termo VARCHAR(50), -- certidão antiga
    livro VARCHAR(10), -- certidão antiga
    folha VARCHAR(10), -- certidão antiga
    data_expedicao_certidao DATE,
    FOREIGN KEY (id_aluno) REFERENCES identificacao_aluno(id_aluno)
);

CREATE TABLE saude (
    id_saude SERIAL PRIMARY KEY,
    id_aluno INT,
    autismo BOOLEAN DEFAULT FALSE,
    rett BOOLEAN DEFAULT FALSE,
    asperger BOOLEAN DEFAULT FALSE,
    transtorno_desintegrativo BOOLEAN DEFAULT FALSE,
    baixa_visao BOOLEAN DEFAULT FALSE,
    cegueira BOOLEAN DEFAULT FALSE,
    auditiva BOOLEAN DEFAULT FALSE,
    intelectual BOOLEAN DEFAULT FALSE,
    fisica BOOLEAN DEFAULT FALSE,
    multipla BOOLEAN DEFAULT FALSE,
    sindrome_down BOOLEAN DEFAULT FALSE,
    surdez BOOLEAN DEFAULT FALSE,
    surdocegueira BOOLEAN DEFAULT FALSE,
    altas_habilidades BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (id_aluno) REFERENCES identificacao_aluno(id_aluno)
);

CREATE TABLE endereco (
	id_endereco SERIAL PRIMARY KEY,
    id_aluno INT,
    endereco VARCHAR(255),
    complemento VARCHAR(200),
    numero_endereco INT,
    municipio VARCHAR(100),
    bairro VARCHAR(100),
    cep INT,
    zona VARCHAR(6),
    telefone BIGINT,
    email VARCHAR(255),
	uf varchar(2),
    FOREIGN KEY (id_aluno) REFERENCES identificacao_aluno(id_aluno)
);

CREATE TABLE dados_pais_responsavel (
	id_dados_pais_responsavel SERIAL PRIMARY KEY,
    id_aluno INT,
    nome_mae VARCHAR(200),
    nome_pai VARCHAR(200),
    FOREIGN KEY (id_aluno) REFERENCES identificacao_aluno(id_aluno)
);

CREATE TABLE informacoes_matricula (
	id_informacoes_matricula SERIAL PRIMARY KEY,
    id_aluno INT,
    nome_escola VARCHAR(255),
    cod_censo_inep INT,
    data_ingresso_escola DATE,
    matricula INT,
    data_matricula DATE,
    codigo_turma INT,
    turno varchar(15),
    codigo_serie varchar(255),
    codigo_procedencia varchar(255),
    participa_programa BOOLEAN,
    transporte_escolar BOOLEAN,
    FOREIGN KEY (id_aluno) REFERENCES identificacao_aluno(id_aluno)
);

ALTER TABLE informacoes_matricula ADD COLUMN ano_letivo INT;

CREATE TABLE frequencia (
    id_frequencia SERIAL PRIMARY KEY,
    id_aluno INT,
	nome_aluno VARCHAR(100),
	matricula INT,
    data_presenca DATE,
    presenca CHAR(1),
    justificativa VARCHAR(255),
	observacoes VARCHAR(255)
);

CREATE TABLE usuarios (
    id_usuario SERIAL PRIMARY KEY,
    login VARCHAR(255) UNIQUE,
    senha VARCHAR(255),
    nome_professor VARCHAR(255)
);

CREATE TABLE solicitacao_matricula (
    id_aluno INT,
    nome_aluno VARCHAR(200),
    matricula INT,
    codigo_turma INT,
    turno CHAR(1),
    codigo_serie INT,
    ano_letivo INT,
    documentos_pendentes BOOLEAN,
    FOREIGN KEY (id_aluno) REFERENCES identificacao_aluno(id_aluno)
);

CREATE TABLE controle (
    total_dias INT,
    mes INT
);

INSERT INTO controle (total_dias, mes) VALUES (0, 0);
