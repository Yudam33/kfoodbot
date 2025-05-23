from app.services.image_recognition import predict_food_name
from app.utils.recipe_loader import load_recipes

# 미리 레시피 데이터를 한 번만 로드해두는 게 효율적입니다.
recipes = load_recipes()

def get_recipe_by_image(image_path):
    # 1. 이미지에서 음식 이름 예측
    food_name = predict_food_name(image_path)
    if not food_name:
        return None

    # 2. 예측한 음식 이름으로 레시피 찾기
    recipe = recipes.get(food_name)
    return recipe
