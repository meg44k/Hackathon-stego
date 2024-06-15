$(function() {
	$('.file-import-direct').on('change', function () { //ファイルが選択されたら
		var file = $(this).prop('files')[0]; //ファイルの情報を代入(file.name=ファイル名/file.size=ファイルサイズ/file.type=ファイルタイプ)
		$('.newcards-button2').text(file.name); //ファイル名を出力
	});
});