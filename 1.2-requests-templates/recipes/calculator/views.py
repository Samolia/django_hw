from django.shortcuts import render, reverse


DATA = {
    'omelet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 100,
        'сыр, г': 50,
    },
    'sandwich': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'salad': {
        'помидор, шт': 1,
        'огурец, шт': 2,
        'лук, шт': 0.5,
        'масло подсолнечное, мл': 10,
    },
}


MSG = 'Блюдо не найдено!'


def home_view(request):
    template_name = 'calculator/index.html'
    context = {
        'dishes': DATA.keys
    }
    return render(request, template_name, context)


def recipes_view(request, dish_name):
    template_name = 'calculator/recipes.html'
    template_error = 'calculator/errors.html'
    quantity_servings = request.GET.get('servings')
    recipe = DATA.get(dish_name, MSG)
    if dish_name not in DATA:
        return render(request, template_error)
    else:
        if quantity_servings:
            ingredient = {key: value * int(quantity_servings) for key, value in recipe.items()}
        else:
            ingredient = {key: value for key, value in recipe.items()}
    context = {'recipe': ingredient}
    return render(request, template_name, context)
