#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Korean Food Chatbot Application
한국 음식 레시피 챗봇 애플리케이션
"""

import os
import sys
from app import create_app
from config import get_config

def main():
    """Main application entry point"""
    try:
        # Get configuration
        config = get_config()
        
        # Create Flask app
        app = create_app()
        app.config.from_object(config)
        
        # Initialize app with configuration
        config.init_app(app)
        
        # Get port from environment or use default
        port = int(os.environ.get('PORT', 5000))
        
        print("🍽️ 한국 음식 레시피 챗봇 시작 중...")
        print(f"📍 서버 주소: http://localhost:{port}")
        print(f"🔧 개발 모드: {'켜짐' if app.config['DEBUG'] else '꺼짐'}")
        print("=" * 50)
        
        # Run the application
        app.run(
            host='0.0.0.0', 
            port=port, 
            debug=app.config['DEBUG']
        )
        
    except KeyboardInterrupt:
        print("\n👋 애플리케이션을 종료합니다.")
        sys.exit(0)
    except Exception as e:
        print(f"❌ 오류가 발생했습니다: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
