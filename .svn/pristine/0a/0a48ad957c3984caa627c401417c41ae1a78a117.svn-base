window.onload = function() {
	var email = document.getElementById("email");
	email.onblur = function() {
		//检查邮箱格式
		alert("检查邮件");
		checkEmail();
	};
	var pwd = document.getElementById('password');
	pwd.onblur = function() {
		//检查密码
		checkPwd();
		
	};
	var repwd = document.getElementById('password2');
	repwd.onblur = function() {
		//检查确认密码
		checkRepwd();
	};
};

//检查邮箱的函数
function checkEmail() {
	var email = document.getElementById("email").value;
	var semail = document.getElementById("semail");
	var reg = new RegExp("^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$")
	if (email == "") {
		semail.innerHTML = "<font color='red'>邮箱不能为空</font>";
		return false;
	} else if (! reg.test(email)) {
		semail.innerHTML = "<font color='red'>邮箱格式错误</font>";
		return false;
	} else {
		semail.innerHTML = "";
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

//检查确认密码的函数
function checkRepwd() {
	var pwd = document.getElementById('password').value;
	var repwd = document.getElementById('password2').value;
	var srepwd = document.getElementById('spwd2');
	if (pwd != "" && repwd != "" && pwd != repwd) {
		srepwd.innerHTML = "<font color='red'>密码和确认密码不一致</font>";
		return false;
	} else {
		srepwd.innerHTML = "";
		return true;
	}
}
	
//检查重置密码表单
function checkReset() {
	if (checkEmail() && checkPwd() && checkRepwd()) {
		return true;
	};
	document.getElementById("msgBox").style.display = "block";
	return false;
}