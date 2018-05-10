from django.urls import path
from coin import views
from django.conf.urls import url
urlpatterns = [
    path('',views.index, name='index'),
    path('CoinCap',views.coinDetail,name='coinDetail'),
    path('MoneyEXC',views.moneyEXC,name='moneyEXC'),
    path('MoneyEXC/excGraph',views.excGraph,name='excGraph'),
    url(r'^graph/(?P<coin_id>[A-Za-z0-9]+)$',views.graph, name='graphDetail'),
]
