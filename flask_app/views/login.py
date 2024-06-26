from flask import Blueprint, render_template, request, redirect

login_bp = Blueprint('login', __name__, url_prefix='/')

@login_bp.route('/login.html')
def redirect_to_login():
    return redirect('/login')

@login_bp.route('/login')
def login():
    return render_template('login.html')