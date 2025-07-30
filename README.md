# 🍽️ 한국 음식 레시피 챗봇 (Korean Food Recipe Chatbot)

> **전통부터 현대까지, 맛있는 한국 요리를 찾아보세요!**  
> 이 프로젝트는 한국 음식 레시피를 검색하고 추천해주는 AI 기반 웹 애플리케이션입니다.

## 📋 목차 (Table of Contents)

- [✨ 주요 기능](#-주요-기능)
- [🎯 프로젝트 개요](#-프로젝트-개요)
- [🏗️ 기술 스택](#️-기술-스택)
- [📁 프로젝트 구조](#-프로젝트-구조)
- [🚀 설치 및 실행](#-설치-및-실행)
- [💻 개발 가이드](#-개발-가이드)
- [🎨 프론트엔드 가이드](#-프론트엔드-가이드)
- [🔧 백엔드 가이드](#-백엔드-가이드)
- [📊 데이터 구조](#-데이터-구조)
- [🔍 API 문서](#-api-문서)
- [🧪 테스트](#-테스트)
- [🐛 문제 해결](#-문제-해결)
- [🤝 기여하기](#-기여하기)

## ✨ 주요 기능 (Features)

### 🗣️ 한국어 자연어 처리
- **완전한 한국어 지원**: 한국어 인터페이스와 자연어 처리
- **지능형 의도 파악**: 사용자 메시지의 의도를 자동으로 분석
- **자연스러운 대화**: 한국어 키워드 기반 응답 시스템

### 🍳 레시피 검색 시스템
- **음식명 검색**: "김치찌개 레시피 알려줘" 같은 자연어 검색
- **카테고리별 분류**: 국, 밥, 면, 반찬, 구이, 튀김, 디저트
- **인기 레시피**: 추천 음식 목록 제공
- **재료 기반 검색**: 특정 재료로 만들 수 있는 음식 찾기

### 🎨 현대적인 웹 인터페이스
- **반응형 디자인**: 모바일과 데스크톱 모두 지원
- **직관적인 채팅**: 실시간 채팅 인터페이스
- **드래그 앤 드롭**: 이미지 업로드 기능
- **한국어 폰트**: Noto Sans KR 폰트 사용

### 📱 완전한 웹 애플리케이션
- **Flask 백엔드**: Python 기반 서버
- **RESTful API**: 표준 HTTP API
- **이미지 처리**: 음식 사진 업로드 및 분석
- **설정 관리**: 환경 변수 기반 설정

## 🎯 프로젝트 개요

이 프로젝트는 다음과 같은 사용자들을 위해 만들어졌습니다:

- **👨‍🍳 요리 애호가**: 한국 음식 레시피를 쉽게 찾고 싶은 분
- **🌍 한국 문화 관심자**: 한국 전통 음식에 관심이 있는 분
- **💻 개발자**: 웹 개발과 AI 챗봇을 학습하고 싶은 분
- **🎓 학생**: Flask, Python, 웹 개발을 배우고 싶은 분

## 🏗️ 기술 스택 (Tech Stack)

### Backend (서버)
| 기술 | 버전 | 설명 |
|------|------|------|
| **Python** | 3.8+ | 메인 프로그래밍 언어 |
| **Flask** | 2.3.2 | 웹 프레임워크 |
| **Pandas** | 2.0.3 | 데이터 처리 |
| **Konlpy** | 0.6.0 | 한국어 자연어 처리 |
| **FuzzyWuzzy** | 0.18.0 | 퍼지 문자열 매칭 |

### Frontend (클라이언트)
| 기술 | 버전 | 설명 |
|------|------|------|
| **HTML5** | - | 웹 페이지 구조 |
| **CSS3** | - | 스타일링 |
| **JavaScript** | ES6+ | 동적 기능 |
| **Font Awesome** | 6.0.0 | 아이콘 |
| **Google Fonts** | - | Noto Sans KR 폰트 |

### 데이터
| 기술 | 설명 |
|------|------|
| **CSV** | 레시피 데이터 저장 |
| **UTF-8/CP949** | 한국어 인코딩 지원 |

## 📁 프로젝트 구조

```
kfoodbot/
├── 📁 app/                          # 메인 애플리케이션 폴더
│   ├── 📁 routes/                   # URL 라우팅 (페이지 연결)
│   │   ├── chatbot.py              # 챗봇 관련 페이지
│   │   └── image_upload.py         # 이미지 업로드 페이지
│   ├── 📁 services/                 # 비즈니스 로직 (핵심 기능)
│   │   ├── chatbot_service.py      # 챗봇 AI 로직
│   │   └── image_recognition.py    # 이미지 인식 서비스
│   ├── 📁 utils/                    # 유틸리티 함수들
│   │   ├── recipe_loader.py        # 레시피 데이터 로더
│   │   └── image_upload.py         # 이미지 업로드 도구
│   ├── 📁 templates/                # HTML 템플릿 (웹페이지)
│   │   ├── index.html              # 메인 페이지
│   │   └── result.html             # 결과 페이지
│   ├── 📁 static/                   # 정적 파일 (CSS, JS, 이미지)
│   │   └── style.css               # 스타일시트
│   └── __init__.py                 # Flask 앱 초기화
├── 📁 data/                         # 데이터 파일들
│   ├── recipe_data_sample.csv      # 샘플 레시피 데이터
│   └── recipe_data.csv             # 전체 레시피 데이터
├── 📁 uploads/                      # 업로드된 이미지 저장소
├── 📄 main.py                       # 애플리케이션 시작점
├── 📄 start.py                      # 시작 스크립트
├── 📄 config.py                     # 설정 파일
├── 📄 test_chatbot.py              # 테스트 스크립트
├── 📄 requirements.txt              # Python 패키지 목록
├── 📄 env_template.txt              # 환경 변수 템플릿
└── 📄 README.md                     # 프로젝트 문서
```

## 🚀 설치 및 실행

### 1단계: 환경 준비

#### Python 설치 확인
```bash
# Python 버전 확인 (3.8 이상 필요)
python --version
# 또는
python3 --version
```

#### Git 설치 확인
```bash
git --version
```

### 2단계: 프로젝트 다운로드

```bash
# GitHub에서 프로젝트 다운로드
git clone https://github.com/yourusername/kfoodbot.git

# 프로젝트 폴더로 이동
cd kfoodbot
```

### 3단계: 가상환경 설정

#### Windows
```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화
venv\Scripts\activate
```

#### macOS/Linux
```bash
# 가상환경 생성
python3 -m venv venv

# 가상환경 활성화
source venv/bin/activate
```

### 4단계: 패키지 설치

```bash
# 필요한 패키지들 설치
pip install -r requirements.txt
```

### 5단계: 데이터 준비

프로젝트에 포함된 CSV 파일들이 있는지 확인:
- `data/recipe_data_sample.csv` (샘플 데이터)
- `data/recipe_data.csv` (전체 데이터)

### 6단계: 애플리케이션 실행

#### 방법 1: 기본 실행
```bash
python main.py
```

#### 방법 2: 시작 스크립트 사용 (권장)
```bash
python start.py
```

### 7단계: 웹 브라우저에서 접속

```
http://localhost:5000
```

## 💻 개발 가이드

### 개발 환경 설정

#### 1. 코드 에디터 설정
VS Code를 사용하는 경우 다음 확장 프로그램을 설치하세요:
- Python
- Flask
- Korean Language Pack

#### 2. 환경 변수 설정
```bash
# .env 파일 생성 (env_template.txt를 복사)
cp env_template.txt .env

# .env 파일 편집
# 필요한 설정값들을 수정
```

#### 3. 개발 모드 실행
```bash
# 개발 모드로 실행
export FLASK_ENV=development  # macOS/Linux
set FLASK_ENV=development     # Windows

python main.py
```

### 코드 구조 이해하기

#### 1. Flask 애플리케이션 구조
```python
# main.py - 애플리케이션 시작점
from app import create_app
from config import get_config

def main():
    config = get_config()
    app = create_app()
    app.config.from_object(config)
    app.run(debug=True)
```

#### 2. 라우팅 (URL 처리)
```python
# app/routes/chatbot.py
@chatbot_bp.route('/chat', methods=['POST'])
def chat():
    user_message = request.form.get('message')
    response = handle_chat_message(user_message)
    return jsonify({'response': response})
```

#### 3. 서비스 로직 (비즈니스 로직)
```python
# app/services/chatbot_service.py
class KoreanFoodChatbot:
    def understand_intent(self, message):
        # 사용자 의도 파악
        pass
    
    def process_message(self, message):
        # 메시지 처리 및 응답 생성
        pass
```

## 🎨 프론트엔드 가이드

### HTML 구조 이해

#### 1. 메인 페이지 (index.html)
```html
<!-- 헤더 섹션 -->
<header class="header">
    <div class="logo">
        <i class="fas fa-utensils"></i>
        <h1>한국 음식 레시피 도우미</h1>
    </div>
</header>

<!-- 채팅 인터페이스 -->
<div class="chat-container">
    <div class="chat-messages" id="chatMessages">
        <!-- 메시지들이 여기에 표시됨 -->
    </div>
    <div class="chat-input-container">
        <input type="text" id="userInput" />
        <button id="sendBtn">전송</button>
    </div>
</div>
```

#### 2. CSS 스타일링
```css
/* 한국어 폰트 설정 */
body {
    font-family: 'Noto Sans KR', sans-serif;
}

/* 반응형 디자인 */
@media (max-width: 768px) {
    .main-content {
        grid-template-columns: 1fr;
    }
}
```

#### 3. JavaScript 기능
```javascript
// 메시지 전송
async function sendMessage() {
    const message = userInput.value;
    const response = await fetch('/chat', {
        method: 'POST',
        body: `message=${encodeURIComponent(message)}`
    });
    const data = await response.json();
    addMessage(data.response, true);
}
```

### 프론트엔드 개발 팁

#### 1. 반응형 디자인
- 모바일 우선 접근법 사용
- CSS Grid와 Flexbox 활용
- 미디어 쿼리로 화면 크기별 대응

#### 2. 사용자 경험 (UX)
- 로딩 상태 표시
- 에러 메시지 처리
- 키보드 단축키 지원

#### 3. 접근성 (Accessibility)
- ARIA 라벨 사용
- 키보드 네비게이션 지원
- 색상 대비 고려

## 🔧 백엔드 가이드

### Flask 애플리케이션 구조

#### 1. 애플리케이션 팩토리 패턴
```python
# app/__init__.py
def create_app():
    app = Flask(__name__)
    
    # 블루프린트 등록
    from app.routes.chatbot import chatbot_bp
    app.register_blueprint(chatbot_bp)
    
    return app
```

#### 2. 라우팅과 뷰 함수
```python
# app/routes/chatbot.py
@chatbot_bp.route('/')
def index():
    return render_template('index.html')

@chatbot_bp.route('/chat', methods=['POST'])
def chat():
    # POST 요청 처리
    pass
```

#### 3. 서비스 레이어
```python
# app/services/chatbot_service.py
class KoreanFoodChatbot:
    def __init__(self):
        self.recipes_df = load_recipes()
    
    def process_message(self, message):
        intent = self.understand_intent(message)
        return self.generate_response(intent, message)
```

### 데이터베이스 대신 CSV 사용

#### 1. 데이터 로딩
```python
# app/utils/recipe_loader.py
def load_recipes(csv_path=None):
    try:
        df = pd.read_csv(csv_path, encoding="utf-8")
    except UnicodeDecodeError:
        df = pd.read_csv(csv_path, encoding="cp949")
    return df
```

#### 2. 데이터 검색
```python
def find_recipes_by_food_name(food_name, df):
    return df[df["CKG_NM"].str.contains(food_name, case=False, na=False)]
```

### 한국어 처리

#### 1. 인코딩 처리
```python
# 여러 인코딩 시도
encodings = ['utf-8', 'cp949', 'euc-kr']
for encoding in encodings:
    try:
        df = pd.read_csv(file, encoding=encoding)
        break
    except UnicodeDecodeError:
        continue
```

#### 2. 의도 파악
```python
def understand_intent(self, message):
    message = message.lower().strip()
    
    # 키워드 기반 의도 파악
    if any(keyword in message for keyword in ['레시피', '조리법']):
        return {'intent': 'recipe_search', 'confidence': 0.8}
    
    return {'intent': 'general', 'confidence': 0.3}
```

## 📊 데이터 구조

### CSV 파일 구조

#### recipe_data_sample.csv
```csv
CKG_NM,IRDNT_NM,COOKING_MTH,CKG_DC,DIFFICULTY,COOKING_TIME,SERVINGS,CALORIES,CATEGORY
김치찌개,김치,양파,돼지고기,김치찌개 만드는 방법,중급,30분,2인분,300kcal,찌개
불고기,소고기,양파,당근,불고기 만드는 방법,초급,20분,2인분,400kcal,구이
```

### 데이터 필드 설명

| 필드명 | 설명 | 예시 |
|--------|------|------|
| `CKG_NM` | 요리 이름 | 김치찌개 |
| `IRDNT_NM` | 재료 목록 | 김치, 양파, 돼지고기 |
| `COOKING_MTH` | 조리법 | 김치찌개 만드는 방법 |
| `CKG_DC` | 요리 설명 | 매콤한 김치찌개 |
| `DIFFICULTY` | 난이도 | 초급, 중급, 고급 |
| `COOKING_TIME` | 조리시간 | 30분 |
| `SERVINGS` | 인분 | 2인분 |
| `CALORIES` | 칼로리 | 300kcal |
| `CATEGORY` | 카테고리 | 찌개, 구이, 국 |

## 🔍 API 문서

### 채팅 API

#### POST /chat
챗봇과 대화하기

**요청:**
```json
{
  "message": "김치찌개 레시피 알려줘"
}
```

**응답:**
```json
{
  "response": "🍽️ 김치찌개\n\n📝 설명: 매콤한 김치찌개\n🥬 재료: 김치, 양파, 돼지고기\n👨‍🍳 조리법: 김치찌개 만드는 방법"
}
```

### 이미지 업로드 API

#### POST /api/image_upload
음식 사진으로 레시피 찾기

**요청:**
```form-data
{
  "foodImage": "image_file"
}
```

**응답:**
```json
{
  "recipe": {
    "name": "김치찌개",
    "ingredients": ["김치", "양파", "돼지고기"],
    "cooking_method": "김치찌개 만드는 방법"
  }
}
```

## 🧪 테스트

### 자동 테스트 실행

```bash
# 챗봇 기능 테스트
python test_chatbot.py
```

### 수동 테스트

#### 1. 기본 기능 테스트
- 웹 브라우저에서 `http://localhost:5000` 접속
- "안녕하세요" 입력
- "김치찌개 레시피 알려줘" 입력
- "도움말" 입력

#### 2. 이미지 업로드 테스트
- 음식 사진 업로드
- 드래그 앤 드롭 기능 테스트

#### 3. 반응형 디자인 테스트
- 브라우저 크기 조절
- 모바일 시뮬레이션

### 테스트 케이스

```python
# test_chatbot.py
test_messages = [
    "안녕하세요",           # 인사
    "김치찌개 레시피 알려줘", # 레시피 검색
    "불고기 만드는법",       # 조리법 검색
    "인기 한국 음식",        # 인기 음식
    "국 종류",              # 카테고리 검색
    "도움말",               # 도움말
    "감사합니다",           # 인사
    "없는음식 레시피"        # 오류 처리
]
```

## 🐛 문제 해결

### 자주 발생하는 문제들

#### 1. Python 패키지 설치 오류
```bash
# 가상환경이 활성화되어 있는지 확인
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# pip 업그레이드
pip install --upgrade pip

# 패키지 재설치
pip install -r requirements.txt
```

#### 2. 한국어 인코딩 문제
```python
# 여러 인코딩 시도
try:
    df = pd.read_csv(file, encoding="utf-8")
except UnicodeDecodeError:
    try:
        df = pd.read_csv(file, encoding="cp949")
    except UnicodeDecodeError:
        df = pd.read_csv(file, encoding="euc-kr")
```

#### 3. Konlpy 설치 문제 (Windows)
```bash
# Java 설치 필요
# https://www.oracle.com/java/technologies/downloads/

# Java 환경변수 설정
set JAVA_HOME=C:\Program Files\Java\jdk-11.0.x
```

#### 4. 포트 충돌 문제
```bash
# 다른 포트 사용
export PORT=5001  # macOS/Linux
set PORT=5001     # Windows

python main.py
```

#### 5. 데이터 파일 없음
```bash
# 데이터 파일 확인
ls data/
# 또는
dir data

# 샘플 데이터 생성 (필요시)
echo "CKG_NM,IRDNT_NM,COOKING_MTH" > data/recipe_data_sample.csv
echo "김치찌개,김치,양파,돼지고기,김치찌개 만드는 방법" >> data/recipe_data_sample.csv
```

### 디버깅 팁

#### 1. Flask 디버그 모드
```python
# main.py
app.run(debug=True)  # 개발 시에만 사용
```

#### 2. 로그 확인
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

#### 3. 브라우저 개발자 도구
- F12 키로 개발자 도구 열기
- Console 탭에서 JavaScript 오류 확인
- Network 탭에서 API 요청/응답 확인

## 🤝 기여하기

### 개발 환경 설정

1. **Fork the repository**
2. **Create your feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### 코딩 스타일 가이드

#### Python
- PEP 8 스타일 가이드 준수
- 함수와 클래스에 docstring 작성
- 변수명은 snake_case 사용

#### JavaScript
- ES6+ 문법 사용
- 함수명은 camelCase 사용
- 주석은 한국어로 작성

#### HTML/CSS
- 시맨틱 HTML 사용
- CSS 클래스명은 kebab-case 사용
- 반응형 디자인 고려

### 새로운 기능 추가

#### 1. 새로운 API 엔드포인트 추가
```python
# app/routes/chatbot.py
@chatbot_bp.route('/api/recipes', methods=['GET'])
def get_recipes():
    # 새로운 API 로직
    pass
```

#### 2. 새로운 서비스 추가
```python
# app/services/new_service.py
class NewService:
    def process_data(self, data):
        # 새로운 비즈니스 로직
        pass
```

#### 3. 새로운 템플릿 추가
```html
<!-- app/templates/new_page.html -->
<!DOCTYPE html>
<html>
<head>
    <title>새로운 페이지</title>
</head>
<body>
    <!-- 새로운 페이지 내용 -->
</body>
</html>
```

## 📝 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 `LICENSE` 파일을 참조하세요.

## 🙏 감사의 말

- 한국 전통 음식 레시피 데이터 제공자
- Flask 커뮤니티
- 한국어 자연어 처리 연구자들
- 오픈소스 프로젝트 기여자들

## 📞 연락처

프로젝트에 대한 질문이나 제안사항이 있으시면 이슈를 등록해주세요.

- **GitHub Issues**: [이슈 등록](https://github.com/yourusername/kfoodbot/issues)
- **Email**: your-email@example.com
- **Discord**: [커뮤니티 참여](https://discord.gg/your-server)

---

## 🎯 학습 목표

이 프로젝트를 통해 배울 수 있는 것들:

### 백엔드 개발
- ✅ Flask 웹 프레임워크 사용법
- ✅ RESTful API 설계
- ✅ 한국어 텍스트 처리
- ✅ CSV 데이터 처리
- ✅ 에러 핸들링

### 프론트엔드 개발
- ✅ HTML5/CSS3 웹 디자인
- ✅ JavaScript 비동기 처리
- ✅ 반응형 웹 디자인
- ✅ 사용자 경험 (UX) 설계

### AI/ML 기초
- ✅ 자연어 처리 (NLP)
- ✅ 의도 분류 (Intent Classification)
- ✅ 키워드 기반 매칭

### 개발 도구
- ✅ Git 버전 관리
- ✅ 가상환경 관리
- ✅ 패키지 의존성 관리
- ✅ 테스트 작성

---

**맛있는 한국 요리로 여러분의 식탁을 풍성하게 만들어보세요! 🍜**

> 💡 **팁**: 이 프로젝트는 학습 목적으로 만들어졌습니다. 실제 서비스에 사용하려면 보안, 성능, 확장성 등을 추가로 고려해야 합니다.
