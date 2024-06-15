from  word2vec.model_loader import load_model_from_pickle,get_model
from sklearn.metrics.pairwise import cosine_similarity

# ピクルファイルからモデルをロード
load_model_from_pickle('word2vec/models/ja_model.pickle', 'ja_model')
ja_model = get_model('ja_model')

#コサイン類似度を計算
def calculate_cosine_similarity(word1, word2):
    vec1 = ja_model[word1]
    vec2 = ja_model[word2]
    similarity = cosine_similarity([vec1], [vec2])
    return similarity[0][0]

#英単語と日単語を組み合わせる
def connection_words(en_words, ja_words):
    connected_en_words = en_words
    connected_ja_words = [None] * len(en_words)#en_wordsと同じ長さのリストを作成
    for index,en_word in enumerate(en_words):
        simirarity = -1
        for ja_word in ja_words:
            if simirarity < calculate_cosine_similarity(en_word, ja_word):
                simirarity = calculate_cosine_similarity(en_word, ja_word)
                most_similar_word = ja_word
        connected_ja_words[index] = most_similar_word
        most_similar_word = None
    return connected_en_words, connected_ja_words
