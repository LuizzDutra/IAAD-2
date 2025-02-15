START TRANSACTION;

DROP SCHEMA IF EXISTS db_equipe2;
CREATE SCHEMA IF NOT EXISTS db_equipe2;
USE db_equipe2;

CREATE TABLE Programador(
    ID_PROGRAMADOR INT AUTO_INCREMENT,
    NOME_PROGRAMADOR VARCHAR(50),
    GENERO_PROGRAMADOR CHAR(1),
    DATA_NASC_PROGRAMADOR DATE,
    PRIMARY KEY (ID_PROGRAMADOR)
);

CREATE TABLE Startup(
    ID_STARTUP INT AUTO_INCREMENT,
    NOME_STARTUP VARCHAR(50),
    CIDADE_SEDE VARCHAR(50),
    PRIMARY KEY (ID_STARTUP)
);

CREATE TABLE Dependente(
    ID_DEPENDENTE INT AUTO_INCREMENT,
    NOME_DEPENDENTE VARCHAR(50),
    PARENTESCO_DEPENDENTE VARCHAR(20),
    DATA_NASC_DEPENDENTE DATE,
    PRIMARY KEY (ID_DEPENDENTE)
);

CREATE TABLE Linguagem(
    ID_LINGUAGEM INT AUTO_INCREMENT,
    NOME_LINGUAGEM VARCHAR(20),
    PRIMARY KEY (ID_LINGUAGEM)
);

CREATE TABLE Programador_Startup(
    ID_STARTUP INT,
    ID_PROGRAMADOR INT,
    FOREIGN KEY (ID_STARTUP) REFERENCES Startup(ID_STARTUP),
    FOREIGN KEY (ID_PROGRAMADOR) REFERENCES Programador(ID_PROGRAMADOR)
);

CREATE TABLE Programador_Linguagem(
    ID_PROGRAMADOR INT,
    ID_LINGUAGEM INT,
    FOREIGN KEY (ID_PROGRAMADOR) REFERENCES Programador(ID_PROGRAMADOR),
    FOREIGN KEY (ID_LINGUAGEM) REFERENCES Linguagem(ID_LINGUAGEM)
);

CREATE TABLE Programador_Dependente(
    ID_PROGRAMADOR INT, 
    ID_DEPENDENTE INT,
    FOREIGN KEY (ID_PROGRAMADOR) REFERENCES Programador(ID_PROGRAMADOR),
    FOREIGN KEY (ID_DEPENDENTE) REFERENCES Dependente(ID_DEPENDENTE)
);




INSERT INTO Programador Values
    (30001, 'João Pedro', 'M', '1993/06/23'),
    (30005, 'Ana Cristina', 'F', '1968/02/19'),
    (30002, 'Paula Silva', 'F', '1986/01/10'),
    (30007, 'Laura Marques', 'F', '1987/10/04'),
    (30003, 'Renata Vieira', 'F', '1991/07/05'),
    (30004, 'Felipe Santos', 'M', '1976/11/25'),
    (30006, 'Fernando Alves', 'M', '1998/07/07'),
    (30008, 'Lucas Lima', 'M', '2000/10/09'),
    (30011, 'Alice Lins', 'F', '2000/10/09')
    -- (30009, 'Leonardo Ramos', 'M', NULL)

;

INSERT INTO STARTUP (ID_STARTUP, NOME_STARTUP, CIDADE_SEDE) VALUES
(10001, 'Tech4Toy', 'Porto Alegre'),
(10002, 'Smart123', 'Belo Horizonte'),
(10003, 'knowledgeUp', 'Rio de Janeiro'),
(10004, 'BSI Next Level', 'Recife'),
(10005, 'QualiHealth', 'São Paulo'),
(10006, 'ProEdu', 'Florianópolis'),
(10007, 'CommerceIA', 'Manaus');

INSERT INTO Linguagem (ID_LINGUAGEM, NOME_LINGUAGEM) VALUES
(20001, 'Python'),
(20002, 'PHP'),
(20003, 'Java'),
(20004, 'C'),
(20005, 'JavaScript'),
(20006, 'Dart'),
(20007, 'SQL');

INSERT INTO Programador_Startup VALUES
(10001, 30001),
(10001, 30005),
(10002, 30007),
(10003, 30003),
(10004, 30004),
(10004, 30006),
(10007, 30011)
;

CREATE VIEW qnt_programador_startup AS
SELECT NOME_STARTUP, COUNT(ID_PROGRAMADOR) as Programadores
FROM startup NATURAL LEFT JOIN programador_startup
WHERE ID_PROGRAMADOR IS NOT NULL
GROUP BY NOME_STARTUP;

COMMIT;