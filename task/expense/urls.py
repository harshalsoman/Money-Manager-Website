from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.Login),
    path('Home',views.Home),
    path('credit',views.credit),
    path('debit',views.debit),
    path('ctransactions',views.ctransactions),
    path('dtransactions',views.dtransactions),
    path('choose', views.choose),
    path('logout', views.logout),


    path('balance',views.balance)

]