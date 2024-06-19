# 2024 ハックツハッカソン　ステゴカップ
### 単語帳を作る魔法 (いーよーグループ)


## 機能

写真から単語を抽出し，自動で単語帳を作成します.  
Topa'z:https://topaz.dev/projects/5881677140e4f927ca3d

## 使用技術
|カテゴリ|技術|
|---|---|
|フロントエンド|JavaScript|
|バックエンド|Flask|

## 使用したライブラリ
Flask==2.3.3<br>
python-dotenv==1.0.1<br>
scikit_learn==1.5.0<br>
gensim==3.8.3<br>
nltk==3.8.1<br>
numpy==1.26.4<br>
scipy==1.12.0<br>

## ディレクトリ構成

```
root
│  .DS_Store
│  .env
│  .gitattributes
│  .gitignore
│  Dockerfile
│  readme.md
│  requirements.txt
│
├─flask_app
│  │  .DS_Store
│  │  app.py
│  │  __init__.py
│  │
│  ├─recognition
│  │  │  .DS_Store
│  │  │  recognitionText.py  //英・日の単語認識
│  │
│  ├─static
│  │  ├─css
│  │  │      index.css //全ページのCSS
│  │  │      responsible.css  //レスポンシブルデザインのCSS
│  │  │
│  │  ├─images
│  │  │      logo_kari.svg //タイトルロゴ
│  │  │
│  │  └─js
│  │          cards_arrow.js  //矢印キーでカードをスクロールする機能
│  │          cards_list.js  //単語帳を表示させる機能
│  │          cards_scroll.js  //カードをスクロールする機能
│  │          file_preview.js  //アップロードしたファイルをプレビューを表示
│  │          index_animation.js  //ロード時のアニメーション
│  │          popup.js  //ポップアップの実装
│  │          popup_animation.js  //ポップアップのアニメーション
│  │          upload_filiname.js  //ホーム画面にアップロードしたファイルを追加
│  │
│  ├─templates
│  │      cards.html  //単語帳の画面
│  │      edit.html  //単語帳の編集画面
│  │      folder.html  //ホーム画面
│  │      index.html  //スタート画面
│  │      login.html  //ログイン画面
│  │      newcards.html  //新たな単語帳の生成画面
│  │      news.html  //ニュースページ
│  │
│  ├─uploads  //読み取った写真の格納場所
│  │
│  │
│  ├─views
│  │  │  cards.py
│  │  │  edit.py
│  │  │  folder.py
│  │  │  index.py
│  │  │  login.py
│  │  │  newcards.py
│  │  │  news.py
│  │
│  ├─word2vec
│  │  │  .DS_Store
│  │  │  generate_flash_card.py
│  │  │  load_model_script.py
│  │  │  model_loader.py
│  │  │  most_similar_word.py
│  │  │
│  │  ├─models
│  │  │      .DS_Store
│  │  │      ja_model.pickle
│  │  │      model.vec   
│  │
│
└─instance
        config.py
```
