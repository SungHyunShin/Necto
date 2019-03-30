// import data from './fake.json';

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
        console.log(request).responseText;
    }
  };

  request.send(eventInfo);
  refresh();

}

function refresh(){

}

var json = [
  {
  "name": "Ice Cream Social at Duncan",
  "time": "12pm",
  "description": "Fun fun fun!",
  "location": "Duncan Student Center",
  "count1": "25",
  "count2": "10",
  "tags": "social",
  "owner": "Andy Shin"
  },

]

function pushCards(json){
  var div = document.getElementById('cardstackID');

  for(var i = 0; i < json.length; i++) {
     var obj = json[i];
     var eventName = obj.name;
     var eventTime = obj.time;
     var eventDesc = obj.description;
     var eventLocation = obj.location;
     var eventCurrentCount = obj.count2;
     var eventTotalCount = obj.count1;
     var eventOwner = obj.owner;
     var eventTag = obj.tags;

    var cardHTML = `
    <div class = "card shadow-sm">
      <div class = "cardEvent bg-primary text-left">
        <div class= "cardDate h4 small">
          FILLER_DATE
        </div>
        <div class = "h3">
          FILLER_NAME
        </div>
        <div class = "cardDescrp"><small>
          FILLER_DESC
        </small>
      </div><br>
        <span class = "cardAction" style="font-size: 2em; color: white;">
          <i class="far fa-map"></i>
        </span>
        <DIV style="position: absolute; top:160px; left:60px; width:200px; height:25px">
          FILLER_LOC
        </DIV>

        <button type="button" class="btn btn-light cardButton" style="float:right;">Join In</button>
        <button type="button" class="btn btn-light cardButton" style="float:right;">View</button>
      </div>
      <div class = "cardStat">
        <div class = "info h1">
          FILLER_CURR <br> FILLER_TOT
        </div>
      </div>
    </div>
    `
    cardHTML = cardHTML.replace('FILLER_DATE', eventTime);
    cardHTML = cardHTML.replace('FILLER_NAME', eventName);
    cardHTML = cardHTML.replace('FILLER_DESC', eventDesc);
    cardHTML = cardHTML.replace('FILLER_LOC', eventLocation);
    cardHTML = cardHTML.replace('FILLER_CURR', eventCurrentCount);
    cardHTML = cardHTML.replace('FILLER_TOT', eventTotalCount);

    div.innerHTML += cardHTML;

  }

}

window.addEventListener("load", submitEvent, false);
// var json = JSON.parse("fake.json");
console.log(json);
window.addEventListener("load", pushCards(json), false);
