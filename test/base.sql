drop database xacademy;
create database xacademy;
use xacademy;

# ---------------- Endereço ---------------- 
# Academia, aluno e professores deverão possuir endereços, para análise técnicas.
create table estado (
	id_estado int PRIMARY KEY auto_increment,
	UF char(2) unique
);

create table cidade (
	id_cidade int PRIMARY KEY auto_increment,
	nome varchar(120) unique,
	id_estado int,
	FOREIGN KEY (id_estado) REFERENCES estado(id_estado)
);

create table bairro (
	id_bairro int PRIMARY KEY auto_increment,
	nome varchar(120),
	id_cidade int,
	FOREIGN KEY (id_cidade) REFERENCES cidade(id_cidade)
);

create table logradouro (
	id_logradouro int PRIMARY KEY auto_increment,
	nome varchar(200),
	complemento varchar(10),
	id_bairro int,
	FOREIGN KEY (id_bairro) REFERENCES bairro(id_bairro)
);

create table endereco (
	id_endereco int PRIMARY KEY auto_increment,
	nome varchar(40),
	id_logradouro int,
	FOREIGN KEY (id_logradouro) REFERENCES logradouro(id_logradouro)
);

# ---------------- Academia ---------------- 
create table academia (
	id_academia int primary key auto_increment,
	nome varchar(60) not null,
	cnpj varchar(14) not null unique,
	quant_aluno int,
	id_endereco int,
	FOREIGN KEY (id_endereco) REFERENCES endereco(id_endereco)
);

# ---------------- Pessoa ---------------- 
create table pessoa (
	id_pessoa int primary KEY auto_increment,
	nome varchar(60) not null,
	email varchar(60) not null unique,
	senha varchar(100) not null unique,
	cpf char(11) not null unique,
	data_nasc date not null,
	id_endereco int,
	id_academia int,
	# Verificar status do cadastro
	status char(1),
	FOREIGN KEY (id_endereco) REFERENCES endereco(id_endereco),
	FOREIGN KEY (id_academia) REFERENCES academia(id_academia)
);

# ---------------- Aluno ---------------- 
create table aluno (
	id_aluno int primary key auto_increment,
	id_pessoa int,
	inicio date not null,
	meta decimal(3,2),
	objetivo varchar(25),
	foreign key(id_pessoa) references pessoa(id_pessoa)
);

# ---------------- Professor ---------------- 
create table professor (
	id_professor int primary key auto_increment,
	id_pessoa int,
	foreign key(id_pessoa) references pessoa(id_pessoa)	
);

# ---------------- Músculo ---------------- 
create table tipo_musculo (
	id_tipo_musculo int primary key auto_increment,
	nome varchar(120)
);

create table musculo (
	id_musculo int primary key auto_increment,
	nome varchar(120) not null unique,
	id_tipo_musculo int,
	foreign key (id_tipo_musculo) references tipo_musculo(id_tipo_musculo)
);

# ---------------- Treino ---------------- 
create table ficha (
	id_ficha int primary key auto_increment,
	nome varchar(30) not null
);

create table exercicio (
	id_exercicio int primary key auto_increment,
	nome varchar(60) not null,
	gif varchar(250) not null,
	id_musculo int,
	foreign key(id_musculo) references musculo(id_musculo)
);

create table ficha_exercicio (
	id_ficha int,
	id_exercicio int,
	carga int,
	serie varchar(250),
	foreign key(id_ficha) references ficha(id_ficha),
	foreign key(id_exercicio) references exercicio(id_exercicio)
);

create table treino (
	id_controle int primary key auto_increment,
	id_aluno int,
	id_ficha int,
	id_professor int,
	id_musculo int,
	# Exibir apenas fichas pendentes
	finalizada char(1),
	foreign key(id_musculo) references musculo(id_musculo),	
	foreign key(id_ficha) references ficha(id_ficha),	
	foreign key(id_professor) references professor(id_professor),	
	foreign key(id_aluno) references aluno(id_aluno)
);




