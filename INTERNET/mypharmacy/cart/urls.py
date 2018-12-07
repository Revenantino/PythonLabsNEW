from django.urls import path
from . import views

urlpatterns = [
    path('remove/<int:medicine_id>', views.CartRemove, name='CartRemove'),
    path('add/<int:medicine_id>', views.CartAdd, name='CartAdd'),
    path('', views.CartDetail, name='CartDetail'),
]