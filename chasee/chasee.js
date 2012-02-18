var site = 'http://willthompson.co.uk:8080'
var div =  $('<div id="WhittonUrl"/>');
$('body').append(div);

function query() {
    return ('?' + (Math.random() * 1000000));
}

function sendUrl()
{
	// do send
	$.get(site+'/chasee/update/'+document.URL + query());
}

function readUrl()
{
	$.get(site+'/chasee/target/' + query(),function(result){
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
