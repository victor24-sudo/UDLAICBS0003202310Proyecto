Drop database if exists POACarrera;
Create database POACarrera;

Use POACarrera;



Create table Proyecto(
IdProyecto int primary key auto_increment not null,
Titulo varchar(150));

Create table Carrera(
IdCarrera int primary key auto_increment not null,
Nombre nvarchar(50),
NumSemestres tinyint
);

Create table Docente(
IdDocente int primary key auto_increment not null,
Nombre varchar(20) not null, 
Apellido varchar(20) not null,
Cedula char(10) not null,
Genero char(1) not null,
Telefono char(10) not null,
Antiguedad smallint not null
);

Create table POA(
IdPoa int primary key auto_increment not null,
IdCarrera int,
IdDocente int,
IdProyecto int,
Periodo char(4) not null,
Trimestre1 char(3) not null,
Trimestre2 char(3) not null,
Trimestre3 char(3) not null,
Trimestre4 char(3) not null
);

ALTER TABLE `poacarrera`.`poa` 
ADD INDEX `IdCarrera_idx` (`IdCarrera` ASC) VISIBLE,
ADD INDEX `IdDocente_idx` (`IdDocente` ASC) VISIBLE,
ADD INDEX `IdProyecto_idx` (`IdProyecto` ASC) VISIBLE;
;
ALTER TABLE `poacarrera`.`poa` 
ADD CONSTRAINT `IdCarrera`
  FOREIGN KEY (`IdCarrera`)
  REFERENCES `poacarrera`.`carrera` (`IdCarrera`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `IdDocente`
  FOREIGN KEY (`IdDocente`)
  REFERENCES `poacarrera`.`docente` (`IdDocente`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `IdProyecto`
  FOREIGN KEY (`IdProyecto`)
  REFERENCES `poacarrera`.`proyecto` (`IdProyecto`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
