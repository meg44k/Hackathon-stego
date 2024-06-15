// cards.htmlで単語を表示させる
let words = [];
let currentIndex = 0;
let showingEnglish = true;
const en_words = '{{en_words}}'
const ja_words = '{{ja_words}}'
console.log(en_words)
console.log(ja_words)
const englishWord = en_words[0];
const japaneseWord = ja_words[0];

const flashcard = document.getElementById('flashcard');
const flashcardNumber = document.getElementById('flashcard-number');

function toggleCard() {
	if (en_words.length === 0) return;
	showingEnglish = !showingEnglish;
	updateCard();
}
function addWords(){
	words = [];
	for (let i = 0; i < en_words.length; i++) {
		if (englishWord && japaneseWord) {
			words.push({ english: en_words[i], japanese: ja_words[i] });
		}
		updateCard();
	}
}

function updateCard() {
	// if (words.length === 0) {
	// 	flashcard.textContent = '[編集]から単語を追加してください';
	// 	return;
	// }
	const word = en_words[currentIndex];
	flashcard.textContent = showingEnglish ? word.english : word.japanese;
	if (en_words.length === 0) {
		flashcardNumber.textContent = '';
	} else {
		flashcardNumber.textContent = `${currentIndex+1}　/　${en_words.length}`;
	}
}


// テスト用

// function addWord() {
//     const englishWord = document.getElementById('englishWord').value;
//     const japaneseWord = document.getElementById('japaneseWord').value;
//     if (englishWord && japaneseWord) {
//         words.push({ english: englishWord, japanese: japaneseWord });
//         document.getElementById('englishWord').value = '';
//         document.getElementById('japaneseWord').value = '';
//         if (words.length === 1) {
//             updateCard();
//         }
//     }
// }

// 初期状態のカードを更新
updateCard();

