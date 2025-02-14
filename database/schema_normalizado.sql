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
    (30011, 'Alice Lins', 'F', '2000/10/09'),
    (30009, 'Leonardo Ramos', 'M', NULL)

;

INSERT INTO Startup (ID_STARTUP, NOME_STARTUP, CIDADE_SEDE) VALUES
(10001, 'Tech4Toy', 'Porto Alegre'),
(10002, 'Smart123', 'Belo Horizonte'),
(10003, 'knowledgeUp', 'Rio de Janeiro'),
(10004, 'BSI Next Level', 'Recife'),
(10005, 'QualiHealth', 'São Paulo'),
(10006, 'ProEdu', 'Florianópolis'),
(10007, 'CommerceIA', 'Manaus')

;

INSERT INTO Programador_Startup (ID_STARTUP, ID_PROGRAMADOR) VALUES
(10001, 30001),
(10001, 30005),
(10002, 30002),
(10002, 30007),
(10003, 30003),
(10004, 30004),
(10004, 30006),
(10007, 30011)

;

INSERT INTO Programador_Linguagem VALUES
(30001, 20001),
(30001, 20002),
(30002, 20003),
(30007, 20001),
(30007, 20002),
(30003, 20004),
(30003, 20005),
(30004, 20005),
(30009, 20004),
(30009, 20007),
(30010, 20007)

;

INSERT INTO Programador_Dependente (ID_PROGRAMADOR, ID_DEPENDENTE) VALUES
(30001, 40001),
(30002, 40002),
(30002, 40003),
(30002, 40004),
(30007, 40005),
(30004, 40006),
(30004, 40007),
(30006, 40008),
(30009, 40009)

;

INSERT INTO Linguagem VALUES
(20001, 'Python'),
(20002, 'PHP'),
(20003, 'Java'),
(20004, 'C'),
(20005, 'JavaScript'),
(20006, 'Dart'),
(20007, 'SQL')

;

INSERT INTO Dependente VALUES
(40001, 'André Sousa', 'Filho', '2020-05-15'),
(40002, 'Luciana Silva', 'Filha', '2018-07-26'),
(40003, 'Elisa Silva', 'Filha', '2020-01-06'),
(40004, 'Breno Silva', 'Esposo', '1984-05-21'),
(40005, 'Daniel Marques', 'Filho', '2014-06-06'),
(40006, 'Rafaela Santos', 'Esposa', '1980-02-12'),
(40007, 'Marcos Martins', 'Filho', '2008-03-26'),
(40008, 'Laís Meneses', 'Esposa', '1990-11-09'),
(40009, 'Lidiane Macedo', 'Filha', '2015-04-14')

;

COMMIT;