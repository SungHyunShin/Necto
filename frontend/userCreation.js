function submitAccount() {
   var submitButton = document.getElementById("buttonSubmit");
   submitButton.addEventListener("click", uploadEvent, false);
 }

function uploadAccount(){
   
   var userName = document.getElementById("userName").value;
   var userPassword = document.getElementById("userPassword").value;
   var userEmail = document.getElementById("userEmail").value;
   
   var userInfo = new FormData();
   userInfo.append('userName', userName);
   userInfo.append('userPassword', userPassword);
   userInfo.append('userEmail', userEmail);

  var request = new XMLHttpRequest();
  request.open('POST', url, true);
  request.onload = function() {
    if(this.readyState==4 && this.status==200){
        console.log(request).responseText)
    }
  };

window.addEventListener("load", submitAccount, false);
