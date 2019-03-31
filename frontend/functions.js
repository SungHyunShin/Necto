/*var json = {"events":[
  {"description":"a",
  "eventID":1,
  "location":"library",
  "members":[],
  "name":"a",
  "ownerName":"admin",
  "population":[2,4],
  "tags":["Food"],
  "message":"OK",
  "response":200
}]
};*/

function pushCards(eventObject){
  var div = document.getElementById('cardstackID');
  var eventName = eventObject.name;
  //var eventTime = eventObject.time;
  var eventTime = 'TIME';
  var eventDesc = eventObject.description;
  var eventLocation = eventObject.location;
  //var eventPopulation = eventObject.population;
  var eventPopulation = [2,4];
  console.log(typeof eventPopulation);
  var eventCurrentCount = eventPopulation[0];
  var eventTotalCount = eventPopulation[1];
  var eventOwner = eventObject.ownerName;
  var eventTag = eventObject.tags;
  var cardBG = eventTag[0];
  var cardHTML = `
     <div class = "card shadow-sm">
      <div class = "cardEvent FILLER_BG text-left">
        <div class= "cardDate h4 small">`
        +eventTime+
        `</div>
        <div class = "h3">`
        +eventName+
        `</div>
        <div class = "cardDescrp"><small>`
        +eventDesc+
        `</small>
      </div><br>
        <div style="position: absolute; top:147px; left:20px; width:200px; height:25px">
          <span class = "cardAction" style="font-size: 2em; color: white;">
            <i class="far fa-map"></i>
          </span>
        </div>
        <DIV style="position: absolute; top:160px; left:60px; width:200px; height:25px">`
        +eventLocation+
        `</DIV>

        <button type="button" class="btn btn-light cardButton" style="position: absolute; top:153px; left:362px; width:90px; height:35px">Join In</button>
        <button type="button" class="btn btn-light cardButton" style="position: absolute; top:153px; left:260px; width:90px; height:35px">View</button>
      </div>
      <div class = "cardStat">
        <div class = "openspots">
          <div class = "spots">Open spots:</div>
          <div class = "spotnum">`+eventCurrentCount+`</div>
        </div>
        <hr class = "spotsbreak">
        <div class = "totspots">
          <div cl ass = "spots">Total spots:</div>
          <div class = "spotnum">`+eventTotalCount+`</div>
        </div>
      </div>
    </div>
  `;
  

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
}
var xhr = new XMLHttpRequest();
//xhr.open('GET', "https://necto-flask.herokuapp.com/events", true);
xhr.open('GET', "http://127.0.0.1:5000/events", true);
xhr.send();
var events = {}
function processRequest(e) {
  if (xhr.readyState == 4 && xhr.status == 200) {
      var response = JSON.parse(xhr.responseText);
      console.log(response);
      events = response.events;
      var arrayLength = events.length;
      console.log(arrayLength)
      for (var i = 0; i < arrayLength; i++) {
        console.log(events)
        pushCards(events[i]);
      }
  }
} 
xhr.onreadystatechange = processRequest;
