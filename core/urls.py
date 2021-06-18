from django.urls import path
from . import views

urlpatterns = [
    # path('signup/', SignUpView.as_view(), name='signup'),
    # path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('home/', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('', views.todoPage, name="todopage"),
    path('addItem/', views.addItem, name="addItem"),
    path('deleteItem/', views.deleteItem, name="deleteItem"),
    path('logout_view/', views.logout_view, name="logout_view"),
]
