import pymysql
import time 

class Database:
    def __init__(self):
        self.db= pymysql.connect(host='localhost', user='mrchoidb',password='centos1!', db='class01')
        self.cur = self.cur.cursor()
        print("good")

    def selectAllJson(self):
        sql = "select * from ultrasonicsensor;"
        self.cur.execute(sql)
        result = self.cur.ftechall()
        return result

    def insertJson(self, hum, temper):
        tm = time.localtime()
        yeardate = "{}-{}-{}",format(tm.tm_year, tm.tm_mon, tm.tm_mday)
        nowtime = "{}:{}:{}",format(tm.tm_hour, tm.tm_min, tm.tm_sec)
        
