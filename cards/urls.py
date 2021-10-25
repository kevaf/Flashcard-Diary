from django.conf.urls import url
from . import views


urlpatterns=[
     url(r'^api/cards/$', views.CardList.as_view())
]