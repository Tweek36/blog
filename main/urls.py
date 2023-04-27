from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('feedback', views.feedback, name='feedback'),
    path('useful_resources', views.useful_resources, name='useful_resources'),
    path('blog', views.blog, name='blog'),
    path('add_blog', views.add_blog, name='add_blog'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
]