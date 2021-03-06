window.onload = function() {
	var booknumber = document.getElementById('booknumber');
	if (booknumber) {
		booknumber.onblur = function () {
			//检查图书编号
			checkBooknum();	
		};
	};
	var bookname = document.getElementById('bookname');
	if (bookname) {
		bookname.onblur = function() {
			//检查图书名称
			checkBookname();
			
		};
	};
	var numbers = document.getElementById('numbers');
	if (numbers) {
		numbers.onblur =  function() {
			//检查数量
			checkNumber();
			
		};
	};
	var prices = document.getElementById('prices');
	if (prices) {
		prices.onblur = function() {
			//检查价格
			checkPrices();
			
		};
	};
	var position = document.getElementById('position');
	if (position) {
		position.onblur = function() {
			//检查存储位置
			checkPosition();
			
		};
	};
	var username = document.getElementById('username');
	if (username) {
		username.onblur = function() {
			//检查借机人名称
			checkUsername();
			
		};
	};
	
	var usermail = document.getElementById('usermail');
	if (usermail) {
		usermail.onblur = function() {
			//检查借用人邮箱
			checkUseremail();
		};
	};
	
	var lendtime = document.getElementById('lendtime');
	if (lendtime) {
		lendtime.onblur = function() {
			//检查借用时间
			checkLendtime();
		};
	};
	
	var backtime = document.getElementById('backtime');
	if (backtime) {
		backtime.onblur = function() {
			//检查预计归还时间
			checkBacktime();
		};
	};
	switchCon(document.getElementById('status').value);
	
}

function testselect(e){
	switchCon(e.value);
}


//错误弹窗
function popTip(mess, type){
	// type: warning, error, success
	type = type || 'success';
	spop({
		template: mess,	
		position  : 'top-center',
		autoclose: 3000
	});
}

//添加数据，状态为在库时隐藏借机信息，借出时显示借机信息
function switchCon(value){
	var $switchCon = document.getElementById('switchCon');
	
	if(value == '1'){
		$switchCon.style.display = 'none';
	}else{
		$switchCon.style.display = 'block';
	}
}

//检查图书编号
function checkBooknum() {
	var obj = document.getElementById('booknumber').value;
	var error = document.getElementById('sbooknumber');
	//var classVal = document.getElementById('username').getAttribute("class");
	if (obj == ""){
		error.innerHTML = "<font color='red'>此项不能为空</font>";
		//classVal = classVal.concat(" is-invalid");
		//document.getElementById('username').setAttribute('class',classVal);
		return false;
	} else if (/^[^a-zA-Z0-9_]+$/.test(obj)) {
		error.innerHTML = "<font color='red'>只能输入数字、字母和下划线</font>";
		return false;
	} else if (getLength(obj)>255) {
		error.innerHTML = "<font color='red'>范围：5-32位</font>";
		return false;
	} else {
		error.innerHTML = "";
		return true;
	}
}

//检查书名
function checkBookname() {
	var obj = document.getElementById('bookname').value;
	var error = document.getElementById('sbookname');
	if (obj == ""){
		error.innerHTML = "<font color='red'>此项不能为空</font>";
		//classVal = classVal.concat(" is-invalid");
		//document.getElementById('username').setAttribute('class',classVal);
		return false;
	} else if (/^[^0-9a-zA-Z_\u4e00-\u9fa5]+$/.test(obj)) {
		error.innerHTML = "<font color='red'>只能输入中文、数字、字母和下划线</font>";
		return false;
	} else if (getLength(obj)>255) {
		error.innerHTML = "<font color='red'>范围：1-255位</font>";
		return false;
	} else {
		error.innerHTML = "";
		return true;
	}
}

