class Product:
    def __init__(self, title, price, calories):
        self.title = title
        self.price = price
        self.calories = calories
        dough_product = Product('Тесто', 200, 20)
        tomato_product = Product('Помидор', 100, 50)
        cheese_product = Product('Сыр', 100, 120)
        sausage_product = Product('Колбаса', 200, 70)
        pizza_product = Product('Пепперони', 600, 260)


class Ingredient:
    def __init__(self, weight):
        self.price = weight
        dough_ingredient = Ingredient(dough_product, 100)
        tomato_ingredient = Ingredient(tomato_product, 100)
        cheese_ingredient = Ingredient(cheese_product, 100)
        sausage_ingredient = Ingredient(sausage_product, 100)
        pizza_ingredient = Ingredient(pizza_product, 400)

class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients
        pizza_pepperoni = Pizza('Пепперони', [dough_ingredient, tomato_ingredient, cheese_ingredient, sausage_ingredient])
        
print('Пепперони', 260, 'kkal', 600, 'руб')

