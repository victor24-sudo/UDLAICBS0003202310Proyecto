Drop database if exists POACarrera_stg;
Create database POACarrera_stg;

Use POACarrera_stg;


Create table Proyecto_ext(
IdProyecto int primary key auto_increment,
Titulo nvarchar(150));

Create table Carrera_ext(
IdCarrera int primary key auto_increment,
Nombre nvarchar(50),
NumSemestres tinyint
);

Create table Docente_ext(
IdDocente int primary key auto_increment ,
Nombre varchar(20) , 
Apellido varchar(20) ,
Cedula char(10) ,
Genero char(1) ,
Telefono char(10),
Antiguedad smallint
);

Create table POA_ext(
IdPoa int primary key auto_increment,
IdCarrera int,
IdDocente int,
IdProyecto int,
Periodo char(4) ,
Trimestre1 char(3) ,
Trimestre2 char(3) ,
Trimestre3 char(3) ,
Trimestre4 char(3) 
);


Create Table Alumnos_ext(
IdAlumno int primary key auto_increment,
Nombre varchar(20), 
Apellido varchar(20),
Genero char(1),
Cedula char(10),
IdCarrera bigint
);


Create table Proyecto_tra(
ID_surr int primary key auto_increment not null,
id int not null,
Titulo varchar(150),
CodigoEtl bigint 
);

Create table Carrera_tra(
ID_surr int primary key auto_increment not null,
id int not null,
Nombre nvarchar(50),
NumSemestres tinyint,
CodigoEtl bigint 
);

Create table Docente_tra(
ID_surr int primary key auto_increment not null,
id int not null,
NombreCompleto varchar(20) not null, 
Cedula char(10) not null,
Genero varchar(10) not null,
Telefono char(10) not null,
Antiguedad smallint,
CodigoEtl bigint 
);

Create table POA_tra(
ID_surr int primary key auto_increment not null,
Id int not null,
IdCarrera int,
IdDocente int,
IdProyecto int,
Periodo char(4) not null,
Trimestre1 char(1) not null,
Trimestre2 char(1) not null,
Trimestre3 char(1) not null,
Trimestre4 char(1) not null,
CodigoEtl bigint 
);

Create Table Alumnos_tra(
ID_surr int primary key auto_increment not null,
Id int not null,
NombreCompleto varchar(20),
Genero char(10),
Cedula char(10),
IdCarrera int,
CodigoEtl bigint
);

DROP TABLE IF EXISTS codigo_etl;
CREATE TABLE codigo_etl(
	ID bigint auto_increment primary key,
    Usuario varchar(10)
);