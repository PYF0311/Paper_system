import pymysql
import re


def connect_db():
    db = pymysql.connect(host='localhost',user='root',password='JMU-bec2017',db='PaperSystem',charset="utf8")
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

def verify_tec_exist(user):

    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql = "SELECT tecName FROM tec_info where tecName = %s"
            cursor.execute(sql,(user,))
            result = cursor.fetchone()
            result = result[0]
            #print("result:",result)
            if user == result:
                return True
               
    finally:
        db.close()

def verify_admin_exist(user):
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql = "SELECT adminId FROM admin_info where adminId = %s"
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

def motify_stu_password(stuid,password):
    db =connect_db()
    print(stuid,password)
    try:
        with db.cursor() as cursor:
            sql = "UPDATE `stu_info` SET password = %s WHERE stuId = %s"
            try:
                cursor.execute(sql,(password,stuid,))
                db.commit()

                msg = True
            except:
                db.rollback()

                msg = False

    finally:
        db.close()
    return msg

def motify_tec_password(stuid,password):
    db =connect_db()
    print(stuid,password)
    try:
        with db.cursor() as cursor:
            sql = "UPDATE `tec_info` SET password = %s WHERE tecId = %s"
            try:
                cursor.execute(sql,(password,stuid,))
                db.commit()

                msg = True
            except:
                db.rollback()

                msg = False

    finally:
        db.close()
    return msg

def verify_admin_password(username,password):
    db = connect_db()
    try:
        with db.cursor() as cursor:
            sql = "SELECT password FROM admin_info WHERE adminId = %s"
            cursor.execute(sql,(username,))
            result = str(cursor.fetchone())
            result = re.sub('[^a-zA-Z0-9]',"",result)
            if password == result:
                return True
    finally:
        db.close()

def verify_tec_password(username,password):
    db = connect_db()
    try:
        with db.cursor() as cursor:
            sql = "SELECT password FROM tec_info WHERE tecName = %s"
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



