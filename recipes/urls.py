from django.contrib import admin
from django.urls import path
from calculator.views import recipe, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("<str:name>/", recipe, name="recipe"),
]
