 
var i=0,k=0,l=0;	
var a=3,c=3,d=3;
//学术论文
function getName(whichname){
	if(whichname.value){
	var name=whichname.value;
	var t_name=document.getElementById("t_name");
	var t_option=document.createElement("option");
	var t_txt=document.createTextNode(name);
	t_name.appendChild(t_option);
	t_option.appendChild(t_txt)
	}
}
function addAcademic(){
	var add_label=document.createElement("label");
	var add_p=document.createElement("p");
	var name=["第四作者","第五作者","第六作者","第七作者","第八作者"];
	var num=["fourthEdit","fifthEdit","sixthEdit","seventhEdit","eighthEdit"];
	if(i<5){
	var label_name=document.createTextNode(name[i]);
	var numb=num[i];
	i++;
	}else{
		alert("已达到最大数");
		return true;
	}
	add_p.appendChild(add_label);
	add_label.appendChild(label_name);
	var add_span=document.createElement("span");
	add_span.setAttribute("class","field");
	add_p.appendChild(add_span);
	var add_input=document.createElement("input");
	add_input.setAttribute("type","text");
	a++;
	add_input.setAttribute("name",numb);
	add_input.setAttribute("class","smallinput");
	add_input.setAttribute("onblur","getName(this)");
	add_span.appendChild(add_input);
	var academic_t_name=document.getElementById("academic_t_name");
	academic_t_name.parentNode.insertBefore(add_p,academic_t_name);
} 
//会议论文
function getcName(whichname){
	if(whichname.value){
	var name=whichname.value;
	var c_name=document.getElementById("c_name");
	var c_option=document.createElement("option");
	var c_txt=document.createTextNode(name);
	c_name.appendChild(c_option);
	c_option.appendChild(c_txt)
	}
}
 
//专利
function addPatent(){
	var patent_name = document.getElementById("patent_name");
	var add_label=document.createElement("label");
	var add_p=document.createElement("p");
	var name=["第四发明人","第五发明人","第六发明人","第七发明人","第八发明人"];
	var num=["fourthEdit","fifthEdit","sixthEdit","seventhEdit","eighthEdit"];
	if(k<5){
	var label_name=document.createTextNode(name[k]);
	var numb=num[k];
	k++;
	}else{
		alert("已达到最大数");
		return true;
	}
	var add_span=document.createElement("span");
	add_span.setAttribute("class","field");
	patent_name.appendChild(add_p);
	add_p.appendChild(add_label);
	add_label.appendChild(label_name);
	add_p.appendChild(add_span);
	var add_input=document.createElement("input");
	add_input.setAttribute("type","text");
	c++;
	add_input.setAttribute("name",numb);
	add_input.setAttribute("class","smallinput");
	add_span.appendChild(add_input);
} 
//项目
function addProject(){
	var project_name = document.getElementById("project_name");
	var add_label=document.createElement("label");
	var add_p=document.createElement("p");
	var name=["第四参与人","第五参与人","第六参与人","第七参与人","第八参与人"];
	var num=["fourthEdit","fifthEdit","sixthEdit","seventhEdit","eighthEdit"];
	if(l<5){
	var label_name=document.createTextNode(name[l]);
	var numb=num[l];
	l++;
	}else{
		alert("已达到最大数");
		return true;
	}
	var add_span=document.createElement("span");
	add_span.setAttribute("class","field");
	project_name.appendChild(add_p);
	add_p.appendChild(add_label);
	add_label.appendChild(label_name);
	add_p.appendChild(add_span);
	var add_input=document.createElement("input");
	add_input.setAttribute("type","text");
	c++;
	add_input.setAttribute("name",numb);
	add_input.setAttribute("class","smallinput");
	add_span.appendChild(add_input);
} 

 
	

 