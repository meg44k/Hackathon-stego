import re

# 出力を文字列として定義
output = """
27. landlord
tenant
國家主
租賃借人
名 衣服 衣料品
28. light fixture
臨 照明器具
□1. clothes,
light bulb
關 電球
clothing,
garment
attire
(特別な) 服装
□29.mow
trim
動〜を刈る
~を刈り揃える
2. detergent
目 洗剂
□30. overlook
3. fabric
日 生地
動を見下ろす位置にある
□ 31. patio
目 中庭
textile
目 織物
texture
名手触り
□32. plumber
4. fold
動~を折りたたむ
日 配管工
33. property, real estate
不動産
動 ~を吊るす
34. remodel
動を改築する
□5. hang
6. laundry
名 洗濯物、 クリーニング店
35. rent
名家賃 ~を賃貸する
do the laundry 洗濯する
cleaner
名 クリーニング店
□ 36. repair, fix
動を修理する
□ 37.replace
動
を交換する
□7. cookware
3 調理器具
tableware
: 食器類
38. resident
名 居住者、住民
8. cupboard
名 食器棚
□39. stairs, staircase
名 階段
□9. dairy
□ 10. grocery store
鹽 乳製品
食料雑貨店
□40. suburb
urban
名 郊外
形 都会の
□11. microwave oven
名電子レンジ
□41. turn on
句をつける
turn off
旬 ~を消す
12. refrigerator, fridge
冷蔵庫
42. utilities
13. stove
名コンロ
□14. utensils
名 台所用品
43. view
その他
名 公共料金
名眺め、視界
●住
15. appliance
□44. blackout
名 電化製品、家電
16. attach
45. convenience
動~を取り付ける
equip
動〜に備え付ける
: 停電
名 便利さ
convenient 形 便利な
install
動 ~を設置する
46. evacuate
17. ceiling
图 天井
動 ~を避難させる、避難する
18.comfortable
形居心地の良い、快適な
147. household
名 形 世帯、家庭(の)
19. condo (minium)
分譲マンション
48. lean against
旬〜に寄りかかる
20. drawer
引き出し
21.electricity
□49. monthly
weekly
形 毎月の
形 毎週の
證 電気
22. enter
□50. neighborhood
近所
〜に入る
entrance
超 入口
nearby
すぐ近くの(に)
exit
超 出口
23. equipment
設備、裝備
24. furniture
: 家具
25. hardware store 名 ホームセンター
26. ladder
名はしご
"""

# 正規表現パターンを定義
english_word_pattern = re.compile(r'\b([a-zA-Z\- \(\)]+)\b')
japanese_meaning_pattern = re.compile(r'(?<!\w)([ぁ-んァ-ヶ一-龥]+)(?!\w)')

# 英語の単語と日本語の意味を格納するリスト
english_words = []
japanese_meanings = []

# 不要な品詞や助詞を除外する正規表現パターン
unnecessary_japanese_pattern = re.compile(r'^(名|動|形|目|超|日|旬|關|图|證|□|\d+|\.|:|~|、|の|に)$')

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

# 結果を出力
print("English words:", english_words)
print("Japanese meanings:", cleaned_japanese_meanings)
