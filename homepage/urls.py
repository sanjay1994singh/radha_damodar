from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('history/', views.history, name='history'),
    path('samadhis/', views.samadhis, name='samadhis'),
    path('biographies/', views.biographies, name='biographies'),
    path('gaushala/', views.gaushala, name='gaushala'),
]
