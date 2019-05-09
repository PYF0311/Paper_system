# -*- coding: UTF-8 -*-

from flask import Flask , jsonify
from flask import render_template,g
from flask import request, url_for, flash, redirect, session, Response,send_from_directory,abort,make_response
from flask_login import UserMixin,LoginManager,login_required,login_user
from flask_wtf import Form 
from wtforms import StringField, PasswordField,SubmitField,DateTimeField
from wtforms.validators import Required
from sqlalchemy import create_engine
from flask import make_response
from werkzeug import secure_filename
import forms
import pandas as pd
import codecs,tablib ,json,os,xlrd,csv

APP_ROOT = os.path.dirname(os.path.abspath(__file__)) 
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/uploads')
ALLOWED_EXTENSIONS = set(['xls', 'csv','xlsx'])

app = Flask(__name__)
app.config['SECRET_KEY'] = 'oh_so_secret'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


class LoginForm(Form):
	username = StringField('uname', validators=[Required()])
	password = PasswordField('passwd',validators=[Required()])
class AddForm(Form):
	tag = StringField('tag', validators=[Required()])
	acadPaperNameCH = StringField('acadPaperNameCH', validators=[Required()])
	acadPaperNameEN = StringField('acadPaperNameEN', validators=[Required()])
	firstEdit = StringField('firstEdit', validators=[Required()])
	secondEdit = StringField('secondEdit', validators=[Required()])
	thirdEdit = StringField('thirdEdit', validators=[Required()])
	fourthEdit = StringField('fourthEdit', validators=[Required()])
	fifthEdit = StringField('fifthEdit', validators=[Required()])
	sixthEdit = StringField('sixthEdit', validators=[Required()])
	seventhEdit = StringField('seventhEdit', validators=[Required()])
	eighthEdit = StringField('eighthEdit', validators=[Required()])
	transEdit = StringField('transEdit', validators=[Required()]) 
	issueNameCH = StringField('issueNameCH', validators=[Required()])
	issueNameEN = StringField('issueNameEN', validators=[Required()])
	pubIssue = StringField('pubIssue', validators=[Required()])
	pubTime = StringField('pubTime', validators=[Required()])
	pubPeriod = StringField('pubPeriod', validators=[Required()])
	pubPage1 = StringField('pubPage', validators=[Required()])
	pubPage2 = StringField('pubPage', validators=[Required()])
	firstdepa = StringField('firstdepa', validators=[Required()])
	paperType = StringField('paperType', validators=[Required()])
	indexNum = StringField('indexNum', validators=[Required()])
	impactFactor = StringField('impactFactor', validators=[Required()])
	submit = SubmitField('Submit')
class RegisterForm(Form):
	stuname = StringField('username', validators=[Required()])
	password = PasswordField('password',validators=[Required()])
	stuid = StringField('stuid', validators=[Required()])
	major = StringField('major', validators=[Required()])
	firstProf = StringField('firstProf', validators=[Required()]) 
	secondProf = StringField('secondProf', validators=[Required()]) 
class MonoForm(Form):
	tag = StringField('tag', validators=[Required()])
	publicationNameCH = StringField('publicationNameCH',validators=[Required()])
	publicationNameEN = StringField('publicationNameEN',validators=[Required()])
	editor = StringField('editor',validators=[Required()])
	editType = StringField('editType',validators=[Required()])
	pubTime = StringField('pubTime',validators=[Required()]) 
	pubUnit = StringField('pubUnit',validators=[Required()])
	ISSN = StringField('ISSN',validators=[Required()])
	wordsNum = StringField('wordsNum',validators=[Required()])
	mainContent = StringField('mainContent',validators=[Required()])	
class PatForm(Form): 
	tag = StringField('tag', validators=[Required()])
	patentNameCH = StringField('patentNameCH', validators=[Required()])
	patentNameEN = StringField('patentNameEN', validators=[Required()])
	patentType = StringField('patentType', validators=[Required()])
	firstEdit = StringField('firstEdit', validators=[Required()]) 
	secondEdit = StringField('secondEdit', validators=[Required()])
	thirdEdit = StringField('thirdEdit', validators=[Required()])
	fourthEdit = StringField('fourthEdit', validators=[Required()])
	fifthEdit = StringField('fifthEdit', validators=[Required()])
	sixthEdit = StringField('sixthEdit', validators=[Required()])
	seventhEdit = StringField('seventhEdit', validators=[Required()])
	eighthEdit = StringField('eighthEdit', validators=[Required()])
	patentApplyTime = StringField('patentApplyTime', validators=[Required()])
	patentNum = StringField('patentNum', validators=[Required()])
	ifAuthority = StringField('ifAuthority', validators=[Required()])
	patentAuthorityTime = StringField('patentAuthorityTime', validators=[Required()])
	ifTransfer = StringField('ifTransfer', validators=[Required()])
	transferSource = StringField('transferSource', validators=[Required()])
	transferComment = StringField('transferComment', validators=[Required()])
class ProForm(Form):
	tag = StringField('tag', validators=[Required()])
	projectId = StringField('projectId', validators=[Required()])
	projectHost = StringField('projectHost', validators=[Required()])
	projectFond = StringField('projectFond', validators=[Required()]) 
	projectBeginTime = StringField('projectBeginTime', validators=[Required()]) 
	projectFinTime = StringField('projectFinTime', validators=[Required()])
	projectTask = StringField('projectTask', validators=[Required()])
	projectNameCH = StringField('projectNameCH', validators=[Required()])
	projectNameEN = StringField('projectNameEN', validators=[Required()])
	projectLevel = StringField('projectLevel', validators=[Required()])
	firstEdit = StringField('firstEdit', validators=[Required()]) 
	secondEdit = StringField('secondEdit', validators=[Required()]) 
	thirdEdit = StringField('thirdEdit', validators=[Required()])
	fourthEdit = StringField('fourthEdit', validators=[Required()])
	fifthEdit = StringField('fifthEdit', validators=[Required()])
	sixthEdit = StringField('sixthEdit', validators=[Required()])
	seventhEdit = StringField('seventhEdit', validators=[Required()])
	eighthEdit = StringField('eighthEdit', validators=[Required()])

class StandForm(Form):
	tag = StringField('tag', validators=[Required()])
	standardNameCH = StringField('standardNameCH', validators=[Required()])
	standardNameEN = StringField('standardNameEN', validators=[Required()])
	standardType = StringField('standardType', validators=[Required()])
	standardNum = StringField('standardNum', validators=[Required()])
	standardAdd = StringField('standardAdd', validators=[Required()])
	standardDate = StringField('standardDate', validators=[Required()])
	editor = StringField('editor', validators=[Required()])

class DegreeForm(Form):
	tag = StringField('tag', validators=[Required()])
	degPaperNameCH = StringField('degPaperNameCH', validators=[Required()])
	degPaperNameEN = StringField('degPaperNameEN', validators=[Required()])
	degType = StringField('degType', validators=[Required()])
	editor = StringField('editor', validators=[Required()])
	firstProf = StringField('firstProf', validators=[Required()])
	secondProf = StringField('secondProf', validators=[Required()])
	gradUnit = StringField('gradUnit', validators=[Required()])
	gradAdd = StringField('gradAdd', validators=[Required()])
	gradDate = StringField('gradDate', validators=[Required()])

@app.route('/login',methods=['GET','POST'])
def login():
	form = LoginForm()
	if request.method == 'POST':
		username = request.form.get('uname')
		password = request.form.get('passwd')
		access_type=request.form.get('type')
		if access_type == 'student':
			user=forms.verify_user_exist(username)
			if user is True and forms.verify_password(username,password):
				session['username']=username
				statecode =1 #学生成功登陆
			else:
				statecode = -2 #重定向于请登录界面
		elif access_type =='teacher':
			user = forms.verify_tec_exist(username)
			if user is True and forms.verify_tec_password(username,password):
				
				session['username']=username
				statecode =2 #老师成功登陆成功登陆
			else:
				statecode = -2 	#重定向于请登录界面
		else:
			statecode=-1 #权限控制错误

		
		return jsonify({'result':statecode})	
	elif request.method == 'GET':
		return render_template('index.html')
 
