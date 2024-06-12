from flask import Blueprint, render_template, request, redirect

news_bp = Blueprint('news', __name__, url_prefix='/')

@news_bp.route('/news')
def news():
    return render_template('news.html')