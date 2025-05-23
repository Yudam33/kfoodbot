import os
from werkzeug.utils import secure_filename
from flask import current_app

def save_image(file):
    if file:
        filename = secure_filename(file.filename)
        upload_folder = current_app.config['UPLOAD_FOLDER']
        os.makedirs(upload_folder, exist_ok=True)  # 폴더 없으면 생성

        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)

        return file_path  # ★ 여기 중요! 전체 경로를 return 해야 함
    return None