@app.route("/404" ,methods=['GET'])
def show_404():
	return render_template('404.html')

@app.route("/logout")
def logout():
	session.pop('username')
	print(session)
	return redirect(url_for('login'))

#--------------student--------------
@app.route("/stu/forms",methods=['GET','POST'])
def show_stu_forms():
	if 'username' in session:
		userid = session['username']
		username = forms.show_stuname_from_db(userid)

	else:
		return redirect(url_for('login'))

	Loginform = LoginForm()
	tag = request.form.get('tag')
	if tag == 'academic_paper':
		Addform = AddForm()
		if request.method == 'POST':
			result = forms.add_info_to_db(Addform.data)
			return jsonify({'result':result,'pageType':'stu'})
	elif tag == 'monograph':
		Monoform = MonoForm()
		if request.method == 'POST':
			result = forms.add_info_to_db(Monoform.data)
			return jsonify({'result':result,'pageType':'stu'})
	elif tag == 'patent':
		Patform = PatForm()
		if request.method == 'POST':
			result = forms.add_info_to_db(Patform.data)
			return jsonify({'result':result,'pageType':'stu'})
	elif tag == 'project':
		Proform = ProForm()
		if request.method == 'POST':
			result = forms.add_info_to_db(Proform.data)
			return jsonify({'result':result,'pageType':'stu'})
	elif tag == 'standard':
		Standform = StandForm()
		if request.method == 'POST':
			result = forms.add_info_to_db(Standform.data)
			return jsonify({'result':result,'pageType':'stu'})
	elif tag == 'degree':
		Degreeform = DegreeForm()
		if request.method == 'POST':
			result = forms.add_info_to_db(Degreeform.data)
			return jsonify({'result':result,'pageType':'stu'})

	return render_template("/stu/forms.html",username=username,userid=userid)







@app.route('/stu/tables',methods=['GET','POST'])
def show_tables():
	lengthset=[]
	if 'username' in session:
		userid = session['username']
		username = forms.show_stuname_from_db(userid)
	else:
		statecode=-2 #返回请登录页面
	result=forms.show_info_from_db(userid)

	length=len(result)
	for i in range(len(result)):
		lengthset.append(len(result[i])-1)
	print(result)
	return render_template('/stu/tables.html',result=result, length=length, lengthset=lengthset,username=username)


@app.route('/stu/editprofile',methods=['GET','POST'])
def show_editprofile():
	form = LoginForm()
	if 'username' not in session :
		return redirect(url_for('login'))
	else:
		userid = session['username']
		username = forms.show_stuname_from_db(userid)

	return render_template('/stu/editprofile.html',form=form,userid=userid,username=username)

@app.route('/stu/editpassword',methods=['GET','POST'])
def show_editpassword():
	if 'username' not in session :
		return redirect(url_for('login'))
	else:
		userid = session['username']
		username = forms.show_stuname_from_db(userid)
	return render_template("/stu/editpassword.html",userid=userid,username=username)

@app.route("/stu/pass_edit",methods=['GET','POST'])
def verify_password():
	if 'username' not in session :
		return redirect(url_for('login'))
	else:
		userid = session['username']
		username = forms.show_stuname_from_db(userid)

	passwd = request.form.get('newPassword')
	result = forms.motify_stu_password(userid,passwd)

	return jsonify({'result':result})


def data_id_operation(datas):
	
	data_set=sorted(datas.items(),key=lambda item:item[1])
	data_set.sort()
	
	length=int(len(data_set)/2)
	if length == 0:
		length = 1
		lists = [[] for i in range(length)]
		for i in range(length):
			lists[i].append(data_set[i*2][1])
	else:
		lists = [[] for i in range(length)]
		for i in range(length):
			lists[i].append(data_set[i*2][1])
			lists[i].append(data_set[i*2+1][1])
	
	print(lists)
	return lists

@app.route('/stu/info',methods=['GET','POST'])
def show_info():
	datax = request.form.to_dict()
	result = data_id_operation(datax)
	paper_type = result[0][1]
	paper_id = result[0][0]
	if (paper_type =='期刊论文'):
		resultset = forms.select_academic_from_db(paper_id)
		reply = aca_data_operation(resultset)
		session['resultset']=reply

	elif (paper_type =='学位论文'):
		resultset = forms.select_degree_from_db(paper_id)
		reply = deg_data_operation(resultset)
		session['resultset']=reply

	elif (paper_type =='专利'):
		resultset = forms.select_patent_from_db(paper_id)
		reply = patent_data_operation(resultset)
		session['resultset']=reply

	elif (paper_type =='参加项目'):
		resultset = forms.select_project_from_db(paper_id)
		reply = pro_data_operation(resultset)
		session['resultset']=reply
		

	elif (paper_type =='专著'):
		resultset = forms.select_mono_from_db(paper_id)
		reply = mono_data_operation(resultset)
		session['resultset']=reply
		

	elif (paper_type =='标准'):
		resultset = forms.select_stand_from_db(paper_id)
		reply = stand_data_operation(resultset)
		session['resultset']=reply
	
	
	return jsonify({'result':resultset,'type':paper_type})
	
@app.route('/stu/aca_info',methods=['GET','POST'])
def show_aca_info():
	if 'username' in session:
		userid = session['username']
		username = forms.show_stuname_from_db(userid)

	else:
		return redirect(url_for('login'))

	resultset = session['resultset']
	print(resultset)
	return render_template("/stu/aca_info.html",resultset = resultset,username=username)
 
@app.route('/stu/deg_info',methods=['GET','POST'])
def show_deg_info():
	if 'username' in session:
		userid = session['username']
		username = forms.show_stuname_from_db(userid)

	else:
		return redirect(url_for('login'))

	resultset = session['resultset']
	return render_template("/stu/deg_info.html",resultset = resultset,username=username)

@app.route('/stu/pat_info',methods=['GET','POST'])
def show_pat_info():
	if 'username' in session:
		userid = session['username']
		username = forms.show_stuname_from_db(userid)

	else:
		return redirect(url_for('login'))

	resultset = session['resultset']
	print(resultset)
	return render_template("/stu/pat_info.html",resultset = resultset,username=username)

@app.route('/stu/pro_info',methods=['GET','POST'])
def show_pro_info():
	if 'username' in session:
		userid = session['username']
		username = forms.show_stuname_from_db(userid)

	else:
		return redirect(url_for('login'))
		
	resultset = session['resultset']
	return render_template("/stu/pro_info.html",resultset = resultset,username=username)

@app.route('/stu/mono_info',methods=['GET','POST'])
def show_mono_info():
	if 'username' in session:
		userid = session['username']
		username = forms.show_stuname_from_db(userid)

	else:
		return redirect(url_for('login'))

	resultset = session['resultset']
	return render_template("/stu/mono_info.html",resultset = resultset,username=username)

@app.route('/stu/stand_info',methods=['GET','POST'])
def show_stand_info():
	if 'username' in session:
		userid = session['username']
		username = forms.show_stuname_from_db(userid)

	else:
		return redirect(url_for('login'))

	resultset = session['resultset']
	print(resultset)
	return render_template("/stu/stand_info.html",resultset = resultset,username=username)

@app.route('/stu/aca_edit',methods=['GET','POST'])
def show_aca_edit():
	if 'username' in session:
		userid = session['username']
		username = forms.show_stuname_from_db(userid)

	else:
		return redirect(url_for('login'))

	resultset = session['resultset']
	print(resultset)
	return render_template("/stu/aca_edit.html",resultset = resultset,username=username)

