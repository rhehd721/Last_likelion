from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('', views.home, name = 'home'),
    path('', views.intro, name = 'intro'),
    path('About', views.About, name = 'About'),
    path('Skill', views.Skill, name = 'Skill'),
    path('Project', views.Project, name = 'Project'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
