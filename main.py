import pandas as pd


data = pd.read_csv('food_ingredients_and_allergens.csv')
# print(data)

# 1.Öncelikle, veri setinde eksik veya hatalı veri olup olmadığını kontrol edelim ve verinin genel yapısını anlamak.
# Ön İşleme Adımları:
# 1.Eksik Verinin Yönetimi:
#   Prediction sütunundaki eksik değeri ya doldurmak ya da bu satırı veri setinden çıkarmak

# Veri türleri ve eksik verileri kontrol ettik.
# data_info = data.info()

missing_value = data.isnull().sum()
# print(missing_value)

# Eksik veri, veri setinden çıkartıldı.
data_cleaned = data.dropna(subset=['Prediction'])
data_cleaned_info = data_cleaned.info()
print(data_cleaned_info)
def allergen_detection(ingredient):
    # Alerjen içeren ürünleri filtreleyelim
    allergen_products = data_cleaned[data_cleaned['Allergens'].str.contains(ingredient, case=False, na=False)]
    
    # Eğer eşleşen alerjen varsa, listeleyelim
    if not allergen_products.empty:
        return allergen_products[['Food Product', 'Allergens']]
    else:
        return "Bu bileşenle ilgili alerjen bulunamadı."

# Fonksiyonu test edelim
test_ingredient = "chicken"  # Kullanıcıdan alınan bileşen
print(allergen_detection(test_ingredient))