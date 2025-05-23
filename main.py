from app import create_app

app = create_app()

if __name__ == "__main__":
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True) # 개발모드 on. 실 서비스 때 변경 필요
