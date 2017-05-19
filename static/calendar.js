//kraitchik variation
var monthDict= {
    january=0,
    february=3,
    march=3,
    april=6,
    may=1,
    june=4,
    july=6,
    august=2,
    september=5,
    october=0,
    november=3,
    december=5,
};

var getDay= function(day,month,year,century){
    
}

var makeCalendar = function(numDays, dayStart){
    // makes empty space for days of last month//
    for (i=0, i< dayStart, i++){
	makeLi= document.createElement("li");
	addDay= document.createTextNode(' ');
	makeLi.appendChild(addDay);
	ele.appendChild(makeLi);
    }
    ///
    ele = document.getElementByID('days')

    // makes actual days //
    for (i=1, i< numDays+1, i++){
	makeLi= document.createElement("li");
	addDay= document.createTextNode(i);
	makeLi.appendChild(addDay);
	ele.appendChild(makeLi);
    }
    ///
}