@app.route('/stu/deg_edit',methods=['GET','POST'])
def show_deg_edit():
	if 'username' in session:
		userid = session['username']
		username = forms.show_stuname_from_db(userid)

	else:
		return redirect(url_for('login'))

	resultset = session['resultset']
	print(resultset)
	return render_template("/stu/deg_edit.html",resultset = resultset,username=username)

@app.route('/stu/pat_edit',methods=['GET','POST'])
def show_pat_edit():
	if 'username' in session:
		userid = session['username']
		username = forms.show_stuname_from_db(userid)

	else:
		return redirect(url_for('login'))

	resultset = session['resultset']
	print(resultset)
	return render_template("/stu/pat_edit.html",resultset = resultset,username=username)

@app.route('/stu/pro_edit',methods=['GET','POST'])
def show_pro_edit():
	if 'username' in session:
		userid = session['username']
		username = forms.show_stuname_from_db(userid)

	else:
		return redirect(url_for('login'))
		
	resultset = session['resultset']
	print(resultset)
	return render_template("/stu/pro_edit.html",resultset = resultset,username=username)

@app.route('/stu/mono_edit',methods=['GET','POST'])
def show_mono_edit():
	if 'username' in session:
		userid = session['username']
		username = forms.show_stuname_from_db(userid)

	else:
		return redirect(url_for('login'))

	resultset = session['resultset']
	print(resultset)
	return render_template("/stu/mono_edit.html",resultset = resultset,username=username)

@app.route('/stu/stand_edit',methods=['GET','POST'])
def show_stand_edit():
	if 'username' in session:
		userid = session['username']
		username = forms.show_stuname_from_db(userid)

	else:
		return redirect(url_for('login'))

	resultset = session['resultset']
	print(resultset)
	return render_template("/stu/stand_edit.html",resultset = resultset,username=username)

@app.route('/stu/del',methods=['GET','POST'])
def do_delete():
	datax = request.form.to_dict()  
	result = data_id_operation(datax)
	for i in range(len(result)):
		msg = forms.del_from_data(result[i])
	
	return jsonify({'result':msg})

 
	



@app.route('/add_succ.html',methods=['GET','POST'])
def show_add_succ_html():
	return render_template("add_succ.html")

#--------------teacher--------------
@app.route("/tec/forms",methods=['GET','POST'])
def show_tec_forms():
	if 'username' in session:
		username = session['username']
	else:
		return redirect(url_for('login'))

	tag = request.form.get('tag')
	if tag == 'academic_paper':
		Addform = AddForm()
		if request.method == 'POST':
			result = forms.add_info_to_db(Addform.data)
			print("result",result)
			return jsonify({'result':result,'pageType':'tec'})
	elif tag == 'monograph':
		Monoform = MonoForm()
		if request.method == 'POST':
			result = forms.add_info_to_db(Monoform.data)
			return jsonify({'result':result,'pageType':'tec'})
	elif tag == 'patent':
		Patform = PatForm()
		if request.method == 'POST':
			result = forms.add_info_to_db(Patform.data)
			return jsonify({'result':result,'pageType':'tec'})
	elif tag == 'project':
		Proform = ProForm()
		if request.method == 'POST':
			result = forms.add_info_to_db(Proform.data)
			return jsonify({'result':result,'pageType':'tec'})
	elif tag == 'standard':
		Standform = StandForm()
		if request.method == 'POST':
			result = forms.add_info_to_db(Standform.data)
			return jsonify({'result':result,'pageType':'tec'})
	elif tag == 'degree':
		Degreeform = DegreeForm()
		if request.method == 'POST':
			result = forms.add_info_to_db(Degreeform.data)
			return jsonify({'result':result,'pageType':'tec'})
	
	return render_template("tec/forms.html",username = username)

def aca_data_operation(result):
	result_set = []
	result_title = ('id','acadPaperNameCH','acadPaperNameEN','pubTime','pubIssue','pubPeriod','pubPage','paperType','issueNameCH','issueNameEN','impactFactor','indexNum','id','FirstEdit','SecondEdit','ThirdEdit','ForthEdit','FifthEdit','SixthEdit','SeventhEdit','EighthEdit','TransEdit')
	for i in range(len(result)):
		temp = dict(zip(result_title,result[i]))
		result_set.append(temp)
	return result_set

def mono_data_operation(result):
	result_set = []
	result_title = ('id','publicationNameCH','publicationNameEN','editor','editType','pubTime','pubUnit','ISSN','wordsNum','mainContent')
	for i in range(len(result)):
		temp = dict(zip(result_title,result[i]))
		result_set.append(temp)
	return result_set

def patent_data_operation(result):
	result_set = []
	result_title = ('id','patentNameCH','patentNameEN','patentType','patentApplyTime','ifAuthority','patentAuthorityTime','ifTransfer','transferSource','transferComment','patentNum','id','FirstEdit','SecondEdit','ThirdEdit','ForthEdit','FifthEdit','SixthEdit','SeventhEdit','EighthEdit')
	for i in range(len(result)):
		temp = dict(zip(result_title,result[i]))
		result_set.append(temp)
	return result_set
def pro_data_operation(result):
	result_set = []
	result_title = ('projectId ', 'projectHost','projectFond','projectBeginTime','projectFinTime','projectTask','projectNameCH','projectNameEN','projectLevel','projectId','FirstEdit','SecondEdit','ThirdEdit','ForthEdit','FifthEdit','SixthEdit','SeventhEdit','EighthEdit')
	for i in range(len(result)):
		temp = dict(zip(result_title,result[i]))
		result_set.append(temp)
	return result_set

def deg_data_operation(result):
	result_set = []
	result_title = ('degPaperId','degPaperNameCH','degPaperNameEN','degType','editor','firstProf','secondProf','gradUnit','gradAdd','gradDate')
	for i in range(len(result)):
		temp = dict(zip(result_title,result[i]))
		result_set.append(temp)
	return result_set

def stand_data_operation(result):
	result_set = []
	result_title = ('standardId' , 'standardNameCH' , 'standardNameEN' , 'standardType', 'standardNum' , 'standardAdd' , 'standardDate','editor')
	for i in range(len(result)):
		temp = dict(zip(result_title,result[i]))
		result_set.append(temp)
	return result_set

def tec_data_operation(result):
	result_set = []
	result_title = ('tecId','tecName','SEX','department','tecType')
	for i in range(len(result)):
		temp = dict(zip(result_title,result[i]))
		result_set.append(temp)
	return result_set

def stu_data_operation(result):
	result_set = []
	result_title = ('stuName','grade','stuId','beginTime','password','SEX','major','type', 'email','stuTel','firstProf','secondProf','unitAddress')
	for i in range(len(result)):
		temp = dict(zip(result_title,result[i]))
		result_set.append(temp)

	return result_set

def aca_print_operation(result):
	editor = ''
	printstr = ''
	if result['FirstEdit'] is not None:
		editor = editor + "," + result['FirstEdit']
		if result['SecondEdit'] is not None:
			editor = editor + "," + result['SecondEdit']
			if result['ThirdEdit'] is not None:
				editor = editor + "," + result['ThirdEdit']
				if result['ForthEdit'] is not None:
					editor = editor + "," + result['ForthEdit']
					if result['FifthEdit'] is not None:
						editor = editor + "," + result['FifthEdit']
						if result['SixthEdit'] is not None:
							editor = editor + "," + result['SixthEdit']
							if result['SeventhEdit'] is not None:
								editor = editor + "," + result['SeventhEdit']
								if result['EighthEdit'] is not None:
									editor = editor + "," + result['EighthEdit']

	editor = editor.strip(',')
	papername = result['acadPaperNameCH']
	pubname = result['issueNameCH']
	issue = result['pubIssue']
	period = result['pubPeriod']
	page = result['pubPage']
	year = result['pubTime'][0:4]
	paperType = result['paperType']
	try:
		if paperType == '学位论文':
			printstr = editor + "." + papername + "[D]" + "." + pubname + "," + year + "," + period + "(" + issue + "):" + page
		elif paperType == '会议论文集':
			printstr = editor + "." + papername + "[A]" + "." + pubname + "," + year + "," + period + "(" + issue + "):" + page
		elif paperType == '一般期刊' or paperType == '核心期刊' or paperType == 'EI收录' or paperType == 'SCI收录':
			printstr = editor + "." + papername + "[J]" + "." + pubname + "," + year + "," + period + "(" + issue + "):" + page
	except Exception:
		pass
	return printstr	 
	
