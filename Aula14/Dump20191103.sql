-- MySQL dump 10.13  Distrib 8.0.16, for macos10.14 (x86_64)
--
-- Host: 127.0.0.1    Database: lp2i2
-- ------------------------------------------------------
-- Server version	8.0.18

DROP SCHEMA IF EXISTS `lp2i2`;
CREATE SCHEMA `lp2i2` DEFAULT CHARACTER SET utf8 ;
USE `lp2i2`;
/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alunopessoal`
--

DROP TABLE IF EXISTS `alunopessoal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `alunopessoal` (
  `idalunopessoal` int(11) NOT NULL AUTO_INCREMENT,
  `sexo` varchar(45) DEFAULT 'Não informado',
  `idade` int(11) NOT NULL,
  `cordeolhos` varchar(45) DEFAULT 'Não informado',
  `alunopessoalid` int(11) DEFAULT NULL,
  PRIMARY KEY (`idalunopessoal`),
  KEY `alunopessoalid_idx` (`alunopessoalid`),
  FOREIGN KEY (`alunopessoalid`) REFERENCES `alunos` (`idaluno`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alunopessoal`
--

LOCK TABLES `alunopessoal` WRITE;
/*!40000 ALTER TABLE `alunopessoal` DISABLE KEYS */;
INSERT INTO `alunopessoal` VALUES (1,'não informado',18,'castanhos',1),(2,'não informado',18,'castanhos',2),(3,'não informado',18,'castanhos',3),(4,'não informado',18,'castanhos',4),(5,'não informado',18,'castanhos',5),(6,'não informado',18,'castanhos',6),(7,'não informado',18,'castanhos',7),(8,'não informado',18,'castanhos',8),(9,'não informado',18,'castanhos',9),(10,'não informado',18,'castanhos',10),(11,'não informado',18,'castanhos',11),(12,'não informado',18,'castanhos',12),(13,'não informado',18,'castanhos',13),(14,'não informado',18,'castanhos',14),(15,'não informado',18,'castanhos',15),(16,'não informado',18,'castanhos',16),(17,'não informado',18,'castanhos',17),(18,'não informado',18,'castanhos',18),(19,'não informado',18,'castanhos',19),(20,'não informado',18,'castanhos',20),(21,'não informado',18,'castanhos',21),(22,'não informado',18,'castanhos',22),(23,'não informado',18,'castanhos',23),(24,'não informado',18,'castanhos',24),(25,'não informado',18,'castanhos',25),(26,'não informado',18,'castanhos',26),(27,'não informado',18,'castanhos',27),(28,'não informado',18,'castanhos',28),(29,'não informado',18,'castanhos',29),(30,'não informado',18,'castanhos',30),(31,'não informado',18,'castanhos',31),(32,'não informado',18,'castanhos',32),(33,'não informado',18,'castanhos',33),(34,'não informado',18,'castanhos',34),(35,'não informado',18,'castanhos',35);
/*!40000 ALTER TABLE `alunopessoal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alunos`
--

DROP TABLE IF EXISTS `alunos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `alunos` (
  `idaluno` int(11) NOT NULL AUTO_INCREMENT,
  `prontuario` varchar(10) NOT NULL,
  `nomecompleto` varchar(100) NOT NULL,
  PRIMARY KEY (`idaluno`),
  UNIQUE KEY `prontuario_UNIQUE` (`prontuario`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alunos`
--

LOCK TABLES `alunos` WRITE;
/*!40000 ALTER TABLE `alunos` DISABLE KEYS */;
INSERT INTO `alunos` VALUES (1,'BP3005925','Bianca da Costa Farias'),(2,'BP3006913','Eduardo Almeida da Silva'),(3,'BP3005771','Felipe Akira Taguchi'),(4,'BP3005798','Flavio Eugenio do Prado Cintra Oliveira'),(5,'BP3000958','Gabriel Souza de Lima'),(6,'BP3004767','Giovanni Canoletti'),(7,'BP3004791','Guilherme de Moraes Pereira'),(8,'BP3004741','Gustavo Mauricio de Barros'),(9,'BP3006948','Israel Ferreira dos Reis de Jesus'),(10,'BP3004376','Jhonatan William Oliveira Leme'),(11,'BP3005348','Julia Andressa Costa Souza'),(12,'BP3004121','Kevin Alves Cardoso'),(13,'BP3005763','Lucas Bandeira de Almeida'),(14,'BP3006051','Lucas Cherez Costa'),(15,'BP3001318','Marcelo de Lima Silva'),(16,'BP1562428','Marcus Vinicius Cunha de Moraes'),(17,'BP300578X','Milena Pires Guedes'),(18,'BP3003426','Renan Lucas de Paula'),(19,'BP3004759','Samuel de Lima Andrade'),(20,'BP3005852','Tiago Silva Fernandes'),(21,'BP3005801','Vinicius Meuci Bastos Machado'),(22,'BP3005054','Dennis Santos Jacintho'),(23,'BP300483X','Driely Cristine Fernandes'),(24,'BP3005089','Gabriel Albinati Sandrini'),(25,'BP3005381','Guilherme Barbosa Chaves da Silva'),(26,'BP3005101','Gustavo Almeida de Souza'),(27,'BP3005844','Helyon Fernando Tollendal Pacheco'),(28,'BP3004732','Jakeson Mateus Pantaleão de Moraes'),(29,'BP3005119','Letícia Mayara Soares Fernandes'),(30,'BP3005828','Lucas Henrique Azzi'),(31,'BP3004309','Maria Luisa Souza Vinagre'),(32,'BP300581X','Vinicius Bento de Souza'),(33,'BP3006891','Wagner de Souza Campos'),(34,'BP3005097','William Masaharu Yoshida'),(35,'BP3002292','Wilson Gimenes da Silva');
/*!40000 ALTER TABLE `alunos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'lp2i2'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-11-03 22:51:31


SELECT a.*, p.sexo, p.idade, p.cordeolhos
FROM alunos a, alunopessoal p
where a.idaluno = p.idalunopessoal;

SELECT a.*, p.sexo, p.idade, p.cordeolhos
FROM alunos a, alunopessoal p
WHERE nomecompleto LIKE '%30%' OR prontuario LIKE '%3005%'
group by a.idaluno;

select * from alunopessoal;

SELECT a.*, p.sexo, p.idade, p.cordeolhos
FROM alunos a, alunopessoal p
WHERE a.nomecompleto LIKE '%18%' OR a.prontuario LIKE '% %'
or p.cordeolhos like '%Castanhos%' OR p.sexo like '%18%' or p.idade = '0'
group by a.idaluno;
