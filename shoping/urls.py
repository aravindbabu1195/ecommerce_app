from django.urls import path
from . import views

app_name = 'shoping'
urlpatterns = [

    path('', views.Allprocat, name='allprocat'),
    path('<slug:c_slug>/', views.Allprocat, name='pro_by_cat'),
    path('<slug:c_slug>/<slug:product_slug>/', views.Prodetail, name='procatdetail')
]
