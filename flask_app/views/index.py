from flask import Blueprint, render_template, request, redirect

index_bp = Blueprint('index', __name__, url_prefix='/')

@index_bp.route('/')
def top():
    redirect('/index')
    return render_template('index.html')

@index_bp.route('/index')
def index():
    return render_template('index.html')