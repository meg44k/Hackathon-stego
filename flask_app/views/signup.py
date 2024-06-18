from flask import Blueprint, render_template, request, redirect

signup_bp = Blueprint('signup', __name__, url_prefix='/')

@signup_bp.route('/signup.html')
def redirect_to_signup():
    return redirect('/signup')

@signup_bp.route('/signup')
def signup():
    return render_template('signup.html')