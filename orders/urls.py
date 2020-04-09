from django.urls import path

from . import views

app_name = "orders"

urlpatterns = [
    path("", views.index, name="index"),
    path("regularpizza/", views.menu0, name="menu0"),
    path("sicilianpizza/", views.menu1, name="menu1"),
    path("sub/", views.menu2, name="menu2"),
    path("pasta", views.menu3, name="menu3"),
    path("salad", views.menu4, name="menu4"),
    path("dinner_platter", views.menu5, name="menu5"),
    path("addToCart", views.addToCart, name="addToCart"),
    path("cart", views.cart, name="cart"),
    path("thankYou", views.thankYou, name="thankYou")
]
