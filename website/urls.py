from django.urls import path
from django.conf.urls.static import static
from .import views
from django.conf import settings

urlpatterns = [

    path('', views.home, name="home"),
    path('about/', views.about_page, name="about"),
    path('services/', views.services_page, name="services"),
    path('work/', views.work_page, name="work"),
    path('contact/', views.contact_page, name="contact"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

