from google.cloud import vision
import io
import os
import re

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './cool-ascent-425906-b5-18c081794b5d.json'

# 画像が含まれるディレクトリのパス（ローカル）
input_directory = '../uploads'

# 正規表現パターンを定義
english_word_pattern = re.compile(r'\b([a-zA-Z\- \(\)]+)\b')
japanese_meaning_pattern = re.compile(r'(?<!\w)([ぁ-んァ-ヶ一-龥]+)(?!\w)')

# 英語の単語と日本語の意味を格納するリスト
english_words = []
japanese_meanings = []

# 不要な品詞や助詞を除外する正規表現パターン
unnecessary_japanese_pattern = re.compile(r'^(名|動|形|目|超|日|旬|關|图|證|□|\d+|\.|:|~|、|の|に)$')

def detect_text(path):
    """ファイル内のテキストを検出します。"""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.document_text_detection(image=image)
    texts = response.text_annotations

    return texts[0].description if texts else ''

def extract_text_from_images(input_directory):
    for filename in os.listdir(input_directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            image_path = os.path.join(input_directory, filename)
            text = detect_text(image_path)
            return text

# 出力を文字列として定義
output = extract_text_from_images(input_directory)

def clean_text(output):
    # 出力を行ごとに分割して処理
    for line in output.splitlines():
        # 英語の単語を抽出
        english_words_match = english_word_pattern.findall(line)
        for word in english_words_match:
            if len(word.split()) == 1:  # 単語が複数単語から成っていないか確認
                english_words.append(word.strip())
        # 日本語の意味を抽出
        japanese_meanings_match = japanese_meaning_pattern.findall(line)
        for meaning in japanese_meanings_match:
            if not unnecessary_japanese_pattern.match(meaning):
                japanese_meanings.append(meaning.strip())
        # 不要な品詞や助詞を除去してクリーンアップ
    cleaned_japanese_meanings = [meaning for meaning in japanese_meanings if not unnecessary_japanese_pattern.match(meaning)]
    return cleaned_japanese_meanings, english_words



# 結果を出力
if __name__ == '__main__':
    
    output = extract_text_from_images(input_directory)
    result = clean_text(output)
    print(result[0])
    print(result[1])