def add_info_to_db(form): #添加数据
    db = connect_db()
    tag = form['tag']
    if tag == 'academic_paper':
  
        try:
            with db.cursor() as cursor:
                form['pubPage']=form['pubPage1']+"-"+form['pubPage2']
                sql1 = "select max(acadPaperId) from academic_paper_info;"
                cursor.execute(sql1)
                result=cursor.fetchone()[0]
                if result is None:
                    querynum = 1
                else:
                    querynum=int(result)+1
                
                sql = "INSERT INTO `academic_paper_info` VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                try:
                    cursor.execute(sql, (querynum, form['acadPaperNameCH'], form['acadPaperNameEN'], form['pubTime'], form['pubIssue'], form['pubPeriod'], form['pubPage'], form['paperType'], form['issueNameCH'], form['issueNameEN'], form['impactFactor'], form['indexNum']))
                    db.commit()
                    result1 = True
                except:
                    db.rollback()
                    result1 = False
                
                sql = "INSERT INTO `academic_paper_edit` VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s ) "

                try:
                    print((querynum, form['firstEdit'], form['secondEdit'], form['thirdEdit'], form['fourthEdit'], form['fifthEdit'], form['sixthEdit'], form['seventhEdit'], form['eighthEdit'],form['transEdit']))
                    cursor.execute(sql, (querynum, form['firstEdit'], form['secondEdit'], form['thirdEdit'], form['fourthEdit'], form['fifthEdit'], form['sixthEdit'], form['seventhEdit'], form['eighthEdit'],form['transEdit'])) 
                    db.commit()
                    result2 = True
                except:
                    db.rollback()
                    result2 = False
                              
        finally:
            db.close()
        result = result1 and result2
        return result
    elif tag == 'monograph':
        try:
            with db.cursor() as cursor:
                
                sql1 = "select max(publicationId) from publication_info;"
                cursor.execute(sql1)
                result = cursor.fetchone()[0]
                if result is None:
                    querynum = 1
                else:
                    querynum = int(result) + 1
                
                sql = "INSERT INTO `publication_info` VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                try:    
                    cursor.execute(sql, (querynum, form['publicationNameCH'], form['publicationNameEN'], form['editor'], form['editType'], form['pubTime'], form['pubUnit'], form['ISSN'], form['wordsNum'], form['mainContent']))
                    db.commit()
                    result = True
                except:
                    db.rollback()
                    result = False
        finally:
            db.close()
        return result
    elif tag == 'patent':
        try:
            with db.cursor() as cursor:
                sql1 = "SELECT max(patentId) FROM patent_info;"
                cursor.execute(sql1)
                result=cursor.fetchone()[0]
                if result is None:
                    querynum = 1
                else:
                    querynum=int(result)+1

                sql = "INSERT INTO `patent_info` VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                
                try:
                    print(querynum, form['patentNameCH'], form['patentNameEN'], form['patentType'], form['patentApplyTime'], form['ifAuthority'], form['patentAuthorityTime'], form['ifTransfer'], form['transferSource'], form['transferComment'],form['patentNum'])
                    cursor.execute(sql, (querynum, form['patentNameCH'], form['patentNameEN'], form['patentType'], form['patentApplyTime'], form['ifAuthority'], form['patentAuthorityTime'], form['ifTransfer'], form['transferSource'], form['transferComment'],form['patentNum']))
                    db.commit()
                    result = True
                except:
                    db.rollback()
                    result = False

                sql = "INSERT INTO `patent_edit` VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s )"
                try:
                    cursor.execute(sql, (querynum, form['firstEdit'], form['secondEdit'], form['thirdEdit'],form['fourthEdit'],form['fifthEdit'],form['sixthEdit'],form['seventhEdit'],form['eighthEdit']))
                    db.commit()
                    result = True
                except:
                    db.rollback()
                    result = False
        finally:
            db.close()
        return result
    elif tag == 'project':
        try:
            with db.cursor() as cursor:
                sql = "INSERT INTO `project_info` VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                try:
                     
                    cursor.execute(sql, (form['projectId'], form['projectHost'], form['projectFond'], form['projectBeginTime'], form['projectFinTime'], form['projectTask'], form['projectNameCH'], form['projectNameEN'], form['projectLevel']))
                    db.commit()
                    result = True
                except:
                    db.rollback()
                    result = False
                sql = "INSERT INTO `project_edit` VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s ) "
                
                try:
                    cursor.execute(sql, (form['projectId'], form['firstEdit'], form['secondEdit'], form['thirdEdit'],form['fourthEdit'],form['fifthEdit'],form['sixthEdit'],form['seventhEdit'],form['eighthEdit']))            
                    db.commit()
                    result = True
                except:
                    db.rollback() 
                    result = False

        finally:
            db.close()
        return result
    elif tag == 'standard':
        try:
            with db.cursor() as cursor:
                sql1 = "select max(standardId) from standard;"
                cursor.execute(sql1)
                result=cursor.fetchone()[0]
                if result is None:
                    querynum = 1
                else:
                    querynum=int(result)+1
                
                sql = "INSERT INTO `standard` VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                try:
                    cursor.execute(sql, (querynum, form['standardNameCH'], form['standardNameEN'], form['standardType'], form['standardNum'], form['standardAdd'], form['standardDate'], form['editor']))
                    db.commit()
                    result = True
                except:
                    db.rollback()
                    result = False
        finally:
            db.close()
        return result
    elif tag == 'degree':
        try:
            with db.cursor() as cursor:
                sql1 = "select max(degPaperId) from degree_paper;"
                cursor.execute(sql1)
                result=cursor.fetchone()[0]
                if result is None:
                    querynum = 1
                else:
                    querynum=int(result)+1
                    
                sql = "INSERT INTO `degree_paper` VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                try:
                    cursor.execute(sql, (querynum, form['degPaperNameCH'], form['degPaperNameEN'], form['degType'], form['editor'], form['firstProf'], form['secondProf'], form['gradUnit'], form['gradAdd'], form['gradDate']))
                    db.commit()
                    result = True
                except:
                    db.rollback()
                    result = False
        finally:
            db.close()
        return result

