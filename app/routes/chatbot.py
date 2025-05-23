# app/routes/chatbot.py
from flask import Blueprint, render_template, request, redirect, url_for
from app.services.chatbot_service import get_recipe_by_image
from app.utils.image_upload import save_image

chatbot_bp = Blueprint('chatbot', __name__)

@chatbot_bp.route('/')
def index():
    return render_template('index.html')

@chatbot_bp.route('/upload', methods=['POST'], strict_slashes=False)
def upload():

    if 'foodImage' not in request.files:
        return redirect(url_for('chatbot.index'))
    
    file = request.files['foodImage']
    if file.filename == '':
        return redirect(url_for('chatbot.index'))
    
    file_path = save_image(file)
    if not file_path:
        # handle error: invalid file
        return redirect(url_for('chatbot.index'))

    # Here, you would call your AI image recognition & recipe matching function
    recipe = get_recipe_by_image(file_path)

    return render_template('result.html', recipe=recipe)
