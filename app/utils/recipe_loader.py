import os
import pandas as pd

def load_recipes(csv_path=None):
    if csv_path is None:
        csv_path = os.path.join("data", "recipe_data_sample.csv")

    df = pd.read_csv(csv_path, encoding="utf-8")
    df = df.dropna(subset=["CKG_NM"])  # 음식명 없는 행 제거
    df["CKG_NM"] = df["CKG_NM"].str.strip()  # 공백 제거
    return df

def find_recipes_by_food_name(food_name, df):
    return df[df["CKG_NM"].str.contains(food_name, case=False, na=False)]