def add_multi_aca(df):
    db = connect_db()
    try:
        with db.cursor() as cursor:
            sql1 = "select max(acadPaperId) from academic_paper_info;"
            cursor.execute(sql1)
            result=cursor.fetchone()[0]
            if result is None:
                querynum = 1
            else:
                querynum=int(result)+1
            
            sql = "INSERT INTO `academic_paper_info` VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            try:
                cursor.execute(sql, (querynum, df[0], df[1], df[12], df[13], df[14], df[15], df[16], df[11], None, df[18], df[17]))
                db.commit()
                result1 = True
            except:
                db.rollback()
                result1 = False

            sql = "INSERT INTO `academic_paper_edit` VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s ) "
            try:
                cursor.execute(sql, (querynum, df[2],df[3],df[4],df[5],df[6], df[7], df[8], df[9],df[10])) 
                db.commit()
                result2 = True
            except:
                db.rollback()
                result2 = False
                          
    finally:
        db.close()
    result = result1 and result2
    print("result",result)
    return result

def add_multi_pat(df):
    db = connect_db()
    try:
        with db.cursor() as cursor:
            sql1 = "SELECT max(patentId) FROM patent_info;"
            cursor.execute(sql1)
            result=cursor.fetchone()[0]
            if result is None:
                querynum = 1
            else:
                querynum=int(result)+1
            
            sql = "INSERT INTO `patent_info` VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            try:
                cursor.execute(sql, (querynum, df[0], df[1], df[12], df[13], df[14], df[15], df[16], df[11], None, df[18], df[17]))
                db.commit()
                result1 = True
            except:
                db.rollback()
                result1 = False

            sql = "INSERT INTO `patent_edit` VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s )"
            try:
                cursor.execute(sql, (querynum, df[2],df[3],df[4],df[5],df[6], df[7], df[8], df[9],df[10])) 
                db.commit()
                result2 = True
            except:
                db.rollback()
                result2 = False
                          
    finally:
        db.close()
    result = result1 and result2
    print("result",result)
    return result


def del_from_data(result): #删除指定元素
    print(result)
    tag = result[1]

    if tag =='期刊论文':
        msg = del_from_academic(result[0])
    elif tag == '学位论文':
        msg = del_from_degree(result[0])
    elif tag == '专著':
        msg = del_from_monograph(result[0])
    elif tag == '专利':
        msg = del_from_patent(result[0])
    elif tag == '参加项目':
        msg = del_from_project(result[0])
    elif tag == '标准':
        msg = del_from_standard(result[0])
    return msg

def del_from_academic(lid):
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql = "DELETE FROM `academic_paper_info` WHERE acadPaperId = %s"
            cursor.execute(sql,(lid,))
            try:
                cursor.execute(sql,(lid,))
                db.commit()
                msg = "ok"
            except:
                db.rollback()
                msg = "error"
    finally:
        db.close()
    return msg
def del_from_degree(lid):
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql = "DELETE FROM `degree_paper` WHERE degPaperId = %s"
            cursor.execute(sql,(lid,))
            try:
                cursor.execute(sql,(lid,))
                db.commit()
                msg = "ok"
            except:
                db.rollback()
                msg = "error"
    finally:
        db.close()
    return msg
def del_from_monograph(lid):
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql = "DELETE FROM `publication_info` WHERE publicationId = %s"
            cursor.execute(sql,(lid,))
            try:
                cursor.execute(sql,(lid,))
                db.commit()
                msg = "数据删除成功"
            except:
                db.rollback()
                msg = "数据删除失败"
    finally:
        db.close()
    return msg
def del_from_patent(lid):
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql = "DELETE FROM `patent_info` WHERE patentId = %s"
            cursor.execute(sql,(lid,))
            try:
                cursor.execute(sql,(lid,))
                db.commit()
                msg = "数据删除成功"
            except:
                db.rollback()
                msg = "数据删除失败"
    finally:
        db.close()
    return msg
