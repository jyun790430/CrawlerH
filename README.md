i# CrawlerH
This project is crawl pronhub, xvideos two sites and provides video download

## Environment, Architecture

Language: Python2.7
Database : Mysql

## Instructions for use

#### Pre-boot configuration

* Install Python dependent modules：Scrapy, pymysql, requests or `pip install -r requirements.txt`
* Modify the configuration by needed and the config path is  `Setting/config.py`

#### Start up

* python Xvideos/quickstart.py
* python Pronhub/quickstart.py
* python Download/run.py


## Database description

The table in the database that holds the data is `crawl_video`. The following is a table schema:

#### crawl_video table schema：

```
CREATE TABLE `crawl_video` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` smallint(6) NOT NULL COMMENT '1:xvideos 2: pronoun ',
  `name` text,
  `file_name` varchar(255) NOT NULL,
  `tags` text,
  `categories` text,
  `download` tinyint(4) NOT NULL DEFAULT '0',
  `origin_url` text,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `status` tinyint(4) DEFAULT '0' COMMENT '1: url 解析異常 2: url 轉檔案異常 3. 影片下載中',
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_md5_url` (`file_name`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=12250 DEFAULT CHARSET=utf8;
```

