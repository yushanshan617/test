# -*-coding: utf-8-*-
# -*-coding:gbk-*-
import json
import datetime
import logging
from logging.handlers import TimedRotatingFileHandler
import os
import pymysql
# import io
# import sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gbk')

def config_log():
    fmt = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
    log = logging.getLogger('')
    fileTimeHandler = TimedRotatingFileHandler('log/Read_shikaobang_json.log', "D", 1, 3)
    fileTimeHandler.suffix = "%Y%m%d"
    fileTimeHandler.setFormatter(logging.Formatter(fmt))
    logging.basicConfig(level=logging.DEBUG, format=fmt)
    log.addHandler(fileTimeHandler)

class ReadJson():

    def __init__(self):
        pass
    def get_fileName(self,rootdir):
        files = []
        try:
            fileList = os.listdir(rootdir)
            for i in range(0, len(fileList)):
                path = os.path.join(rootdir, fileList[i])
                if os.path.isdir(path):
                    files.extend(self.getFileName(path))
                if os.path.isfile(path):
                    self.getFileData(path)
        except Exception as e:
            logging.info(e)

    def getDatabase(self):
        # return pymysql.connect(host="rm-bp108682nces7278eqo.mysql.rds.aliyuncs.com", port=3306, user="year2001",
        #                        passwd="Pachong0920", db="spider", use_unicode=True, charset="utf8")
        return pymysql.connect(host="101.37.17.55", port=3306, user="yushanshan",
                               passwd="Yushanshan.123", db="test", use_unicode=True, charset="utf8")

    def getsqlData(self,file):
        print(file)

    def Selectsqltable(self):
        db = self.getDatabase()
        title = '2018-1-4'
        sql = "select id ,year from sp_shijuan "
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            # print(result)
            result = cursor.fetchall()
            print(result)
            db.commit()
        except Exception as e:
            logging.info("addErrorUrl Exception", e)
            db.rollback()
        db.close()

    def Inserttable(self):
        title = '2018-1-4'
        db = self.getDatabase()
        sql = "INSERT INTO sp_shijuan(title, province, city, area, year,update_date) " \
              "VALUES (%s, %s, %s, %s, %s, %s)"
        cursor = db.cursor()
        try:
            result = cursor.execute(sql, (title, title, title, title, title,title))
            db.commit()
        except Exception as e:
            logging.info("addErrorUrl Exception", e)
            db.rollback()
        db.close()

    def getFileData(self,path):
        nowdate = datetime.datetime.now().strftime('%Y-%m-%d')
        question_dict = {
            "laiyuan": "事考帮",
            "kaoshi_type": "教师招聘",
            "province": "广东",  # 省
            "jieduan": "",
            "kemu": "",
            "zhang": "",
            "jie": "",
            "zhishidian": "",
            "ti_type": "",  # 题目类型
            "yudue_content": "",  # 阅读理解内容
            "question": "",  # 问题
            "choice_a": "",
            "choice_b": "",
            "choice_c": "",
            "choice_d": "",
            "choice_e": "",
            "choice_f": "",
            "right_awswer": "",  # 正确答案
            "jiexi": "",  # 题目解析
            "chuchu": "",  # 出自哪套真题目
            "qufen": "",  # 真题专题
            "insert_date": nowdate,
            "yuedu_pic1": "",
            "yuedu_pic2": "",
            "yuedu_pic3": "",
            "question_pic": "",
            "choice_pic": "",
            "jiexi_pic": ""  # 解析图片

        }
        f = open(path, encoding="utf-8")
        files = json.load(f)
        all_questions = files["data"]["questions"]
        common = files["data"]["common"]
        self.getsqlData(common)
    #     question_dict["chuchu"] = files["data"]["common"]["title"]
    #     for questions_id, questions_info in all_questions.items():
    #         if questions_info["t"] == "single":
    #             self.__handling_single_question(questions_info, question_dict)  # 处理单选
    #         elif questions_info["t"] == "multiple":
    #             self.__handling_multiple_question(questions_info, question_dict)
    #         elif questions_info["t"] == "judge":
    #             self.__handling_judge_question(questions_info, question_dict)
    #         else:
    #             self.__handling_other_question(questions_info,question_dict)
    #
    # def __handling_single_question(self, singleQuesion, question_dict):
    #         question_dict["ti_type"] = "单选"
    #         try:
    #             question_dict["question"] = singleQuesion["c"]["c"]      # 拿到单选题题目
    #             question_dict["choice_a"] = singleQuesion["a"]["opt"][0]['c']
    #             question_dict["choice_b"] = singleQuesion["a"]["opt"][1]['c']
    #             question_dict["choice_c"] = singleQuesion["a"]["opt"][2]['c']
    #             question_dict["choice_d"] = singleQuesion["a"]["opt"][3]['c']
    #             question_dict["right_awswer"] = singleQuesion["a"]["a"]
    #             question_dict["jiexi"] = singleQuesion["p"]["c"]      # 拿到题目解析
    #         except Exception as e:
    #             logging.info(e)
    #         self.addContent(question_dict)
    #         logging.info("add mysql success!")
    #
    # # 处理多选题
    # def  __handling_multiple_question(self, multipleQuesion,question_dict):
    #     question_dict["ti_type"] = "多选"
    #     try:
    #         question_dict["question"] = multipleQuesion["c"]["c"]  # 拿到多选题题目
    #         question_dict["choice_a"] = multipleQuesion["a"]["opt"][0]['c']
    #         question_dict["choice_b"] = multipleQuesion["a"]["opt"][1]['c']
    #         question_dict["choice_c"] = multipleQuesion["a"]["opt"][2]['c']
    #         question_dict["choice_d"] = multipleQuesion["a"]["opt"][3]['c']
    #         question_dict["right_awswer"] = multipleQuesion["a"]["a"]
    #         question_dict["jiexi"] = multipleQuesion["p"]["c"]  # 拿到题目解析
    #     except Exception as e:
    #         logging.info(e)
    #     self.addContent(question_dict)
    #     logging.info("add mysql success!")
    #
    # # 处理判断题
    # def  __handling_judge_question(self,judgeQuestion,question_dict):
    #     question_dict["ti_type"] = "判断"
    #     try:
    #         question_dict["question"] = judgeQuestion["c"]["c"]  # 拿到多选题题目
    #         question_dict["choice_a"] = judgeQuestion["a"]["opt"][0]['c']
    #         question_dict["choice_b"] = judgeQuestion["a"]["opt"][1]['c']
    #         question_dict["choice_c"] = ""
    #         question_dict["choice_d"] = ""
    #         right_awser= judgeQuestion["a"]["a"]
    #         if right_awser == "t":
    #             question_dict["right_awswer"]="对"
    #         if right_awser == "f":
    #             question_dict["right_awswer"]="错"
    #         question_dict["jiexi"] = judgeQuestion["p"]["c"]  # 拿到题目解析
    #     except Exception as e:
    #         logging.info(e)
    #     self.addContent(question_dict)
    #     logging.info("add mysql success!")
    #
    # def  __handling_other_question(self,otherQuestion,question_dict):
    #     question_dict["choice_a"] = ""
    #     question_dict["choice_b"] = ""
    #     question_dict["choice_c"] = ""
    #     question_dict["choice_d"] = ""
    #     try:
    #         question_dict["ti_type"] = otherQuestion["t"]
    #         question_dict["jiexi"] = otherQuestion["p"]["c"]  # 拿到题目解析
    #         question_dict["question"] = otherQuestion["c"]["c"]  # 拿到单选题题目
    #         question_dict["right_awswer"] = otherQuestion["a"]["a"]
    #         question_dict["choice_a"] = otherQuestion["a"]["opt"][0]['c']
    #         question_dict["choice_b"] = otherQuestion["a"]["opt"][1]['c']
    #         question_dict["choice_c"] = otherQuestion["a"]["opt"][2]['c']
    #         question_dict["choice_d"] = otherQuestion["a"]["opt"][3]['c']
    #     except  Exception as e :
    #         logging.info(e)
    #     self.addContent(question_dict)
    #     logging.info("add mysql success!")
    #
    #
    # def addContent(self,dict):
    #     db = self.getDatabase()
    #     sql = "INSERT INTO sp_tiku(laiyuan, kaoshi_type, province, jieduan, kemu, zhang,jie,zhishidian,ti_type,yudue_content,question,choice_a,choice_b,choice_c,choice_d,choice_e,choice_f,right_awswer,jiexi,chuchu,qufen,insert_date,yuedu_pic1,yuedu_pic2,yuedu_pic3,question_pic,choice_pic,jiexi_pic) \
    #     			   VALUES (%s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    #     cursor = db.cursor()
    #     try:
    #         result = cursor.execute(sql, (dict['laiyuan'], dict['kaoshi_type'], dict['province'], dict['jieduan'], dict['kemu'], dict['zhang'],dict['jie'],dict['zhishidian'],dict['ti_type'],dict['yudue_content'],dict['question'],dict['choice_a'],dict['choice_b'],dict['choice_c'],dict['choice_d'],dict['choice_e'],dict['choice_f'],dict['right_awswer'],dict['jiexi'],
    #                                       dict['chuchu'],dict['qufen'],dict['insert_date'],dict['yuedu_pic1'],dict['yuedu_pic2'],dict['yuedu_pic3'],dict['question_pic'],dict['choice_pic'],dict['jiexi_pic']))
    #         db.commit()
    #     except Exception as e:
    #         logging.info("addErrorUrl Exception", e)
    #         db.rollback()
    #     db.close()

    def SaveWordFile(self):
        pass

if __name__=="__main__":
    config_log()
    readJson = ReadJson()
    # readJson.get_fileName('广东')
    # readJson.Inserttable()
    readJson.Selectsqltable()


