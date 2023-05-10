from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse


DATA = {
    "omlet": {
        "яйца, шт": 2,
        "молоко, л": 0.1,
        "соль, ч.л.": 0.5,
    },
    "pasta": {
        "макароны, г": 0.3,
        "сыр, г": 0.05,
    },
    "sandwich": {
        "хлеб, ломтик": 1,
        "колбаса, ломтик": 1,
        "сыр, ломтик": 1,
        "помидор, ломтик": 1,
    },
}


def home(request):
    return HttpResponse(f'Hello! <br> Enter the name of the dish in the address bar.'
                        f'<br> Use the "serving" as get-parameter to set up the number of ingredients.')


def recipe(request, name):
    servings = int(request.GET.get("servings", 1))
    context = {"recipe": "", "pages": {"Главная страница": reverse("home")}}
    if name in DATA:
        context["recipe"] = DATA[name]
        for item in context["recipe"]:
            context["recipe"][item] *= servings

    return render(request, "calculator.html", context)
