import os
from flask import Blueprint, request, render_template, current_app
from werkzeug.utils import secure_filename
from app.services.image_recognition import predict_food_name
from app.utils.recipe_loader import load_recipes, find_recipes_by_food_name

image_upload_bp = Blueprint("image_upload", __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_image(file):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        upload_folder = current_app.config['UPLOAD_FOLDER']
        os.makedirs(upload_folder, exist_ok=True)

        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)
        return file_path
    return None

@image_upload_bp.route("/image_upload", methods=["POST"])
def upload_image():
    file = request.files.get("image")
    if not file:
        return "No file uploaded", 400

    image_path = save_image(file)
    if not image_path:
        return "Invalid file format", 400

    predicted_food = predict_food_name(image_path)
    recipes_df = load_recipes()
    matches = find_recipes_by_food_name(predicted_food, recipes_df)

    if not matches.empty:
        recipe = matches.iloc[0]  # 첫 번째 매칭된 레시피
        return render_template("result.html", recipe=recipe, predicted_food=predicted_food)
    else:
        return render_template("result.html", recipe=None, predicted_food=predicted_food)
