# !/usr/bin/env python
# -*- coding:utf-8 -*-
import logging


class Logger(object):
    def __init__(self, logfile, loglevel):
        """初始化Logger类
        logfile   日志文件
        loglevel  日志等级
        """
        self.logfile = logfile
        self.loglevel = loglevel

    def get_hdr(self):
        """获取日志的句柄
        如果日志文件不存在的话，则输出到屏幕
        """
        logger = logging.getLogger()
        if not self.logfile:
           #如果没有指定日志文件，获取屏幕输出流句柄
            log_handler = logging.StreamHandler()
        else:
            log_handler = logging.FileHandler(self.logfile)
        formatter = logging.Formatter('%(asctime)s - %(module)s.\
        %(funcName)12s- %(levelname)s - %(message)s')
                                      #时间，函数名，日志等级，消息
        log_handler.setFormatter(formatter)
        ll = (logging.CRITICAL, logging.ERROR, logging.WARNING,
              logging.INFO, logging.DEBUG)
        if not self.loglevel in range(1, 6):
            self.loglevel = 5
        logger.setLevel(ll[self.loglevel - 1])
        log_handler.setLevel(ll[self.loglevel - 1])
        logger.addHandler(log_handler)
        return logger

#  test

#if __name__ == '__main__':
#   log = Logger('/tmp/spider.log',5).get_logger()
#   log.error('ghjkl')
