# Paper_system_demo
1��ajax��������custom.js��
2��execl����jq���£����˷�����������
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
				        alert("����ʧ��");
				      }
			 }); 
	}
		else alert('��ѡ������');								//alert to ��ѡ������
	});
3����ʦ��ӳɹ��󣬱���ʦ����������ֵ��ǽ̹��š