def patent_print_operation(result):
	editor = ''
	printstr = ''
	if result['FirstEdit'] is not None:
		editor = editor + "," + result['FirstEdit']
		if result['SecondEdit'] is not None:
			editor = editor + "," + result['SecondEdit']
			if result['ThirdEdit'] is not None:
				editor = editor + "," + result['ThirdEdit']
				if result['ForthEdit'] is not None:
					editor = editor + "," + result['ForthEdit']
					if result['FifthEdit'] is not None:
						editor = editor + "," + result['FifthEdit']
						if result['SixthEdit'] is not None:
							editor = editor + "," + result['SixthEdit']
							if result['SeventhEdit'] is not None:
								editor = editor + "," + result['SeventhEdit']
								if result['EighthEdit'] is not None:
									editor = editor + "," + result['EighthEdit']

	editor = editor.strip(',')
	papername = result['patentNameCH']
	patentNum = result['patentNum']
	patentApplyTime = result['patentApplyTime']
	try:
		printstr = editor + "." + papername + "[P]" + "." + patentNum + ":" + patentApplyTime + "." 
	except Exception:
		pass
	return printstr


def mono_print_operation(result):
	print(result)
	editor = ''
	printstr = ''
	editor = result['editor']
	papername = result['publicationNameCH']
	pubadd = '中国'
	pubeditor = '出版者'
	year = result['pubTime'][0:4]
	try:
		printstr = editor + "." + papername + "[M]" + "." + pubadd + ":" + pubeditor + "," + year + "."
	except Exception:
		pass
	return printstr

def deg_print_operation(result):
	print(result)
	editor = ''
	printstr = ''
	editor = result['editor']
	papername = result['degPaperNameCH']
	year = result['gradDate'][0:4]
	gradAdd = result['gradAdd']
	firstProf = result['firstProf']
	try:
		printstr = editor + "." + papername + "[D]" + "." + gradAdd + ":" + firstProf + "," + year + "."
	except Exception:
		pass
	return printstr

def pro_print_operation(result):
	editor = ''
	printstr = ''
	if result['FirstEdit'] is not None:
		editor = editor + "," + result['FirstEdit']
		if result['SecondEdit'] is not None:
			editor = editor + "," + result['SecondEdit']
			if result['ThirdEdit'] is not None:
				editor = editor + "," + result['ThirdEdit']
				if result['ForthEdit'] is not None:
					editor = editor + "," + result['ForthEdit']
					if result['FifthEdit'] is not None:
						editor = editor + "," + result['FifthEdit']
						if result['SixthEdit'] is not None:
							editor = editor + "," + result['SixthEdit']
							if result['SeventhEdit'] is not None:
								editor = editor + "," + result['SeventhEdit']
								if result['EighthEdit'] is not None:
									editor = editor + "," + result['EighthEdit']
	editor = editor.strip(',')
	projectNameCH = result['projectNameCH']
	projectId = result['projectId']
	projectBeginTime = result['projectBeginTime']
	try:
		printstr = editor + "." + projectNameCH + "[Pro]" + "." + projectId + ":" + projectBeginTime + "." 
	except Exception:
		pass
	return printstr

def stand_print_operation(result):
	printstr = ''
	if result['standardType'] =='国家标准[GB]':
		standtype = 'GB/T'
	elif result['standardType'] =='地方标准[DB]':
		standtype = 'DB'
	elif result['standardType'] =='企业标准[Q/]':
		standtype = 'Q/'
	standnum = result['standardNum']
	standname = result['standardNameCH']
	try:
		printstr = standtype + " " + standnum + "," + standname +  "[S]" +"."
	except Exception:
		pass
	return printstr
	
	
@app.route('/txtdownload01', methods=['POST','GET'])
def testdownload01():
	Postid=[]
	resultset=[]
	datax = request.form.to_dict()  
	for value in datax.values():
		Postid.append(value)
	Postid.sort()

	length = len(Postid)
	for i in range(length):
		temp_result = forms.select_academic_from_db(Postid[i])
		results = aca_data_operation(temp_result)
		resultset.append(results)
	
	content = ""
	
	for i in range(int(len(resultset)/2)):
		content = content + aca_print_operation(resultset[i][0]) + '\n'
	print("content:",content)
	session['content'] = content
	response = make_response(content)
	response.headers["Content-Disposition"] = "attachment; filename=list.txt"
	return redirect(url_for('testdownload'))

@app.route('/txtdownload02', methods=['POST','GET'])
def testdownload02():
	Postid=[]
	resultset=[]
	datax = request.form.to_dict()  
	for value in datax.values():
		Postid.append(value)
	Postid.sort()
	print(Postid)
	length = len(Postid)
	for i in range(length):
		temp_result = forms.select_degree_from_db(Postid[i])
		results = deg_data_operation(temp_result)
		resultset.append(results)

	content = ""
	for i in range(int(len(resultset)/2)):
		content = content + deg_print_operation(resultset[i][0]) + '\n'
	
	print("content:",content)
	session['content'] = content
	response = make_response(content)
	response.headers["Content-Disposition"] = "attachment; filename=list.txt"
	return redirect(url_for('testdownload'))

@app.route('/txtdownload', methods=['GET','POST'])
def testdownload():
	content = session['content']
	response = make_response(content)
	response.headers["Content-Disposition"] = "attachment; filename=list.txt"
	return response

@app.route('/txtdownload03', methods=['GET','POST'])
def testdownload03():
	Postid=[]
	resultset=[]
	datax = request.form.to_dict()  
	for value in datax.values():
		Postid.append(value)
	Postid.sort()
	print(Postid)
	length = len(Postid)
	for i in range(length):
		temp_result = forms.select_patent_from_db(Postid[i])
		results = patent_data_operation(temp_result)
		resultset.append(results)

	content = ""

	for i in range(int(len(resultset)/2)):
		content = content + patent_print_operation(resultset[i][0]) + '\n'
	
	print("content:",content)
	session['content'] = content
	response = make_response(content)
	response.headers["Content-Disposition"] = "attachment; filename=list.txt"
	return redirect(url_for('testdownload'))


@app.route('/txtdownload04', methods=['GET','POST'])
def testdownload04():
	Postid=[]
	resultset=[]
	datax = request.form.to_dict()  
	for value in datax.values():
		Postid.append(value)
	Postid.sort()
	print(Postid)
	length = len(Postid)
	for i in range(length):
		temp_result = forms.select_project_from_db(Postid[i])
		results = pro_data_operation(temp_result)
		resultset.append(results)

	print(resultset)
	content = ""
	for i in range(int(len(resultset)/2)):
		content = content + pro_print_operation(resultset[i][0]) + '\n'
	
	session['content'] = content
	print("session['content']:",session['content'])

	response = make_response(content)
	response.headers["Content-Disposition"] = "attachment; filename=list.txt"
	return redirect(url_for('testdownload'))

