from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('lk', views.lk, name = 'lk'),
    path('logg', views.logg, name = 'logg'),
    path('loggout', views.loggout, name = 'loggout'),
    path('grath/<sensid>', views.grath, name = 'grath'),
    path('timech/<sensid>', views.timech, name = 'timech'),
    path('grathtime/<sensid>', views.grathtime, name = 'grathtime'),
    path('send', views.send, name = 'send'),
]
