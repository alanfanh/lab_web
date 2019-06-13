window.onload = function() {
	var username = document.getElementById('username');
	username.onblur = function() {
		//检查用户名
		alert("检查用户名");
		checkUsername();
			
	};
	var pwd = document.getElementById('password');
	pwd.onblur = function() {
		//检查密码
		checkPwd();
		
	};
}

//检查用户名的函数
function checkUsername() {
	var username = document.getElementById('username').value;
	var sname = document.getElementById('sname');
	//var classVal = document.getElementById('username').getAttribute("class");
	if (username == ""){
		sname.innerHTML = "<font color='red'>用户名不能为空</font>";
		//classVal = classVal.concat(" is-invalid");
		//document.getElementById('username').setAttribute('class',classVal);
		return false;
	} else if (/^[^a-zA-Z0-9_]+$/.test(username)) {
		sname.innerHTML = "<font color='red'>用户名只能输入数字、字母和下划线</font>";
		return false;
	} else if (String(username).length>32 || String(username).length<5) {
		sname.innerHTML = "<font color='red'>范围：5-32位</font>";
		return false;
	} else {
		sname.innerHTML = "";
		return true;
	}
}

//检查密码的函数
function checkPwd() {
	var pwd = document.getElementById('password').value;
	var spwd = document.getElementById('spwd')
	if (pwd == "") {
		spwd.innerHTML = "<font color='red'>密码不能为空</font>";
		return false;
	} else if (/^[^a-zA-Z0-9_]+$/.test(pwd)) {
		spwd.innerHTML = "<font color='red'>密码只能输入数字、字母和下划线</font>";
		return false;
	} else if (String(pwd).length>32 || String(pwd).length<5) {
		spwd.innerHTML = "<font color='red'>范围：5-32位</font>";
		return false;
	} else {
		spwd.innerHTML = "";
		return true;
	}
}

//检查登录提交的表单
function checkLoginForm() {
	if (checkUsername() && checkPwd()) {
		return true;
	}
	document.getElementById("msgBox").style.display = "block";
	return false;
}	
