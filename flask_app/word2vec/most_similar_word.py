import model_loader
from sklearn.metrics.pairwise import cosine_similarity

# ピクルファイルからモデルをロード
model_loader.load_model_from_pickle('models/ja_model.pickle', 'ja_model')
ja_model = model_loader.get_model('ja_model')

#コサイン類似度を計算
def calculate_cosine_similarity(word1, word2):
    vec1 = ja_model[word1]
    vec2 = ja_model[word2]
    similarity = cosine_similarity([vec1], [vec2])
    return similarity[0][0]

#英単語と日単語を組み合わせる
def connection_words(en_words, ja_words):
    connected_words = {}
    for en_word in en_words:
        simirarity = -1
        for ja_word in ja_words:
            if simirarity < calculate_cosine_similarity(en_word, ja_word):
                simirarity = calculate_cosine_similarity(en_word, ja_word)
                most_similar_word = ja_word
        connected_words[en_word] = most_similar_word
        most_similar_word = None
    return connected_words