//親要素取得  
var element = document.getElementById("jsnap");

//子要素を参照するための番号
var num = 0;

// next
function next() {
	if(num+1 < element.children.length) {
		var child = element.children[num+1];  
		child.scrollIntoView(  
		{
			behavior:"smooth",
			block:"nearest",
			inline:"nearest",
		});
		num++;
	}
	else {
		return;
	}
}


// prev
function prev() {
	if(num-1 >= 0) {
		var child = element.children[num-1];  
		child.scrollIntoView(  
		{
			behavior:"smooth",
			block:"nearest",
			inline:"nearest",
		});
		num--;
	}
	else {
		return;
	}
}