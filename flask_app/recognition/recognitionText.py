from google.cloud import vision
import io
import os
import re
import json
import base64
from dotenv import load_dotenv, find_dotenv
from google.oauth2.service_account import Credentials

# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '../recognition/cool-ascent-425906-b5-18c081794b5d.json'

input_path = '../uploads'

load_dotenv(find_dotenv())


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
    cred = Credentials.from_service_account_info({ 
        "type": "service_account",
        "project_id": os.environ["PROJECT_ID"],
        "private_key_id": os.environ["PRIVATE_KEY_ID"],
        "private_key": os.environ["PRIVATE_KEY"].replace("\\n", "\n"),
        "client_email": os.environ["CLIENT_EMAIL"],
        "client_id": os.environ["CLIENT_ID"],
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": os.environ["CLIENT_X509_CERT_URL"]
    })
    client = vision.ImageAnnotatorClient(credentials=cred)

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
    lower_english_words = [w.lower() for w in english_words]
    cleaned_japanese_meanings = [meaning for meaning in japanese_meanings if not unnecessary_japanese_pattern.match(meaning)]
    return  lower_english_words,cleaned_japanese_meanings

if __name__ == "__main__":
    output = extract_text_from_images(input_path)
    result = clean_text(output)
    print(result[0])
    print(result[1])

