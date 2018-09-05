jQuery(document).ready(function(){
	var finish=false;
	
	    $.fn.drag = function(options){
        var x, drag = this, isMove = false, defaults = {
        };
        var options = $.extend(defaults, options);
        //添加背景，文字，滑块
        var html = '<div class="drag_bg"></div>'+
                    '<div class="drag_text" onselectstart="return false;" unselectable="on">拖动滑块验证</div>'+
                    '<div class="handler handler_bg"></div>';
        this.append(html);
        
        var handler = drag.find('.handler');
        var drag_bg = drag.find('.drag_bg');
        var text = drag.find('.drag_text');
        var maxWidth = drag.width() - handler.width();  //能滑动的最大间距
        
        //鼠标按下时候的x轴的位置
        handler.mousedown(function(e){
            isMove = true;
            x = e.pageX - parseInt(handler.css('left'), 10);
        });
        
        //鼠标指针在上下文移动时，移动距离大于0小于最大间距，滑块x轴位置等于鼠标移动距离
        $(document).mousemove(function(e){
            var _x = e.pageX - x;
            if(isMove){
                if(_x > 0 && _x <= maxWidth){
                    handler.css({'left': _x});
                    drag_bg.css({'width': _x});
                }else if(_x > maxWidth){  //鼠标指针移动距离达到最大时清空事件
                    dragOk();
                }
            }
        }).mouseup(function(e){
            isMove = false;
            var _x = e.pageX - x;
            if(_x < maxWidth){ //鼠标松开时，如果没有达到最大距离位置，滑块就返回初始位置
                handler.css({'left': 0});
                drag_bg.css({'width': 0});
            }
        });
        
        //清空事件
        function dragOk(){
        	finish=true;
            handler.removeClass('handler_bg').addClass('handler_ok_bg');
            text.text('验证通过');
            drag.css({'color': '#fff'});
            handler.unbind('mousedown');
            $(document).unbind('mousemove');
            $(document).unbind('mouseup');
        }
    };
								
	///// TRANSFORM CHECKBOX /////							
	jQuery('input:checkbox').uniform();
	jQuery('#drag').drag();
	///// LOGIN FORM SUBMIT /////
	jQuery('#loginbutton').click(function(){
		var uname=jQuery('#username').val();
		var passwd=jQuery('#password').val();
		var type=jQuery("input[name='type']:checked").val();
		var msg;
		if(uname && passwd){
			jQuery('.nousername').hide();
			if(finish){
				console.log("验证码正确");
        $.ajax({
             url: "",
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
      if(finish){
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
	});
  jQuery('#username').attr('placeholder','请输入用户名');
  jQuery('#password').attr('placeholder','请输入密码');

	
});
