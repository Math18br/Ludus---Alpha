CREATE TABLE identificacao_aluno (
    id_aluno SERIAL PRIMARY KEY,
    NIS VARCHAR(100),
    nome_aluno VARCHAR(100),
    sexo VARCHAR(15),
    UF VARCHAR(2),
    local_nascimento_municipio VARCHAR(100),
    uf_cartorio VARCHAR(2),
    municipio_cartorio VARCHAR(100),
    nome_cartorio VARCHAR(100),
    identidade_docEstrangeiro_passaporte VARCHAR(100),
    data_expedicao_identidade DATE,
    orgao_emissor VARCHAR(2),
    uf_identidade VARCHAR(2),
    cpf VARCHAR(15),
	aluno_raca varchar(50)
);
ALTER TABLE identificacao_aluno
ADD COLUMN cartao_sus VARCHAR(20);

ALTER TABLE identificacao_aluno
ADD COLUMN data_nascimento DATE,
ADD COLUMN tipo_nascimento VARCHAR(100),
ADD COLUMN nacionalidade VARCHAR(100),
ADD COLUMN codigo_INEP VARCHAR(100);

CREATE TABLE certidao (
	id_certidao SERIAL PRIMARY KEY,
    id_aluno INT,
    num_matricula_registro_civil VARCHAR(100), -- certidão nova
    num_termo VARCHAR(50), -- certidão antiga
    livro VARCHAR(50), -- certidão antiga
    folha VARCHAR(50), -- certidão antiga
    data_expedicao_certidao DATE,
    tipo_certidao_civil VARCHAR(200),
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

ALTER TABLE saude
ADD COLUMN vacina VARCHAR(40);

CREATE TABLE endereco (
	id_endereco SERIAL PRIMARY KEY,
    id_aluno INT,
    endereco VARCHAR(255),
    complemento VARCHAR(200),
    numero_endereco VARCHAR(50),
    municipio VARCHAR(100),
    bairro VARCHAR(100),
    cep VARCHAR(50),
    zona VARCHAR(6),
    telefone VARCHAR(50),
    email VARCHAR(255),
	uf VARCHAR(2),
    FOREIGN KEY (id_aluno) REFERENCES identificacao_aluno(id_aluno)
);

CREATE TABLE dados_pais_responsavel (
	id_dados_pais_responsavel SERIAL PRIMARY KEY,
    id_aluno INT,
    nome_mae VARCHAR(200),
    nome_pai VARCHAR(200),
    responsavel VARCHAR(255),
    FOREIGN KEY (id_aluno) REFERENCES identificacao_aluno(id_aluno)
);
ALTER TABLE dados_pais_responsavel
ADD COLUMN cpf_responsavel VARCHAR(15),
ADD COLUMN rg_responsavel VARCHAR(10);

CREATE TABLE informacoes_matricula (
	id_informacoes_matricula SERIAL PRIMARY KEY,
    id_aluno INT,
    nome_escola VARCHAR(255),
    cod_censo_inep VARCHAR(50),
    data_ingresso_escola DATE,
    matricula BIGINT,
    data_matricula DATE,
    codigo_turma VARCHAR(50),
    turno varchar(15),
    codigo_serie varchar(255),
    codigo_procedencia varchar(255),
    participa_programa BOOLEAN,
    transporte_escolar BOOLEAN,
    FOREIGN KEY (id_aluno) REFERENCES identificacao_aluno(id_aluno)
);

ALTER TABLE informacoes_matricula
ADD COLUMN ano_letivo INT;

ALTER TABLE informacoes_matricula
ADD COLUMN codigo_aluno VARCHAR(20),
ADD COLUMN documento_pendente BOOLEAN,
ADD COLUMN transferencia VARCHAR(200),
ADD COLUMN ressalvas VARCHAR(255);

CREATE TABLE frequencia (
    id_frequencia SERIAL PRIMARY KEY,
    id_aluno INT,
	nome_aluno VARCHAR(100),
	matricula BIGINT,
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

CREATE TABLE controle (
	ano INT,
    letivos_jan INT,
	letivos_fev INT,
	letivos_mar INT,
	letivos_abr INT,
	letivos_mai INT,
	letivos_jun INT,
	letivos_jul INT,
	letivos_ago INT,
	letivos_set INT,
	letivos_out INT,
	letivos_nov INT,
	letivos_dez INT
);

INSERT INTO usuarios (login, senha, nome_professor) VALUES ('admin', 'admin', 'ADMIN');

INSERT INTO controle (ano, letivos_jan, letivos_fev, letivos_mar, letivos_abr, letivos_mai, letivos_jun, letivos_jul, letivos_ago, letivos_set, letivos_out, letivos_nov, letivos_dez) VALUES (2024, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);



