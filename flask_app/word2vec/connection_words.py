import most_similar_word

#ワードの例
en_words = ["run","apple","human","sky","water","orange","run","blue","die","blood","draw","strong"]

ja_words = ["りんご", "人間","血" ,"空", "水", "オレンジ", "走る", "青い", "衣装","死ぬ","書く","強い","あんぱん"]

connected_words = most_similar_word.connection_words(en_words, ja_words)

print(connected_words)