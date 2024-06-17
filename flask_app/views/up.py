from flask import Blueprint, render_template, request, redirect,url_for
from flask_app.word2vec.generate_flash_card import generate_flash_cards
import os
import json

up_bp = Blueprint('up', __name__, url_prefix='/')


@up_bp.route('/up', methods=['GET', 'POST'])
def up():
    if request.method == 'GET':
        return render_template('up.html')
    elif request.method == 'POST':
        # formからファイルデータを取得
        file = request.files['file']
        file.save(os.path.join('./uploads', file.filename))
        
        return render_template('up.html')