from django.urls import path

from django.urls import path
from . import views

app_name = 'infos'
urlpatterns = [
    # ...
    # your other urls
    # ...
    path('add-user', views.add_user, name='add_user'),
    path('users', views.user_list, name='user_list'),
]


'''
urlpatterns = [
    path('', views.index, name='index'),
]
'''
