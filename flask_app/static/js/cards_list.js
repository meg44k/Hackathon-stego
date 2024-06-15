// cards.htmlで単語を表示させる
let words = [];
let currentIndex = 0;
let showingEnglish = true;

const flashcard = document.getElementById('flashcard');
const flashcardNumber = document.getElementById('flashcard-number');

function toggleCard() {
	if (words.length === 0) return;
	showingEnglish = !showingEnglish;
	updateCard();
}

function updateCard() {
	if (words.length === 0) {
		flashcard.textContent = '[編集]から単語を追加してください';
		return;
	}
	const word = words[currentIndex];
	flashcard.textContent = showingEnglish ? word.english : word.japanese;
	if (words.length === 0) {
		flashcardNumber.textContent = '';
	} else {
		flashcardNumber.textContent = `${currentIndex+1}　/　${words.length}`;
	}
}


// テスト用

function addWord() {
    const englishWord = document.getElementById('englishWord').value;
    const japaneseWord = document.getElementById('japaneseWord').value;
    if (englishWord && japaneseWord) {
        words.push({ english: englishWord, japanese: japaneseWord });
        document.getElementById('englishWord').value = '';
        document.getElementById('japaneseWord').value = '';
        if (words.length === 1) {
            updateCard();
        }
    }
}

// 初期状態のカードを更新
updateCard();

