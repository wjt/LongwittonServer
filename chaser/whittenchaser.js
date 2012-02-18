var site = 'http://willthompson.co.uk:8080'
var div =  $('<div id="WhittonUrl"/>');
$('body').append(div);

function sendUrl()
{
	// do send
	$.get(site+'/chaser/update/'+document.URL);
}

function readUrl()
{
	$.get(site+'/chasee/current/',function(result){
    showUrl(result);
  });
}

function showUrl(data)
{
	// display text in diff
	div.text(data);
	// repeat after time	
	var t=setTimeout("readUrl()",1000);
}

sendUrl();
readUrl();
