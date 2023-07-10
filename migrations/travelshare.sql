SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for thirdparty_logins
-- ----------------------------
DROP TABLE IF EXISTS `thirdparty_logins`;
CREATE TABLE `thirdparty_logins` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL COMMENT '关联用户id',
  `provider` varchar(10) NOT NULL DEFAULT '' COMMENT '第三方（目前仅支持一个）：wechat',
  `provider_app_id` varchar(20) NOT NULL DEFAULT '' COMMENT '第三方app id',
  `provider_user_id` varchar(50) NOT NULL DEFAULT '' COMMENT '第三方user id（比如微信openid）',
  `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '是否有效： 0 - 无效； 1 - 有效',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `user_id_idx` (`user_id`) USING HASH
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='第三方登录表';

-- ----------------------------
-- Table structure for travel_plan
-- ----------------------------
DROP TABLE IF EXISTS `travel_plan`;
CREATE TABLE `travel_plan` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '行程id',
  `host_user_id` bigint(20) NOT NULL COMMENT '行程创建人id',
  `travel_name` varchar(50) NOT NULL DEFAULT '' COMMENT '行程名',
  `start_time` datetime DEFAULT NULL COMMENT '行程开始时间',
  `end_time` datetime DEFAULT NULL COMMENT '行程结束时间',
  `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '行程状态：',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `host_user_id_idx` (`host_user_id`) USING HASH
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='行程表';

-- ----------------------------
-- Table structure for travel_plan_member
-- ----------------------------
DROP TABLE IF EXISTS `travel_plan_member`;
CREATE TABLE `travel_plan_member` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `member_name` varchar(50) NOT NULL DEFAULT '' COMMENT '参与人名字，非用户时必填',
  `travel_plan_id` bigint(20) NOT NULL COMMENT '所属行程id',
  `user_id` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '系统用户id',
  `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '状态：0 - 无效； 1 - 有效',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `travel_plan_id_idx` (`travel_plan_id`) USING HASH,
  KEY `user_id_idx` (`user_id`) USING HASH
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='行程参与人表\n';

-- ----------------------------
-- Table structure for travel_plan_payment
-- ----------------------------
DROP TABLE IF EXISTS `travel_plan_payment`;
CREATE TABLE `travel_plan_payment` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `travel_plan_id` bigint(11) NOT NULL COMMENT '所属行程id',
  `created_user_id` bigint(11) NOT NULL COMMENT '记录人，user_id',
  `payer_member_id` bigint(11) NOT NULL COMMENT '支付人，member_id',
  `payment_time` datetime DEFAULT NULL COMMENT '支付时间',
  `payment_amount` decimal(10,2) NOT NULL COMMENT '支付金额',
  `payment_type` tinyint(1) NOT NULL DEFAULT '0' COMMENT '支付类型：\n0 - 未定义\n1 - 餐饮\n2 - 住宿\n3 - 交通\n4 - 景点\n5 - 购物\n6 - 签证\n7 - 导游\n8 - 行李\n9 - 医疗',
  `payment_comment` varchar(255) DEFAULT NULL COMMENT '支付备注说明',
  `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '记录状态：0 - 无效；1 - 有效',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='支付记录表';

-- ----------------------------
-- Table structure for travel_plan_payment_detail
-- ----------------------------
DROP TABLE IF EXISTS `travel_plan_payment_detail`;
CREATE TABLE `travel_plan_payment_detail` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `payment_id` bigint(20) NOT NULL COMMENT '关联支付记录id',
  `travel_member_id` bigint(20) NOT NULL COMMENT '关联行程参与人id',
  `sharing_amount` decimal(10,2) NOT NULL COMMENT '分摊金额',
  `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '分摊记录状态： 0 - 无效； 1 - 有效',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='支付分摊表';

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL DEFAULT '' COMMENT '用户名：微信昵称',
  `mobile` char(11) NOT NULL DEFAULT '' COMMENT '手机号：微信绑定手机号',
  `account` varchar(50) NOT NULL DEFAULT '' COMMENT '账号',
  `password` char(60) NOT NULL DEFAULT '' COMMENT '密码',
  `avatar` varchar(200) NOT NULL DEFAULT '' COMMENT '头像：微信头像',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_mobile_unique` (`mobile`) USING HASH,
  UNIQUE KEY `user_account_unique` (`account`) USING HASH
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户表';

SET FOREIGN_KEY_CHECKS = 1;
