 function submitEvent() {
   var submitButton = document.getElementById("buttonSubmit");
   submitButton.addEventListener("click", uploadEvent, false);
 }

 function uploadEvent(){
   var eventName = document.getElementById("eventNamelabel").value;
   var eventTime = document.getElementById("eventDatetimeLabel").value;
   var eventDesc = document.getElementById("eventDescLabel").value;
   var eventLocation = document.getElementById("eventLocationLabel").value;
   var eventCount = document.getElementById("eventCountLabel").value;
   var eventTag = document.getElementById("eventTagLabel").value;

   var eventInfo = new FormData();
   eventInfo.append('name', eventName);
   eventInfo.append('time', eventTime);
   eventInfo.append('desc', eventDesc);
   eventInfo.append('location', eventLocation);
   eventInfo.append('count', eventCount);
   eventInfo.append('tags', eventTag);


  var request = new XMLHttpRequest();
  //  var url = "";
  request.open('POST', url, true);
  request.onload = function() {
    if(this.readyState==4 && this.status==200){
        console.log(request).responseText)
    }
  };
  request.send(eventInfo);
 }


window.addEventListener("load", submitEvent, false);
