/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.5-10.4.24-MariaDB : Database - forgery_detection
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`forgery_detection` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `forgery_detection`;

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `complaint` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `complaints` */

insert  into `complaints`(`complaint_id`,`user_id`,`complaint`,`reply`,`date`) values (1,1,'dfvdsgf','ok','2022-11-16 12:24:46'),(3,2,'fgdf','pending','2022-11-25 09:24:40');

/*Table structure for table `crimes` */

DROP TABLE IF EXISTS `crimes`;

CREATE TABLE `crimes` (
  `crime_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `crime` varchar(100) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`crime_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `crimes` */

/*Table structure for table `enquiry` */

DROP TABLE IF EXISTS `enquiry`;

CREATE TABLE `enquiry` (
  `enquiry_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `enquiry` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`enquiry_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `enquiry` */

insert  into `enquiry`(`enquiry_id`,`user_id`,`enquiry`,`reply`,`date`) values (1,1,'frsgtr','ok','2022-11-16 12:29:36'),(2,2,'gdfg','pending','2022-11-25 09:24:46');

/*Table structure for table `history` */

DROP TABLE IF EXISTS `history`;

CREATE TABLE `history` (
  `history_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `fplace` varchar(100) DEFAULT NULL,
  `tplace` varchar(100) DEFAULT NULL,
  `booked_for` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`history_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `history` */

insert  into `history`(`history_id`,`user_id`,`fplace`,`tplace`,`booked_for`,`date`) values (1,1,'Kochi','TVM','2022-11-30','2022-11-16 17:52:59');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values (1,'admin','admin','admin'),(2,'sara','sara@123','user'),(3,'anju','anju@123','staff'),(4,'jinu','jinu@123','security authority'),(5,'emelda','emelda@123','user');

/*Table structure for table `passportrequest` */

DROP TABLE IF EXISTS `passportrequest`;

CREATE TABLE `passportrequest` (
  `prequest_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `passport_num` varchar(100) DEFAULT NULL,
  `requested_date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `qr` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`prequest_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `passportrequest` */

insert  into `passportrequest`(`prequest_id`,`user_id`,`passport_num`,`requested_date`,`status`,`qr`) values (1,1,'UUYO79OYY6','2022-11-16','Accepted','static/qrcode/5e14b92f-ab95-4b46-93ec-9a8ead3b8deb.png'),(2,2,'6OIUY6O796','2022-11-25','Accepted','static/qrcode/d9ee7cb2-533a-4a77-bac3-d889be94a18f.png');

/*Table structure for table `security_authority` */

DROP TABLE IF EXISTS `security_authority`;

CREATE TABLE `security_authority` (
  `authority_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `designation` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`authority_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `security_authority` */

insert  into `security_authority`(`authority_id`,`login_id`,`fname`,`lname`,`place`,`phone`,`email`,`designation`) values (1,4,'Jinuu','John','Kochin','9812345678','jinu123@gmail.com','po');

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `designation` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `staff` */

insert  into `staff`(`staff_id`,`login_id`,`fname`,`lname`,`place`,`phone`,`email`,`designation`) values (1,3,'Anjuu','Rose','kollam','9812345678','anju@gmail.com','sd');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

/*Data for the table `user` */

insert  into `user`(`user_id`,`login_id`,`fname`,`lname`,`place`,`phone`,`email`,`photo`) values (1,2,'Sara','Mary','Kochi','9812345678','marysara@gmail.com','static/9f1d8e8f-97b8-4e6a-b032-9dd1242259a5team-1.jpg'),(2,5,'Emelda','John','kochi','9812345678','emelda@gmail.com','static/6bf9c36e-02fc-47cb-b6c6-567a6880000eabout.PNG');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
