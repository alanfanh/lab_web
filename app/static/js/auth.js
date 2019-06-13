window.onload = function() {
	var name = document.getElementById('name');
	if (name) {
		name.onblur = function() {
			//检查名称
			checkName();
				
		};
	};
	
	var username = document.getElementById('username');
	if (username) {
		username.onblur = function() {
			//检查用户名
			checkUsername();
				
		};
	};
	
	var email = document.getElementById("email");
	if (email) {
		email.onblur = function() {
			//检查邮箱格式
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
	
	var pwd = document.getElementById('password');
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
	
	//修改管理员密码-点击更改密码，显示或隐藏密码设置输入框
	var ischangepwd = document.getElementById('changepwd');
	if (ischangepwd) {
		ischangepwd.onclick = function() {
			var target = document.getElementsByClassName('form-group');
			if (ischangepwd.checked) {
				for (var i=3;i<target.length-1;i++) {
					target[i].style.display="block";
				}
			} else {
				for (var i=3;i<target.length-2;i++) {
					target[i].style.display="none";
				}
			}
		}
	};
	
	var depotname = document.getElementById('depotname');
	if (depotname) {
		depotname.onblur = function() {
			//检查仓库名称
			checkDepot();
		}
	};
	
	
};

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

//检查真实名称的函数
function checkName() {
	var name = document.getElementById('name').value;
	var error = document.getElementById('sname');
	if (name == "") {
		error.innerHTML = "<font color='red'>名称不能为空</font>";
		return false;
	} else if (/^[^0-9A-Aa-z_\u4e00-\u9fa5]+$/.test(name)) {
		error.innerHTML = "<font color='red'>只能输入数字、字母、下划线和中文</font>";
		return false;
	} else if (getLength(name) > 64) {
		error.innerHTML = "<font color='red'>范围：1-64</font>";
		return false;
	} else {
		error.innerHTML = "";
		return true;
	};
}


//检查用户名的函数
function checkUsername() {
	var username = document.getElementById('username').value;
	var error = document.getElementById('susername');
	//var classVal = document.getElementById('username').getAttribute("class");
	if (username == ""){
		error.innerHTML = "<font color='red'>用户名不能为空</font>";
		//classVal = classVal.concat(" is-invalid");
		//document.getElementById('username').setAttribute('class',classVal);
		return false;
	} else if (/^[^a-zA-Z0-9_]+$/.test(username)) {
		error.innerHTML = "<font color='red'>用户名只能输入数字、字母和下划线</font>";
		return false;
	} else if (getLength(String(username))>64 || getLength(String(username))<5) {
		error.innerHTML = "<font color='red'>范围：5-64位</font>";
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
	} else if (getLength(String(pwd))>64 || getLength(String(pwd))<5) {
		error.innerHTML = "<font color='red'>范围：5-64位</font>";
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
		error.innerHTML = "<font color='red'>旧密码不能为空</font>";
		return false;
	} else if (/^[^a-zA-Z0-9_]+$/.test(opwd)) {
		error.innerHTML = "<font color='red'>旧密码只能输入数字、字母和下划线</font>";
		return false;
	} else if (getLength(String(opwd))>64 || getLength(String(opwd))<5) {
		error.innerHTML = "<font color='red'>范围：5-64位</font>";
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
	var error = document.getElementById('spwd2');
	if (pwd != "" && repwd != "" && pwd != repwd) {
		error.innerHTML = "<font color='red'>密码和确认密码不一致</font>";
		return false;
	} else if (repwd == "") {
		error.innerHTML = "<font color='red'>确认密码不能为空</font>";
		return false;
	} else {
		error.innerHTML = "";
		return true;
	}
}

//检查登录提交的表单
function checkLoginForm() {
	if (checkUsername() && checkPwd()) {
		return true;
	}
	//document.getElementById("msgBox").style.display = "block";
	popTip('输入有误,请检查输入框', 'error');
	return false;
}	

	
//检查重置密码提交的表单
function checkReset() {
	if (checkEmail() && checkPwd() && checkRepwd()) {
		return true;
	};
	//document.getElementById("msgBox").style.display = "block";
	popTip('输入有误,请检查输入框', 'error');
	return false;
}

//检查忘记密码-邮箱提交的函数
function checkForget() {
	if (checkEmail()) {
		return true;
	}
	//document.getElementById("msgBox").style.display = "block";
	popTip('输入有误,请检查输入框', 'error');
	return false;
}


//检查修改管理员密码提交的函数
function checkChangePwd() {
	var ischangepwd = document.getElementById('changepwd');
	var flag = 0;
	if (ischangepwd.checked) {
		if (checkEmail() && checkOldPwd() && checkPwd() && checkRepwd()) {
			return true;
		} else { var flag=1;}
	} else {
		if (checkEmail()) {alert("checkemail");return true;} else {var flag=1}
	};
	//document.getElementById("msgBox").style.display = "block";
	if (flag = 1) {
		popTip('输入有误,请检查输入框', 'error');
		return false;
	}
}


//检查普通用户添加/编辑提交的函数
function checkUser() {
	if (checkName() && checkUsername() && checkPwd() && checkRepwd() ) {
		return true;
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





