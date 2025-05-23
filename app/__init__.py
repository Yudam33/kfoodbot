from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__, static_folder='static')
    CORS(app)  # Cross-Origin 허용, API 개발 시 필요하면 사용

    # 블루프린트 등록 예시 (나중에 routes/chatbot.py에서 불러올 예정)
    from app.routes.chatbot import chatbot_bp
    from app.routes.image_upload import image_upload_bp
    app.register_blueprint(chatbot_bp)
    app.register_blueprint(image_upload_bp, url_prefix='/api/image_upload')

    app.config['UPLOAD_FOLDER'] = 'uploads/'

    return app
