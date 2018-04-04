from flask import Flask
from flask import render_template,g
from flask import request, url_for, flash,redirect,session,Response,send_from_directory,abort,make_response
from flask_login import UserMixin,LoginManager,login_required,login_user
from flask_wtf import Form 
from wtforms import StringField, PasswordField,SubmitField
from wtforms.validators import Required
import forms

app = Flask(__name__)
app.config['SECRET_KEY'] = 'oh_so_secret'


class LoginForm(Form):
	username = StringField('username', validators=[Required()])
	password = PasswordField('password',validators=[Required()])
	submit = SubmitField('Submit')
class AddForm(Form):
	tag = StringField('tag', validators=[Required()])
	acadPaperNameCH = StringField('acadPaperNameCH', validators=[Required()])
	acadPaperNameEN = StringField('acadPaperNameEN', validators=[Required()])
	FirstEdit = StringField('FirstEdit', validators=[Required()])
	SecondEdit = StringField('SecondEdit', validators=[Required()])
	ThreeEdit = StringField('ThirdEdit', validators=[Required()])
	ForthEdit = StringField('FourthEdit', validators=[Required()])
	transEdit = StringField('transEdit', validators=[Required()]) 
	issueName = StringField('issueName', validators=[Required()])
	pubIssue = StringField('pubIssue', validators=[Required()])
	pubPeriod = StringField('pubPeriod', validators=[Required()])
	pubPage = StringField('pubPage', validators=[Required()])
	depa = StringField('depa', validators=[Required()])
	paperType = StringField('paperType', validators=[Required()])
	indexNum = StringField('indexNum', validators=[Required()])
	part = StringField('part', validators=[Required()])
	impactFactor = StringField('impactFactor', validators=[Required()])
	submit = SubmitField('Submit')
class RegisterForm(Form):
	stuname = StringField('username', validators=[Required()])
	password = PasswordField('password',validators=[Required()])
	stuid = StringField('stuid', validators=[Required()])
	major = StringField('major', validators=[Required()])
	firstProf = StringField('firstProf', validators=[Required()]) 
	secondProf = StringField('secondProf', validators=[Required()]) 

@app.route("/forms",methods=['GET','POST'])
def show_forms():
	global SESSIONID
	username=forms.show_stuname_from_db(SESSIONID)
	Loginform = LoginForm()
	Addform = AddForm()
#	name=request.cookies.get('username')
#	print("name:",name)
#	name2=session.get('username')
#	print("name2:",name
	print(Addform['FirstEdit'])
	print(Addform['issueName'])
	print(Addform['SecondEdit'])
	print("ADD:",Addform.data)
	if request.method == 'POST':
		forms.add_info_to_db(Addform.data)
	
	return render_template("forms.html",username = username)

@app.route('/success',methods=['GET','POST'])
def show_add_succ():
	return render_template("add_succ.html")




@app.route('/register',methods=['GET','POST'])
def show_register():
	form = RegisterForm()
	if request.method == 'POST':
		user=forms.verify_user_exist(form.stuid.data)
#		print("user:",user)
		if user is not True:
			forms.add_stu_info_to_db(form.data)
			return redirect(url_for('show_tables'))
		else:
			statecode=-1  #用户已存在

	return render_template('register.html',form=form)

@app.route('/newpost',methods=['GET','POST'])
def show_newpost():
	editor=[]
	global SESSIONID
	username=forms.show_stuname_from_db(SESSIONID)
	form = LoginForm()
	result=forms.all_paper_from_db()
	length=len(result)
	print(result)
	return render_template('newpost.html',result=result, length=length, username=username)
	
	#return render_template('newpost.html',form=form,result=result,username=username)

@app.route('/info',methods=['GET','POST'])

def show_information():
	form = LoginForm()
	return render_template('information.html',form=form)


@app.route('/tables',methods=['GET','POST'])
def show_tables():
	lengthset=[]
	global SESSIONID
	username=forms.show_stuname_from_db(SESSIONID)
	form = LoginForm()
	result=forms.show_info_from_db(SESSIONID)
	print(result)
	length=len(result)
	for i in range(len(result)):
		lengthset.append(len(result[i])-1)
	print (lengthset)
	return render_template('tables.html',result=result, length=length, lengthset=lengthset,username=username)

@app.route('/dashboard',methods=['GET','POST'])
def show_dashboard():
	form = LoginForm()
	return render_template('dashboard.html',form=form)

@app.route('/editprofile',methods=['GET','POST'])
def show_editprofile():
	form = LoginForm()
	if 'username' not in session :
		return redirect(url_for('show_dashboard'))

	return render_template('editprofile.html',form=form)
@app.route('/add_succ.html',methods=['GET','POST'])
def show_add_succ_html():
	return render_template("add_succ.html")

@app.route("/logout")
def logout():
	logout_user() #Flask-Login中的logout_user函数
	flash('You have been logged out.') 
	return redirect(url_for('show_dashboard'))


@app.route('/login',methods=['GET','POST'])
def login():
	form = LoginForm()
	global SESSIONID
	if request.method == 'POST':
		username=form.username.data
		password=form.password.data
		session['username']="nihao"
		SESSIONID=str(request.form['username'])
		user=forms.verify_user_exist(form.username.data)
		forms.verify_password(form.username.data,form.password.data)
		result=forms.verify_password(username,form.password.data)
		if user is True and forms.verify_password(form.username.data,form.password.data):
			rsp = make_response()
			rsp.set_cookie('username','SESSIONID')
			return redirect(url_for('show_forms'))
			
		else:
			statecode=-1
	
	return render_template('index.html', form=form)

@app.route('/do_login', methods=['POST'])
def do_login():
	name = request.form.get('username')
	session['username'] = name
	return 'success'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000,debug=True)
#threaded=True,
