products = {
    "Ноутбук": {"price": 50000, "sold": 15},
    "Мышь": {"price": 1000, "sold": 45},
    "Клавиатура": {"price": 2500, "sold": 30},
    "Монитор": {"price": 30000, "sold": 8}
}

# 1. Самый продаваемый товар (максимум sold)
best_seller = None
max_sold = 0
for name, info in products.items():
    if info["sold"] > max_sold:
        max_sold = info["sold"]
        best_seller = name
print("Самый продаваемый товар:", best_seller)

# 2. Общая выручка (price * sold)
total_revenue = 0
for name, info in products.items():
    total_revenue += info["price"] * info["sold"]
print("Общая выручка:", total_revenue)

# 3. Товар с наибольшей выручкой
best_revenue_product = None
max_revenue = 0
for name, info in products.items():
    revenue = info["price"] * info["sold"]
    if revenue > max_revenue:
        max_revenue = revenue
        best_revenue_product = name
print("Товар с наибольшей выручкой:", best_revenue_product)