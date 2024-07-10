backend calendario produccion 

Crear .env con las sig. variables
MYSQL_HOST=127.0.0.1
MYSQL_USER=user
MYSQL_PASSWORD=pass
MYSQL_DB=assembled_db
SECRET_KEY=B!1w8*NAt1T^%kvhUI*S^_
JWT_KEY=D5*F?_1?-d$f*1


base de datos 

CREATE DATABASE  IF NOT EXISTS `assembled_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `assembled_db`;
DROP TABLE IF EXISTS `Eventos`;

CREATE TABLE `Eventos` (
  `ID_EVENTO` int NOT NULL AUTO_INCREMENT,
  `TIPO` enum('S','E','F','M') NOT NULL,
  `OP` int DEFAULT NULL,
  `TITULO` varchar(255) NOT NULL,
  `DESCRIPCION` varchar(255) DEFAULT NULL,
  `FECHA_INICIO` datetime NOT NULL,
  `FECHA_FIN` datetime NOT NULL,
  `EQUIPOS` varchar(300) DEFAULT NULL,
  `ACTIVO` tinyint NOT NULL DEFAULT '1',
  PRIMARY KEY (`ID_EVENTO`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

