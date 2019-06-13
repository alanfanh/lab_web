window.onload = function() {
	var username = document.getElementById('username');
	if (username) {
		username.onblur = function() {
			//检查用户名
			alert("检查用户名");
			checkUsername();
				
		};
	};
	
	var email = document.getElementById("email");
	if (email) {
		email.onblur = function() {
			//检查邮箱格式
			alert("检查邮件");
			checkEmail();
		};
	}
	
	var oldpwd = document.getElementById('oldpassword');
	if (oldpwd) {
		oldpwd.onblur = function () {
			//检查旧密码格式
			checkOldPwd();
		};
	};
	
	var  pwd = document.getElementById('password');
	if (pwd) {
		pwd.onblur = function() {
			//检查密码
			checkPwd();
		};
	};
	
	var repwd = document.getElementById('password2');
	if (repwd) {
		repwd.onblur = function() {
			//检查确认密码
			checkRepwd();
		};
	};
	
	var ischangepwd = document.getElementById('changepwd');
	if (ischangepwd) {
		ischangepwd.onclick = function() {
			var traget = document.getElementsByClassName('form-group');
		
		
		
		};
	};
};

//检查用户名的函数
function checkUsername() {
	var username = document.getElementById('username').value;
	var error = document.getElementById('sname');
	//var classVal = document.getElementById('username').getAttribute("class");
	if (username == ""){
		error.innerHTML = "<font color='red'>用户名不能为空</font>";
		//classVal = classVal.concat(" is-invalid");
		//document.getElementById('username').setAttribute('class',classVal);
		return false;
	} else if (/^[^a-zA-Z0-9_]+$/.test(username)) {
		error.innerHTML = "<font color='red'>用户名只能输入数字、字母和下划线</font>";
		return false;
	} else if (String(username).length>32 || String(username).length<5) {
		error.innerHTML = "<font color='red'>范围：5-32位</font>";
		return false;
	} else {
		error.innerHTML = "";
		return true;
	}
}


//检查密码的函数
function checkPwd() {
	var pwd = document.getElementById('password').value;
	var error = document.getElementById('spwd');
	if (pwd == "") {
		error.innerHTML = "<font color='red'>密码不能为空</font>";
		return false;
	} else if (/^[^a-zA-Z0-9_]+$/.test(pwd)) {
		error.innerHTML = "<font color='red'>密码只能输入数字、字母和下划线</font>";
		return false;
	} else if (String(pwd).length>32 || String(pwd).length<5) {
		error.innerHTML = "<font color='red'>范围：5-32位</font>";
		return false;
	} else {
		error.innerHTML = "";
		return true;
	}
}


//检查邮箱的函数
function checkEmail() {
	var email = document.getElementById("email").value;
	var error = document.getElementById("semail");
	var reg = new RegExp("^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$")
	if (email == "") {
		error.innerHTML = "<font color='red'>邮箱不能为空</font>";
		return false;
	} else if (! reg.test(email)) {
		error.innerHTML = "<font color='red'>邮箱格式错误</font>";
		return false;
	} else {
		error.innerHTML = "";
		return true;	
	}
}

//检查旧密码的函数
function checkOldPwd() {
	var opwd = document.getElementById('oldpassword').value;
	var error = document.getElementById('soldpassword')
	if (opwd == "") {
		error.innerHTML = "<font color='red'>密码不能为空</font>";
		return false;
	} else if (/^[^a-zA-Z0-9_]+$/.test(opwd)) {
		error.innerHTML = "<font color='red'>密码只能输入数字、字母和下划线</font>";
		return false;
	} else if (String(opwd).length>32 || String(opwd).length<5) {
		error.innerHTML = "<font color='red'>范围：5-32位</font>";
		return false;
	} else {
		error.innerHTML = "";
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

//检查登录提交的表单
function checkLoginForm() {
	if (checkUsername() && checkPwd()) {
		return true;
	}
	document.getElementById("msgBox").style.display = "block";
	return false;
}	

	
//检查重置密码提交的表单
function checkReset() {
	if (checkEmail() && checkPwd() && checkRepwd()) {
		return true;
	};
	document.getElementById("msgBox").style.display = "block";
	return false;
}

//检查忘记密码-邮箱提交的函数
function checkForget() {
	if (checkEmail()) {
		return true;
	}
	document.getElementById("msgBox").style.display = "block";
	return false;
}

//检查修改管理员密码提交的函数

