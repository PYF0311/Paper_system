jQuery(document).ready(function(){
	var finish=false;
						
	///// TRANSFORM CHECKBOX /////							
	// jQuery('input:checkbox').uniform();
	///// LOGIN FORM SUBMIT /////
	var slider = new SliderUnlock("#slider",{
			successLabelTip : "验证成功"	
		},function(){
	    	finish=true;
		});
	slider.init();
	jQuery('#loginbutton').click(function(){
		var uname=jQuery('#username').val();
		var passwd=jQuery('#password').val();
		var type=jQuery("input[name='type']:checked").val();
		var msg;
		if(uname && passwd){
			jQuery('.nousername').hide();
			if(finish){
        $.ajax({
             url: "/login",
           data:{
              type:type,
              uname:uname,
              passwd:passwd,
			  dateTime: Math.random()
              },
              dataType: "json",
              type:"POST",
              success: function(data){
                msg = data.result;
                if(msg== 1){ 
                    window.open("/stu/forms","_self")
                }
                else if (msg== -2){
                    jQuery('.nopassword').fadeIn();
					 
                }
                else if(msg ==-1){
                  jQuery('.nopassword').fadeIn();
                }
                else if(msg ==2){ 
                  window.open("/tec/forms","_self")
                }

             },
              error:function(){
                jQuery('.nopassword').fadeIn();
				console.log("请求失败！");
              }
       }); 
			}else{
				jQuery('.nocode').fadeIn();
				return false;
			}
		}
		else {
			jQuery('.nousername').fadeIn();
			return false;	
		}
	});

jQuery('#rloginbutton').click(function(){
			var runame=jQuery('#runame').val();
			var rpasswd=jQuery('#rpasswd').val();
			var msg;
			if(runame && rpasswd){
				jQuery('.nousername').hide();
				if(finish){
				jQuery('.nousername').hide();
				$.ajax({
					 url: "/su/admin_login",
				     data:{
					  runame:runame,
					  rpasswd:rpasswd,
					  dateTime: Math.random()
					  },
					  dataType: "json",
					  type:"POST",
					  success: function(data){
						msg = data.result;
						if(msg==1){
							window.open("/su/academic_manage","_self");
						} 
						else if (msg==-2){
							jQuery('.nopassword').fadeIn();
						} 
						},
					  error:function(){
						  jQuery('.nopassword').fadeIn();
						  console.log("请求失败！");
					  }
			   }); 
			   }else{
			   		jQuery('.nocode').fadeIn();
			   		return false;
			   	}
			   }else {
			   	jQuery('.nousername').fadeIn();
			   	return false;	
			   }
			});
	jQuery('.loginboxinner').click(function(){
		jQuery('.nousername').hide();
		jQuery('.nocode').hide();
	});
  jQuery('#username').attr('placeholder','请输入账号');
  jQuery('#password').attr('placeholder','请输入密码');
  jQuery('#runame').attr('placeholder','请输入账号');
  jQuery('#rpasswd').attr('placeholder','请输入密码');
	
});
