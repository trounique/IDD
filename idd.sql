/*
 Navicat Premium Data Transfer

 Source Server         : DB
 Source Server Type    : MySQL
 Source Server Version : 50719
 Source Host           : localhost:3306
 Source Schema         : idd

 Target Server Type    : MySQL
 Target Server Version : 50719
 File Encoding         : 65001

 Date: 03/02/2022 15:31:12
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for results
-- ----------------------------
DROP TABLE IF EXISTS `results`;
CREATE TABLE `results`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` datetime(0) NULL DEFAULT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of results
-- ----------------------------
INSERT INTO `results` VALUES (1, '2022-01-27 18:01:50', 'origin11.jpg');
INSERT INTO `results` VALUES (2, '2022-01-27 19:01:46', 'origin11.jpg');
INSERT INTO `results` VALUES (3, '2022-01-27 19:01:34', 'origin11.jpg');
INSERT INTO `results` VALUES (4, '2022-01-27 20:01:52', 'origin11.jpg');
INSERT INTO `results` VALUES (5, '2022-01-27 21:01:11', 'origin11.jpg');
INSERT INTO `results` VALUES (6, '2022-01-28 00:01:02', 'origin11.jpg');
INSERT INTO `results` VALUES (7, '2022-01-28 00:01:16', 'origin11.jpg');
INSERT INTO `results` VALUES (8, '2022-01-28 00:01:05', 'origin12.jpg');
INSERT INTO `results` VALUES (9, '2022-01-28 00:01:38', 'origin11.jpg');
INSERT INTO `results` VALUES (10, '2022-01-28 00:01:53', 'origin11.jpg');

SET FOREIGN_KEY_CHECKS = 1;
