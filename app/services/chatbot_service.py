# app/services/chatbot_service.py
import re
import random
from typing import List, Dict, Optional
from app.utils.recipe_loader import (
    load_recipes, 
    find_recipes_by_food_name, 
    get_recipe_details,
    search_recipes_by_ingredients,
    get_popular_recipes,
    format_recipe_for_chat
)

# Load recipes once when module is imported
try:
    RECIPES_DF = load_recipes()
except Exception as e:
    print(f"Error loading recipes: {e}")
    RECIPES_DF = None

class KoreanFoodChatbot:
    def __init__(self):
        self.recipes_df = RECIPES_DF
        self.conversation_history = []
        
        # Korean food-related keywords and patterns
        self.food_keywords = {
            'recipe_search': ['레시피', '조리법', '만드는법', '만드는 방법', '어떻게', '방법'],
            'ingredient_search': ['재료', '들어가는', '필요한', '준비물'],
            'popular': ['인기', '추천', '맛있는', '좋은'],
            'category': ['국', '밥', '면', '반찬', '디저트', '음료'],
            'greeting': ['안녕', '하이', 'hello', 'hi'],
            'farewell': ['잘가', '바이', 'bye', 'goodbye', '감사', '고마워'],
            'help': ['도움', 'help', '도와', '어떻게', '사용법']
        }
        
        # Korean food categories
        self.food_categories = {
            '국': ['국', '탕', '찌개', '전골'],
            '밥': ['밥', '비빔밥', '덮밥', '볶음밥'],
            '면': ['면', '국수', '라면', '우동'],
            '반찬': ['반찬', '김치', '나물', '조림'],
            '구이': ['구이', '불고기', '갈비', '삼겹살'],
            '튀김': ['튀김', '전', '부침개'],
            '디저트': ['디저트', '후식', '과자', '빵']
        }

    def understand_intent(self, message: str) -> Dict:
        """Understand user intent from Korean message"""
        message = message.lower().strip()
        
        # Check for greetings
        if any(keyword in message for keyword in self.food_keywords['greeting']):
            return {'intent': 'greeting', 'confidence': 0.9}
        
        # Check for farewells
        if any(keyword in message for keyword in self.food_keywords['farewell']):
            return {'intent': 'farewell', 'confidence': 0.9}
        
        # Check for help requests
        if any(keyword in message for keyword in self.food_keywords['help']):
            return {'intent': 'help', 'confidence': 0.8}
        
        # Check for recipe searches
        if any(keyword in message for keyword in self.food_keywords['recipe_search']):
            return {'intent': 'recipe_search', 'confidence': 0.8}
        
        # Check for ingredient searches
        if any(keyword in message for keyword in self.food_keywords['ingredient_search']):
            return {'intent': 'ingredient_search', 'confidence': 0.7}
        
        # Check for popular recipe requests
        if any(keyword in message for keyword in self.food_keywords['popular']):
            return {'intent': 'popular_recipes', 'confidence': 0.7}
        
        # Check for category searches
        for category, keywords in self.food_categories.items():
            if any(keyword in message for keyword in keywords):
                return {'intent': 'category_search', 'category': category, 'confidence': 0.6}
        
        # Default to general conversation
        return {'intent': 'general', 'confidence': 0.3}

    def extract_food_name(self, message: str) -> Optional[str]:
        """Extract food name from Korean message"""
        # Remove common words that aren't food names
        stop_words = ['레시피', '조리법', '만드는법', '어떻게', '방법', '알려줘', '보여줘', '찾아줘']
        
        for word in stop_words:
            message = message.replace(word, '').strip()
        
        return message if message else None

    def get_greeting_response(self) -> str:
        """Get greeting response"""
        greetings = [
            "안녕하세요! 🍽️ 한국 음식 레시피 도우미입니다. 어떤 음식에 대해 궁금하신가요?",
            "반갑습니다! 👨‍🍳 한국 요리 레시피를 찾아드릴게요. 무엇을 도와드릴까요?",
            "안녕하세요! 🥘 한국 전통 음식부터 현대적인 요리까지 알려드릴 수 있어요. 어떤 음식을 찾고 계신가요?"
        ]
        return random.choice(greetings)

    def get_farewell_response(self) -> str:
        """Get farewell response"""
        farewells = [
            "맛있는 요리 되세요! 👋 다음에 또 찾아주세요!",
            "건강하고 맛있는 식사 하세요! 😊",
            "좋은 하루 보내세요! 🍜 다음에 또 도움이 필요하시면 언제든 말씀해주세요!"
        ]
        return random.choice(farewells)

    def get_help_response(self) -> str:
        """Get help response"""
        return """🔍 **한국 음식 레시피 도우미 사용법**

다음과 같이 질문해주세요:

🍽️ **특정 음식 레시피 찾기**
- "김치찌개 레시피 알려줘"
- "불고기 만드는법"
- "된장찌개 조리법"

🥬 **재료로 레시피 찾기**
- "고구마로 만들 수 있는 음식"
- "닭고기 재료 음식"

📊 **카테고리별 음식**
- "국 종류"
- "반찬 추천"
- "디저트 레시피"

🔥 **인기 음식**
- "인기 한국 음식"
- "추천 레시피"

무엇을 도와드릴까요?"""

    def search_and_format_recipe(self, food_name: str) -> str:
        """Search for recipe and format response"""
        if not self.recipes_df is not None:
            return "죄송합니다. 레시피 데이터를 불러올 수 없습니다."
        
        if not food_name:
            return "어떤 음식의 레시피를 찾고 계신가요?"
        
        # Search for recipes
        matching_recipes = find_recipes_by_food_name(food_name, self.recipes_df)
        
        if matching_recipes.empty:
            return f"죄송합니다. '{food_name}'에 대한 레시피를 찾을 수 없습니다. 다른 음식을 시도해보세요."
        
        # Get the first matching recipe
        recipe_name = matching_recipes.iloc[0]['CKG_NM']
        recipe_details = get_recipe_details(recipe_name, self.recipes_df)
        
        return format_recipe_for_chat(recipe_details)

    def get_popular_recipes_response(self) -> str:
        """Get popular recipes response"""
        if not self.recipes_df is not None:
            return "죄송합니다. 레시피 데이터를 불러올 수 없습니다."
        
        popular_recipes = get_popular_recipes(self.recipes_df, 5)
        
        if popular_recipes.empty:
            return "죄송합니다. 인기 레시피를 불러올 수 없습니다."
        
        response = "🔥 **인기 한국 음식 레시피**\n\n"
        
        for idx, recipe in popular_recipes.iterrows():
            response += f"{idx+1}. {recipe['CKG_NM']}\n"
        
        response += "\n특정 음식의 상세 레시피를 원하시면 음식 이름을 말씀해주세요!"
        
        return response

    def get_category_recipes_response(self, category: str) -> str:
        """Get recipes by category"""
        if not self.recipes_df is not None:
            return "죄송합니다. 레시피 데이터를 불러올 수 없습니다."
        
        category_recipes = self.recipes_df[
            self.recipes_df['CATEGORY'].str.contains(category, case=False, na=False)
        ].head(5)
        
        if category_recipes.empty:
            return f"죄송합니다. '{category}' 카테고리의 레시피를 찾을 수 없습니다."
        
        response = f"🍽️ **{category} 카테고리 레시피**\n\n"
        
        for idx, recipe in category_recipes.iterrows():
            response += f"{idx+1}. {recipe['CKG_NM']}\n"
        
        response += f"\n특정 {category}의 상세 레시피를 원하시면 음식 이름을 말씀해주세요!"
        
        return response

    def get_general_response(self, message: str) -> str:
        """Get general response for unrecognized queries"""
        responses = [
            "죄송합니다. 한국 음식 레시피에 대한 질문을 해주세요. 예: '김치찌개 레시피 알려줘'",
            "한국 음식 레시피를 찾고 계신가요? 어떤 음식을 원하시는지 말씀해주세요!",
            "도움이 필요하시면 '도움말'을 입력해주세요. 한국 음식 레시피를 찾아드릴게요!"
        ]
        return random.choice(responses)

    def process_message(self, message: str) -> str:
        """Process user message and return appropriate response"""
        # Add to conversation history
        self.conversation_history.append({'user': message, 'timestamp': 'now'})
        
        # Understand intent
        intent = self.understand_intent(message)
        
        # Generate response based on intent
        if intent['intent'] == 'greeting':
            return self.get_greeting_response()
        
        elif intent['intent'] == 'farewell':
            return self.get_farewell_response()
        
        elif intent['intent'] == 'help':
            return self.get_help_response()
        
        elif intent['intent'] == 'recipe_search':
            food_name = self.extract_food_name(message)
            return self.search_and_format_recipe(food_name)
        
        elif intent['intent'] == 'popular_recipes':
            return self.get_popular_recipes_response()
        
        elif intent['intent'] == 'category_search':
            category = intent.get('category', '')
            return self.get_category_recipes_response(category)
        
        else:
            # Try to extract food name and search anyway
            food_name = self.extract_food_name(message)
            if food_name:
                return self.search_and_format_recipe(food_name)
            else:
                return self.get_general_response(message)

# Global chatbot instance
chatbot = KoreanFoodChatbot()

def get_recipe_by_image(image_path):
    """Placeholder function for getting a recipe by image"""
    return {"name": "Placeholder Recipe", "description": "This is a placeholder recipe.", "ingredients": [], "steps": []}

def handle_chat_message(message):
    """Handle chatbot messages with Korean text support"""
    return chatbot.process_message(message)