def del_from_project(lid):
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql = "DELETE FROM `project_edit` WHERE projectId = %s"
            cursor.execute(sql,(lid,))
            try:
                cursor.execute(sql,(lid,))
                db.commit()
                msg = "数据删除成功"
            except:
                db.rollback()
                msg = "数据删除失败"
    finally:
        db.close()
    return msg
def del_from_standard(lid):
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql = "DELETE FROM `standard` WHERE standardId = %s"
            cursor.execute(sql,(lid,))
            try:
                cursor.execute(sql,(lid,))
                db.commit()
                msg = "数据删除成功"
            except:
                db.rollback()
                msg = "数据删除失败"
    finally:
        db.close()
    return msg
def del_from_stu(stuid):
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql = "DELETE FROM `stu_info` WHERE stuId = %s"
            cursor.execute(sql,(stuid,))
            try:
                cursor.execute(sql,(stuid,))
                db.commit()
                result = True
            except:
                db.rollback()
                result = False
    finally:
        db.close()
    return result

def del_from_tec(tecid):
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql = "DELETE FROM `tec_info` WHERE tecId = %s"
            try:
                cursor.execute(sql,(tecid,))
                db.commit()
                result = True
            except:
                db.rollback()
                result = False
    finally:
        db.close()
    return result

def show_info_from_db(userId):  #查询学号对应的同学所有的文章
    print(userId)
    resultset = []
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql = "SELECT stuName FROM stu_info WHERE stuId= %s"
            cursor.execute(sql,(userId,))
            stuName = str(cursor.fetchall())
            stuName = re.sub('["(),\']','',stuName)
            temp=list(show_academic_from_db(stuName))
            if len(temp):
                temp.append('期刊论文')
                resultset.append(temp)
                #print(resultset)
            temp=list(show_monograph_from_db(stuName))
            if len(temp):
                temp.append('专著')
                resultset.append(temp)
                #print(resultset)
            temp=list(show_degree_from_db(stuName))
            if len(temp):
                temp.append('学位论文')
                resultset.append(temp)
                #print(resultset)
            temp=list(show_patent_from_db(stuName))
            if len(temp):
                temp.append('专利')
                resultset.append(temp)
                #print(resultset)
            temp=list(show_project_from_db(stuName))
            if len(temp):
                temp.append('参加项目')
                resultset.append(temp)
                #print(resultset)
            temp=list(show_standard_from_db(stuName))
            if len(temp):
                temp.append('标准')
                resultset.append(temp)
               # print(resultset)
            return (resultset)
    finally:
        db.close()

def show_tec_info_from_db(userId):  #查询学号对应的老师所有的文章
    resultset = []
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql = "SELECT tecName FROM tec_info WHERE tecId= %s"
            cursor.execute(sql,(userId,))
            tecName = str(cursor.fetchall())
            tecName = re.sub('["(),\']','',tecName)
            temp=list(show_academic_from_db(tecName))
            if len(temp):
                temp.append('期刊论文')
                resultset.append(temp)
                #print(resultset)
            temp=list(show_monograph_from_db(tecName))
            if len(temp):
                temp.append('专著')
                resultset.append(temp)
                #print(resultset)
            temp=list(show_degree_from_db(tecName))
            if len(temp):
                temp.append('学位论文')
                resultset.append(temp)
                #print(resultset)
            temp=list(show_patent_from_db(tecName))
            if len(temp):
                temp.append('专利')
                resultset.append(temp)
                #print(resultset)
            temp=list(show_project_from_db(tecName))
            if len(temp):
                temp.append('参加项目')
                resultset.append(temp)
                #print(resultset)
            temp=list(show_standard_from_db(tecName))
            if len(temp):
                temp.append('标准')
                resultset.append(temp)
               # print(resultset)
            return (resultset)
    finally:
        db.close()
