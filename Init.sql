# 如果已经存在report_sys数据库，先删除它
DROP DATABASE IF EXISTS report_sys;
# 创建数据库report_sys
CREATE DATABASE report_sys CHARACTER SET = 'utf8';
USE report_sys;

# 创建用人单位表--unit_info
CREATE TABLE unit_info
(
    unit_id      SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    unit_name    VARCHAR(35)       NOT NULL,
    unit_address VARCHAR(60),
    unit_linkman VARCHAR(8),
    unit_phone   VARCHAR(13),
    unit_parent  SMALLINT UNSIGNED,
    zipcode      VARCHAR(10)
);

# 创建报告书信息表--report_info
CREATE TABLE report_info
(
    report_id       SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    report_unit     SMALLINT UNSIGNED NOT NULL,
    report_num      VARCHAR(10)       NOT NULL,
    report_date     DATETIME          NOT NULL,
    report_category TINYINT UNSIGNED DEFAULT 0,
    test_category   TINYINT UNSIGNED DEFAULT 0,
    report_status   TINYINT UNSIGNED DEFAULT 0,
    report_mtime    TIMESTAMP        DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

# 创建创建国家标准表--gb_info
CREATE TABLE gb_info
(
    gb_id       SMALLINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
    gb_num      VARCHAR(50),/*暂时设计可以为空，避免无标准号的文件*/
    gb_name     VARCHAR(80)       NOT NULL,
    gb_status   TINYINT UNSIGNED DEFAULT 0,
    gb_category TINYINT UNSIGNED,
    gb_control  TINYINT UNSIGNED,
    gb_date     TIMESTAMP
);

# 创建仪器设备表--instrument
CREATE TABLE instrument
(
    instrument_id       SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    instrument_name     VARCHAR(20)       NOT NULL,
    instrument_num      VARCHAR(20)       NOT NULL,
    instrument_status   TINYINT UNSIGNED DEFAULT 0,
    instrument_category TINYINT UNSIGNED DEFAULT 0,
    instrument_belong   TINYINT UNSIGNED
);

# 创建报告书所用的仪器设备表instr_report
CREATE TABLE instr_report
(
    instr_report_id SMALLINT UNSIGNED NOT NULL,
    instr_id        SMALLINT UNSIGNED NOT NULL
);

# 创建检测项目表test_item
CREATE TABLE test_item
(
    test_item_id   MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    test_item_name VARCHAR(20),
    sample_name    VARCHAR(20),
    mac_limit      FLOAT(8, 3),
    twa_limit      FLOAT(8, 3),
    stel_limit     FLOAT(8, 3)
);

# 检测项目与国家标准关系表（多对多关系表）test_item_gb
CREATE TABLE test_item_gb
(
    relation_id MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    test_item   MEDIUMINT UNSIGNED NOT NULL,
    gb_id       MEDIUMINT UNSIGNED NOT NULL
);

# 创建工作岗位表--job_post
CREATE TABLE job_post
(
    job_id       MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    department   VARCHAR(80),
    group_in     VARCHAR(80),
    location     VARCHAR(80),
    job_position VARCHAR(80),
    exposed_num  SMALLINT UNSIGNED,
    exposed_time FLOAT(4, 2),
    unit_id      SMALLINT UNSIGNED,
    report_id    SMALLINT UNSIGNED
);

# 创建粉尘毒物采样表toxicant_info
CREATE TABLE tocicant_info
(
    sample_id         MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    sample_num        VARCHAR(10)        NOT NULL,
    test_num          VARCHAR(10)        NOT NULL,
    sample_way        TINYINT UNSIGNED DEFAULT 0, #默认为定点采样
    sample_instrument SMALLINT UNSIGNED,
    department_id     SMALLINT UNSIGNED,
    location          SMALLINT UNSIGNED,
    monitored_person  SMALLINT UNSIGNED,
    sample_flow       FLOAT(6, 3),
    presample_time    DATETIME,
    postsample_time   DATETIME,
    sample_date       DATETIME,
    test_date         DATETIME,
    exposed_time      FLOAT(4, 2),
    shift             VARCHAR(20),
    temperature       FLOAT(6, 3),
    humidity          FLOAT(6, 3),
    wind_velocity     FLOAT(6, 3),
    air_pressure      FLOAT(6, 3),
    a                 FLOAT(8, 4),
    b                 FLOAT(8, 4),
    c                 FLOAT(8, 4),
    d                 FLOAT(8, 4),
    e                 FLOAT(8, 4),
    f                 FLOAT(8, 4),
    g                 FLOAT(8, 4),
    h                 FLOAT(8, 4),
    sample_name_id    SMALLINT UNSIGNED,
    unit_id           SMALLINT UNSIGNED,
    report_id         SMALLINT UNSIGNED,
    notes             VARCHAR(300)
);

# 创建X射线检测表xray_info
CREATE TABLE xray_info
(
    xray_id       MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    station       VARCHAR(10)        NOT NULL,
    location      VARCHAR(10)        NOT NULL,
    product_model VARCHAR(20)        NOT NULL,
    service_time  DATETIME,
    test_day      DATETIME,
    power_light   TINYINT UNSIGNED DEFAULT 1,
    xray_light    TINYINT UNSIGNED DEFAULT 1,
    entrance      FLOAT(5, 3) UNSIGNED,
    exit_door     FLOAT(5, 3) UNSIGNED,
    left_wall     FLOAT(5, 3) UNSIGNED,
    right_wall    FLOAT(5, 3) UNSIGNED,
    top           FLOAT(5, 3) UNSIGNED,
    workbench     FLOAT(5, 3) UNSIGNED,
    exposed_num   TINYINT UNSIGNED,
    shift         VARCHAR(10)        NOT NULL,
    unit_id       SMALLINT UNSIGNED  NOT NULL,
    report_id     SMALLINT UNSIGNED  NOT NULL
);
