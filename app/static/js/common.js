//获取name=box的checkbox框的状态
    function checkboxAll(obj){
        //alert(obj.checked);
        //获取name=box的复选框
        var userids=document.getElementsByName("box");
		
		//alert(userids.length);
        for(var i=0;i<userids.length;i++){
            userids[i].checked=obj.checked;
        }
    }
	
	//checkbox全选/取消全选
    function selectAll(){ 
        //获取name=box的复选框
        var userids=document.getElementsByName("box");
        var count=0;
        //遍历所有的复选框
        for(var i=0;i<userids.length;i++){
            if(userids[i].checked){  
                 count++;
            }
        }
        //选中复选框的个数==获取复选框的个数 
        if(count==userids.length){
			//设置id为all复选框选中
            document.getElementById("all").checked=true;
        }else{
			//设置id为all复选框不选中
            document.getElementById("all").checked=false;
        }   
    }
	
	//全选删除容错判断
	function delAll() {
		var userids=document.getElementsByName("box");
		var all = document.getElementById("all").checked;
		var count=0;
        //遍历所有的复选框
        for(var i=0;i<userids.length;i++){
            if(userids[i].checked){
                 count++;
            }
        };
		alert(count);
		if(count<=0) {
			alert("至少选择一条条目");
			return false;
		};
		return true;
	}
	
	//检查上传文件的类型
	function checkUploadFile() {
		var obj = document.getElementById('file')
		if (obj.value == "") {
			alert("请选择要上传的文件");
			return false;	
		}
		var stuff = obj.value.match(/^(.*)(\.)(.{1,8}$/)[3];
		if (stuff != "xls" || stuff != "xlsx") {
			alert("文件类型不正确");
			return false;
		}
		return true;
	}
	
	//管理员账户修改密码，根据checkbox框的状态判断显示/隐藏元素
	function checkSelectBox(){
		var check = document.getElementById('changepwd');
		var traget = document.getElementsByClassName('form-group');
		if(check.checked){
			for (var i=3;i<traget.length-1;i++) {
				traget[i].style.display="block";
			}
		}else{
			for (var i=3;i<traget.length-2;i++) {
				traget[i].style.display="none";
			}
		}
	}
	