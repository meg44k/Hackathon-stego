const clickBtn = document.getElementById('click-btn');
const popupWrapper = document.getElementById('popup-wrapper');
const close = document.getElementById('close');

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