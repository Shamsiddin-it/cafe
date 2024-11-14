from django.urls import path
from .views import *

urlpatterns = [
    path("", HomeView.as_view(), name = 'home'),
    path("menu/", MenuView.as_view(), name = 'menu'),
    path("dish_create/", DishCreateView.as_view(), name = 'dish_create'),
    path("dish_list/", DishListView.as_view(), name = 'dish_list'),
    path("dish_detail/<int:pk>/", DishDetailView.as_view(), name = 'dish_detail'),
    path("category_detail/<int:pk>/", CategoryDetailView.as_view(), name = 'category_detail'),
    path("dish_update/<int:pk>/", DishUpdateView.as_view(), name = 'dish_update'),
    path("dish_delete/<int:pk>/", DishDeleteView.as_view(), name = 'dish_delete'),
    path("signup/", register, name = 'signup'),
]
