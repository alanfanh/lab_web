window.onload = function() {
	var email = document.getElementById("email");
	email.onblur = function() {
		//检查邮箱格式
		alert("检查邮件");
		checkEmail();
	}
};

//检查邮箱的函数
function checkEmail() {
	var email = document.getElementById("email").value;
	var semail = document.getElementById("semail");
	var reg = new RegExp("^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$")
	if (email == "") {
		semail.innerHTML = "<font color='red'>邮箱不能为空</font>";
		var flag=0;
	} else if (! reg.test(email)) {
		semail.innerHTML = "<font color='red'>邮箱格式错误</font>";
		var flag=0;
	} else {
		return true;	
	}
	;
	document.getElementById("submit").onclick = function() {
		if (flag == 0) {
			document.getElementById("msgBox").style.display = "block";
			return false;
		}
	}
}