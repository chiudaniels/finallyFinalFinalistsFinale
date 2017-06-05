var month;
var year;

var changeMonth = function(val){
	console.log('change month');
	month = val;
}

var changeYear = function (val){
	console.log('change year');
	year=val;
}

var checkMonth = function(day){
	if (month == 1 && (year%4 != 0 && (day > 28 || day <1))){
		console.log(1);
		document.getElementById('dayError').innerHTML = "Invalid Date";
	}
	else if (month == 1 && (year%4 == 0 && (day > 29 || day <1))){
		console.log(2);
		document.getElementById('dayError').innerHTML = "Invalid Date";
	}
	else if (month%2==0 && (day > 30 || day <1)){
		console.log(3);
		document.getElementById('dayError').innerHTML = "Invalid Date";
	}
	else if (day > 31 || day <1){
		console.log(4);
	    document.getElementById('dayError').innerHTML = "Invalid Date";
	}
	else{
		console.log(5);
		document.getElementById('dayError').innerHTML = "";
	}
	/* console.log(day)
	console.log(month);
	console.log(year%4);
    console.log('hehe'); */
}

