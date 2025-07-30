import os
import pandas as pd
import re
from typing import List, Dict, Optional

def load_recipes(csv_path=None):
    """Load Korean recipe data with proper Korean text encoding"""
    if csv_path is None:
        csv_path = os.path.join("data", "recipe_data_sample.csv")

    try:
        # Try UTF-8 first
        df = pd.read_csv(csv_path, encoding="utf-8")
    except UnicodeDecodeError:
        try:
            # Try CP949 (Korean encoding)
            df = pd.read_csv(csv_path, encoding="cp949")
        except UnicodeDecodeError:
            # Try EUC-KR
            df = pd.read_csv(csv_path, encoding="euc-kr")
    
    # Clean the data
    df = df.dropna(subset=["CKG_NM"])  # 음식명 없는 행 제거
    df["CKG_NM"] = df["CKG_NM"].str.strip()  # 공백 제거
    
    # Remove duplicates based on recipe name
    df = df.drop_duplicates(subset=["CKG_NM"])
    
    return df

def find_recipes_by_food_name(food_name: str, df: pd.DataFrame) -> pd.DataFrame:
    """Find recipes by Korean food name with fuzzy matching"""
    if not food_name:
        return pd.DataFrame()
    
    # Clean the search term
    food_name = food_name.strip()
    
    # Try exact match first
    exact_matches = df[df["CKG_NM"].str.contains(food_name, case=False, na=False)]
    
    if len(exact_matches) > 0:
        return exact_matches
    
    # Try partial matches
    partial_matches = df[df["CKG_NM"].str.contains(food_name, case=False, na=False)]
    
    return partial_matches

def get_recipe_details(recipe_name: str, df: pd.DataFrame) -> Optional[Dict]:
    """Get detailed recipe information"""
    recipe = df[df["CKG_NM"] == recipe_name]
    
    if recipe.empty:
        return None
    
    recipe_row = recipe.iloc[0]
    
    return {
        "name": recipe_row.get("CKG_NM", ""),
        "ingredients": recipe_row.get("IRDNT_NM", ""),
        "cooking_method": recipe_row.get("COOKING_MTH", ""),
        "description": recipe_row.get("CKG_DC", ""),
        "difficulty": recipe_row.get("DIFFICULTY", ""),
        "cooking_time": recipe_row.get("COOKING_TIME", ""),
        "servings": recipe_row.get("SERVINGS", ""),
        "calories": recipe_row.get("CALORIES", ""),
        "category": recipe_row.get("CATEGORY", "")
    }

def search_recipes_by_ingredients(ingredients: List[str], df: pd.DataFrame) -> pd.DataFrame:
    """Search recipes by ingredients"""
    if not ingredients:
        return pd.DataFrame()
    
    matching_recipes = []
    
    for ingredient in ingredients:
        # Search for recipes containing this ingredient
        matches = df[df["IRDNT_NM"].str.contains(ingredient, case=False, na=False)]
        matching_recipes.append(matches)
    
    if matching_recipes:
        return pd.concat(matching_recipes).drop_duplicates()
    
    return pd.DataFrame()

def get_popular_recipes(df: pd.DataFrame, limit: int = 10) -> pd.DataFrame:
    """Get popular Korean recipes (placeholder - could be based on views/ratings)"""
    # For now, return first N recipes
    return df.head(limit)

def get_recipes_by_category(category: str, df: pd.DataFrame) -> pd.DataFrame:
    """Get recipes by category"""
    if not category:
        return pd.DataFrame()
    
    return df[df["CATEGORY"].str.contains(category, case=False, na=False)]

def format_recipe_for_chat(recipe: Dict) -> str:
    """Format recipe information for chatbot response"""
    if not recipe:
        return "죄송합니다. 해당 레시피를 찾을 수 없습니다."
    
    response = f"🍽️ **{recipe['name']}**\n\n"
    
    if recipe.get('description'):
        response += f"📝 설명: {recipe['description']}\n\n"
    
    if recipe.get('ingredients'):
        response += f"🥬 재료:\n{recipe['ingredients']}\n\n"
    
    if recipe.get('cooking_method'):
        response += f"👨‍🍳 조리법:\n{recipe['cooking_method']}\n\n"
    
    if recipe.get('cooking_time'):
        response += f"⏰ 조리시간: {recipe['cooking_time']}\n"
    
    if recipe.get('difficulty'):
        response += f"📊 난이도: {recipe['difficulty']}\n"
    
    if recipe.get('servings'):
        response += f"👥 인분: {recipe['servings']}\n"
    
    return response
