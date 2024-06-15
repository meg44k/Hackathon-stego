from word2vec.most_similar_word import connection_words
from flask_app.recognition.recognitionText import extract_text_from_images,clean_text

# 画像が含まれるディレクトリのパス
input_directory = './uploads'

def generate_flash_cards():
    output = extract_text_from_images(input_directory)
    result = clean_text(output)

    #ワードの例
    en_words = result[0]
    ja_words = result[1]

    connected_words = connection_words(en_words,ja_words)
    return connected_words[0],connected_words[1]

if __name__ == '__main__':
    results = generate_flash_cards()
    print(results[0])
    print(results[1])