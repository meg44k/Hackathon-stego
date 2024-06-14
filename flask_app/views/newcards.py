from flask import Blueprint, render_template, request, redirect
import os

newcards_bp = Blueprint('newcards', __name__, url_prefix='/')

@newcards_bp.route('/newcards.html')
def redirect_to_newcards():
    return redirect('/newcards')

@newcards_bp.route('/newcards')
def newcards():
    return render_template('newcards.html')

@newcards_bp.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        file.save(os.path.join('./uploads', file.filename))
        return redirect('/index') #要変更