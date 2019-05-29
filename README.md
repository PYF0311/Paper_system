## 1.su端
- /su/teachers

~~1.教师密码没有显示，可能是对应字段填错~~

~~2. 删除教师：删除链接填在/static/js/su/teacher.js里248行~~

3.编辑教师：

```
进入编辑页面的处理链接填在/static/js/su/teacher.js里273行
提交已修改好的处理链接填在/static/js/su/teacher.js里293行
```
**ERROR: --进入编辑页面的ajax，custom.js 827line:post_data输出为空，下面的删除链接是正常的，有返回值。见845行**
            
~~4.添加教师：添加链接填在/static/js/su/teacher.js里317行~~

- /su/students

1.编辑学生：

```
进入编辑页面的处理链接填在/static/js/su/student.js里294行
提交已修改好的处理链接填在/static/js/su/student.js里293行
```


**ERROR: --问题同[编辑教师]，console.log(post_data)输出为空，custom.js 704行**

~~2.添加学生：添加链接填在/static/js/su/student.js里317行~~

- /su/各类论文

~~1.txt导出时需要做一下是否为空判断~~

2.管理员修改密码链接/static/js/su/common.js里192行

**ERROR:仍然有上次那个问题，点击提交按钮没有反应。看不到有数据被获取**


## 2.stu端
1、``aca_edit``和``deg_edit``等edit页面：论文修改好提交的链接填在/static/js/tec/general.js里362行

**ERROR:仍然有上次那个问题，点击提交按钮没有反应。看不到有数据被获取**

2、/stu/editprofile

~~（1）需要placeholder填充默认值~~

（2）学生信息修改好提交的链接填在/static/js/tec/general.js里337行
**ERROR:仍然有上次那个问题，点击提交按钮没有反应。看不到有数据被获取**


##  3.tec端

1、``aca_edit``和``deg_edit``等edit页面：论文修改好提交的链接填在/static/js/tec/general.js里362行

**ERROR:仍然有上次那个问题，点击提交按钮没有反应。看不到有数据被获取**

2、/stu/editprofile


（1）需要placeholder填充默认值

（2）教师信息修改好提交的链接填在/static/js/tec/general.js里317行

**ERROR:仍然有上次那个问题，点击提交按钮没有反应。看不到有数据被获取**

----
### Extra(另外要做的):

1.把``/su/student``表格中默认人数从100改成25吧，100(per page)需要几秒的加载时间