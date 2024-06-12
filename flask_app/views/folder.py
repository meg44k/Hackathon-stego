from flask import Blueprint, render_template, request, redirect

folder_bp = Blueprint('folder', __name__, url_prefix='/')

@folder_bp.route('/folder')
def folder():
    return render_template('folder.html')