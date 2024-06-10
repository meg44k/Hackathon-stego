# 単語帳を作る魔法

## What is this?

写真から単語を抽出し，自動で単語帳を作成します．


## ディレクトリ構成

```
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
├─instance					設定
│      config.py
│
└─__pycache__
        app.cpython-38.pyc
```
