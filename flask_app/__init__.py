from flask import Flask

def create_app():
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_pyfile('config.py')

    from flask_app.views.index import index_bp
    from flask_app.views.folder import folder_bp
    from flask_app.views.login import login_bp
    from flask_app.views.news import news_bp
    from flask_app.views.newcards import newcards_bp
    from flask_app.views.cards import cards_bp

    app.register_blueprint(index_bp)
    app.register_blueprint(folder_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(news_bp)
    app.register_blueprint(newcards_bp)
    app.register_blueprint(cards_bp)

    return app