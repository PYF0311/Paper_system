# Paper_system_demo
1、ajax交互都在custom.js里  
2、execl导出jq如下，须后端返回论文类型  
jQuery('.exportbutton_execl').click(function(){
		 。。。。。。。
					    if(msg== 'academic'){
					            window.open("/xlsdownload01");
					        }
					        else if (msg== 'degree'){ 
					            window.open("/xlsdownload02");
					        }
					        else if(msg =='patent'){
					            window.open("/xlsdownload03");
					        }
					        else if(msg =='project'){ 
					            window.open("/xlsdownload04");
					        }
					        else if(msg =='mono'){ 
					            window.open("/xlsdownload05");
					        }
					        else if(msg =='stand'){ 
					            window.open("/xlsdownload06");
					        }
					   }   
3、教师添加成功后，表格教师姓名栏里出现的是教工号，可能哪里出现了错误。
