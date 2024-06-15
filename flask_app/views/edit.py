from flask import Blueprint, render_template, request, redirect

edit_bp = Blueprint('edit', __name__, url_prefix='/')

@edit_bp.route('/edit.html')
def redirect_to_folder():
    return redirect('/edit')

@edit_bp.route('/edit')
def edit():
    return render_template('edit.html')