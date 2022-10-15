from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    # path('blogs', views.blogs, name="blogs"),
    path('about', views.about, name="about"),
    path('todo', views.todo, name="todo"),
    path('ventfeels', views.ventfeels, name="ventfeels"),
    path('products3', views.products3, name="products3"),
    path('feedback', views.feedback, name="feedback"),
    path('calmball', views.calmball, name="calmball"),





]