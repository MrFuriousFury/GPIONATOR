function switchState(item,arg)
{
	if(item.className == "bon")
	{
		item.className = "b";
		document.location="/cgi-bin/set0"+ arg + ".cgi";
	}
	else
	{
		item.className = 'bon';
		document.location="/cgi-bin/set" + arg + ".cgi";
	}
}

function rset() {
	document.location="/cgi-bin/rset.cgi";
}
function full(){
	document.location="/cgi-bin/full.cgi";
}