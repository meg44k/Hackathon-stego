# 2024 ハックツハッカソン　ステゴカップ
### 単語帳を作る魔法 (いーよーグループ)


## 機能

写真から単語を抽出し，自動で単語帳を作成します．


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
roo
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
│  │  │  recognitionText.py     
│  │
│  ├─static
│  │  ├─css
│  │  │      index.css
│  │  │      responsible.css
│  │  │
│  │  ├─images
│  │  │      logo_kari.svg
│  │  │
│  │  └─js
│  │          cards_arrow.js
│  │          cards_list.js
│  │          cards_scroll.js
│  │          file_preview.js
│  │          index_animation.js
│  │          popup.js
│  │          popup_animation.js
│  │          upload_filiname.js
│  │
│  ├─templates
│  │      cards.html
│  │      edit.html
│  │      folder.html
│  │      index.html
│  │      login.html
│  │      newcards.html
│  │      news.html
│  │
│  ├─uploads
│  │      a.jpg
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
