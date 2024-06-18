from flask import Blueprint, render_template, request, redirect,url_for
from flask_app.word2vec.generate_flash_card import generate_flash_cards
import os
import json

json_path = './uploads/flashcards.json'
newcards_bp = Blueprint('newcards', __name__, url_prefix='/')


@newcards_bp.route('/newcards.html')
def redirect_to_newcards():
    return redirect('/newcards')

@newcards_bp.route('/newcards', methods=['GET', 'POST'])
def newcards():
    if request.method == 'GET':
        return render_template('newcards.html')
    elif request.method == 'POST':
        folder_name = request.form['folder_name']
        # formからファイルデータを取得
        file = request.files['file']
        file.save(os.path.join('./uploads', file.filename))
        return redirect('/cards',folder_name=folder_name)