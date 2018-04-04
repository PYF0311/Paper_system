<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>发布文章页面</title>
<link href="http://code.jquery.com/jquery-1.7.js" rel="stylesheet">

<link rel="stylesheet" type="text/css" href=" {{ url_for('static',filename='css/style.default.css')}}" >
<script type="text/javascript" src=" {{ url_for('static',filename='js/plugins/jquery-1.7.min.js')}}"></script>
<script src="//code.jquery.com/ui/1.10.4/jquery-ui.js"></script>
<script type="text/javascript" src=" {{ url_for('static',filename='js/plugins/jquery.uniform.min.js')}}"></script>
<script type="text/javascript" src=" {{ url_for('static',filename='js/plugins/jquery.cookie.js')}}"></script>
<script type="text/javascript" src=" {{ url_for('static',filename='js/custom/general.js')}}"></script>
<script type="text/javascript" src=" {{ url_for('static',filename='js/plugins/newpost.js')}}"></script>


</head>

<body class="withvernav">
<div class="bodywrapper">
    <div class="topheader">
        <div class="left">
            <h1 class="logo">集美<span>大学</span></h1>
            <span class="slogan">科研成果统计软件</span>
            
            
            <br clear="all" />
            
        </div><!--left-->
        
        <div class="right">
            <div class="userinfo">
            	<span style="color: #FB9337;">欢迎!</span>
                <span style="color: #FB9337;">姓名</span>
            </div><!--userinfo-->
            
            <div class="userinfodrop">
            	
				<div class="userdata">
                    <h4>Juan</h4>
                    <span class="email">youremail@yourdomain.com</span>
                    <ul>
                    	<li><a href="editprofile.html">编辑资料</a></li>
                        <li><a href="dashboard.html">退出</a></li>
                    </ul>
                </div><!--userdata-->
            </div><!--userinfodrop-->
        </div><!--right-->
    </div><!--topheader-->
    
    
    <div class="header">
    	<ul class="headermenu">
    		<li><a href="/dashboard"><span class="icon icon-flatscreen"></span>首页</a></li>
        	<li><a href="/forms"><span class="icon icon-pencil"></span>论文录入</a></li>
            <li class="current"><a href="/newpost"><span class="icon icon-message"></span>论文导出</a></li>
            <li><a href="/tables"><span class="icon icon-chart"></span>论文列表</a></li>
        </ul>
    </div><!--header-->
    
    
    <div class="centercontent">
    
        <div class="pageheader">
			<ul class="hornav">
               
                <li class="current" id="show_academic"><a href="#academic_paper"><span>学术论文</span></a></li>
                
                <li id="show_conference"><a href="#conference_paper"><span>会议论文及学术交流</span></a></li>
              
                <li id="show_patent"><a href="#patent"><span>专利</span></a></li>
                
                <li id="show_project"><a href="#project"><span>参加项目</span></a></li>
                
            </ul>
        </div><!--pageheader-->
        
        
        <div id="contentwrapper" class="contentwrapper">
        	<div id="academic_paper" class="subcontent" >
		        <p>
		        	<br  />
		            <span id="academic_select" class="dualselect">
		                <select class="uniformselect" name="academic_choose" multiple="multiple" size="10">
		                    <option value="acadPaperNameCH">论文名称（中文名称）</option>
		                    <option value="acadPaperNameEN">论文名称（英文名称）</option>
		                    <option value="1stEdit">第一作者</option>
		                    <option value="2ndEdit">第二作者</option>
		                    <option value="3rdEdit">第三作者</option>
		                    <option value="4rdEdit">第四作者</option>
		                    <option value="transEdit">通讯作者</option>
		                    <option value="issueName">刊物名称</option>
		                    <option value="pubTime">发表时间</option>
		                    <option value="pubIssue">发表期</option>
		                    <option value="pubPeriod">发表卷</option>
		                    <option value="pubPage">发表页码</option>
		                    <option value="depa">第一通讯单位</option>
		                    <option value="paperType">收录类型</option>
		                    <option value="indexNum">检索号</option>
		                    <option value="part">分区</option>
		                    <option value="impactFactor">影响因子</option>
		                    <option value="5rdEdit">第五作者</option>
		                    <option value="6rdEdit">第六作者</option>
		                    <option value="7rdEdit">第七作者</option>
		                    <option value="8rdEdit">第八作者</option>
		                </select>
			            <span class="ds_arrow">
			                <span class="arrow ds_prev">&laquo;</span>
			                <span class="arrow ds_next">&raquo;</span>
			            </span>
			            <select multiple="multiple" size="10" form="academic_form" id="academic_choosed">
			               
			            </select>

			        </span>   
			    </p>  
			<form id="academic_form">
				<input type="hidden" name="hidden" id="academic_hidden">
			    <span class="two_third" style="text-align: center;">
				    <input type="submit" name="save" />
			    </span><!--two_third-->
		    </form>
	                    
	                    <br /><br />
	                    
	            <!-- Gets replaced with TinyMCE, remember HTML in a textarea should be encoded -->
		    <form name="academic_view"action="" method="post">            
	                    <div class="dualselect">
	                        <textarea id="elm1" name="elm1" rows="15" cols="80" style="width: 85%" class="tinymce">
	                           
	                        </textarea>
	                        <br />
	                    </div>
	                    <span class="two_third" style="text-align: center;">
				            <input type="submit" name="save" value="导出" />
				        </span>
	        </form>   
         </div> <!--subcontent-->
        	<div id="conference_paper" class="subcontent" style="display: none">
		        <p>
		        	<br  />
		            <span id="conference_select" class="dualselect">
		                <select class="uniformselect" name="conference_chooose" multiple="multiple" size="10">
		                    <option value="confPaperNameCH">论文名称（中文名称）</option>
		                    <option value="confPaperNameEN">论文名称（英文名称）</option>
		                    <option value="1stEdit">第一作者</option>
		                    <option value="2ndEdit">第二作者</option>
		                    <option value="3rdEdit">第三作者</option>
		                    <option value="4rdEdit">第四作者</option>
		                    <option value="transEdit">通讯作者</option>
		                    <option value="confName">会议名称</option>
		                    <option value="confTime">会议时间</option>
		                    <option value="confAddress">会议地址</option>
		                    <option value="confHost">会议主办单位</option>
		                    <option value="paperType">论文形式</option>
		                    <option value="confType">参会形式</option>
		                    <option value="pubTime">论文发表时间</option>
		                    <option value="pubIssue">发表期</option>
		                    <option value="pubPeriod">发表卷</option>
		                    <option value="pubPage">发表页码</option>
		                    <option value="depa">第一通讯单位</option>
		                    <option value="issueType">收录类型</option>
		                    <option value="indexNum">检索号</option>
		                    <option value="subarea">分区</option>
		                    <option value="impactFactor">影响因子</option>
		                    <option value="5rdEdit">第五作者</option>
		                    <option value="6rdEdit">第六作者</option>
		                    <option value="7rdEdit">第七作者</option>
		                    <option value="8rdEdit">第八作者</option>
		                </select>
			            <span class="ds_arrow">
			                <span class="arrow ds_prev">&laquo;</span>
			                <span class="arrow ds_next">&raquo;</span>
			            </span>
			            <select name="" multiple="multiple" size="10"id="conference_chooosed" form="conference_form">
			            </select>
			        </span>   
			    </p>
			    <form name="conference_form" action="" method="post" id="conference_form" >
			    	<input type="hidden" id="conference_hidden"> 
			    	<input type="hidden" name="tag" value="conference_paper">

				    <span class="two_third" style="text-align: center;">
					    <input type="submit" name="save"  />
				    </span><!--two_third-->
		        </form>
	                    
	                    <br /><br />
	                    
	            <!-- Gets replaced with TinyMCE, remember HTML in a textarea should be encoded -->
		        <form name="conference_view" action="" method="post">            
	                    <div class="dualselect">
	                        <textarea id="elm1" name="elm1" rows="15" cols="80" style="width: 85%" class="tinymce">
	                           
	                        </textarea>
	                        <br />
	                    </div>
	                    <span class="two_third" style="text-align: center;">
				            <input type="submit" name="save" value="导出" />
				        </span><!--two_third-->
	            </form>   

            </div>
        	<div id="patent" class="subcontent" style="display: none">
		        <p>
		        	<br  />
		            <span id="dualselect" class="dualselect">
		                <select class="uniformselect" name="select3" multiple="multiple" size="10">
		                    <option value="patentNameCH">专利名称（中文名称）</option>
		                    <option value="patentNameEN">专利名称（英文名称）</option>
		                    <option value="patentType">专利类型</option>
		                    <option value="1stEdit">第一发明人</option>
		                    <option value="2ndEdit">第二发明人</option>
		                    <option value="3rdEdit">第三发明人</option>
		                    <option value="4rdEdit">第四发明人</option>
		                    <option value="patentApplyTime">专利申请时间</option>
		                    <option value="patentAuthorityTime">专利授权时间</option>
		                    <option value="patentId">专利号</option>
		                    <option value="transferSource">转让单位</option>
		                    <option value="transferComment">转让应用情况</option>
		                    <option value="5rdEdit">第五作者</option>
		                    <option value="6rdEdit">第六作者</option>
		                    <option value="7rdEdit">第七作者</option>
		                    <option value="8rdEdit">第八作者</option>
		                </select>
			            <span class="ds_arrow">
			                <span class="arrow ds_prev">&laquo;</span>
			                <span class="arrow ds_next">&raquo;</span>
			            </span>
			            <select name="" multiple="multiple" size="10" id="patent_choosed">
			            </select>
			        </span>   
			    </p>    
			    <form id="patent_form" action="" method="post">
			    	<input type="hidden" id="patent_hidden">
			    	<input type="hidden" name="tag" value="patent">
				    <span class="two_third" style="text-align: center;">
					    <input type="submit"  />
				    </span><!--two_third-->
		        </form>
	                    
	                    <br /><br />
	                    
	            <!-- Gets replaced with TinyMCE, remember HTML in a textarea should be encoded -->
		        <form name="patent_view" action="" method="post">            
	                    <div class="dualselect">
	                        <textarea id="elm1" name="elm1" rows="15" cols="80" style="width: 85%" class="tinymce">
	                           
	                        </textarea>
	                        <br />
	                    </div>
	                    <span class="two_third" style="text-align: center;">
				            <input type="submit" name="save" value="导出" />
				        </span><!--two_third-->
	            </form>    
            </div><!--subcontent-->
            <div id="project" class="subcontent" style="display: none">
		        <p>
		        	<br  />
		            <span id="dualselect" class="dualselect">
		                <select class="uniformselect"  multiple="multiple" size="10">
		                    <option value="projectName">项目名称</option>
		                    <option value="projectSourceType">项目来源</option>
		                    <option value="projectId">项目编号</option>
		                    <option value="projectHost">项目主持人</option>
		                    <option value="1stEdit">第一发明人</option>
		                    <option value="2ndEdit">第二发明人</option>
		                    <option value="3rdEdit">第三发明人</option>
		                    <option value="4rdEdit">第四发明人</option>
		                    <option value="projectFond">项目经费</option>
		                    <option value="projectBeginTime">项目开始时间</option>
		                    <option value="projectFinTime">项目停止时间</option>
		                    <option value="projectTask">承担任务</option>
		                    <option value="5rdEdit">第五作者</option>
		                    <option value="6rdEdit">第六作者</option>
		                    <option value="7rdEdit">第七作者</option>
		                    <option value="8rdEdit">第八作者</option>
		                </select>
			            <span class="ds_arrow">
			                <span class="arrow ds_prev">&laquo;</span>
			                <span class="arrow ds_next">&raquo;</span>
			            </span>
			            <select id="project_choosed" multiple="multiple" size="10" >
			            </select>
			        </span>   
			    </p>   
			    <form id="project_form" action="" method="post">
			    	<input type="hidden" id="project_hidden" >
			    	<input type="hidden" name="tag" value="project ">
				    <span class="two_third" style="text-align: center;">
					    <input type="submit" name="save"  />
				    </span><!--two_third-->
		        </form>
	                    
	                    <br /><br />
	                    
	            <!-- Gets replaced with TinyMCE, remember HTML in a textarea should be encoded -->
		        <form name="project_view" action="" method="post">      

	                    <div class="dualselect">
	                        <textarea id="elm1" name="elm1" rows="15" cols="80" style="width: 85%" class="tinymce">
	                           
	                        </textarea>
	                        <br />
	                    </div>
	                    <span class="two_third" style="text-align: center;">
				            <input type="submit" name="save" value="导出" />
				        </span><!--two_third-->
	            </form>      
            </div>
        </div><!--centercontent-->
    
    
</div><!--bodywrapper-->

</body>

</html>
