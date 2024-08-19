import pandas as pd

data = pd.read_csv('food_ingredients_and_allergens.csv')
print(data)

kolonlar = data.columns.tolist()
print(kolonlar)