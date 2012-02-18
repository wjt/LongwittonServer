
var div =  $('<div id="destination"/>');
$('body').prepend(div);

function sendUrl()
{
	// do send
}

function readUrl()
{
	$.get('http://jonathanwhiting.com/test.txt',function(result){
    showUrl(result);
  });
}

function showUrl(data)
{
	alert("callback");
	// do read
	
	// display text in diff
	div.text(data);
	// repeat after time	
	var t=setTimeout("readUrl()",3000);
}

sendUrl();
readUrl();
//showUrl("http://url.com/");
