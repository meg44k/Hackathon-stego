from flask import Blueprint, render_template, request, redirect

login_bp = Blueprint('login', __name__, url_prefix='/')

@login_bp.route('/login.html')
def redirect_to_login():
    return redirect('/login')

@login_bp.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print(email, password,)
        return redirect('/index')