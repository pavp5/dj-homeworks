from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'cocktail': {
        'пиво Жигулевское, г': 100,
        'шампунь Садко - богатый гость,': 30,
        'резоль для очистки волос от перхоти, г': 70,
        'средство от потливости ног, г': 30,
        'дезинсектакль для уничтожения мелких насекомых, г': 20,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

# Возвращает список ингредиентов и их количество на определенное количество блюд
def calc(request, name):
    count = int(request.GET.get('servings', 1))
    context = {}
    recipe = DATA.get(name)
    if not recipe is None:
        context['recipe'] = recipe.copy()
        for ingredient, amount in context['recipe'].items():
            context['recipe'][ingredient] = count * amount
    return render(request, 'calculator/index.html', context)




