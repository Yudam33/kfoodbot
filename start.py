#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Startup script for Korean Food Chatbot
한국 음식 챗봇 시작 스크립트
"""

import os
import sys
import subprocess
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are installed"""
    required_packages = [
        'flask',
        'pandas',
        'python-dotenv'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("❌ 다음 패키지들이 설치되지 않았습니다:")
        for package in missing_packages:
            print(f"   - {package}")
        print("\n다음 명령어로 설치하세요:")
        print("pip install -r requirements.txt")
        return False
    
    return True

def check_data_files():
    """Check if required data files exist"""
    data_files = [
        'data/recipe_data_sample.csv',
        'data/recipe_data.csv'
    ]
    
    missing_files = []
    
    for file_path in data_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
    
    if missing_files:
        print("⚠️  다음 데이터 파일들이 없습니다:")
        for file_path in missing_files:
            print(f"   - {file_path}")
        print("\n데이터 파일을 확인해주세요.")
        return False
    
    return True

def create_directories():
    """Create necessary directories"""
    directories = [
        'uploads',
        'data',
        'logs'
    ]
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✅ 디렉토리 생성: {directory}")

def main():
    """Main startup function"""
    print("🍽️ 한국 음식 레시피 챗봇 시작 준비 중...")
    print("=" * 50)
    
    # Check dependencies
    print("📦 의존성 확인 중...")
    if not check_dependencies():
        sys.exit(1)
    print("✅ 모든 의존성이 설치되어 있습니다.")
    
    # Check data files
    print("\n📁 데이터 파일 확인 중...")
    if not check_data_files():
        print("⚠️  일부 데이터 파일이 없습니다. 계속 진행합니다.")
    else:
        print("✅ 데이터 파일이 준비되어 있습니다.")
    
    # Create directories
    print("\n📂 디렉토리 생성 중...")
    create_directories()
    
    # Start the application
    print("\n🚀 애플리케이션 시작 중...")
    print("=" * 50)
    
    try:
        # Import and run the main application
        from main import main as run_app
        run_app()
    except KeyboardInterrupt:
        print("\n👋 애플리케이션을 종료합니다.")
    except Exception as e:
        print(f"\n❌ 오류가 발생했습니다: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 