## 1.su端
- /su/teachers

1.编辑教师：
@app.route("/su/tec_edit",methods=['GET','POST'])  
@app.route("/su/tec_edit_sub",methods=['GET','POST'])  
测试时后台可以输出信息

- /su/students

1.编辑学生：
@app.route("/su/stu_edit",methods=['GET','POST'])  
@app.route("/su/stu_edit_sub",methods=['GET','POST'])  
测试时后台可以输出信息

- /su/editpassword
@app.route("/su/pass_edit",methods=['GET','POST'])  
测试时后台可以输出信息,前端密码验证不完善，正在完善中


## 2.stu端
1、``aca_edit``和``deg_edit``等edit页面
@app.route("/form_edit",methods=['GET','POST'])
测试时后台可以输出信息


2、/stu/editprofile
@app.route("/stu/edit_pro_sub",methods=['GET','POST'])
测试时后台可以输出信息


##  3.tec端

1、``aca_edit``和``deg_edit``等edit页面
提交的ajax请求与学生端同一个，是否需要分开？

2、/tec/editprofile
@app.route("/tec/edit_pro_sub",methods=['GET','POST'])
测试时后台可以输出信息
----