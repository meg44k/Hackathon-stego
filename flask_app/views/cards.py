from flask import Blueprint, render_template, request, redirect
from flask_app.word2vec.generate_flash_card import generate_flash_cards
import os

cards_bp = Blueprint('cards', __name__, url_prefix='/')

@cards_bp.route('/cards.html')
def redirect_to_cards():
    return redirect('/cards')

@cards_bp.route('/cards')
def cards():
    connected_words = generate_flash_cards()
    connected_en_words = connected_words[0]
    connected_ja_words = connected_words[1]
    print(connected_en_words)
    print(connected_ja_words)
    # os.remove('./uploads/')
    return render_template('cards.html',en_words=connected_en_words,ja_words=connected_ja_words)
