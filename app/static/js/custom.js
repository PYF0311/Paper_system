// /login.html
$(function () {
	jQuery('#loginbtn').click(function(){
		post_data = $('#loginform').serialize();
		var uname=jQuery('#username').val();
		var passwd=jQuery('#password').val();
		if(uname && passwd){
			jQuery('.nousername').hide();
		 if(finish){
	    $.ajax({
	         url: "/login",
	         data: post_data,
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
	});
// /su/admin_login.html	
$(function() {
    jQuery('#su_loginbtn').click(function() {
        post_data = $('#su_login').serialize();
        var runame = jQuery('#runame').val();
        var rpasswd = jQuery('#rpasswd').val();
        var msg;
        if (runame && rpasswd) {
            jQuery('.nousername').hide();
            if (finish) {
                jQuery('.nousername').hide();
                $.ajax({
                    url: "/su/admin_login",
                    data: post_data,
                    dataType: "json",
                    type: "POST",
                    success: function(data) {
                        msg = data.result;
                        if (msg == 1) {
                            window.open("/su/academic_manage", "_self");
                        } else if (msg == -2) {
                            jQuery('.nopassword').fadeIn();
                        }
                    },
                    error: function() {
                        jQuery('.nopassword').fadeIn();
                        console.log("请求失败！");
                    }
                });
            } else {
                jQuery('.nocode').fadeIn();
                return false;
            }
        } else {
            jQuery('.nousername').fadeIn();
            return false;
        }
    });
});
// /stu/editpassword
$(function () {
    $("#editpassword button").click(function(){
	  post_data = $('#editpassword').serialize();
      if(oldpasswd && repeatPasswd && newPasswd){
       $.ajax({
         url:"/stu/pass_edit",
         data:post_data,  
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
});
// /tec/editpassword
$(function () {
 $("#editpassword_tec button").click(function(){
	  post_data = $('#editpassword_tec').serialize();
      if(oldpasswd && repeatPasswd && newPasswd){
       $.ajax({
         url:"/tec/pass_edit",
         data:post_data, 
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
}); 
//  /tec/editprofile
$(function () {
	    $("#editprofile_tec button").click(function(){
			post_data = $('#editprofile_tec').serialize();
	       $.ajax({
	         url:"",
	         type:"POST",
	         dataType: "json",
	         data:post_data,  
	         success:function(data){
		         alert(data.msg);
				 location.reload();
	       },
	       error:function(){
	         alert("修改失败！");
	       }
	       }); 
	});
});
// /stu/editprofile 
$(function () {
	    $("#editprofile_stu button").click(function(){
			post_data = $('#editprofile_stu').serialize();
	       $.ajax({
	         url:"",
	         type:"POST",
	         data:post_data, 
	         success:function(data){
		         alert(data.msg);
		         location.reload();
	       },
	       error:function(){
	         console.log("请求出错！");
	       }
	       });
	       
	});
});
// /form.html
$(function () {
	jQuery('form[name="form_sub"] button').click(function(){
		        post_data = $(this).parents('form').serialize();
		    	var need=true;
		    	var tag=$(this).parents('form').children("input[type='hidden']").val();
		    	console.log(tag);
		    	 $('.'+tag).parent().children('input').each(function(){
		            if (!$(this).val()) {
		                need=false;
		            }
		       });
		    	if(need){
		    		var gnl=confirm("确定要保存吗?");
					if (gnl==true){  
						 $.ajax({
		                type: "POST", 
		                dataType: "json", 
		                url: "/stu/forms" ,//url
		                data: post_data,
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
//form_edit 
$(function () {
	jQuery('form[name="form_edit"] button').click(function(){ 
		        post_data = $(this).parents('form').serialize();
		    	var tag=$(this).parents('form').children("input[type='hidden']").val(); 
		    	var gnl=confirm("确定要保存吗?");
					if (gnl==true){  
						$.ajax({
		                type: "POST", 
		                dataType: "json", 
		                url: "" , 
		                data: post_data,
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
});

$(function () {
	jQuery('.deletebutton').click(function(){
	post_data=table_data.getData();
	if(post_data.length){
		var con= confirm('确定删除吗?');
		if(con){
		 $.ajax({
	   			   url: "/stu/del", //删除处理链接
				   data:{post_data: post_data},
				      dataType: "json",
				      type:"POST",
				      success: function(data){
				          alert("删除成功！");
	                      location.reload();
				      	},
				      error:function(){
	                      alert("删除失败！");
				     
				      },
	                  complete:function(data){
	                  }
			 }); 
		}
	}else alert('请选择数据');								//alert to 请选择数据
	});
// /stu/table.html 	
	jQuery('.detailbutton_stu').click(function(){
		post_data=table_data.getData();
		if(post_data.length==1){
			 $.ajax({
		   			   url: "/stu/info", 
					   data:{post_data: post_data},
					      dataType: "json",
					      type:"POST",
					      success: function(data){
	                        msg = data.type
					      	if(msg== '期刊论文'){
	                                window.open("/stu/aca_info","_self")
	                            }
	                            else if (msg== '学位论文'){
	                                window.open("/stu/deg_info","_self")
	                            }
	                            else if(msg =='专利'){
	                              window.open("/stu/pat_info","_self")
	                            }
	                            else if(msg =='参加项目'){
	                             
	                              window.open("/stu/pro_info","_self")
	                            }
	                            else if(msg =='专著'){
	                             
	                              window.open("/stu/mono_info","_self")
	                            }
	                            else if(msg =='标准'){
	                             
	                              window.open("/stu/stand_info","_self")
	                            }
	
	
	                         },
					      error:function(){
					     
					      }
				})
		}else alert('请选择一条数据');	
		});
 
	jQuery('.editbutton_stu').click(function(){
		post_data=table_data.getData();
		if(post_data.length==1){
	     $.ajax({
	               url: "/stu/info", 
	               data:{post_data: post_data},
	                  dataType: "json",
	                  type:"POST",
	                  success: function(data){
	                    msg = data.type
	                    if(msg== '期刊论文'){
	                            window.open("/stu/aca_edit","_self")
	                        }
	                        else if (msg== '学位论文'){
	                            window.open("/stu/deg_edit","_self")
	                        }
	                        else if(msg =='专利'){
	                          window.open("/stu/pat_edit","_self")
	                        }
	                        else if(msg =='参加项目'){
	                          window.open("/stu/pro_edit","_self")
	                        }
	                        else if(msg =='专著'){
	                          window.open("/stu/mono_edit","_self")
	                        }
	                        else if(msg =='标准'){
	                          window.open("/stu/stand_edit","_self")
	                        }
	                     },
	                  error:function(){
							window.open("/404","_self")
	                  }
	        })
	}else alert('请选择一条数据');   
	});
});
// /tec/table.html 
$(function () {
	jQuery('.editbutton_tec').click(function(){
		post_data=table_data.getData();
		if(post_data.length==1){
	     $.ajax({
	               url: "/stu/info", 
	               data:{post_data: post_data},
	                  dataType: "json",
	                  type:"POST",
	                  success: function(data){
	                    msg = data.type
	                    if(msg== '期刊论文'){
	                            window.open("/tec/aca_edit","_self")
	                        }
	                        else if (msg== '学位论文'){
	                            window.open("/tec/deg_edit","_self")
	                        }
	                        else if(msg =='专利'){
	                          window.open("/tec/pat_edit","_self")
	                        }
	                        else if(msg =='参加项目'){
	                          window.open("/tec/pro_edit","_self")
	                        }
	                        else if(msg =='专著'){
	                          window.open("/tec/mono_edit","_self")
	                        }
	                        else if(msg =='标准'){
	                          window.open("/tec/stand_edit","_self")
	                        }
	                     },
	                  error:function(){
							window.open("/404","_self")
	                  }
	        })
	}else alert('请选择一条数据');   
	});
 
	jQuery('.detailbutton_tec').click(function(){
		post_data=table_data.getData();
		if(post_data.length==1){
			 $.ajax({
		   			   url: "/stu/info", 
					   data:{
					   	post_data: post_data
					   },
					      dataType: "json",
					      type:"POST",
					      success: function(data){
	                        msg = data.type
					      	if(msg== '期刊论文'){
	                                window.open("/tec/aca_info","_self")
	                            }
	                            else if (msg== '学位论文'){
	                                window.open("/tec/deg_info","_self")
	                            }
	                            else if(msg =='专利'){
	                              window.open("/tec/pat_info","_self")
	                            }
	                            else if(msg =='参加项目'){
	                              window.open("/tec/pro_info","_self")
	                            }
	                            else if(msg =='专著'){
	                              window.open("/tec/mono_info","_self")
	                            }
	                            else if(msg =='标准'){
	                              window.open("/tec/stand_info","_self")
	                            }
	                         },
					      error:function(){
							window.open("/404","_self");
					      }
				})
		}else alert('请选择一条数据');	
		}); 
});
// /su/academic.html
$(function () {
	jQuery('.deletebutton_su').click(function(){
	post_data=table_data.getData();
	if(post_data.length){
		var con= confirm('确定删除吗?');
		if(con){
		 $.ajax({
	   			   url: "/su/del", //删除处理链接
				   data:{post_data: post_data},
	                  dataType: "json",
	                  type:"POST",
	                  success: function(data){
	                      alert("删除成功！");
	                      location.reload();
	                    },
	                  error:function(){
	                      alert("删除失败！");
	                 
	                  },
	                  complete:function(data){
	                  }
			 }); 
		}
	}else alert('请选择数据');								//alert to 请选择数据
	});
	jQuery('.detailbutton_su').click(function(){
	post_data=table_data.getData();
	if(post_data.length==1){
	     $.ajax({
	               url: "/stu/info", 
	               data:{
	               	post_data: post_data
	               },
	                  dataType: "json",
	                  type:"POST",
	                  success: function(data){
	                    msg = data.type  
	                    if(msg== '期刊论文'){
	                            window.open("/tec/aca_info","_self"); 
	                        }
	                        else if (msg== '学位论文'){ 
	                            window.open("/tec/deg_info","_self"); 
	                        }
	                        else if(msg =='专利'){
	                          window.open("/tec/pat_info","_self");
	                        }
	                        else if(msg =='参加项目'){ 
	                          window.open("/tec/pro_info","_self");
	                        }
	                        else if(msg =='专著'){ 
	                          window.open("/tec/mono_info","_self");
	                        }
	                        else if(msg =='标准'){ 
	                          window.open("/tec/stand_info","_self");
	                        }
	                   },
	                  error:function(){
	                    window.open("/404","_self");
	                  }
	        })
	}else alert('请选择一条数据');   
	});
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
				        alert("下载失败");
				      }
			 }); 
	}
		else alert('请选择数据');								//alert to 请选择数据
	});
 
	jQuery('.exportbutton_txt').click(function(){
		var pattern=jQuery('.pattern').val();
		var txt_url;
		if(pattern== 'academic'){ txt_url="/txtdownload01";}
		else if (pattern== 'degree'){txt_url="/txtdownload02";}
		else if(pattern =='patent'){txt_url="/txtdownload03";}
		else if(pattern =='project'){txt_url="/txtdownload04";}
		else if(pattern =='mono'){txt_url="/txtdownload05";}
		else if(pattern =='stand'){txt_url="/txtdownload06";}
		post_data=table_data.getData();
		if(post_data.length){ 
		 $.ajax({
	   			   url: txt_url,
				   data:{post_data: post_data},
				      dataType: "text",
				      type:"POST",
				      success: function(){
				      	window.open("/txtdownload");
				      	},
				      error:function(){
				        alert("下载失败");
				      }
			 }); 
	}
		else alert('请选择数据');								//alert to 请选择数据
	});
	//academic
	$("#aca_btnImport").click(function () { 
	              var formData = new FormData($("#aca_uploadForm")[0]); 
	              $.ajax({
	                  type: "POST",
	                  data:formData, 
	                  url: "/up_file",
	                  contentType: false,
	                  processData: false,
	                  success:function (returndata) {
						alert(returndata) 
	　　				  }, 
	　　				  error: function (returndata) { 
	　　　　　			alert("上传失败！")
	                  }
	　　					}) 
	          });
    //degree
    $("#deg_btnImport").click(function () { 
                  var formData = new FormData($("#deg_uploadForm")[0]); 
                  $.ajax({
                      type: "POST",
                      data:formData, 
                      url: "/up_file",
                      contentType: false,
                      processData: false,
                      success:function (returndata) {
    					alert(returndata) 
    　　				  }, 
    　　				  error: function (returndata) { 
    　　　　　			alert("上传失败！")
                      }
    　　					}) 
    });
	//monograph
	$("#mono_btnImport").click(function () { 
	              var formData = new FormData($("#mono_uploadForm")[0]); 
	              $.ajax({
	                  type: "POST",
	                  data:formData, 
	                  url: "/up_file",
	                  contentType: false,
	                  processData: false,
	                  success:function (returndata) {
						alert(returndata) 
	　　				  }, 
	　　				  error: function (returndata) { 
	　　　　　			alert("上传失败！")
	                  }
	　　					}) 
	});
	//patent
	$("#pat_btnImport").click(function () { 
	              var formData = new FormData($("#pat_uploadForm")[0]); 
	              $.ajax({
	                  type: "POST",
	                  data:formData, 
	                  url: "/up_file",
	                  contentType: false,
	                  processData: false,
	                  success:function (returndata) {
						alert(returndata) 
	　　				  }, 
	　　				  error: function (returndata) { 
	　　　　　			alert("上传失败！")
	                  }
	　　					}) 
	});
	//project
	$("#pro_btnImport").click(function () { 
	              var formData = new FormData($("#pro_uploadForm")[0]); 
	              $.ajax({
	                  type: "POST",
	                  data:formData, 
	                  url: "/up_file",
	                  contentType: false,
	                  processData: false,
	                  success:function (returndata) {
						alert(returndata) 
	　　				  }, 
	　　				  error: function (returndata) { 
	　　　　　			alert("上传失败！")
	                  }
	　　					}) 
	});
	//stand
	$("#sta_btnImport").click(function () { 
	              var formData = new FormData($("#sta_uploadForm")[0]); 
	              $.ajax({
	                  type: "POST",
	                  data:formData, 
	                  url: "/up_file",
	                  contentType: false,
	                  processData: false,
	                  success:function (returndata) {
						alert(returndata) 
	　　				  }, 
	　　				  error: function (returndata) { 
	　　　　　			alert("上传失败！")
	                  }
	　　			 }) 
	});
	 
});
// /su/students.html  
$(function () {
	jQuery('.stu_deletebutton').click(function(){
	post_data=table_data.getData();
	if(post_data.length){
		var con= confirm('确定删除吗?');
		if(con){
		 $.ajax({
	   			   url: "/su/stu_del", //删除处理链接
				   data:{post_data: post_data},
				      dataType: "json",
				      type:"POST",
				      success: function(){
	                      alert("删除成功！");
	                      location.reload();
				      	},
				      error:function(){
	                      alert("删除失败！请稍后再试！");
				      }
			 }); 
		}
	}else alert('请选择数据');								//alert to 请选择数据
	});
	
	jQuery('.stu_editbutton').click(function(){
		post_data=table_data.getData();
		console.log(post_data)
		if(post_data.length==1){
		 $.ajax({
	   			   url: "/su/stu_edit", //进入学生编辑链接
				  data:{post_data: post_data},
				      dataType: "json",
				      type:"POST",
				      success: function(){
				        window.open("/su/stu_edit","_self");
				      	},
				      error:function(){
						window.open("/404","_self");
				      }
			})
		}else alert('请选择一条数据');	
	});
	//student批量导入
	$("#stu_btnImport").click(function () { 
	              var formData = new FormData($("#stu_uploadForm")[0]); 
	              $.ajax({
	                  type: "POST",
	                  data:formData, 
	                  url: "/up_file",
	                  contentType: false,
	                  processData: false,
	                  success:function (returndata) {
						alert(returndata) 
	　　				  }, 
	　　				  error: function (returndata) { 
	　　　　　			alert("上传失败！")
	                  }
	　　			 }) 
	});
});
// /su/stu_edit.html
$(function () {
	jQuery('#stu_edit_form button').click(function(){
			post_data=$("#stu_edit_form").serialize();
			if(table_data.getData().length==1){
		     $.ajax({
		               url: "", //提交已修改好的信息
		               data:post_data,
		                  dataType: "json",
		                  type:"POST",
		                  success: function(data){
		                    alert("修改成功！");
		                    location.reload();
		                    },
		                  error:function(){
								window.open("/404","_self")
		                  }
		        })
		}else alert('请选择一条数据');   
		});
});
// /su/stu_add.html
$(function () {
	    $("#stu_add_form button").click(function(){ 
			post_data = $("#stu_add_form").serialize();
	       $.ajax({
	         url:"",//点击添加学生处理链接
	         data:post_data, 
	         dataType: "json",
	         type:"POST",
	         success:function(data){
		         alert(data.msg)
		         window.location.reload()
	      	 },
	       error:function(){
			 window.open("/404","_self");
	       }
	       }); 
	});
});
// /su/tec_add.html
$(function () {
	 $("#tec_add_form button").click(function(){
		 post_data = $("#tec_add_form").serialize();
	       $.ajax({
	         url:"",  //教师添加链接
	         data:post_data, 
	         dataType: "json",
	         type:"POST",
	         success:function(data){
		        alert(data.msg);
		        location.reload();
	       },
	       error:function(){ 
			 window.open("/404","_self");
	       }
	       }); 
	});
});
// /su/tec_edit.html
$(function () {
	jQuery('#tec_edit_form button').click(function(){
			post_data = $("#tec_edit_form").serialize();
			
			if(table_data.getData().length==1){
		     $.ajax({
		               url: " ", //提交已修改的信息
		               data:post_data,
		               dataType: "json",
		               type:"POST",
		               success: function(data){
		                    alert("修改成功！");
						location.reload();
		                     },
		                  error:function(){
								window.open("/404","_self")
		                  }
		        })
		}else alert('请选择一条数据');   
		});
});
// /su/teachers.html
$(function () {
	jQuery('.tec_editbutton').click(function(){
		post_data=table_data.getData();
		console.log(post_data);
		if(post_data.length==1){
			 $.ajax({
		   			   url: "/su/tec_edit", //进入教师编辑链接
					   data:{post_data: post_data},
					      dataType: "json",
					      type:"POST",
					      success: function(data){ 
	                        window.open("/su/tec_edit","_self") 
	                      },
					      error:function(){
							window.open("/404","_self");
					      }
				})
		}else alert('请选择一条数据');	
		}); 
jQuery('.tec_deletebutton').click(function(){
		post_data=table_data.getData();
		console.log(post_data)
		if(post_data.length){
			var con= confirm('确定删除吗?');
			if(con){
			 $.ajax({
		   			   url: "/su/tec_del", //删除处理链接
					    data:{post_data: post_data},
					      dataType: "json",
					      type:"POST",
					      success: function(data){
					          alert(data.msg);
					          location.reload();
					        },
					      error:function(){
					          alert("删除失败！请稍后再试！"); 
					      },
					      complete:function(data){
					      }
				 }); 
			}
		}else alert('请选择数据');							 
		});
//teacher批量导入
	$("#tec_btnImport").click(function () { 
	              var formData = new FormData($("#tec_uploadForm")[0]); 
	              $.ajax({
	                  type: "POST",
	                  data:formData, 
	                  url: "/up_file",
	                  contentType: false,
	                  processData: false,
	                  success:function (returndata) {
						alert(returndata) 
	　　				  }, 
	　　				  error: function (returndata) { 
	　　　　　			alert("上传失败！")
	                  }
	　　			 }) 
	});
});
// /su/editpassword
$(function () {
	    //表单提交前校验
	    $("#su_editpasswd button").click(function(){
			post_data = $("#su_editpasswd").serialize();
	      if(oldpasswd && repeatPasswd && newPasswd){
	       $.ajax({
	         url:"",//管理员修改密码
	         data:post_data, 
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
 