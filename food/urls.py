from django.urls import path
from .views import index, home_page, order_page, main_order

urlpatterns = [
    path('', index, name='index'),
    path('home_page/', home_page, name='home_page'),
    path('order_page/', order_page, name='order_page'),
    path('order', main_order, name='order'),
]