@app.route('/txtdownload05', methods=['GET','POST'])
def testdownload05():
	Postid=[]
	resultset=[]
	datax = request.form.to_dict()  
	for value in datax.values():
		Postid.append(value)
	Postid.sort()
	print(Postid)
	length = len(Postid)
	for i in range(length):
		temp_result = forms.select_mono_from_db(Postid[i])
		results = mono_data_operation(temp_result)
		resultset.append(results)

	content = ""
	for i in range(int(len(resultset)/2)):
		content = content + mono_print_operation(resultset[i][0]) + '\n'
	
	session['content'] = content
	print("session['content']:",session['content'])

	response = make_response(content)
	response.headers["Content-Disposition"] = "attachment; filename=list.txt"
	return redirect(url_for('testdownload'))

@app.route('/txtdownload06', methods=['GET','POST'])
def testdownload06():
	Postid=[]
	resultset=[]
	datax = request.form.to_dict()  
	for value in datax.values():
		Postid.append(value)
	Postid.sort()
	length = len(Postid)
	for i in range(length):
		temp_result = forms.select_stand_from_db(Postid[i])
		results = stand_data_operation(temp_result)
		resultset.append(results)
	
	content = ""
	for i in range(int(len(resultset)/2)):

		content = content + stand_print_operation(resultset[i][0]) + '\n'
	
	session['content'] = content
	print("session['content']:",session['content'])

	response = make_response(content)
	response.headers["Content-Disposition"] = "attachment; filename=list.txt"
	return redirect(url_for('testdownload'))

@app.route('/xlsdownload_academic', methods=['GET','POST'])
def xlsdownload00():
	Postid=[]
	resultset=[]
	datax = request.form.to_dict()  
	for value in datax.values():
		Postid.append(value)
	Postid.sort()
	
	length = int(len(Postid)/2)
	for i in range(length):
		temp_result = forms.select_academic_from_db(Postid[i])
		results = aca_data_operation(temp_result)
		resultset.append(results)
	print("result",resultset)
	dataList=[[] for i in range(length)]
	for i in range(length):
		dataList[i].append(resultset[i][0]['acadPaperNameCH'])
		dataList[i].append(resultset[i][0]['acadPaperNameEN'])
		dataList[i].append(resultset[i][0]["FirstEdit"])
		dataList[i].append(resultset[i][0]["SecondEdit"])
		dataList[i].append(resultset[i][0]["ThirdEdit"])
		dataList[i].append(resultset[i][0]["ForthEdit"])
		dataList[i].append(resultset[i][0]["FifthEdit"])
		dataList[i].append(resultset[i][0]["SixthEdit"])
		dataList[i].append(resultset[i][0]["SeventhEdit"])
		dataList[i].append(resultset[i][0]["EighthEdit"])
		dataList[i].append(resultset[i][0]["TransEdit"])
		dataList[i].append(resultset[i][0]["issueNameCH"])
		dataList[i].append(resultset[i][0]["pubTime"])
		dataList[i].append(resultset[i][0]["pubIssue"])
		dataList[i].append(resultset[i][0]["pubPeriod"])
		dataList[i].append(resultset[i][0]["pubPage"])
		dataList[i].append(resultset[i][0]["paperType"])
		dataList[i].append(resultset[i][0]["indexNum"])
		dataList[i].append(resultset[i][0]["impactFactor"])
	session['xls'] = dataList
	return redirect(url_for('xlsdownload01'))

@app.route('/xlsdownload_degree', methods=['GET','POST'])
def xlsdownload_degree():
	Postid=[]
	resultset=[]
	datax = request.form.to_dict()  
	for value in datax.values():
		Postid.append(value)
	Postid.sort()
	length = int(len(Postid)/2)
	for i in range(length):
		temp_result = forms.select_degree_from_db(Postid[i])
		results = deg_data_operation(temp_result)
		resultset.append(results)
	print(resultset)	
	dataList=[[] for i in range(length)]
	for i in range(length):
		dataList[i].append(resultset[i][0]['degPaperNameCH'])
		dataList[i].append(resultset[i][0]['degPaperNameEN'])
		dataList[i].append(resultset[i][0]['degType'])
		dataList[i].append(resultset[i][0]['editor'])
		dataList[i].append(resultset[i][0]['firstProf'])
		dataList[i].append(resultset[i][0]['secondProf'])
		dataList[i].append(resultset[i][0]['gradUnit'])
		dataList[i].append(resultset[i][0]['gradAdd'])
		dataList[i].append(resultset[i][0]['gradDate'])
	session['xls'] = dataList
	return redirect(url_for('xlsdownload02'))

@app.route('/xlsdownload_patent', methods=['GET','POST'])
def xlsdownload_patent():
	Postid=[]
	resultset=[]
	datax = request.form.to_dict()  
	for value in datax.values():
		Postid.append(value)
	Postid.sort()
	length = int(len(Postid)/2)
	for i in range(length):
		temp_result = forms.select_patent_from_db(Postid[i])
		results = patent_data_operation(temp_result)
		resultset.append(results)	
	dataList=[[] for i in range(length)]
	for i in range(length):
		dataList[i].append(resultset[i][0]['patentNum'])
		dataList[i].append(resultset[i][0]['patentNameCH'])
		dataList[i].append(resultset[i][0]['patentNameEN'])
		dataList[i].append(resultset[i][0]['patentType'])
		dataList[i].append(resultset[i][0]['FirstEdit'])
		dataList[i].append(resultset[i][0]['SecondEdit'])
		dataList[i].append(resultset[i][0]['ThirdEdit'])
		dataList[i].append(resultset[i][0]['ForthEdit'])
		dataList[i].append(resultset[i][0]['FifthEdit'])
		dataList[i].append(resultset[i][0]['SixthEdit'])
		dataList[i].append(resultset[i][0]['SeventhEdit'])
		dataList[i].append(resultset[i][0]['EighthEdit'])
		dataList[i].append(resultset[i][0]['patentApplyTime'])
		dataList[i].append(resultset[i][0]['ifAuthority'])
		dataList[i].append(resultset[i][0]['patentAuthorityTime'])
		dataList[i].append(resultset[i][0]['ifTransfer'])
		dataList[i].append(resultset[i][0]['transferSource'])
	session['xls'] = dataList
	return redirect(url_for('xlsdownload03'))

@app.route('/xlsdownload_project', methods=['GET','POST'])
def xlsdownload_project():
	Postid=[]
	resultset=[]
	datax = request.form.to_dict()  
	for value in datax.values():
		Postid.append(value)
	Postid.sort()
	print(Postid)
	length = int(len(Postid)/2)
	for i in range(length):
		temp_result = forms.select_project_from_db(Postid[i])
		results = pro_data_operation(temp_result)
		resultset.append(results)	
	dataList=[[] for i in range(length)]
	for i in range(length):
		dataList[i].append(resultset[i][0]['projectNameCH'])
		dataList[i].append(resultset[i][0]['projectNameEN'])
		dataList[i].append(resultset[i][0]['projectLevel'])
		dataList[i].append(resultset[i][0]['projectId'])
		dataList[i].append(resultset[i][0]['projectHost'])
		dataList[i].append(resultset[i][0]['FirstEdit'])
		dataList[i].append(resultset[i][0]['SecondEdit'])
		dataList[i].append(resultset[i][0]['ThirdEdit'])
		dataList[i].append(resultset[i][0]['ForthEdit'])
		dataList[i].append(resultset[i][0]['FifthEdit'])
		dataList[i].append(resultset[i][0]['SixthEdit'])
		dataList[i].append(resultset[i][0]['SeventhEdit'])
		dataList[i].append(resultset[i][0]['EighthEdit'])
		dataList[i].append(resultset[i][0]['projectFond'])
		dataList[i].append(resultset[i][0]['projectBeginTime'])
		dataList[i].append(resultset[i][0]['projectFinTime'])
		dataList[i].append(resultset[i][0]['projectTask'])

		
	session['xls'] = dataList

	return redirect(url_for('xlsdownload04'))

