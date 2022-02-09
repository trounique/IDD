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

 Date: 09/02/2022 22:01:26
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
  `mainboard_good` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `interface_good` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `mainboard_lack` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `interface_lack` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `fan_good` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `fan_lack` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of results
-- ----------------------------
INSERT INTO `results` VALUES (1, '2022-02-09 19:02:12', 'origin2 (104).jpg', '6', '1', '2', '0', '3', '1');
INSERT INTO `results` VALUES (2, '2022-02-09 20:02:01', 'origin2 (104).jpg', '6', '1', '2', '0', '3', '1');
INSERT INTO `results` VALUES (3, '2022-02-09 20:02:53', 'origin2 (104).jpg', '6', '1', '2', '0', '3', '1');
INSERT INTO `results` VALUES (4, '2022-02-09 20:02:20', 'origin2 (104).jpg', '6', '1', '2', '0', '3', '1');
INSERT INTO `results` VALUES (5, '2022-02-09 21:02:18', 'origin2 (165).jpg', '3', '1', '3', '0', '2', '2');
INSERT INTO `results` VALUES (6, '2022-02-09 21:02:48', 'origin2 (112).jpg', '6', '1', '2', '0', '0', '4');
INSERT INTO `results` VALUES (7, '2022-02-09 22:02:15', 'origin2 (173).jpg', '3', '1', '2', '0', '1', '3');

SET FOREIGN_KEY_CHECKS = 1;
