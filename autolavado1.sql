-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: autolavado
-- ------------------------------------------------------
-- Server version	8.0.37

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tbb_productos`
--

DROP TABLE IF EXISTS `tbb_productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbb_productos` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  `descripcion` varchar(500) DEFAULT NULL,
  `categoria` varchar(50) DEFAULT NULL,
  `unidad_medida` varchar(20) DEFAULT NULL,
  `stock_actual` float DEFAULT NULL,
  `stock_minimo` float DEFAULT NULL,
  `precio` float DEFAULT NULL,
  `fecha_registro` datetime DEFAULT NULL,
  `fecha_actualizacion` datetime DEFAULT NULL,
  `estado` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `ix_tbb_productos_Id` (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbb_productos`
--

LOCK TABLES `tbb_productos` WRITE;
/*!40000 ALTER TABLE `tbb_productos` DISABLE KEYS */;
INSERT INTO `tbb_productos` VALUES (1,'habon','limpieza','baño','100ml',1,2,500,'2026-03-06 19:16:36','2026-03-06 19:16:36',1);
/*!40000 ALTER TABLE `tbb_productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbb_usuarios`
--

DROP TABLE IF EXISTS `tbb_usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbb_usuarios` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `rol_Id` int DEFAULT NULL,
  `nombre` varchar(60) DEFAULT NULL,
  `primer_apellido` varchar(60) DEFAULT NULL,
  `segundo_apellido` varchar(60) DEFAULT NULL,
  `direccion` varchar(200) DEFAULT NULL,
  `correo_electronico` varchar(100) DEFAULT NULL,
  `numero_telefono` varchar(20) DEFAULT NULL,
  `contrasena` varchar(255) DEFAULT NULL,
  `estado` tinyint(1) DEFAULT NULL,
  `fecha_registro` datetime DEFAULT NULL,
  `fecha_actualizacion` datetime DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `rol_Id` (`rol_Id`),
  KEY `ix_tbb_usuarios_Id` (`Id`),
  CONSTRAINT `tbb_usuarios_ibfk_1` FOREIGN KEY (`rol_Id`) REFERENCES `tbc_roles` (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbb_usuarios`
--

LOCK TABLES `tbb_usuarios` WRITE;
/*!40000 ALTER TABLE `tbb_usuarios` DISABLE KEYS */;
INSERT INTO `tbb_usuarios` VALUES (1,1,'raul','pazos','cruz','mayo','giovanyraul359@gmail.com','7641235117','$argon2id$v=19$m=65536,t=3,p=4$aI3Res9ZSwmhdO6ds7Y2Rg$qthbGTJb/qUNTdo6hrSgKe7qrFUKhfkx64XyKrk0n7g',1,'2026-03-06 19:11:15','2026-03-06 19:11:15');
/*!40000 ALTER TABLE `tbb_usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbb_vehiculos`
--

DROP TABLE IF EXISTS `tbb_vehiculos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbb_vehiculos` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `usuario_Id` int DEFAULT NULL,
  `placa` varchar(20) DEFAULT NULL,
  `marca` varchar(50) DEFAULT NULL,
  `modelo` varchar(50) DEFAULT NULL,
  `serie` varchar(50) DEFAULT NULL,
  `color` varchar(20) DEFAULT NULL,
  `tipo` varchar(20) DEFAULT NULL,
  `anio` varchar(4) DEFAULT NULL,
  `estado` tinyint(1) DEFAULT NULL,
  `fecha_registro` datetime DEFAULT NULL,
  `fecha_actualizacion` datetime DEFAULT NULL,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `placa` (`placa`),
  KEY `usuario_Id` (`usuario_Id`),
  KEY `ix_tbb_vehiculos_Id` (`Id`),
  CONSTRAINT `tbb_vehiculos_ibfk_1` FOREIGN KEY (`usuario_Id`) REFERENCES `tbb_usuarios` (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbb_vehiculos`
--

LOCK TABLES `tbb_vehiculos` WRITE;
/*!40000 ALTER TABLE `tbb_vehiculos` DISABLE KEYS */;
INSERT INTO `tbb_vehiculos` VALUES (1,1,'6556',NULL,'gtr','2025','blue','deportivo','2023',1,'2026-03-06 19:15:18','2026-03-06 19:15:18'),(3,1,'67890','toyota','prius','34','red','carrito','2025',1,'2026-03-10 02:07:32','2026-03-10 02:07:32');
/*!40000 ALTER TABLE `tbb_vehiculos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbc_roles`
--

DROP TABLE IF EXISTS `tbc_roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbc_roles` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `nombre_rol` varchar(15) DEFAULT NULL,
  `estado` tinyint(1) DEFAULT NULL,
  `fecha_registro` datetime DEFAULT NULL,
  `fecha_actualizacion` datetime DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `ix_tbc_roles_Id` (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbc_roles`
--

LOCK TABLES `tbc_roles` WRITE;
/*!40000 ALTER TABLE `tbc_roles` DISABLE KEYS */;
INSERT INTO `tbc_roles` VALUES (1,'admin',NULL,NULL,NULL),(2,'admin',NULL,NULL,NULL);
/*!40000 ALTER TABLE `tbc_roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbc_servicios`
--

DROP TABLE IF EXISTS `tbc_servicios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbc_servicios` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(60) DEFAULT NULL,
  `descripcion` varchar(150) DEFAULT NULL,
  `costo` float DEFAULT NULL,
  `duracion_minutos` int DEFAULT NULL,
  `estado` tinyint(1) DEFAULT NULL,
  `fecha_registro` datetime DEFAULT NULL,
  `fecha_actualizacion` datetime DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `ix_tbc_servicios_Id` (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbc_servicios`
--

LOCK TABLES `tbc_servicios` WRITE;
/*!40000 ALTER TABLE `tbc_servicios` DISABLE KEYS */;
INSERT INTO `tbc_servicios` VALUES (1,'lavado','llimpieza',100,30,1,'2026-03-06 19:14:39','2026-03-06 19:14:39');
/*!40000 ALTER TABLE `tbc_servicios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbd_movimientos_inventario`
--

DROP TABLE IF EXISTS `tbd_movimientos_inventario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbd_movimientos_inventario` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `producto_Id` int DEFAULT NULL,
  `tipo_movimiento` enum('entrada','salida') DEFAULT NULL,
  `cantidad` int DEFAULT NULL,
  `fecha_movimiento` datetime DEFAULT NULL,
  `usuario_Id` int DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `producto_Id` (`producto_Id`),
  KEY `usuario_Id` (`usuario_Id`),
  KEY `ix_tbd_movimientos_inventario_Id` (`Id`),
  CONSTRAINT `tbd_movimientos_inventario_ibfk_1` FOREIGN KEY (`producto_Id`) REFERENCES `tbb_productos` (`Id`),
  CONSTRAINT `tbd_movimientos_inventario_ibfk_2` FOREIGN KEY (`usuario_Id`) REFERENCES `tbb_usuarios` (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbd_movimientos_inventario`
--

LOCK TABLES `tbd_movimientos_inventario` WRITE;
/*!40000 ALTER TABLE `tbd_movimientos_inventario` DISABLE KEYS */;
INSERT INTO `tbd_movimientos_inventario` VALUES (1,1,'entrada',1,'2026-03-06 19:18:14',1);
/*!40000 ALTER TABLE `tbd_movimientos_inventario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbd_usuario_vehiculo_servicio`
--

DROP TABLE IF EXISTS `tbd_usuario_vehiculo_servicio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbd_usuario_vehiculo_servicio` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `vehiculo_Id` int DEFAULT NULL,
  `cajero_Id` int DEFAULT NULL,
  `operativo_Id` int DEFAULT NULL,
  `servicio_Id` int DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `hora` time DEFAULT NULL,
  `estatus` varchar(20) DEFAULT NULL,
  `estado` tinyint(1) DEFAULT NULL,
  `fecha_registro` datetime DEFAULT NULL,
  `fecha_actualizacion` datetime DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `vehiculo_Id` (`vehiculo_Id`),
  KEY `cajero_Id` (`cajero_Id`),
  KEY `operativo_Id` (`operativo_Id`),
  KEY `servicio_Id` (`servicio_Id`),
  KEY `ix_tbd_usuario_vehiculo_servicio_Id` (`Id`),
  CONSTRAINT `tbd_usuario_vehiculo_servicio_ibfk_1` FOREIGN KEY (`vehiculo_Id`) REFERENCES `tbb_vehiculos` (`Id`),
  CONSTRAINT `tbd_usuario_vehiculo_servicio_ibfk_2` FOREIGN KEY (`cajero_Id`) REFERENCES `tbb_usuarios` (`Id`),
  CONSTRAINT `tbd_usuario_vehiculo_servicio_ibfk_3` FOREIGN KEY (`operativo_Id`) REFERENCES `tbb_usuarios` (`Id`),
  CONSTRAINT `tbd_usuario_vehiculo_servicio_ibfk_4` FOREIGN KEY (`servicio_Id`) REFERENCES `tbc_servicios` (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbd_usuario_vehiculo_servicio`
--

LOCK TABLES `tbd_usuario_vehiculo_servicio` WRITE;
/*!40000 ALTER TABLE `tbd_usuario_vehiculo_servicio` DISABLE KEYS */;
INSERT INTO `tbd_usuario_vehiculo_servicio` VALUES (1,1,1,1,1,'2026-03-10','10:30:00','completado',1,'2026-03-10 02:18:00','2026-03-10 02:18:00'),(2,1,1,1,1,'2026-03-10','10:30:00','completado',1,'2026-03-10 02:18:00','2026-03-10 02:18:00');
/*!40000 ALTER TABLE `tbd_usuario_vehiculo_servicio` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-03-09 20:29:26
