from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('detail/<keyword>=<value>', views.search, name='search'),
    path('search/', views.live_search),
]
