from django.conf.urls import url
from . import views
from django.urls import path
from .views import RegisterAPI, LoginAPI
from knox import views as knox_views


urlpatterns=[
     url(r'^$',LoginAPI.as_view(), name='login'),
     url(r'^api/cards/$', views.CardList.as_view()),
     url(r'api/cards/card-id/(?P<pk>[0-9]+)/$', views.CardDets.as_view()),
     path('api/register/', RegisterAPI.as_view(), name='register'),
     path('api/login/', LoginAPI.as_view(), name='login'),
     path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
]