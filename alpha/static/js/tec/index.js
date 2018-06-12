jQuery(document).ready(function(){
								
	///// TRANSFORM CHECKBOX /////							
	jQuery('input:checkbox').uniform();
	
	///// LOGIN FORM SUBMIT /////
	var verifyCode = new GVerify("v_container");
jQuery('#loginbutton').click(function(){
    
    var uname=jQuery('#username').val();
    var passwd=jQuery('#password').val();
    var type=jQuery("input[name='type']:checked").val();
    console.log(type);
    if(uname && passwd){
      jQuery('.nousername').hide();
      var res = verifyCode.validate(document.getElementById("code").value);
      if(res){
        console.log("验证码正确");
        $.ajax({
             url: "",
           data:{
              type:type,
              uname:uname,
              passwd:passwd
              },
              dataType: "json",
              type:"POST",
              success: function(data){
                msg = data.result
                if(msg== 1){
                    alert("登陆成功！");
                    window.open("/stu/forms","_self")
                }
                else if (msg== -2){
                    alert("用户名或密码错误！");
                    window.location.reload();
                    
                }
                else if(msg ==-1){
                  window.location.reload();
                }
                else if(msg ==2){
                  alert("登陆成功！");
                  window.open("/tec/forms","_self")
                }

             },
              error:function(){
                jQuery('.nopassword').fadeIn();
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
    var uname=jQuery('#username').val();
    var passwd=jQuery('#password').val();
    if(uname && passwd){
      jQuery('.nousername').hide();
      var res = verifyCode.validate(document.getElementById("code").value);
      if(res){
        console.log("验证码正确");
        $.ajax({
             url: "",
           data:{
              uname:uname,
              passwd:passwd
              },
              dataType: "json",
              type:"POST",
              success: function(){
                console.log("成果！");
                },
              error:function(){
                jQuery('.nopassword').fadeIn();
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



	jQuery('.loginboxinner').click(function(){
		jQuery('.nousername').hide();
		jQuery('.nocode').hide();
		jQuery('.nopassword').hide();
	});
	///// ADD PLACEHOLDER /////
	jQuery('#username').attr('placeholder','请输入用户名');
	jQuery('#password').attr('placeholder','请输入密码');
	
	
});

