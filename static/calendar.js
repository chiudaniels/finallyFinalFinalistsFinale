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
    d = new Date(year,month-1,day);
    console.log(d.getDate());
    console.log(d.getMonth());
    console.log(d.getFullYear());
    console.log(d.getDay());
    return d.getDay();
}

var makeCalendar = function(numDays, dayStart){
	
	ele = document.getElementById('days')
	ele.innerHTML="";
	
    // makes empty space for days of last month//
    for (i=0; i< dayStart-1; i++){
		makeLi= document.createElement("li");
		addDay= document.createTextNode('b');
		makeLi.className = "empty";
		makeLi.appendChild(addDay);
		ele.appendChild(makeLi);
    }
    ///
	
    // makes actual days //
	
	for(i = 1; i < numDays +1; i++){
			makeLi= document.createElement("li");
			addDay= document.createTextNode(i);
			makeLi.className = "selected";
			
			var presDate = {'day' : i, 'month' : monthArray[currentMonth-1], 'year' : currentYear}
			
			$.ajax({
				url: "/eventExists/",
				type: "GET",
				data: presDate,
				async: false,
				success: function(d) {
					d = JSON.parse(d);
					if (d != null){
						makeLi.style.backgroundColor = "yellow";
						makeLi.popover({
							html: true,
							title: "BOOOOOOK",
							content: "ASDASDASDASDA"
						});
					}
				
				}		
			});
			
			makeLi.appendChild(addDay);
			ele.appendChild(makeLi);
	}
    ///

}


//month stuff//

var getMonthInfo = function (month,year){
	// format: results[numDays, dayofweekstart]
	results=[0,0]
	if (month == 2 && year%4 != 0){
		results[0]=28;
	}
	else if (month == 2 && year%4 == 0){
		results[0]=29;
	}
	else if (month%2==0){
		results[0]=30;
	}
	else{
	    results[0]=31;
	}
    
	results[1]=getDay(1,month,year);
	
	return results
	}

var changeMonth= function(month){
	eleMonth= document.getElementById('month');
	eleMonth.innerHTML = monthArray[month-1];
}


var currentMonth=1;
var getMonth= getMonthInfo(currentMonth,2017);
///

// year stuff//
var currentYear=2017;

var checkYear=function (){
    if (currentMonth == 13){
	currentYear++;
	currentMonth=1;
    }
    if (currentMonth == 0){
	currentYear--;
	currentMonth=12; 
    }
}

var changeYear=function(){
    eleYear=document.getElementById('year');
    eleYear.innerHTML = currentYear;
}

///

//add event stuff//
var getDays = document.getElementById('days');
var dayLi= getDays.getElementsByTagName("li");
var addEvent = function(day,event){
    dayLi[day-1].innerHTML= day + "<br>"+ event;
}
//


//change month stuff//
var clickChangeMonthFoward= function(){
    currentMonth++;
    checkYear();
    changeYear();
    changeMonth(currentMonth);
    getMonth= getMonthInfo(currentMonth,currentYear);
    makeCalendar(getMonth[0],getMonth[1]);
    //console.log(currentMonth);
    
}

var clickChangeMonthPrevious= function(){
    currentMonth--;
    checkYear();
    changeYear();
    changeMonth(currentMonth);
    getMonth= getMonthInfo(currentMonth,currentYear);
    makeCalendar(getMonth[0],getMonth[1]);
   // console.log(currentMonth);
}
//

getDay(2017,4,26);
changeYear();
changeMonth(currentMonth);
makeCalendar(getMonth[0],getMonth[1]);



