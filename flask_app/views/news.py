from flask import Blueprint, render_template, request, redirect,url_for

news_bp = Blueprint('news', __name__, url_prefix='/')

@news_bp.route('/news.html')
def redirect_to_news():
    return redirect('/news')

@news_bp.route('/news')
def news():
    return render_template('news.html')