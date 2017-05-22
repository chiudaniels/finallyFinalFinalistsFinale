//kraitchik variation
// var monthDict= {
    // january:0,
    // february:3,
    // march:3,
    // april:6,
    // may:1,
    // june:4,
    // july:6,
    // august:2,
    // september:5,
    // october:0,
    // november:3,
    // december:5,
// };

var monthArray= ["January","February","March","April","May",
"June","July","August","September","October","November","December"];

var getDay= function(day,month,year){
	d = new Date(year,month,day);
	return d.getDay();
}

var makeCalendar = function(numDays, dayStart){
	
	ele = document.getElementById('days')
	ele.innerHTML="";
	
    // makes empty space for days of last month//
    for (i=0; i< dayStart; i++){
		makeLi= document.createElement("li");
		addDay= document.createTextNode(' ');
		makeLi.appendChild(addDay);
		ele.appendChild(makeLi);
    }
    ///

    // makes actual days //
    for (i=1; i< numDays+1; i++){
		makeLi= document.createElement("li");
		addDay= document.createTextNode(i);
		makeLi.appendChild(addDay);
		ele.appendChild(makeLi);
    }
    ///
}


var getMonthInfo = function (month,year){
	// format: results[numDays, dayofweekstart]
	results=[0,0]
	if (month == 1 && year%4 == 0){
		results[0]=28;
	}
	else if (month == 1 && year%4 != 0){
		results[0]=29;
	}
	else if (month%2==0){
		results[0]=31;
	}
	else{
		results[0]=30
	}
	results[1]=getDay(year,month,1);
	
	return results
	}

var changeMonth= function(month){
	eleMonth= document.getElementById('month');
	eleMonth.innerHTML = monthArray[month-1];
}


var currentMonth=1;
var getMonth= getMonthInfo(currentMonth,2017);

var clickChangeMonthFoward= function(){
	currentMonth++;
	changeMonth(currentMonth);
	getMonth= getMonthInfo(currentMonth,2017);
	makeCalendar(getMonth[0],getMonth[1]);
	console.log(currentMonth);
	
}

var clickChangeMonthPrevious= function(){
	currentMonth--;
	changeMonth(currentMonth);
	getMonth= getMonthInfo(currentMonth,2017);
	makeCalendar(getMonth[0],getMonth[1]);
	console.log(currentMonth);
}


changeMonth(currentMonth);
makeCalendar(getMonth[0],getMonth[1]);



