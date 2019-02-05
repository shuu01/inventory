--
-- Table structure for table `address`
--

DROP TABLE IF EXISTS `address`;
CREATE TABLE `address` (
  `serial` varchar(15) DEFAULT NULL,
  `address` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `bgp`
--

DROP TABLE IF EXISTS `bgp`;
CREATE TABLE `bgp` (
  `serial` varchar(15) DEFAULT NULL,
  `instance` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `credentials`
--

DROP TABLE IF EXISTS `credentials`;
CREATE TABLE `credentials` (
  `serial` varchar(15) NOT NULL DEFAULT '',
  `user` varchar(15) DEFAULT NULL,
  `password` varchar(16) DEFAULT NULL,
  PRIMARY KEY (`serial`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `device`
--

DROP TABLE IF EXISTS `device`;
CREATE TABLE `device` (
  `serial` varchar(15) NOT NULL DEFAULT '',
  `version` varchar(15) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `type` varchar(10) DEFAULT NULL,
  `board` varchar(15) DEFAULT NULL,
  `updatedAt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `ports` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`serial`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `gateway`
--

DROP TABLE IF EXISTS `gateway`;
CREATE TABLE `gateway` (
  `serial` varchar(15) DEFAULT NULL,
  `gateway` varchar(15) DEFAULT NULL,
  `weight` int(11) DEFAULT NULL,
  `static` tinyint(4) DEFAULT NULL,
  `active` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


--
-- Table structure for table `route`
--

DROP TABLE IF EXISTS `route`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `route` (
  `serial` varchar(15) DEFAULT NULL,
  `dst_address` varchar(18) DEFAULT NULL,
  `gateway` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