@app.route('/xlsdownload_mono', methods=['GET','POST'])
def xlsdownload_mono():
	Postid=[]
	resultset=[]
	datax = request.form.to_dict()  
	for value in datax.values():
		Postid.append(value)
	Postid.sort()
	print(Postid)
	length = int(len(Postid)/2)
	for i in range(length):
		temp_result = forms.select_mono_from_db(Postid[i])
		results = mono_data_operation(temp_result)
		resultset.append(results)	
	dataList=[[] for i in range(length)]
	for i in range(length):
		dataList[i].append(resultset[i][0]['id'])
		dataList[i].append(resultset[i][0]['publicationNameCH'])
		dataList[i].append(resultset[i][0]['publicationNameEN'])
		dataList[i].append(resultset[i][0]['editor'])
		dataList[i].append(resultset[i][0]['editType'])
		dataList[i].append(resultset[i][0]['pubTime'])
		dataList[i].append(resultset[i][0]['pubUnit'])
		dataList[i].append(resultset[i][0]['ISSN'])
		dataList[i].append(resultset[i][0]['wordsNum'])
		dataList[i].append(resultset[i][0]['mainContent'])
	session['xls'] = dataList
	return redirect(url_for('xlsdownload05'))

@app.route('/xlsdownload_stand', methods=['GET','POST'])
def xlsdownload_stand():
	Postid=[]
	resultset=[]
	datax = request.form.to_dict()  
	for value in datax.values():
		Postid.append(value)
	Postid.sort()
	print(Postid)
	length = int(len(Postid)/2)
	for i in range(length):
		temp_result = forms.select_stand_from_db(Postid[i])
		results = stand_data_operation(temp_result)
		resultset.append(results)	
	dataList=[[] for i in range(length)]
	for i in range(length):
		dataList[i].append(resultset[i][0]['standardNum'])
		dataList[i].append(resultset[i][0]['standardNameCH'])
		dataList[i].append(resultset[i][0]['standardNameEN'])
		dataList[i].append(resultset[i][0]['standardType'])
		dataList[i].append(resultset[i][0]['standardAdd'])
		dataList[i].append(resultset[i][0]['standardDate'])
		dataList[i].append(resultset[i][0]['editor'])
	session['xls'] = dataList
	return redirect(url_for('xlsdownload06'))

@app.route('/xlsdownload01',methods=['GET'])
def xlsdownload01():
	headerList = [u"论文名称", u"英文名称", u"第一作者", u"第二作者", u"第三作者", u"第四作者", u"第五作者", u"第六作者", u"第七作者", u"第八作者", u"通讯作者", u"刊物名称", u"论文发表时间", u"卷", u"期", u"发表页码", u"收录类型", u"DOI", u"IF"]
	if 'xls' in session:
		dataList = session['xls']
		data = tablib.Dataset(*dataList, headers=headerList)
		response = make_response(data.xls)
		response.headers["Content-Type"] = 'xls'
		filename = "list.xls"
		response.headers["Content-Disposition"] = "attachment; filename=" + filename
		return response
	else:
		return redirect(url_for('show_404'))

@app.route('/xlsdownload02' ,methods=['GET'])
def xlsdownload02():
	headerList = [u"中文名称",u"英文名称",u"论文类别",u"作者",u"第一导师",u"第二导师",u"毕业单位",u"学校所在地",u"主要内容"]
	if 'xls' in session:
		dataList = session['xls']
		data = tablib.Dataset(*dataList, headers=headerList)
		response = make_response(data.xls)
		response.headers["Content-Type"] = 'xls'
		filename = "list.xls"
		response.headers["Content-Disposition"] = "attachment; filename=" + filename
		return response
	else:
		return redirect(url_for('show_404'))

@app.route('/xlsdownload03',methods=['GET'])
def xlsdownload03():
	headerList = [u"专利号", u"专利名称", u"英文名称", u"专利类型", u"第一发明人", u"第二发明人", u"第三发明人", u"第四发明人", u"第五发明人", u"第六发明人", u"第七发明人", u"第八发明人", u"专利申请时间", u"是否授权", u"专利授权时间", u"是否转让", u"转让单位"]
	if 'xls' in session:
		dataList = session['xls']
		data = tablib.Dataset(*dataList, headers=headerList)
		response = make_response(data.xls)
		response.headers["Content-Type"] = 'xls'
		filename = "list.xls"
		response.headers["Content-Disposition"] = "attachment; filename=" + filename
		return response
	else:
		return redirect(url_for('show_404'))

@app.route('/xlsdownload04',methods=['GET'])
def xlsdownload04():
	headerList = [u"项目名称", u"英文名称", u"项目级别", u"项目编号", u"项目主持人", u"第一参与人", u"第二参与人", u"第三参与人", u"第四参与人", u"第五参与人", u"第六参与人", u"第七参与人", u"第八参与人", u"项目经费", u"项目开始时间", u"项目结束时间", u"项目其他内容"]
	if 'xls' in session:
		dataList = session['xls']
		data = tablib.Dataset(*dataList, headers=headerList)
		response = make_response(data.xls)
		response.headers["Content-Type"] = 'xls'
		filename = "list.xls"
		response.headers["Content-Disposition"] = "attachment; filename=" + filename
		return response
	else:
		return redirect(url_for('show_404'))

@app.route('/xlsdownload05',methods=['GET'])
def xlsdownload05():
	headerList = [u"编号", u"专著名称", u"英文名称", u"作者",u"编者类型", u"出版时间", u"出版单位", u"ISSN", u"完成字数", u"主要内容"]
	if 'xls' in session:
		dataList = session['xls']
		data = tablib.Dataset(*dataList, headers=headerList)
		response = make_response(data.xls)
		response.headers["Content-Type"] = 'xls'
		filename = "list.xls"
		response.headers["Content-Disposition"] = "attachment; filename=" + filename
		return response
	else:
		return redirect(url_for('show_404'))

@app.route('/xlsdownload06',methods=['GET'])
def xlsdownload06():
	headerList = [u"标准编号", u"标准名称", u"英文名称", u"标准类型",u"标准颁布单位", u"颁布时间", u"作者"]
	if 'xls' in session:
		dataList = session['xls']
		data = tablib.Dataset(*dataList, headers=headerList)
		response = make_response(data.xls)
		response.headers["Content-Type"] = 'xls'
		filename = "list.xls"
		response.headers["Content-Disposition"] = "attachment; filename=" + filename
		return response
	else:
		return redirect(url_for('show_404'))

@app.route('/tec/export_academic',methods=['GET','POST'])
def show_export_academic():
	results = aca_data_operation(forms.all_academic_from_db())
	length = len(results)
	return render_template("tec/ex_academic.html",result = results,length = length)

@app.route('/tec/export_monograph',methods=['GET','POST'])
def show_export_monograph():
	results = mono_data_operation(forms.all_monograph_from_db())
	length = len(results)
	return render_template("tec/ex_monograph.html", results = results,length = length)

@app.route('/tec/export_patent',methods=['GET','POST'])
def show_export_patent():
	results = patent_data_operation(forms.all_patent_from_db())
	length = len(results)
	return render_template("tec/ex_patent.html", results = results,length = length)

@app.route('/tec/export_project',methods=['GET','POST'])
def show_export_project():
	results = project_data_operation(forms.all_project_from_db())
	length = len(results)
	return render_template("tec/ex_project.html", results = results,length = length)

@app.route('/tec/aca_info',methods=['GET','POST'])
def show_aca_info_tec():
	if 'username' in session:
		username = session['username']
	else:
		return redirect(url_for('login'))
		
	resultset = session['resultset']
	print(resultset)
	return render_template("/tec/aca_info.html",resultset = resultset,username=username)