def select_academic_from_db(postid): #查询对应文章号的学术论文
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql= "SELECT * from `academic_paper_info`, `academic_paper_edit` WHERE (academic_paper_edit.acadPaperId = academic_paper_info.acadPaperId and academic_paper_info.acadPaperId = %s) "
            cursor.execute(sql,(postid,))
            result= cursor.fetchall()
            return (result)
    finally:
        db.close() 

def select_degree_from_db(postid):
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql= "SELECT * from `degree_paper` WHERE (degPaperId = %s) "
            cursor.execute(sql,(postid,))
            result= cursor.fetchall()
            return (result)
    finally:
        db.close() 

def select_patent_from_db(postid):
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql= "SELECT * from `patent_info`, `patent_edit` WHERE (patent_edit.patentId = patent_info.patentId and patent_info.patentId = %s) "
            cursor.execute(sql,(postid,))
            result= cursor.fetchall()
            return (result)
    finally:
        db.close() 

def select_project_from_db(postid):
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql= "SELECT * from `project_info`, `project_edit` WHERE (project_edit.projectId = project_info.projectId and project_info.projectId = %s) "
            cursor.execute(sql,(postid,))
            result= cursor.fetchall()
            return (result)
    finally:
        db.close() 

def select_mono_from_db(postid):
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql= "SELECT * from `publication_info` WHERE (publicationId = %s)"
            cursor.execute(sql,(postid,))
            result= cursor.fetchall()
            return (result)
    finally:
        db.close() 

def select_stand_from_db(postid):
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql= "SELECT * from `standard` WHERE (standardId = %s)"
            cursor.execute(sql,(postid,))
            result= cursor.fetchall()
            return (result)
    finally:
        db.close() 

def all_academic_from_db(): #查询全部学术论文
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql= "SELECT * from `academic_paper_info`, `academic_paper_edit` WHERE (academic_paper_edit.acadPaperId = academic_paper_info.acadPaperId) "
            cursor.execute(sql)
            result= cursor.fetchall()
            return (result)
    finally:
        db.close() 

def all_monograph_from_db(): #查询全部专著
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql= "SELECT * from `publication_info` "
            cursor.execute(sql)
            result= cursor.fetchall()
            return (result)
    finally:
        db.close() 

def all_patent_from_db():
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql= "SELECT * from `patent_info` , `patent_edit` WHERE (patent_edit.patentId = patent_info.patentId) "
            cursor.execute(sql)
            result= cursor.fetchall()
            return (result)
    finally:
        db.close() 

def all_degree_from_db():
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql= "select * from degree_paper"
            cursor.execute(sql)
            result= cursor.fetchall()
            return (result)
    finally:
        db.close() 

def all_project_from_db():
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql= "SELECT * from `project_info` , `project_edit` WHERE (project_edit.projectId = project_info.projectId) "
            cursor.execute(sql)
            result= cursor.fetchall()
            return (result)
    finally:
        db.close() 

def all_standard_from_db():
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql= "SELECT * from `standard` "
            cursor.execute(sql)
            result= cursor.fetchall()
            return (result)
    finally:
        db.close() 

def show_academic_from_db(stuName):#查询姓名对应的学术论文
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql= "SELECT academic_paper_edit.acadPaperId, `acadPaperNameCH` from `academic_paper_edit`,`academic_paper_info` WHERE (academic_paper_edit.acadPaperId = academic_paper_info.acadPaperId) and (firstEdit = %s or secondEdit = %s or forthEdit = %s or thirdEdit = %s or fifthEdit = %s or sixthEdit = %s or seventhEdit = %s or eighthEdit = %s )"
            cursor.execute(sql,(stuName,stuName,stuName,stuName,stuName,stuName,stuName,stuName,))
            result= cursor.fetchall()
            return (result)
    finally:
        db.close() 

def show_monograph_from_db(stuName):#查询姓名对应的专著
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql= "SELECT `publicationId`, `publicationNameCH` from `publication_info` WHERE (editor = %s)"
            cursor.execute(sql,(stuName,))
            result= cursor.fetchall()
            return (result)
    finally:
        db.close()

