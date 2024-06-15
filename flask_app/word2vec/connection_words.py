import most_similar_word

from flask_app.recognition.recognitionText import extract_text_from_images,clean_text

# 画像が含まれるディレクトリのパス
input_directory = '../uploads'

output = extract_text_from_images(input_directory)
result = clean_text(output)

#ワードの例
en_words = result[0]
ja_words = result[1]

connected_words = most_similar_word.connection_words(en_words, ja_words)

print(connected_words)