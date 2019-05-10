var finish;
jQuery(document).ready(function(){ 
	var slider = new SliderUnlock("#slider",{
			successLabelTip : "验证成功"	
		},function(){
	    	finish=true;
		});
	slider.init();
	


	jQuery('.loginboxinner').click(function(){
		jQuery('.nousername').hide();
		jQuery('.nocode').hide();
	});
  jQuery('#username').attr('placeholder','请输入账号');
  jQuery('#password').attr('placeholder','请输入密码');
  jQuery('#runame').attr('placeholder','请输入账号');
  jQuery('#rpasswd').attr('placeholder','请输入密码');
	
});