def show_patent_from_db(stuName):#查询姓名对应的专利
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql= "SELECT patent_edit.patentId, `patentNameCH` from `patent_edit`,`patent_info` WHERE (patent_edit.patentId = patent_info.patentId) and (firstEdit = %s or secondEdit = %s or thirdEdit = %s or fourthEdit = %s or fifthEdit = %s or sixthEdit = %s or seventhEdit = %s or eightEdit = %s)"

            cursor.execute(sql,(stuName,stuName,stuName,stuName,stuName,stuName,stuName,stuName,))
            result= cursor.fetchall()
            return (result)
    finally:
        db.close()

def show_project_from_db(stuName):#查询姓名对应的项目
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql= "SELECT project_edit.projectId, `projectNameCH` from `project_edit`,`project_info` WHERE (project_edit.projectId = project_info.projectId) and (firstEdit = %s or secondEdit = %s or thirdEdit = %s or fourthEdit = %s or fifthEdit = %s or sixthEdit = %s or seventhEdit = %s or eighthEdit = %s)"
            cursor.execute(sql,(stuName,stuName,stuName,stuName,stuName,stuName,stuName,stuName,))
            result= cursor.fetchall()
            
            return (result)
    finally:
        db.close()

def show_standard_from_db(stuName):#查询姓名对应的专著
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql= "SELECT `standardId`, `standardNameCH` from `standard` WHERE (editor = %s)"
            cursor.execute(sql,(stuName,))
            result= cursor.fetchall()
            return (result)
    finally:
        db.close()

def show_degree_from_db(stuName):
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql= "SELECT `degPaperId`, `degPaperNameCH` from `degree_paper` WHERE (editor = %s)"
            cursor.execute(sql,(stuName,))
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

def show_stuinfo_from_db():
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql='select * from stu_info'
            cursor.execute(sql)
            result= cursor.fetchall()
            return (result)
    finally:
        db.close() 

def show_stuinfo_from_db_by_userid(userId):
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql = "SELECT * FROM stu_info WHERE stuId= %s"
            cursor.execute(sql,(userId,))
            result= cursor.fetchall()
            return (result)           
    finally:
        db.close() 
def show_tecinfo_from_db():
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql='select * from tec_info'
            cursor.execute(sql)
            result= cursor.fetchall()
            return (result)
    finally:
        db.close()

def show_tecname_from_db(userId):
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql = "SELECT tecName FROM tec_info WHERE tecId= %s"
            cursor.execute(sql,(userId,))
            tecName = str(cursor.fetchall())
            tecName = re.sub('["(),\']','',tecName)
            return (tecName)           
    finally:
        db.close() 
def show_userid_from_tecdb(username):
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql = "SELECT tecId from tec_info where tecName = %s"
            cursor.execute(sql,(username,))
            tecId = cursor.fetchone()

            tecId = tecId[0]
            return (tecId)           
    finally:
        db.close() 

def insert_tec(tecname,tecid,sex,department,tectype):
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql = "INSERT INTO `tec_info` VALUES (%s,%s,%s,%s,%s,%s)"
            try:
                cursor.execute(sql,(tecname,tecid,sex,department,tectype,'123456'))
                db.commit()
                result = True
            except (pymysql.err.ProgrammingError):
                result = pymysql.err.ProgrammingError
            return result
    finally:
        db.close()

def insert_stu(stuName,stuId,SEX,major,stuType,email,stuTel,firstProf,secondProf,unitAddress):
    db = connect_db()
    try :
        with db.cursor() as cursor:
            sql = "INSERT INTO `stu_info` VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            try:
                cursor.execute(sql,(stuName,'',stuId,'','123456',SEX,major,stuType,email,stuTel,firstProf,secondProf,unitAddress))
                db.commit()
                result = True
            except (pymysql.err.ProgrammingError):
                result = pymysql.err.ProgrammingError
            return result
    finally:
        db.close()