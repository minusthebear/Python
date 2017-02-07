(function(){
	function loadJSON(callback) {   

	    var xobj = new XMLHttpRequest();
	        xobj.overrideMimeType("application/json");
	    xobj.open('GET', 'data.json', true); // Replace 'my_data' with the path to your file
	    xobj.onreadystatechange = function () {
	          if (xobj.readyState == 4 && xobj.status == "200") {
	            // Required use of an anonymous callback as .open will NOT return a value but simply returns undefined in asynchronous mode
	            callback(xobj.responseText);
	          }
	    };
	    xobj.send(null);  
	 }

	function init(){
		loadJSON(function(response){
			var actual_JSON = JSON.parse(response);
			console.log(actual_JSON);
			var app = document.getElementById("appendHere");
			for (var a in actual_JSON){
				console.log(actual_JSON[a]);
				var t = document.createTextNode(actual_JSON[a]);
				app.appendChild(t);
				var line = document.createElement("HR");
				app.appendChild(line);
			}
		});
	}

	window.onload = init();
})();