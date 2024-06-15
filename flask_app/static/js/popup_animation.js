const popclk = document.getElementById('click-btn');

popclk.addEventListener('click', () => {
	const popup = document.getElementById('popup-inside');
	popup.style.display = 'block'; // ポップアップを表示
	popup.classList.add('is-animated'); // アニメーションクラスを追加
});