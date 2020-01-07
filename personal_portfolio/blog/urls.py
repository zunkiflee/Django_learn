from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name="hello"),
	path('blog_index', views.blog_index, name="blog_index"),
	path("<int:pk>/", views.blog_detail, name="blog_detail"),
    path("<category>/", views.blog_category, name="blog_category"),

]