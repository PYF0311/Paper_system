import pymysql
import re


def connect_db():
    db = pymysql.connect(host='localhost',user='###',password='###',db='###')
    return db

def verify_user_exist(user):
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql = "SELECT stuId FROM stu_info where stuId = %s"
            cursor.execute(sql,(user,))
            result = str(cursor.fetchone())
            result = re.sub('[^a-zA-Z0-9]',"",result)
            #print("result:",result)
            if user == result:
                return True
               
    finally:
        db.close()

def verify_password(username,password):
    #print("beforedb user:",username)
    db =connect_db()
    try:
        with db.cursor() as cursor:
            sql = "SELECT password FROM stu_info WHERE stuId = %s"
            #print(sql)
            cursor.execute(sql,(username,))
            result = str(cursor.fetchone())
            result = re.sub('[^a-zA-Z0-9]',"",result)
        
            if password == result:
                return True
    finally:
        db.close()
def test():
    db = connect_db() 
    try:
        with db.cursor() as cursor:
            sql1="select count(*) from academic_paper_info;"
            duoshaoge=cursor.execute(sql1)
            result = cursor.fetchone()
            print(result)           
    finally:
        db.close()



def add_info_to_db(form):
    db = connect_db()

    tag = form['tag']
    if tag == 'academic_paper':
        try:
            with db.cursor() as cursor:
                sql1 = "select count(*) from academic_paper_info;"
                cursor.execute(sql1)
                result=str(cursor.fetchone())
                querynum=int(re.sub('["(),\']','',result))+1
                sql = "INSERT INTO `academic_paper_info` VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                try:
                    cursor.execute(sql, (querynum, form['acadPaperNameCH'], form['acadPaperNameEN'], form['issueName'], "2007-10-01", form['pubIssue'], form['pubPeriod'], form['pubPage'], form['depa'], form['paperType'], form['indexNum'], form['part'], form['impactFactor']))
                    db.commit()
                except:
                    db.rollback()
                
                print("firstedit:",form['FirstEdit'], form['SecondEdit'])
                sql = "INSERT INTO `academic_paper_edit` VALUES (%s, %s, %s, %s, %s, %s ) "
                try:
                    cursor.execute(sql, (querynum, form['FirstEdit'], form['SecondEdit'], form['ThreeEdit'], form['ForthEdit'], form['transEdit'])) 
                    db.commit()
                except:
                    db.rollback()
                              
        finally:
            db.close()
    elif tag == 'conference_paper':
        try:
            with db.cursor() as cursor:
                sql1 = "select count(*) from conference_paper_info;"
                cursor.execute(sql1)
                result=str(cursor.fetchone())
                querynum=int(re.sub('["(),\']','',result))+1

                sql = "INSERT INTO `conference_paper_info` VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                try:    
                    print("here!")

                    cursor.execute(sql, (querynum, form['confPaperNameCH'], form['confPaperNameEN'], form['confName'], form['confTime'], form['confAddress'], form['confHost'], form['paperType'], form['confType'], form['ifPub'], form['pubTime'], form['depa'], form['pubIssue'],form['pubPeriod'],form['pubPage'],form['issueType'],form['indexNum'],form['part'],form['impactFactor'] ))
                    db.commit()
                except:
                    db.rollback()

                sql = "INSERT INTO `conference_paper_edit` VALUES (%s, %s, %s, %s, %s, %s ) "
                try:
                    print("here!!")
                    cursor.execute(sql, (querynum, form['FirstEdit'], form['SecondEdit'], form['ThreeEdit'], form['ForthEdit'], form['transEdit']))               
                    db.commit()
                except:
                    db.rollback()
        finally:
            db.close()
    elif tag == 'patent':
        try:
            with db.cursor() as cursor:
                sql1 = "select count(*) from patent_info;"
                cursor.execute(sql1)
                result=str(cursor.fetchone())
                querynum=int(re.sub('["(),\']','',result))+1

                sql = "INSERT INTO `patent_info` VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                try:
                    cursor.execute(sql, (querynum, form['patentNameCH'], form['patentNameEN'], form['patentType'], form['patentApplyTime'], form['ifAuthority'], form['patentAuthorityTime'], form['ifTransfer'], form['transferSource'], form['transferComment']))
                    db.commit()
                except:
                    db.rollback()

                sql = "INSERT INTO `patent_edit` VALUES (%s, %s, %s, %s ) "
                try:
                    cursor.execute(sql, (querynum, form['FirstEdit'], form['SecondEdit'], form['ThreeEdit']))
                    db.commit()
                except:
                    db.rollback()
        finally:
            db.close()

    elif tag == 'project':
        try:
            with db.cursor() as cursor:
                sql1 = "select count(*) from project_info;"
                cursor.execute(sql1)
                result=str(cursor.fetchone())
                querynum=int(re.sub('["(),\']','',result))+1

                sql = "INSERT INTO `project_info` VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                try:
                    cursor.execute(sql, (querynum, form['projectName'], form['projectSourceType'], form['projectHost'], form['projectFond'], form['projectBeginTime'], form['projectFinTime'], form['projectTask']))
                    db.commit()
                except:
                    db.rollback()
                sql = "INSERT INTO `project_edit` VALUES (%s, %s, %s, %s ) "
                try:
                    cursor.execute(sql, (querynum, form['FirstEdit'], form['SecondEdit'], form['ThreeEdit']))               
                    db.commit()
                except:
                    db.rollback() 

        finally:
            db.close()

