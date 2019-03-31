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
   var cBoxes = document.getElementsByName("Tags");
   var cChecked = [];
   for (var i = 0;i<cBoxes.length;i++){
     if (cBoxes[i].checked){
       cChecked.push($(cBoxes[i]).attr("value"));
     }
   }
   var eventTags = cChecked.join(", ");

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
  "tags": "Food",
  "owner": "Andy Shin"
  },

  {
  "name": "Disco Roll",
  "time": "9pm",
  "description": "all night long~~~~",
  "location": "Dank-eee ballroom",
  "count1": "200",
  "count2": "42",
  "tags": "Sports",
  "owner": "Keenan Hall"
  }

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
     var cardBG = eventTag.split(", ")[0];



     var cardHTML = `
     <div class = "card shadow-sm">
      <div class = "cardEvent FILLER_BG text-left">
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
        <div style="position: absolute; top:147px; left:20px; width:200px; height:25px">
          <span class = "cardAction" style="font-size: 2em; color: white;">
            <i class="far fa-map"></i>
          </span>
        </div>
        <DIV style="position: absolute; top:160px; left:60px; width:200px; height:25px">
          FILLER_LOC
        </DIV>

        <button type="button" class="btn btn-light cardButton" style="position: absolute; top:153px; left:362px; width:90px; height:35px">Join In</button>
        <button type="button" class="btn btn-light cardButton" style="position: absolute; top:153px; left:260px; width:90px; height:35px">View</button>
      </div>
      <div class = "cardStat">
        <div class = "openspots">
          <div class = "spots">Open spots:</div>
          <div class = "spotnum">FILLER_CURR</div>
        </div>
        <hr class = "spotsbreak">
        <div class = "totspots">
          <div cl ass = "spots">Total spots:</div>
          <div class = "spotnum">FILLER_TOT</div>
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

    if(cardBG == "Academics"){
      cardHTML = cardHTML.replace('FILLER_BG', "cc-acad");
    }else if(cardBG == "Food"){
      cardHTML = cardHTML.replace('FILLER_BG', "cc-food");
    }else if(cardBG == "Faith"){
      cardHTML = cardHTML.replace('FILLER_BG', "cc-faith");
    }else if(cardBG == "Sports"){
      cardHTML = cardHTML.replace('FILLER_BG', "cc-sports");
    }else if(cardBG == "Travel"){
      cardHTML = cardHTML.replace('FILLER_BG', "cc-travel");
    }else{
      cardHTML = cardHTML.replace('FILLER_BG', "cc-other");
    }

    div.innerHTML += cardHTML;

    var inputHTML = `
    {
    "name": "FILLER_DATE",
    "time": "FILLER_TIME",
    "description": "FILLER_DESC",
    "location": "FILLER_LOC",
    "count1": "FILLER_CURR",
    "count2": "FILLER_TOT",
    "owner": "NOBODY FOR NOW"
    }
    `

    inputHTML = inputHTML.replace('FILLER_DATE', eventTime);
    inputHTML = inputHTML.replace('FILLER_NAME', eventName);
    inputHTML = inputHTML.replace('FILLER_DESC', eventDesc);
    inputHTML = inputHTML.replace('FILLER_LOC', eventLocation);
    inputHTML = inputHTML.replace('FILLER_CURR', eventCurrentCount);
    inputHTML = inputHTML.replace('FILLER_TOT', eventTotalCount);
    
    /// write to file
    var txtFile = "fake.json";
    var file = new File(txtFile);
    var str = inputHTML;

    file.open("w"); // open file with write access
    file.write(str);
    file.close();

  }

  

}

window.addEventListener("load", submitEvent, false);
// var json = JSON.parse("fake.json");
console.log(json);
window.addEventListener("load", pushCards(json), false);
