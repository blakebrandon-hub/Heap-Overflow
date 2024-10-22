from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from heap import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('question/<int:pk>/', views.question_detail, name='question_detail'),
    path('question/<int:pk>/answer/', views.answer_question, name='answer_question'),
    path('question/ask/', views.ask_question, name='ask_question'),
    path('tags/', views.tag_list, name='tag_list'),
    path('tags/<int:tag_id>/', views.questions_by_tag, name='questions_by_tag'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.custom_logout, name='custom_logout'),
]
