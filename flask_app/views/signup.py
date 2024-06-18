from flask import Blueprint, render_template, request, redirect

signup_bp = Blueprint('signup', __name__, url_prefix='/')

@signup_bp.route('/signup.html')
def redirect_to_signup():
    return redirect('/signup')

@signup_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        repassword = request.form['repassword']
        print(email, username, password, repassword)
        return redirect('/index')