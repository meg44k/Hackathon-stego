$(function() {
	$('.file-import-direct').on('change', function () { //ファイルが選択されたら
		var file = $(this).prop('files')[0]; //ファイルの情報を代入(file.name=ファイル名/file.size=ファイルサイズ/file.type=ファイルタイプ)
		$('.newcards-button2').text(file.name); //ファイル名を出力
		$('.js-upload-fileclear').show(); //クリアボタンを表示
	});
	$('.js-upload-fileclear').click(function() { //クリアボタンがクリックされたら
		$('.file-import-direct').val(); //inputをリセット
		$('.newcards-button2').text('読み取る写真を選択...'); //ファイル名をリセット
		$(this).hide(); //クリアボタンを非表示
		$('#file-preview').hide();
	  });
});