@app.route('/tec/deg_info',methods=['GET','POST'])
def show_deg_info_tec():
	if 'username' in session:
		username = session['username']
	else:
		return redirect(url_for('login'))
		
	resultset = session['resultset']
	return render_template("/tec/deg_info.html",resultset = resultset,username=username)

@app.route('/tec/pat_info',methods=['GET','POST'])
def show_pat_info_tec():
	if 'username' in session:
		username = session['username']
	else:
		return redirect(url_for('login'))
		
	resultset = session['resultset']
	print(resultset)
	return render_template("/tec/pat_info.html",resultset = resultset,username=username)

@app.route('/tec/pro_info',methods=['GET','POST'])
def show_pro_info_tec():
	if 'username' in session:
		username = session['username']
	else:
		return redirect(url_for('login'))

	resultset = session['resultset']
	return render_template("/tec/pro_info.html",resultset = resultset,username=username)

@app.route('/tec/mono_info',methods=['GET','POST'])
def show_mono_info_tec():
	if 'username' in session:
		username = session['username']
	else:
		return redirect(url_for('login'))

	resultset = session['resultset']
	return render_template("/tec/mono_info.html",resultset = resultset,username=username)

@app.route('/tec/stand_info',methods=['GET','POST'])
def show_stand_info_tec():
	if 'username' in session:
		username = session['username']
	else:
		return redirect(url_for('login'))

	resultset = session['resultset']
	print(resultset)
	return render_template("/tec/stand_info.html",resultset = resultset,username=username)

@app.route('/tec/aca_edit',methods=['GET','POST'])
def show_aca_edit_tec():
	if 'username' in session:
		username = session['username']
	else:
		return redirect(url_for('login'))

	resultset = session['resultset']
	print(resultset)
	return render_template("/tec/aca_edit.html",resultset = resultset,username=username)

@app.route('/tec/deg_edit',methods=['GET','POST'])
def show_deg_edit_tec():
	if 'username' in session:
		username = session['username']
	else:
		return redirect(url_for('login'))

	resultset = session['resultset']
	print(resultset)
	return render_template("/tec/deg_edit.html",resultset = resultset,username=username)

@app.route('/tec/pat_edit',methods=['GET','POST'])
def show_pat_edit_tec():
	if 'username' in session:
		username = session['username']
	else:
		return redirect(url_for('login'))

	resultset = session['resultset']
	print(resultset)
	return render_template("/tec/pat_edit.html",resultset = resultset,username=username)

@app.route('/tec/pro_edit',methods=['GET','POST'])
def show_pro_edit_tec():
	if 'username' in session:
		username = session['username']
	else:
		return redirect(url_for('login'))
		
	resultset = session['resultset']
	print(resultset)
	return render_template("/tec/pro_edit.html",resultset = resultset,username=username)

@app.route('/tec/mono_edit',methods=['GET','POST'])
def show_mono_edit_tec():
	if 'username' in session:
		username = session['username']
	else:
		return redirect(url_for('login'))

	resultset = session['resultset']
	print(resultset)
	return render_template("/tec/mono_edit.html",resultset = resultset,username=username)

@app.route('/tec/stand_edit',methods=['GET','POST'])
def show_stand_edit_tec():
	if 'username' in session:
		username = session['username']
	else:
		return redirect(url_for('login'))

	resultset = session['resultset']
	print(resultset)
	return render_template("/tec/stand_edit.html",resultset = resultset,username=username)

@app.route('/tec/editprofile',methods=['GET','POST'])
def show_tec_editprofile():
	if 'username' in session:
		username = session['username']
	else:
		return redirect(url_for('login'))

	return render_template('/tec/editprofile.html')

@app.route("/tec/academic_manage",methods=['GET','POST'])
def show_academic_manage_tec():
	if 'username' in session:
		username = session['username']
	else:
		return redirect(url_for('login'))
		
	results = forms.all_academic_from_db()
	length = len(results)
	return render_template("/tec/academic.html",results = results,length = length, username = username)

@app.route("/tec/project_manage",methods=['GET','POST'])
def show_project_manage_tec():
	if 'username' in session:
		username = session['username']
	else:
		return redirect(url_for('login'))

	results = forms.all_project_from_db()
	length = len(results)
	print(results)
	return render_template("/tec/project.html",results = results,length = length, username = username)

@app.route("/tec/patent_manage",methods=['GET','POST'])
def show_patent_manage_tec():
	if 'username' in session:
		username = session['username']
	else:
		return redirect(url_for('login'))

	results = forms.all_patent_from_db()
	length = len(results)
	return render_template("/tec/patent.html",results = results,length = length, username = username)

@app.route("/tec/monograph_manage",methods=['GET','POST'])
def show_monograph_manage_tec():
	if 'username' in session:
		username = session['username']
	else:
		return redirect(url_for('login'))

	results = forms.all_monograph_from_db()
	length = len(results)
	return render_template("/tec/monograph.html",results = results,length = length, username = username)

@app.route("/tec/degree_manage",methods=['GET','POST'])
def show_degree_manage_tec():
	if 'username' in session:
		username = session['username']
	else:
		return redirect(url_for('login'))

	results = forms.all_degree_from_db()
	length = len(results)
	return render_template("/tec/degree.html",results = results,length = length, username = username)

@app.route("/tec/standard_manage",methods=['GET','POST'])
def show_standard_manage_tec():
	if 'username' in session:
		username = session['username']
	else:
		return redirect(url_for('login'))

	results = forms.all_standard_from_db()
	length = len(results)
	print(results)
	return render_template("/tec/standard.html",results = results,length = length, username = username)

@app.route('/tec/tables',methods=['GET','POST'])
def show_tables_tec():
	lengthset=[]
	if 'username' in session:
		username = session['username']
	else:
		return redirect(url_for('login'))
		
	userid=forms.show_userid_from_tecdb(username)
	result=forms.show_tec_info_from_db(userid)

	length=len(result)
	for i in range(len(result)):
		lengthset.append(len(result[i])-1)
	
	return render_template('/tec/tables.html',result=result, length=length, lengthset=lengthset,username=username)

@app.route('/tec/editpassword',methods=['GET','POST'])
def show_editpassword_tec():
	if 'username' in session:
		username = session['username']
	else:
		return redirect(url_for('login'))

	return render_template("/tec/editpassword.html",username=username)

@app.route("/tec/pass_edit",methods=['GET','POST'])
def verify_password_tec():
	if 'username' not in session :
		return redirect(url_for('login'))
	else:
		username = session['username']
		userid = forms.show_userid_from_tecdb(username)

	passwd = request.form.get('newPassword')
	
	result = forms.motify_tec_password(userid,passwd)
	
	return jsonify({'result':result})

#--------------su--------------
@app.route("/su/logout")
def su_logout():
	session.pop('username')
	print(session)
	return redirect(url_for('show_login'))

@app.route("/su/admin_login",methods=['GET','POST'])
def show_login():
	form = LoginForm()
	if request.method == 'POST':
		username=request.form.get('runame')
		password=request.form.get('rpasswd')
		print(username,password)
		user=forms.verify_admin_exist(username)
		if user is True and forms.verify_admin_password(username,password):
			session['username']=username
			statecode =1
		else:
			statecode = -2 #返回请登录界
		return jsonify({'result':statecode})
	return render_template("/su/index.html")

@app.route('/su/editpassword',methods=['GET','POST'])
def show_editpassword_su():
	if 'username' in session:
		username = session['username']
	else:
		return redirect(url_for('show_login'))

	return render_template("/su/editpassword.html",username=username)

@app.route("/su/academic_manage",methods=['GET','POST'])
def show_academic_manage():
	results = forms.all_academic_from_db()
	length = len(results)
	return render_template("/su/academic.html",results = results,length = length)

