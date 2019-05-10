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
 
 var oldpasswd,repeatPasswd,newPasswd,finish;
 var table_data;

 
jQuery(document).ready(function($) {
								
	 var calendars = document.getElementsByClassName("flatpickr").flatpickr();								
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
	 var paperType_hid=$("#paperType_hid").val()
	 if(paperType_hid){
	 	paperType_hid=paperType_hid.replace("/",""); 
	 	$(":radio[name='paperType'][value='" + paperType_hid + "']").prop("checked", "checked");
	 } 
	 
	 var pubPage_hid=$("#pubPage_hid").val()
	 if(pubPage_hid){
	 	pubPage_hid=pubPage_hid.replace("/","").split("-"); 
	 	$("input[name='pubPage1']").attr('placeholder',pubPage_hid[0]);
	 	$("input[name='pubPage2']").attr('placeholder',pubPage_hid[1]);
	 } 
	 var degType_hid=$("#degType_hid").val()
	 if(degType_hid){
	 	degType_hid=degType_hid.replace("/",""); 
	 	$(":radio[name='degType'][value='" + degType_hid + "']").prop("checked", "checked");
	 } 
	 var SEX_hid=$("#SEX_hid").val()
	 if(SEX_hid){
	 	SEX_hid=SEX_hid.replace("/",""); 
	 	$(":radio[name='SEX'][value='" + SEX_hid + "']").prop("checked", "checked");
	 }  
	 var department_hid=$("#department_hid").val()
	 if(department_hid){
	 	department_hid=department_hid.replace("/",""); 
	 	$(":radio[name='department'][value='" + department_hid + "']").prop("checked", "checked");
	 }     
	 var tecType_hid=$("#tecType_hid").val()
	 if(tecType_hid){
	 	tecType_hid=tecType_hid.replace("/",""); 
	 	$(":radio[name='paperType'][value='" + tecType_hid + "']").prop("checked", "checked");
	 } 
	 var editType_hid=$("#editType_hid").val()
	 if(editType_hid){
	 	editType_hid=editType_hid.replace("/",""); 
	 	$(":radio[name='editType'][value='" + editType_hid + "']").prop("checked", "checked");
	 }
	 var patentType_hid=$("#patentType_hid").val()
	 if(patentType_hid){
	 	patentType_hid=patentType_hid.replace("/",""); 
	 	$(":radio[name='patentType'][value='" + patentType_hid + "']").prop("checked", "checked");
	 }
	 var ifAuthority_hid=$("#ifAuthority_hid").val()
	 if(ifAuthority_hid){
	 	ifAuthority_hid=ifAuthority_hid.replace("/",""); 
	 	if(ifAuthority_hid=='是'){
	 		$(":radio[name='ifAuthority'][value='是']").prop("checked", "checked");
	 		$("#authorize_time").css('display','block');//显示
	 	}
	 }
	 var ifTransfer_hid=$("#ifTransfer_hid").val()
	 if(ifTransfer_hid){
	 	ifTransfer_hid=ifTransfer_hid.replace("/",""); 
	 	if(ifTransfer_hid=='是'){
	 		$(":radio[name='ifTransfer'][value='是']").prop("checked", "checked"); 
	 	 	$("#transfer_info").css('display','block');//显示
	 	 }
	 } 
	 var projectLevel_hid=$("#projectLevel_hid").val()
	 if(projectLevel_hid){
	 	projectLevel_hid=projectLevel_hid.replace("/",""); 
	 	$(":radio[name='projectLevel'][value='" + projectLevel_hid + "']").prop("checked", "checked");
	 } 
	 var standardType_hid=$("#standardType_hid").val()	
	 if(standardType_hid){	
	 standardType_hid=standardType_hid.replace("/","");  
	 $(":radio[name='standardType'][value='" + standardType_hid + "']").prop("checked", "checked");
	  }
  
	
});
