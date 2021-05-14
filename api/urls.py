from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.Purchase.as_view(), name='purchase'),
    path('ingredients', views.IngredientApi.as_view(), name='ingredients'),
    path('favorites/', views.Favorites.as_view(), name='favorites'),
    path('favorites/<int:recipe_id>/', views.Favorites.as_view()),
    path('subscriptions/', views.Subscribe.as_view(), name='subscriptions'),
    path('subscriptions/<int:author_id>/', views.Subscribe.as_view()),
    path('purchases/', views.Purchase.as_view(), name='purchases'),
    path('purchases/<int:recipe_id>/', views.Purchase.as_view()),
]

urlpatterns = [
    path('v1/', include(urlpatterns))
]
