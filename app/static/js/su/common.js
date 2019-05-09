jQuery(document).ready(function(){
	///// SHOW/HIDE USERDATA WHEN USERINFO IS CLICKED ///// 
	
	jQuery('.userinfo').click(function(){
		if(!jQuery(this).hasClass('active')) {
			jQuery('.userinfodrop').show();
			jQuery(this).addClass('active');
		} else {
			jQuery('.userinfodrop').hide();
			jQuery(this).removeClass('active');
		}
		//remove notification box if visible
		jQuery('.notification').removeClass('active');
		jQuery('.noticontent').remove();
		
		return false;
	});
	
	//显示个人信息编辑窗口
		jQuery(document).click(function(event) {
			var ud = jQuery('.userinfodrop');
			var nb = jQuery('.noticontent');
			
			//hide user drop menu when clicked outside of this element
			if(!jQuery(event.target).is('.userinfodrop') 
				&& !jQuery(event.target).is('.userdata') 
				&& ud.is(':visible')) {
					ud.hide();
					jQuery('.userinfo').removeClass('active');
			}
			
			//hide notification box when clicked outside of this element
			if(!jQuery(event.target).is('.noticontent') && nb.is(':visible')) {
				nb.remove();
				jQuery('.notification').removeClass('active');
			}
		});
		
		///// HORIZONTAL NAVIGATION (AJAX/INLINE DATA) /////	
		
		jQuery('.hornav a').click(function(){
			//this is only applicable when window size below 450px
			if(jQuery(this).parents('.more').length == 0)
				jQuery('.hornav li.more ul').hide();
			//remove current menu
			jQuery('.hornav li').each(function(){
				jQuery(this).removeClass('current');
			});
			jQuery(this).parent().addClass('current');	// set as current menu
			var url = jQuery(this).attr('href');
			if(jQuery(url).length > 0) {
				jQuery('.contentwrapper .subcontent').hide();
				jQuery(url).show();
			} else {
				jQuery.post(url, function(data){
					jQuery('#contentwrapper').html(data);
					jQuery('.stdtable input:checkbox').uniform();	//restyling checkbox
				});
			}
			return false;
		});
		
		
		
		///// SEARCH BOX ON FOCUS /////
		
		jQuery('#keyword').bind('focusin focusout', function(e){
			var t = jQuery(this);
			if(e.type == 'focusin' && t.val() == 'Enter keyword(s)') {
				t.val('');
			} else if(e.type == 'focusout' && t.val() == '') {
				t.val('Enter keyword(s)');	
			}
		});
		
		
		
		
		///// RESPONSIVE /////
		if(jQuery(document).width() < 640) {
			jQuery('.togglemenu').addClass('togglemenu_collapsed');
			if(jQuery('.vernav').length > 0) {
				
				jQuery('.iconmenu').addClass('menucoll');
				jQuery('body').addClass('withmenucoll');
				jQuery('.centercontent').css({marginLeft: '56px'});
				if(jQuery('.iconmenu').length == 0) {
					jQuery('.togglemenu').removeClass('togglemenu_collapsed');
				} else {
					jQuery('.iconmenu > ul > li > a').each(function(){
						var label = jQuery(this).text();
						jQuery('<li><span>'+label+'</span></li>')
							.insertBefore(jQuery(this).parent().find('ul li:first-child'));
					});		
				}
		
			} else {
				
				jQuery('.iconmenu').addClass('menucoll2');
				jQuery('body').addClass('withmenucoll2');
				jQuery('.centercontent').css({marginLeft: '36px'});
				
				jQuery('.iconmenu > ul > li > a').each(function(){
					var label = jQuery(this).text();
					jQuery('<li><span>'+label+'</span></li>')
						.insertBefore(jQuery(this).parent().find('ul li:first-child'));
				});		
			}
		}
		
		 
		
		
		
		///// ON LOAD WINDOW /////
		function reposSearch() {
			if(jQuery(window).width() < 520) {
				if(jQuery('.searchinner').length == 0) {
					jQuery('.search').wrapInner('<div class="searchinner"></div>');	
					jQuery('<a class="searchicon"></a>').insertBefore(jQuery('.searchinner'));
					jQuery('<a class="searchcancel"></a>').insertAfter(jQuery('.searchinner button'));
				}
			} else {
				if(jQuery('.searchinner').length > 0) {
					jQuery('.search form').unwrap();
					jQuery('.searchicon, .searchcancel').remove();
				}
			}
		}
		reposSearch();
		
		///// ON RESIZE WINDOW /////
		jQuery(window).resize(function(){
			
			if(jQuery(window).width() > 640)
				jQuery('.centercontent').removeAttr('style');
			reposSearch();
			
		});
  //6到15位字母或数字
    var reg=/^[0-9a-zA-Z]{6,15}$/;
    //新密码校验
    var oldpasswd=false;
    var newPasswd=false;
    var repeatPasswd=false;
    $("#OldPassword").blur(function(){
      var Password = $(this).val();
      if(Password==""||Password==null){
       $(this).next('span').css("display","inline-block");
       oldpasswd=false;
      }
      else if(!reg.test(Password)){
       $(this).next('span').html("密码格式不正确,请重新输入！").css("display","inline-block");
       oldpasswd=false;
      }
      else{
      	$(this).next('span').css("display","none");
      	oldpasswd=true;
      }
    });
    $("#newPassword").blur(function(){
      var newPassword = $(this).val();
      if(newPassword==""||newPassword==null){
       $(this).next('span').css("display","inline-block");
       newPasswd=false;
      }
      else if(!reg.test(newPassword)){
       $(this).next('span').html("密码格式不正确,请重新输入！").css("display","inline-block");
       newPasswd=false;
      }
      else{
      	$(this).next('span').css("display","none");
      	newPasswd=true;
      }
    });
    //重复密码校验
    $("#repeatPassword").blur(function(){
      var newPass = $("#newPassword").val();
      var repPass = $(this).val();
      if(newPass != repPass){
       $(this).next('span').css("display","inline-block");
       repeatPasswd=false;
      }else{
      	$(this).next('span').css("display","none");
      	repeatPasswd=true;
      }
    });
    //表单提交前校验
    $("#editpassword button").click(function(){
      if(oldpasswd && repeatPasswd && newPasswd){
       $.ajax({
         url:"",//管理员修改密码
         data:$("#editpassword").serialize(), //表单数据序列化, 可以对form表单进行序列化，从而将form表单中的所有参数传递到服务端。
         dataType: "json",
         type:"POST",
         success:function(data){
	         msg = data.result
	         if(msg == true){
	           alert("修改成功");
	           window.open("/su/login","_self")
	         }else{
	           alert("修改失败"); 
	         }
       },
       error:function(){
         console.log("请求出错！");
       }
       });
      }   
});
});