
//加载当前时间
setInterval(function () {
var date = new Date();	//获得当前时间
var yy = date.getFullYear();	//年份
var mm = date.getMonth() + 1;	//获得月份
mm = (mm < 10 ? "0" + mm : mm);	//月份小于10时，前面加个0(例如9 ->09)天，小时，分钟，秒同理
var dd = (date.getDate() < 10 ? "0" + date.getDate() : date.getDate());	//天
var hours = (date.getHours() < 10 ? "0" + date.getHours() : date.getHours());	//小时
var minutes = (date.getMinutes() < 10 ? "0" + date.getMinutes() : date.getMinutes());	//分钟
var seconds = (date.getSeconds() < 10 ? "0" + date.getSeconds() : date.getSeconds());	//秒
document.getElementById("timer").innerHTML = yy + '年' + mm + "月" + dd + "日 " + hours + ':' + minutes + ':' + seconds;
}, 1000);
