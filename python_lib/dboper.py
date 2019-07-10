#!/usr/bin/env python3
# coding=utf-8

import pymysql
import sys
import re
import logging

logger = logging.getLogger("sdlog")

class DBHelper():
    # 构造函数,初始化数据库连接
    def __init__(self,db_config,params=None):
        self.params = params
        self.conn = None
        self.cur = None
        self.db_config=db_config

    def connectiondatabase(self):
        try:
            self.conn = pymysql.connect(self.db_config['host'],self.db_config['username'],
                                    self.db_config['password'],self.db_config['database'],charset=self.db_config['charset'])
        except:
            logger.error("connectDatabase failed")
            return False
        self.cur = self.conn.cursor()
        logger.info("database is connected to:"+self.db_config["host"]+":"+str(self.db_config["port"]))
        return True



    # 关闭数据库
    def closedatabase(self):
        # 如果数据打开，则关闭；否则没有操作
        if self.conn and self.cur:
            self.cur.close()
            self.conn.close()
        return True

    # 执行数据库的sq语句,主要用来做插入操作
    def execute(self,sql):
        #self.connectiondatabase()
        try:
            logger.info("execute:"+sql)
            if self.conn and self.cur:
                # 正常逻辑，执行sql，提交操作
                self.cur.execute(sql,self.params)
                self.conn.commit()
        except:
            logger.error("execute failed: " + sql)
            logger.error("params: " + self.params)
            self.closedatabase()
            return False
        return True
        
    # 用来查询表数据
    def select(self,sql):
        #self.connectiondatabase()

        logger.info("execute:"+sql)
        self.cur.execute(sql,self.params)
        result = self.cur.fetchall()
 #      print(result)
        return result

    # check the table exist or not
    def tableExist(self,table_name):
        sql = "show tables;"
        self.cur.execute(sql)
        tables = [self.cur.fetchall()]
        table_list = re.findall('(\'.*?\')',str(tables))
        table_list = [re.sub("'",'',each) for each in table_list]
        if table_name in table_list:
            return True
        else:
            return False
        
