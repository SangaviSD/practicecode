from django.urls import path
from . import views

urlpatterns=[
    # path('',views.hello,name='hello'),
    path('',views.input_numbers, name='input'),
    path('calcul/',views.add_numbers, name='calcul'),
] 