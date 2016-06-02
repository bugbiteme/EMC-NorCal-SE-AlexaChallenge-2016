//require('dotenv').load();



/****************************************************************************************
	In this section we are requiring the Node package http so we can interact with the MTA 
   	API, the Alexa Skills Kit SDK, and specifying our Alexa skill’s app ID plus our MTA 
   	key. You can grab the app ID from the Skill Information section where you created your 
   	Alexa skill. The MTA_KEY is what you received when signing up with the MTA earlier.
****************************************************************************************/
var http       = require('http')
  , AlexaSkill = require('./AlexaSkill')
  , APP_ID     = 'amzn1.echo-sdk-ams.app.49fa3c1c-be09-4c2d-8bd1-5ac351ce5339'
  , MTA_KEY    = '300bb65b-7c6b-4a1f-aba0-3293cc562824';

/****************************************************************************************
	function that will assemble the endpoint we’ll communicate with to get the bus 
	information from the MTA. It should be pretty self-explanatory:
****************************************************************************************/
var url = function(stopId){
  return 'http://bustime.mta.info/api/siri/stop-monitoring.json?key=' + MTA_KEY + '&OperatorRef=MTA&MaximumStopVisits=1&MonitoringRef=' + stopId;
};

/****************************************************************************************
	grab JSON from the MTA
	This function accepts two arguments: 
		- stopId: stop ID the user has requested
		- callback: to handle the data once we’re finished grabbing it.

	If you’re not familiar with Node’s http library, we’re listening to the incoming data 
	stream. As soon as it’s finished we parse the string into JSON and pass it to our 
	callback. If there’s an error, we log the error–we’ll look at how to view the logs 
	later.
****************************************************************************************/
var getJsonFromMta = function(stopId, callback){
  http.get(url(stopId), function(res){
    var body = '';

    res.on('data', function(data){
      body += data;
    });

    res.on('end', function(){
      var result = JSON.parse(body);
      callback(result);
    });

  }).on('error', function(e){
    console.log('Error: ' + e);
  });
};

/****************************************************************************************
	The next function we create is what will be invoked when the user invokes the 
	GetNextBusIntent, i.e. when they request a bus stop. This function will invoke the 
	getJsonFromMta function we just created and grab just the string we need from the 
	response and send it back to the user.
****************************************************************************************/
var handleNextBusRequest = function(intent, session, response){

  //The first is intent.slots.bus.value. We are reaching a few levels deep into the intent 
  //object and grabbing the bus slot. We know to grab the bus slot because that’s what we 
  //named it in our IntentSchema we created earlier.
  getJsonFromMta(intent.slots.bus.value, function(data){
    if(data.Siri.ServiceDelivery.StopMonitoringDelivery[0].MonitoredStopVisit){
    
      //The next thing we want to do is grab the data that was returned to the callback 
      //and traverse the structure. Unfortunately the MTA structure isn’t the most ideal, 
      //we need to go nine levels deep before we get what we’re looking for: the 
      //PresentableDistance which equates to something like 1.8 miles away, 2 stops away, 
      //or Arriving.
      var text = data
                  .Siri
                  .ServiceDelivery
                  .StopMonitoringDelivery[0]
                  .MonitoredStopVisit[0]
                  .MonitoredVehicleJourney
                  .MonitoredCall
                  .Extensions
                  .Distances
                  .PresentableDistance;
      var cardText = 'The next bus is: ' + text;
    } else {
      var text = 'That bus stop does not exist.'
      var cardText = text;
    }

    var heading = 'Next bus for stop: ' + intent.slots.bus.value;
    
    //Finally, we call the tellWithCard method on the response object. If you’re 
    //interested in finding out more about the response object, check out my guide to the 
    //Alexa Skills Kit JavaScript SDK. But in this situation, just know that tellWithCard 
    //will tell the user the answer (via Alexa) and display a card in the Echo App. The 
    //first argument is what Alexa will say, the second argument is the header for the 
    //card, and the remaining argument is the body of the card.
    response.tellWithCard(text, heading, cardText);
  });
};

/****************************************************************************************
	Now what we’re going to do is extend the AlexaSkill SDK and create our own 
	BusSchedule constructor. Again, if you want to dive deep you can check out the SDK 
	guide, but you’ll be able to follow along without reading it first.
****************************************************************************************/
var BusSchedule = function(){
  AlexaSkill.call(this, APP_ID);
};

BusSchedule.prototype = Object.create(AlexaSkill.prototype);
BusSchedule.prototype.constructor = BusSchedule;


/****************************************************************************************
	Event Handlers:
	We are only required to override onLaunch event handler. You’re unlikely to override 
	onIntent and onSessionStarted and onSessionEnded are available for setup and tear 
	down.

	onLaunch is the event handler that is called when a user has launched the skill but 
	hasn’t specified which intent they want. For example, Alexa ask bus schedule versus 
	Alexa ask bus schedule for the next bus at stop 304442.
****************************************************************************************/
BusSchedule.prototype.eventHandlers.onLaunch = function(launchRequest, session, response){
  var output = 'Welcome to EMC Install Base. ' +
    'Ask me something about your EMC customer install base and I shall do my best to get you an answer.';

  var reprompt = 'So what do you want me to query about your install base?';

  response.ask(output, reprompt);
};



/****************************************************************************************
	Intent Handlers:
	The SDK defines an intent handlers object, but leaves it up to you to define the 
	handlers themselves. These correspond to the intents that we specified in our intent 
	schema that we created earlier. In our case, GetNextBusIntent and HelpIntent
****************************************************************************************/
BusSchedule.prototype.intentHandlers = {
  GetNextBusIntent: function(intent, session, response){
    handleNextBusRequest(intent, session, response);
  },

  HelpIntent: function(intent, session, response){
    var speechOutput = 'Get information about your EMC customer install base. ' +
      'What would you like to know?';
    response.ask(speechOutput);
  }
};



/****************************************************************************************
	Finally, we tie all the code together and export our handler
****************************************************************************************/
exports.handler = function(event, context) {
    var skill = new BusSchedule();
    skill.execute(event, context);
};