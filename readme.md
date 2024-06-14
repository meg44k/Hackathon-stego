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
root
│  .gitignore					Gitで追跡し裏利ないファイル指定
│  readme.md
│  requirements.txt
│  
├─flask_app					アプリケーションの本体
│  │  app.py
│  │  __init__.py
│  │  
│  ├─images					画像
│  │      logo_kari.svg			ロゴ
│  │
│  ├─static					CSSやJS
│  │  └─css
│  │          index.css			index.htmlのスタイルシート
│  │
│  ├─templates				HTML
│  │      index.html			「はじめる」画面
│  │
│  └─views.py				コントローラ
│          index.py
│
└─instance					設定
       config.py

```
<!--つづきはまた書きます-->