//检查数量
function checkNumber() {
	var obj = document.getElementById('numbers').value;
	var error = document.getElementById('snumbers');
	if (obj == ""){
		error.innerHTML = "<font color='red'>此项不能为空</font>";
		return false;
	} else if (Number(obj) <= 0 || Number(obj) > 65535) {
		error.innerHTML = "<font color='red'>范围：1-65535</font>";
		return false;
	} else if (/^\D+$/.test(Number(obj))) {
		error.innerHTML = "<font color='red'>只能输入数字</font>";
		return false;
	} else if (/^\d+\.\d+$/.test(Number(obj))) {
		error.innerHTML = "<font color='red'>只能输入整数</font>";
		return false;	
	} else {
		error.innerHTML = "";
		return true;
	}
}

//检查价格
function checkPrices() {
	var obj = document.getElementById('prices').value;
	var error = document.getElementById('sprices');
	if (obj == ""){
		error.innerHTML = "<font color='red'>此项不能为空</font>";
		return false;
	} else if (Number(obj) <= 0 || Number(obj) > 65535) {
		error.innerHTML = "<font color='red'>范围：1-65535</font>";
		return false;
	} else if (!(/^\d+(\.\d+)?$/.test(Number(obj)))) {
		error.innerHTML = "<font color='red'>只能输入数字</font>";
		return false;
	} else {
		error.innerHTML = "";
		return true;
	}
}

//检查存储位置
function checkPosition() {
	var obj = document.getElementById('position').value;
	var error = document.getElementById('sposition');
	if (obj == "") {
		error.innerHTML = "<font color='red'>此项不能为空</font>";
		//classVal = classVal.concat(" is-invalid");
		//document.getElementById('username').setAttribute('class',classVal);
		return false;
	} else if (/^[^0-9a-zA-Z_\u4e00-\u9fa5]+$/.test(obj)) {
		error.innerHTML = "<font color='red'>只能输入中文、数字、字母和下划线</font>";
		return false;
	} else if (getLength(obj)>255) {
		error.innerHTML = "<font color='red'>范围：1-255位</font>";
		return false;
	} else {
		error.innerHTML = "";
		return true;
	}
}

//检查借机人名称
function checkUsername() {
	var obj = document.getElementById('username').value;
	var error = document.getElementById('susername');
	if (obj == ""){
		error.innerHTML = "<font color='red'>此项不能为空</font>";
		//classVal = classVal.concat(" is-invalid");
		//document.getElementById('username').setAttribute('class',classVal);
		return false;
	} else if (/^[^0-9a-zA-Z_\u4e00-\u9fa5]+$/.test(obj)) {
		error.innerHTML = "<font color='red'>只能输入中文、数字、字母和下划线</font>";
		return false;
	} else if (getLength(obj)>255) {
		error.innerHTML = "<font color='red'>范围：1-255位</font>";
		return false;
	} else {
		error.innerHTML = "";
		console.log('testtttt')
		return true;
	}
}


//检查借机人邮箱
function checkUseremail() {
	var email = document.getElementById("usermail").value;
	var error = document.getElementById("susermail");
	var reg = new RegExp("^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$")
	if (email == "") {
		error.innerHTML = "<font color='red'>此项不能为空</font>";
		return false;
	} else if (! reg.test(email)) {
		error.innerHTML = "<font color='red'>邮箱格式错误</font>";
		return false;
	} else {
		error.innerHTML = "";
		return true;	
	}
}


