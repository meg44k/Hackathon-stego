const clickBtn = document.querySelector('#click-btn');
const popupWrapper = document.querySelector('#popup-wrapper');
const close = document.querySelector('#close');

// ボタンをクリックしたときにポップアップを表示させる
clickBtn.addEventListener('click', () => {
	popupWrapper.style.display = "block";
});

// ポップアップの外側又は「x」のマークをクリックしたときポップアップを閉じる
popupWrapper.addEventListener('click', e => {
	if (e.target.id === popupWrapper.id || e.target.id === close.id) {
		popupWrapper.style.display = 'none';
	}
});
