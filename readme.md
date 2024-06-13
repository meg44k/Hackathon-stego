# 2024 ハックツハッカソン　ステゴカップ
### 単語帳を作る魔法 (いーよーグループ)


## 機能

写真から単語を抽出し，自動で単語帳を作成します．

## 作成した経緯

私の学校では英語の毎授業で英単語テストがあるので，みんな必死で単語帳アプリに英単語と日本語訳を入力していました．

写真から単語帳ができたらみんな楽になるだろうなーと思いこのアプリを作成しようと決意しました．

## 使用技術
|カテゴリ|技術|
|---|---|
|フロントエンド|JavaScript|
|バックエンド|Flask|

## ディレクトリ構成

```
root
│  .gitignore					Gitで追跡しないファイル指定
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