//检查借机时间
function checkLendtime(){
	var date = document.getElementById("lendtime").value;
	var error = document.getElementById("slendtime");
	//var result = date.match(/^(\d{4})(-|\/)(\d{1,2})\2(\d{1,2})$/)
	var result = date.match(/^(\d{4})(-|\/)(\d+)\2(\d+)$/)
	if (date == "") {
		error.innerHTML = "<font color='red'>此项不能为空</font>";
		return false;
	} else if (!(/^(.+)(-|\/)(.+)\2(.+)$/.test(date))) {
		error.innerHTML = "<font color='red'>请输入正确的日期格式年/月/日或年-月-日</font>";
		return false;
	} else if (date.match(/^(\d{4})(-|\/)(\d+)\2(\d+)$/)) {
		var d = new Date(result[1], result[3] - 1, result[4]);
		if (!(d.getFullYear() == result[1] && (d.getMonth() + 1) == result[3] && d.getDate() == result[4])) {
			error.innerHTML = "<font color='red'>请输入正确的日期</font>";
			return false;
		} else {
			error.innerHTML = "";
			return true;
		}
	} else if (!(/^(\d{4})(-|\/)(\d{1,2})\2(\d{1,2})$/.test(date))) {
		error.innerHTML = "<font color='red'>请输入正确的日期</font>";
	    return false;
	} else if (!(/^(\D*)(-|\/)(\D*)\2(\D*)$/.test(date))) {
		error.innerHTML = "<font color='red'>请输入正确的日期</font>";
	    return false;
	} else {
		error.innerHTML = "";
		return true;	
	}
}

//检查还机时间
function checkBacktime() {
	var date = document.getElementById("backtime").value;
	var error = document.getElementById("sbacktime");
	var result = date.match(/^(\d{4})(-|\/)(\d+)\2(\d+)$/)
	if (date == "") {
		error.innerHTML = "<font color='red'>此项不能为空</font>";
		return false;
	} else if (!(/^(.+)(-|\/)(.+)\2(.+)$/.test(date))) {
		error.innerHTML = "<font color='red'>请输入正确的日期格式年/月/日或年-月-日</font>";
		return false;
	} else if (date.match(/^(\d{4})(-|\/)(\d+)\2(\d+)$/)) {
		var d = new Date(result[1], result[3] - 1, result[4]);
		if (!(d.getFullYear() == result[1] && (d.getMonth() + 1) == result[3] && d.getDate() == result[4])) {
			error.innerHTML = "<font color='red'>请输入正确的日期</font>";
			return false;
		} else {
			error.innerHTML = "";
			return true;
		}
	} else if (!(/^(\d{4})(-|\/)(\d{1,2})\2(\d{1,2})$/.test(date))) {
		error.innerHTML = "<font color='red'>请输入正确的日期</font>";
	    return false;
	} else if (!(/^(\D*)(-|\/)(\D*)\2(\D*)$/.test(date))) {
		error.innerHTML = "<font color='red'>请输入正确的日期</font>";
	    return false;
	} else {
		error.innerHTML = "";
		return true;	
	}
}

//检查还机时间是否大于借机时间
function checkTime() {
	var lenddate = document.getElementById("lendtime").value;
	var backdate = document.getElementById("backtime").value;
	var dateDiff = new Date(backdate).getTime() - new Date(lenddate).getTime();
	 var dayDiff = Math.floor(dateDiff / (24 * 3600 * 1000));
	if (dayDiff < 0) {
		return false;
	};
	return true;
}

//检查图书管理提交表单
function  checkBook() {
	var status = document.getElementById("status").value;
	if (status == 1) {
		if (checkBooknum() && checkBookname() && checkNumber() && checkPrices() && checkPosition() )  {
			return true;
		};
	} else {
		if (checkBooknum() && checkBookname() && checkNumber() && checkPrices() && checkPosition() && checkUsername() &&  checkLendtime() && checkBacktime() && checkTime() )  {
			return true;
		};
	};
	if (! checkTime()) {
		//document.getElementById("msgBox").innerHTML = "归还时间必须大于等于借用时间";
		//document.getElementById("msgBox").style.display = "block";
		popTip('归还时间必须大于等于借用时间', 'error');
		return false;
	};
	//document.getElementById("msgBox").style.display = "block";
	popTip('输入有误,请检查输入框', 'error');
    return false;
}

//检查字符长度
function getLength(str) {
	var len = 0;
	var str = String(str);
	for (var i=0;i<str.length;i++) {
		var c = str.charCodeAt(i);
		//单字节加1
		if ((c >= 0x0001 && c <= 0x007e) || (0xff60 <= c && c <= 0xff9f))  {
			len++;
		} else {
			len += 2;
		}	
	}
	return len;
}
