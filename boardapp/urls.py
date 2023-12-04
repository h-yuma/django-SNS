from django.contrib import admin
from django.urls import path
from .views import signupfunc, loginfunc, listfunc, logoutfunc, detailfunc, goodfunc, readfunc, BoardCreate, userfunc, deletecheckfunc, deletefunc

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login', loginfunc, name='login'),
    path('list/', listfunc, name='list'),
    path('logout/', logoutfunc, name='logout'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('good/<int:pk>', goodfunc, name='good'),
    path('read/<int:pk>', readfunc, name='read'),
    path('create/', BoardCreate.as_view(), name='create'),
    path('user/<str:username>', userfunc, name='user'),
    path('deletecheck/<int:pk>', deletecheckfunc, name='deletecheck'),
    path('delete/<int:pk>', deletefunc, name='delete')
    
]