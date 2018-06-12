/*
 * 	Additional function for widgets.html
 *	Written by ThemePixels	
 *	http://themepixels.com/
 *
 *	Copyright (c) 2012 ThemePixels (http://themepixels.com)
 *	
 *	Built for Amanda Premium Responsive Admin Template
 *  http://themeforest.net/category/site-templates/admin-templates
 */

jQuery(document).ready(function(){
	
		//论文提交
		jQuery('form button').click(function(){
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
                url: "" ,//url
                data: $(this).parents('form').serialize(),
                success: function (data) {
                    msg = data.result
                    if(msg== true){
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

		//论文分类显示
	$('.pageheader .hornav li').click(function(){
		var show=jQuery(this).attr('title');
		jQuery('.contentwrapper .subcontent').css('display','none');
		$('.pageheader .hornav li').removeClass('current');
		$(this).addClass('current');
		$('#'+show).css('display','block');
		
	});
});