def show_info_from_db(userId):  #查询学号对应的同学所有的文章
    resultset = []
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql = "SELECT stuName FROM stu_info WHERE stuId= %s"
            cursor.execute(sql,(userId,))
            stuName = str(cursor.fetchall())
            stuName = re.sub('["(),\']','',stuName)
            print(stuName)
            temp=list(show_academic_from_db(stuName))
            if len(temp):
                temp.append('学术论文')
                resultset.append(temp)

            temp=list(show_conference_from_db(stuName))
            if len(temp):
                temp.append('会议论文')
                resultset.append(temp)
            
            temp=list(show_patent_from_db(stuName))
            if len(temp):
                temp.append('专利')
                resultset.append(temp)
            temp=list(show_project_from_db(stuName))
            if len(temp):
                temp.append('项目')  
                resultset.append(temp)
            return (resultset)
    finally:
        db.close()

def all_paper_from_db():
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql= "SELECT academic_paper_edit.acadPaperId, `firstEdit`,`secondEdit`,`thirdEdit`,acadPaperNameCH,issueName,pubTime,pubIssue,pubPage from `academic_paper_edit`,`academic_paper_info` WHERE (academic_paper_edit.acadPaperId = academic_paper_info.acadPaperId) "
            cursor.execute(sql)
            result= cursor.fetchall()
            return (result)
    finally:
        db.close() 

def show_academic_from_db(stuName):#查询姓名对应的学术论文
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql= "SELECT academic_paper_edit.acadPaperId, `acadPaperNameCH` from `academic_paper_edit`,`academic_paper_info` WHERE (academic_paper_edit.acadPaperId = academic_paper_info.acadPaperId) and (firstEdit = %s or secondEdit = %s or fourthEdit = %s or thirdEdit = %s)"
            cursor.execute(sql,(stuName,stuName,stuName,stuName,))
            result= cursor.fetchall()
            return (result)
    finally:
        db.close() 

def show_conference_from_db(stuName):#查询姓名对应的会议论文
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql= "SELECT conference_paper_edit.confPaperId, `confPaperNameCH` from `conference_paper_edit`,`conference_paper_info` WHERE (conference_paper_edit.confPaperId = conference_paper_info.confPaperId) and (firstEdit = %s or secondEdit = %s or fourthEdit = %s or thirdEdit = %s)"
            cursor.execute(sql,(stuName,stuName,stuName,stuName,))
            result= cursor.fetchall()
            return (result)
    finally:
        db.close()

def show_patent_from_db(stuName):#查询姓名对应的专利
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql= "SELECT patent_edit.patentId, `patentNameCH` from `patent_edit`,`patent_info` WHERE (patent_edit.patentId = patent_info.patentId) and (firstEdit = %s or secondEdit = %s or fourthEdit = %s or thirdEdit = %s)"

            cursor.execute(sql,(stuName,stuName,stuName,stuName,))
            result= cursor.fetchall()
            return (result)
    finally:
        db.close()

def show_project_from_db(stuName):#查询姓名对应的项目
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql= "SELECT project_edit.projectId, `projectName` from `project_info`,`project_edit` WHERE (project_edit.projectId = project_info.projectId) and (firstEdit = %s or secondEdit = %s or fourthEdit = %s or thirdEdit = %s)"

            cursor.execute(sql,(stuName,stuName,stuName,stuName,))
            result= cursor.fetchall()
            return (result)
    finally:
        db.close()

def add_stu_info_to_db(form):#注册
    db =connect_db()
    try:
        with db.cursor() as cursor:
            sql = "INSERT INTO `stu_info` VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql,(form['stuid'],form['password'],form['stuname'],form['major'],form['firstProf'],form['secondProf']))
            result = cursor.fetchall()
            db.commit()
            print(result)
    finally:
        db.close() 

def show_more_academic_info_from_db(multi_object):
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql='SELECT academic_paper_edit.acadPaperId,'+multi_object+ ' from `academic_paper_edit`,`academic_paper_info` WHERE (academic_paper_edit.acadPaperId = academic_paper_info.acadPaperId)'
            print(sql)
            cursor.execute(sql)
            result= cursor.fetchall()
            return (result)
    finally:
        db.close()  

def show_more_conference_info_from_db(multi_object):
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql='SELECT conference_paper_edit.confPaperId,'+multi_object+ ' from `conference_paper_edit`,`conference_paper_info` WHERE (conference_paper_edit.confPaperId = conference_paper_info.confPaperId)'
            print(sql)
            cursor.execute(sql)
            result= cursor.fetchall()
            return (result)
    finally:
        db.close() 

def show_more_patent_info_from_db(multi_object):
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql='SELECT patent_edit.patentId,'+multi_object+ ' from `patent_edit`,`patent_info` WHERE (patent_edit.patentId = patent_info.patentId)'
            print(sql)
            cursor.execute(sql)
            result= cursor.fetchall()
            return (result)
    finally:
        db.close() 

def show_more_project_info_from_db(multi_object):
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql='SELECT project_edit.projectId,'+multi_object+ ' from `project_edit`,`project_info` WHERE (project_edit.projectId = project_info.projectId)'
            print(sql)
            cursor.execute(sql)
            result= cursor.fetchall()
            return (result)
    finally:
        db.close() 

def show_stuname_from_db(userId):
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql = "SELECT stuName FROM stu_info WHERE stuId= %s"
            cursor.execute(sql,(userId,))
            stuName = str(cursor.fetchall())
            stuName = re.sub('["(),\']','',stuName)
            return (stuName)           
    finally:
        db.close() 
