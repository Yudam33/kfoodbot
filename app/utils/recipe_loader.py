# app/utils/recipe_loader.py

import csv
import os

def load_recipes(csv_path=None):
    if csv_path is None:
        csv_path = os.path.join("data", "recipe_data.csv")

    recipes = {}
    with open(csv_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row.get("CKG_NM", "").strip()
            if name:
                recipes[name] = {
                    "title": row.get("RCP_TTL", ""),
                    "ingredients": row.get("CKG_MTRL_CN", ""),
                    "portions": row.get("CKG_INBUN_NM", ""),
                    "difficulty": row.get("CKG_DODF_NM", ""),
                    "time": row.get("CKG_TIME_NM", ""),
                    "cook_type": row.get("CKG_MTH_ACTO_NM", "")



    return recipes

def find_recipe_by_food_name(food_name, recipes):
    return recipes.get(food_name)