@app.route("/su/project_manage",methods=['GET','POST'])
def show_project_manage():
	results = forms.all_project_from_db()
	length = len(results)
	print(results)
	return render_template("/su/project.html",results = results,length = length)

@app.route("/su/patent_manage",methods=['GET','POST'])
def show_patent_manage():
	results = forms.all_patent_from_db()
	length = len(results)
	return render_template("/su/patent.html",results = results,length = length)

@app.route("/su/monograph_manage",methods=['GET','POST'])
def show_monograph_manage():
	results = forms.all_monograph_from_db()
	length = len(results)
	return render_template("/su/monograph.html",results = results,length = length)

@app.route("/su/degree_manage",methods=['GET','POST'])
def show_degree_manage():
	results = forms.all_degree_from_db()
	length = len(results)
	return render_template("/su/degree.html",results = results,length = length)

@app.route("/su/standard_manage",methods=['GET','POST'])
def show_standard_manage():
	results = forms.all_standard_from_db()
	length = len(results)
	print(results)
	return render_template("/su/standard.html",results = results,length = length)

@app.route("/su/students",methods=['GET','POST'])
def show_su_studens():
	results = stu_data_operation(forms.show_stuinfo_from_db())
	length = len(results)
	return render_template("/su/students.html", results = results,length = length)

@app.route("/su/stu_del",methods=['GET','POST'])
def do_stu_del():
	datax = request.form.to_dict() 
	result = data_id_operation(datax)
	for i in range(len(result)):
		msg = forms.del_from_stu(result[i])

	return jsonify({'result':msg})

@app.route("/su/stu_add",methods=['GET','POST'])
def show_su_student_add():
	if 'username' in session:
		username = session['username']
	else:
		return redirect(url_for('show_login'))
	
	return render_template("/su/stu_add.html",username=username)

@app.route('/su/del',methods=['GET','POST'])
def do_su_delete():
	datax = request.form.to_dict() 

	result = data_id_operation(datax)

	for i in range(len(result)):
		msg = forms.del_from_data(result[i])
	
	return jsonify({'result':msg})

@app.route("/su/teachers",methods=['GET','POST'])
def show_su_teachers():
	results = tec_data_operation(forms.show_tecinfo_from_db())
	length = len(results)
	print(results)
	return render_template("/su/teachers.html", results = results,length = length)
	
@app.route("/su/tec_add",methods=['GET','POST'])
def show_su_teacher_add():
	if 'username' in session:
		username = session['username']
	else:
		return redirect(url_for('show_login'))

	if request.method == 'POST':
		tecName = request.form.get('tecName')
		tecId = request.form.get('tecId')
		SEX = request.form.get('SEX')
		department = request.form.get('department')
		tecType = request.form.get('tecType')
		result = forms.insert_tec(tecName,tecId,SEX,department,tecType)
 		if result == True:
			return jsonify({"msg":"已添加成功"})
		else:
			return jsonify({"msg":"抱歉，字段输入错误，请稍后再试"})


	return render_template("/su/tec_add.html",username=username)
 
@app.route("/su/tec_del",methods=['GET','POST'])
def def_tec():
	result=True
	value_set=[]
	index = request.form.to_dict()
	for value in index.values():
		value_set.append(value)
	
	for i in range(len(value_set)):
		result = result and forms.del_from_tec(value_set[i])

	if result == True:
		return jsonify({"msg":"已成功删除"})
	else:
		return jsonify({"msg":"抱歉，请稍后再试"})



@app.route('/su/aca_info',methods=['GET','POST'])
def show_aca_info_su():
	if 'username' in session:
		username = session['username']
	else:
		return redirect(url_for('show_login'))
		
	resultset = session['resultset']
	print(resultset)
	return render_template("/su/aca_info.html",resultset = resultset)

@app.route('/su/deg_info',methods=['GET','POST'])
def show_deg_info_su():
	if 'username' in session:
		username = session['username']
	else:
		return redirect(url_for('show_login'))
		
	resultset = session['resultset']
	return render_template("/su/deg_info.html",resultset = resultset)

@app.route('/su/pat_info',methods=['GET','POST'])
def show_pat_info_su():
	if 'username' in session:
		username = session['username']
	else:
		return redirect(url_for('show_login'))
		
	resultset = session['resultset']
	print(resultset)
	return render_template("/su/pat_info.html",resultset = resultset)

@app.route('/su/pro_info',methods=['GET','POST'])
def show_pro_info_su():
	if 'username' in session:
		username = session['username']
	else:
		return redirect(url_for('show_login'))

	resultset = session['resultset']
	return render_template("/su/pro_info.html",resultset = resultset)

@app.route('/su/mono_info',methods=['GET','POST'])
def show_mono_info_su():
	if 'username' in session:
		username = session['username']
	else:
		return redirect(url_for('show_login'))

	resultset = session['resultset']
	return render_template("/su/mono_info.html",resultset = resultset)

@app.route('/su/stand_info',methods=['GET','POST'])
def show_stand_info_su():
	if 'username' in session:
		username = session['username']
	else:
		return redirect(url_for('show_login'))

	resultset = session['resultset']
	print(resultset)
	return render_template("/su/stand_info.html",resultset = resultset)

@app.route('/up_file', methods=['GET', 'POST'])
def up_file():
    if request.method == "POST":
        file = request.files['file'] 
        file_name = file.filename
        file.save(os.path.join('templates/files', file_name)) 
        return '上传成功'
		
		
@app.route("/aca_upload",methods=['GET','POST'])
def upload_file():
	if request.method =='POST':
		
		file = request.files['file']
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			msg = load_file(filename)
			return jsonify({'result':msg})
		else:
			msg = '文件格式错误' 
			
			return jsonify({'result':msg})
	else:
		msg = '上传错误'
		return jsonify({'result':msg})

def load_file(filename):
	res = True
	if 'xlsx' in filename.rsplit('.', 1)[1] or 'xls' in filename.rsplit('.', 1)[1]:
		new_filename = xlsx_to_csv(filename)
		load_file(new_filename)
	else:
		pass

	filename = str(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	df = pd.read_csv(filename)
	df = df.dropna(axis = 0,how='all') #去掉NaN项
	df = df.where(df.notnull(), "")
	df_list = df.values.tolist()	#转为列表
	for i in range(len(df_list)):
		res = res and forms.add_multi_aca(df_list[i])
	return res

@app.route("/pat_upload",methods=['GET','POST'])
def upload_file_pat():
	if request.method =='POST':
		file = request.files['file']
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		print("test")
		msg = load_file_pat(filename)

		return jsonify({'result':msg})
	else: 
		print("test1")
		msg = '上传错误'
		return jsonify({'result':msg})

def load_file_pat(filename):
	res = True
	if 'xlsx' in filename.rsplit('.', 1)[1] or 'xls' in filename.rsplit('.', 1)[1]:
		new_filename = xlsx_to_csv(filename)
		load_file_pat(new_filename)
	else:
		pass

	filename = str(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	df = pd.read_csv(filename)
	df = df.dropna(axis = 0,how='all') #去掉NaN项
	df = df.where(df.notnull(), "")
	df_list = df.values.tolist()	#转为列表
	prinf(df_list)
	for i in range(len(df_list)):
		res = res and forms.add_multi_pat(df_list[i])
	return res






def xlsx_to_csv(filename):
	filename = str(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	workbook = xlrd.open_workbook(filename)
	table = workbook.sheet_by_index(0)
	with codecs.open(os.path.join(app.config['UPLOAD_FOLDER'], filename)+'.csv', 'w', encoding='utf-8') as f:
		write = csv.writer(f)
		for row_num in range(table.nrows):
			row_value = table.row_values(row_num)
			write.writerow(row_value)
	return filename+".csv"



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000,debug=True)

