from pprint import pprint

cook_book = {}
with open('recipes.txt', 'r', encoding='utf-8') as file:
    for k in file:
        name_ingred = k.strip()
        name_count = int(file.readline())
        ingredients = []
        for ind in range(name_count):
            recipie = file.readline().strip().split(' | ')
            ingredient_name, quantity, measure = recipie
            ingredients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        file.readline()
        cook_book[name_ingred] = ingredients

pprint(cook_book)

