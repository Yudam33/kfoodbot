#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Korean Food Chatbot Test Script
한국 음식 챗봇 테스트 스크립트
"""

import sys
import os

# Add the app directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from app.services.chatbot_service import handle_chat_message

def test_korean_chatbot():
    """Test the Korean food chatbot with various inputs"""
    
    print("🍽️ 한국 음식 레시피 챗봇 테스트")
    print("=" * 50)
    
    # Test cases
    test_messages = [
        "안녕하세요",
        "김치찌개 레시피 알려줘",
        "불고기 만드는법",
        "인기 한국 음식",
        "국 종류",
        "도움말",
        "감사합니다",
        "없는음식 레시피"
    ]
    
    for message in test_messages:
        print(f"\n👤 사용자: {message}")
        try:
            response = handle_chat_message(message)
            print(f"🤖 챗봇: {response}")
        except Exception as e:
            print(f"❌ 오류: {e}")
    
    print("\n" + "=" * 50)
    print("✅ 테스트 완료!")

if __name__ == "__main__":
    test_korean_chatbot() 