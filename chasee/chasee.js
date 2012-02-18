var site = 'http://willthompson.co.uk:8080'
var div =  $('<div id="WhittonUrl"/>');
$('body').append(div);

function sendUrl()
{
	// do send
	$.get(site+'/chasee/update/'+document.URL);
}

function readUrl()
{
	$.get(site+'/chasee/target/',function(result){
    showUrl(result);
  });
}

function showUrl(data)
{
	// display text in diff
	div.text(data);
	// repeat after time	
	var t=setTimeout("readUrl()",3000);
}

sendUrl();
readUrl();
