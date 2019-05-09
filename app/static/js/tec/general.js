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
 
jQuery.noConflict();
jQuery(document).ready(function($) { 
								
								
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
	

	//论文分类显示
	$('.pageheader .hornav li').click(function(){
		var show=jQuery(this).attr('title');
		jQuery('.contentwrapper .subcontent').css('display','none');
		$('.pageheader .hornav li').removeClass('current');
		$(this).addClass('current');
		$('#'+show).css('display','block');
		
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

    $("#editpassword_tec button").click(function(){
      if(oldpasswd && repeatPasswd && newPasswd){
       $.ajax({
         url:"/tec/pass_edit",
         data:$("#editpassword_tec").serialize(), //表单数据序列化, 可以对form表单进行序列化，从而将form表单中的所有参数传递到服务端。
         dataType: "json",
         type:"POST",
         success:function(data){
	         msg = data.result
	         if(msg == true){
	           alert("修改成功");
	           window.open("/login","_self")

	         }else{
	           alert("修改失败");
	           console.log(oldpasswd);
	         }
       },
       error:function(){
         console.log("请求出错！");
       }
       });
      }   
});
//教师修改个人信息
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
//学生修改个人信息
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

 //修改论文提交
jQuery('form[name="form_edit"] button').click(function(){ 
	    	var tag=$(this).parents('form').children("input[type='hidden']").val(); 
	    	var gnl=confirm("确定要保存吗?");
				if (gnl==true){  
					$.ajax({
	                type: "POST",//方法类型
	                dataType: "json",//预期服务器返回的数据类型
	                url: "" ,//url
	                data: $(this).parents('form').serialize(),
	                success: function (data) {
	                    msg = data.result
	                    type = data.pageType 
	                    if(msg == true && type == 'tec'){
	                    alert("修改成功！");
	                    window.open("/tec/tables","_self")
	                }
	                    else if(msg == true && type == 'stu'){
	                    alert("修改成功！");
	                    window.open("/stu/tables","_self")
	                }
	                    else if(msg== false){
	                    alert("修改失败！"); 
	                    
	                }
	            },
	                error: function() {
	                    alert('请求失败'); 
	                }
	            }); 
				}else{  
					return false;  
				}   
	});	 

	
	//专利是否授权
	jQuery(':radio[name="ifAuthority"]').change(function(){
	if($(":radio[name='ifAuthority'][value='是']").attr("checked")){
		
		$("#authorize_time").css('display','block');//显示
	}else{
		$("#authorize_time").css('display','none');//隐藏  
		$("input[name='patentAuthorityTime']").attr("value",""); 
	}
	})
	//专利是否转让
	jQuery(':radio[name="ifTransfer"]').change(function(){
	if($(":radio[name='ifTransfer'][value='是']").attr("checked")){
		$("#transfer_info").css('display','block');//显示
	}else{
		$("#transfer_info").css('display','none');//隐藏  
		$("input[name='transferSource']").attr("value","");
		$("textarea[name='transferComment']").attr("value",""); 
	}
	})
	 
	  //论文提交
	jQuery('form[name="stu_form_sub"] button').click(function(){
		    	var need=true;
		    	var tag=$(this).parents('form').children("input[type='hidden']").val();
		    	console.log(tag);
		    	 $('.'+tag).parent().children('input').each(function(){
		            if (!$(this).val()) {
		                need=false;
		            }
		       })
		    	if(need){
		    		var gnl=confirm("确定要保存吗?");
					if (gnl==true){  
						 $.ajax({
		                type: "POST",//方法类型
		                dataType: "json",//预期服务器返回的数据类型
		                url: "/stu/forms" ,//url
		                data: $(this).parents('form').serialize(),
		                success: function (data) {
		                    msg = data.result
		                    type = data.pageType 
		                    if(msg == true && type == 'tec'){
		                    alert("添加成功！");
		                    window.open("/tec/tables","_self")
		                }
		                    else if(msg == true && type == 'stu'){
		                    alert("添加成功！");
		                    window.open("/stu/tables","_self")
		                }
		                    else if(msg== false){
		                    alert("添加失败！");
		                    window.location.reload()
		                    
		                }
		            },
		                error: function() {
		                    alert('添加错误'); 
		                }
		            }); 
					}else{  
						return false;  
					}  
				}else{
					alert('带*号不能为空')
					return false;
				}
		});	
    
		jQuery('form[name="tec_form_sub"] button').click(function(){
			    	var need=true;
			    	var tag=$(this).parents('form').children("input[type='hidden']").val();
			    	console.log(tag);
			    	 $('.'+tag).parent().children('input').each(function(){
			            if (!$(this).val()) {
			                need=false;
			            }
			       })
			    	if(need){
			    		var gnl=confirm("确定要保存吗?");
						if (gnl==true){  
							 $.ajax({
			                type: "POST",//方法类型
			                dataType: "json",//预期服务器返回的数据类型
			                url: "/stu/forms" ,//url
			                data: $(this).parents('form').serialize(),
			                success: function (data) {
			                    msg = data.result
			                    type = data.pageType 
			                    if(msg == true && type == 'tec'){
			                    alert("添加成功！");
			                    window.open("/tec/tables","_self")
			                }
			                    else if(msg == true && type == 'stu'){
			                    alert("添加成功！");
			                    window.open("/stu/tables","_self")
			                }
			                    else if(msg== false){
			                    alert("添加失败！");
			                    window.location.reload()
			                    
			                }
			            },
			                error: function() {
			                    alert('添加错误'); 
			                }
			            }); 
						}else{  
							return false;  
						}  
					}else{
						alert('带*号不能为空')
						return false;
					}
			});    
    
	
 
   
	
});