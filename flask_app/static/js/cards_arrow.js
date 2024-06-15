// 矢印キー（←→）を押されるとカードがスクロールされる
let code = document.getElementById('code');
let key = document.getElementById('key');

document.addEventListener('keydown', (event)=>{
	if (event.code === 'ArrowLeft') {
		prev();
	} else if (event.code === 'ArrowRight') {
		next();
	} else if (event.code === 'Space') {
		toggleCard();
	} else {
		return;
	}
});