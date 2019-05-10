# Paper_system_demo
1、ajax交互都在custom.js里
2、execl导出jq如下，须后端返回论文类型
jQuery('.exportbutton_execl').click(function(){
		var pattern=jQuery('.pattern').val();  
		post_data=table_data.getData();
		var ex_url="/xlsdownload_"+pattern;
		console.log(ex_url); 
		if(post_data.length){ 
		 $.ajax({
	   			   url: ex_url, 
				   data:{post_data: post_data},
				      dataType: "text",
				      type:"POST",
					  success: function(data){
					    msg = data.type  
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
					   }, 
				      error:function(){
				        alert("下载失败");
				      }
			 }); 
	}
		else alert('请选择数据');								//alert to 请选择数据
	});
3、教师添加成功后，表格教师姓名栏里出现的是教工号。