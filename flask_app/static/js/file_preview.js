document.getElementById('file-import-choose').addEventListener('change', (e) => {
	const file = e.target.files[0]; // ファイル本体

	// エラー回避
	if(!file) {
		return;
	}
	const reader = new FileReader();
	reader.onload = (e) => {
		document.getElementById('file-preview').src = e.target.result; // 読み込み完了時にData URIをsrcに渡す
	};
	reader.readAsDataURL(file); // 画像をData URIとして読み込む
});