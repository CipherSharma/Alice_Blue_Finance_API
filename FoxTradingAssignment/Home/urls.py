from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.LoginAPI),
    path("order/",views.OrderAPI),
    path("orderBook/",views.GetOrderBookAPI),
   ]