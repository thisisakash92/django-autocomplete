from django.conf.urls import url
from myapp import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^search/', views.my_search_view, name = 'article_detail')
    ]