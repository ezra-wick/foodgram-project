from django.urls import path
from . import views

urlpatterns = [
    path('', views.Purchase.as_view()),
    path('v1/ingredients', views.IngredientApi.as_view(), name='ingredients'),
    path('v1/favorites/', views.Favorites.as_view()),
    path('v1/favorites/<int:recipe_id>/', views.Favorites.as_view()),
    path('v1/subscriptions/', views.Subscribe.as_view()),
    path('v1/subscriptions/<int:author_id>/', views.Subscribe.as_view()),
    path('v1/purchases/', views.Purchase.as_view()),
    path('v1/purchases/<int:recipe_id>/', views.Purchase.as_view()),
]
