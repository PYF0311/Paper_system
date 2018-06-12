/*
 * 	Additional function for this template
 *	Written by ThemePixels	
 *	http://themepixels.com/
 *
 *	Copyright (c) 2012 ThemePixels (http://themepixels.com)
 *	
 *	Built for Amanda Premium Responsive Admin Template
 *  http://themeforest.net/category/site-templates/admin-templates
 */

//jQuery.noConflict();

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
	
	//学生专业选择
jQuery('.formwrapper > input[name="major"]').change(function(){
	   if(jQuery('input[name="major"]:first').attr("checked")) {
			jQuery('.formwrapper >span:first').css("display","inline");
			jQuery("biology").val("微生物学");
			jQuery('#bio_select').change(function(){
				var bio_select=jQuery(this).val();
				console.log(bio_select);
				jQuery('#biology').val(bio_select);
			});
			console.log(jQuery('#bio_select').val());
		} else {
			jQuery('.formwrapper >span:first').css("display","none");
		}
		if(jQuery('input[name="major"]').eq(1).attr("checked")) {
			jQuery('.formwrapper span').eq(1).css("display","inline");
			jQuery("#food").val("食品科学");
			jQuery('#food_select').change(function(){
				var food_select=jQuery(this).val();
				console.log(food_select);
				jQuery('#food').val(food_select);
			});
			console.log(jQuery('#food').val());
		} else {
			jQuery('.formwrapper span').eq(1).css("display","none");
		}
		if(jQuery('input[name="major"]').eq(2).attr("checked")) {
			jQuery('.formwrapper span').eq(2).css("display","inline");
		} else {
			jQuery('.formwrapper span').eq(2).css("display","none");
		}
		if(jQuery('input[name="major"]').eq(3).attr("checked")) {
			jQuery('.formwrapper span').eq(3).css("display","inline");
		} else {
			jQuery('.formwrapper span').eq(3).css("display","none");
		}
		if(jQuery('input[name="major"]').eq(4).attr("checked")) {
			jQuery('.formwrapper span').eq(4).css("display","inline");
		} else {
			jQuery('.formwrapper span').eq(4).css("display","none");
		}
	});	
	//上传文件
	$('.addmulti').click(function(){
			$('#dialogBox').dialogBox({
				type: 'correct',  //three type:'normal'(default),'correct','error',
				width: 300,
				height: 200,
				hasMask: true,
				hasClose: true,
				effect: 'sign',
				title: '上传文件',
				content: '<form name="upload" action="1.php"><input type="file" name="filename"><br/><br/><button type="submit">上传</button></form>'
				//content:'<form action="" method="post" enctype="multipart/form-data"><input type="file" name="files[]" id="demo-fileInput-3" multiple><input type="submit" class="btn-custom green" value="上传"></form>'
			});
	});
	//论文分类显示
	$('.pageheader .hornav li').click(function(){
		var show=jQuery(this).attr('title');
		jQuery('.contentwrapper .subcontent').css('display','none');
		$('.pageheader .hornav li').removeClass('current');
		$(this).addClass('current');
		$('#'+show).css('display','block');
		
	});
	

	
	///// SHOW/HIDE NOTIFICATION /////
	
	jQuery('.notification a').click(function(){
		var t = jQuery(this);
		var url = t.attr('href');
		if(!jQuery('.noticontent').is(':visible')) {
			jQuery.post(url,function(data){
				t.parent().append('<div class="noticontent">'+data+'</div>');
			});
			//this will hide user info drop down when visible
			jQuery('.userinfo').removeClass('active');
			jQuery('.userinfodrop').hide();
		} else {
			t.parent().removeClass('active');
			jQuery('.noticontent').hide();
		}
		return false;
	});
	
	
	
	///// SHOW/HIDE BOTH NOTIFICATION & USERINFO WHEN CLICKED OUTSIDE OF THIS ELEMENT /////


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
	
	
	///// NOTIFICATION CONTENT /////
	
	jQuery('.notitab a').live('click', function(){
		var id = jQuery(this).attr('href');
		jQuery('.notitab li').removeClass('current'); //reset current 
		jQuery(this).parent().addClass('current');
		if(id == '#messages')
			jQuery('#activities').hide();
		else
			jQuery('#messages').hide();
			
		jQuery(id).show();
		return false;
	});
	
	
	
	///// SHOW/HIDE VERTICAL SUB MENU /////	
	
	jQuery('.vernav > ul li a, .vernav2 > ul li a').each(function(){
		var url = jQuery(this).attr('href');
		jQuery(this).click(function(){
			if(jQuery(url).length > 0) {
				if(jQuery(url).is(':visible')) {
					if(!jQuery(this).parents('div').hasClass('menucoll') &&
					   !jQuery(this).parents('div').hasClass('menucoll2'))
							jQuery(url).slideUp();
				} else {
					jQuery('.vernav ul ul, .vernav2 ul ul').each(function(){
							jQuery(this).slideUp();
					});
					if(!jQuery(this).parents('div').hasClass('menucoll') &&
					   !jQuery(this).parents('div').hasClass('menucoll2'))
							jQuery(url).slideDown();
				}
				return false;	
			}
		});
	});
	
	
	///// SHOW/HIDE SUB MENU WHEN MENU COLLAPSED /////
	jQuery('.menucoll > ul > li, .menucoll2 > ul > li').live('mouseenter mouseleave',function(e){
		if(e.type == 'mouseenter') {
			jQuery(this).addClass('hover');
			jQuery(this).find('ul').show();	
		} else {
			jQuery(this).removeClass('hover').find('ul').hide();	
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
	
	
	///// NOTIFICATION CLOSE BUTTON /////
	
	jQuery('.notibar .close').click(function(){
		jQuery(this).parent().fadeOut(function(){
			jQuery(this).remove();
		});
	});
	
	
	///// COLLAPSED/EXPAND LEFT MENU /////
	jQuery('.togglemenu').click(function(){
		if(!jQuery(this).hasClass('togglemenu_collapsed')) {
			
			//if(jQuery('.iconmenu').hasClass('vernav')) {
			if(jQuery('.vernav').length > 0) {
				if(jQuery('.vernav').hasClass('iconmenu')) {
					jQuery('body').addClass('withmenucoll');
					jQuery('.iconmenu').addClass('menucoll');
				} else {
					jQuery('body').addClass('withmenucoll');
					jQuery('.vernav').addClass('menucoll').find('ul').hide();
				}
			} else if(jQuery('.vernav2').length > 0) {
			//} else {
				jQuery('body').addClass('withmenucoll2');
				jQuery('.iconmenu').addClass('menucoll2');
			}
			
			jQuery(this).addClass('togglemenu_collapsed');
			
			jQuery('.iconmenu > ul > li > a').each(function(){
				var label = jQuery(this).text();
				jQuery('<li><span>'+label+'</span></li>')
					.insertBefore(jQuery(this).parent().find('ul li:first-child'));
			});
		} else {
			
			//if(jQuery('.iconmenu').hasClass('vernav')) {
			if(jQuery('.vernav').length > 0) {
				if(jQuery('.vernav').hasClass('iconmenu')) {
					jQuery('body').removeClass('withmenucoll');
					jQuery('.iconmenu').removeClass('menucoll');
				} else {
					jQuery('body').removeClass('withmenucoll');
					jQuery('.vernav').removeClass('menucoll').find('ul').show();
				}
			} else if(jQuery('.vernav2').length > 0) {	
			//} else {
				jQuery('body').removeClass('withmenucoll2');
				jQuery('.iconmenu').removeClass('menucoll2');
			}
			jQuery(this).removeClass('togglemenu_collapsed');	
			
			jQuery('.iconmenu ul ul li:first-child').remove();
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
	
	
	jQuery('.searchicon').live('click',function(){
		jQuery('.searchinner').show();
	});
	
	jQuery('.searchcancel').live('click',function(){
		jQuery('.searchinner').hide();
	});
	
	
	
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
         url:"/stu/pass_edit",

       
         data:$("#editpassword").serialize(), //表单数据序列化, 可以对form表单进行序列化，从而将form表单中的所有参数传递到服务端。
         dataType: "json",
         type:"POST",

         success:function(data){
	         msg = data.result

	         if(msg == true){
	           alert("修改成功");
	           window.open("/login","_self")

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
    $("#editprofile_tec button").click(function(){
      
       $.ajax({
         url:"",
         type:"POST",
         dataType: "json",
         data:$("#editprofile_tec").serialize(), //表单数据序列化, 可以对form表单进行序列化，从而将form表单中的所有参数传递到服务端。
         success:function(data){
	         if(data = 200){
	           console.log("修改成功");
	         }else{
	           console.log("密码错误");
	         }
       },
       error:function(){
         console.log("请求出错！");
       }
       });
      
});
    $("#editprofile_stu button").click(function(){
       $.ajax({
         url:"",
         type:"POST",
         data:$("#editprofile_stu").serialize(), //表单数据序列化, 可以对form表单进行序列化，从而将form表单中的所有参数传递到服务端。
         success:function(data){
	         if(data = 200){
	           console.log("修改成功");
	         }else{
	           console.log("密码错误");
	         }
       },
       error:function(){
         console.log("请求出错！");
       }
       });
       
});
	
});