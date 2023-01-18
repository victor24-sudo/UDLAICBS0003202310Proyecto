Drop database if exists POACarrera_sor;
Create database POACarrera_sor;

Use POACarrera_sor;

Create table Proyecto_sor(
ID_surr int primary key auto_increment not null,
Id int not null,
Titulo varchar(150),
CodigoEtl bigint
);

Create table Carrera_sor(
ID_surr int primary key auto_increment not null,
Id int not null,
Nombre nvarchar(50),
NumSemestres tinyint,
CodigoEtl bigint
);

Create table Docente_sor(
ID_surr int primary key auto_increment not null,
Id int not null,
NombreCompleto varchar(20) not null, 
Cedula char(10) not null,
Genero char(10) not null,
Telefono char(10) not null,
Antiguedad smallint,
CodigoEtl bigint 
);

Create table POA_sor(
ID_surr int primary key auto_increment not null,
Id int not null,
IdCarrera int,
IdDocente int,
IdProyecto int,
Periodo char(4) not null,
Trimestre1 char(3) not null,
Trimestre2 char(3) not null,
Trimestre3 char(3) not null,
Trimestre4 char(3) not null,
CodigoEtl bigint,
Fecha DATETIME DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE `poacarrera_sor`.`poa_sor` 
ADD CONSTRAINT `IdCarrera`
  FOREIGN KEY (`IdCarrera`)
  REFERENCES `poacarrera_sor`.`carrera_sor` (`ID_surr`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `IdDocente`
  FOREIGN KEY (`IdDocente`)
  REFERENCES `poacarrera_sor`.`docente_sor` (`ID_surr`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
  ADD CONSTRAINT `IdProyecto`
  FOREIGN KEY (`IdProyecto`)
  REFERENCES `poacarrera_sor`.`proyecto_sor` (`ID_surr`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
  
  
