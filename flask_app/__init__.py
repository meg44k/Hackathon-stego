from flask import Flask

def create_app():
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_pyfile('config.py')

    from flask_app.views.index import index_bp

    app.register_blueprint(index_bp)
    return app