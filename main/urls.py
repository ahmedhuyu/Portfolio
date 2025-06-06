from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import my_works, contact_me

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('my-works/', my_works, name='my_works'),
    path('contact/', contact_me, name='contact_me'),
]