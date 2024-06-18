from flask import Flask
from flask import Flask, make_response, jsonify
# from .views.user import user_router
from flask_cors import CORS
from flask_app.database import db
import config

def create_app():
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_pyfile('config.py')

    #blueprintを登録
    from flask_app.views.index import index_bp
    from flask_app.views.folder import folder_bp
    from flask_app.views.login import login_bp
    from flask_app.views.news import news_bp
    from flask_app.views.newcards import newcards_bp
    from flask_app.views.cards import cards_bp
    from flask_app.views.edit import edit_bp

    app.register_blueprint(index_bp)
    app.register_blueprint(folder_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(news_bp)
    app.register_blueprint(newcards_bp)
    app.register_blueprint(cards_bp)      
    app.register_blueprint(edit_bp)
      
    # CORS対応
    CORS(app)

    # DB設定を読み込む
    app.config.from_object('config.Config')
    db.init_app(app)

    return app