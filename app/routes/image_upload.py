import os
from werkzeug.utils import secure_filename
from flask import current_app
from app.services.image_recognition import predict_food_name

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

#Checks the uploaded file extension to allow only image types
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#Sanitizes the filename to prevent security issues like directory traversal.
#save_image(file): Saves the uploaded image to the configured UPLOAD_FOLDER. Creates the folder if it doesn’t exist.
def save_image(file):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        upload_folder = current_app.config['UPLOAD_FOLDER']
        
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        
        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)
        return file_path
    return None
