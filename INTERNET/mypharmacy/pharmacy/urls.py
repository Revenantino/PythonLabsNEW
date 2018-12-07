from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'pharmacy'
urlpatterns = [
    path('', views.medicines_list, name='medicines_list'),
    path('<int:medicine_id>/', views.detail, name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)