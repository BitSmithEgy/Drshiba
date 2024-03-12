from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
   
    path('d2', views.d2, name='d2'),
    
    path('d1', views.d1, name='d1'),
    path('q1', views.q1, name='q1'),
    
    
    path('q2', views.q1, name='q2'),
    
    #This is the first condition in the first scenario
    
    
    path('d11', views.d11, name='d11'),
    path('q11', views.q11, name='q11'),
    
    
    path('d111', views.d111, name='d111'),
    path('d112', views.d112, name='d112'),
    path('d113', views.d113, name='d113'),
    path('q112', views.q112, name='q112'),
    path('q113', views.q113, name='q113'),
    
    path('d1111', views.d1111, name='d1111'),
    path('d1112', views.d1112, name='d1112'),
    path('d1113', views.d1113, name='d1113'),
    path('q1111', views.q1111, name='q1111'),
    path('q1112', views.q1112, name='q1112'),
    path('q1113', views.q1113, name='q1113'),
    
    #This is the second condition in the first scenario
    path('d12', views.d12, name='d12'),
    path('q12', views.q12, name='q12'),
    
    path('d121', views.d121, name='d121'),
    path('q121', views.q121, name='q121'),
    
    
    path('d122', views.d122, name='d122'),
    path('q122', views.q122, name='q122'),
    
    path('d123', views.d123, name='d123'),
    path('q123', views.q123, name='q123'),
    
    path('d1221', views.d1221, name='d1221'),
    path('q1221', views.q1221, name='q1221'),
    
    path('d1222', views.d1222, name='d1222'),
    path('q1222', views.q1222, name='q1222'),
    
    #This is the third condition of the first scenario
    path('d13', views.d13, name='d13'),
    path('q13', views.q13, name='q13'),
    
    path('d131', views.d131, name='d131'),
    path('q131', views.q131, name='q131'),
    
    path('d132', views.d132, name='d132'),
    path('q132', views.q132, name='q132'),
    
    path('d133', views.d133, name='d133'),
    path('q133', views.q133, name='q133'),
    
    #User auth system
    path('login/', views.login_user, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register, name="register"),
    
]