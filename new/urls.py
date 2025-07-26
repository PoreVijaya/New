from django.urls import path
from .views import Home, About, Contact, A, Img, Login, Logout

urlpatterns = [ 
    path('', Login, name='login'),
    path('home/', Home, name='home'),
    path('logout/', Logout, name='logout'),  
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
    path('A/', A, name='a'),
    path('Img/', Img, name='img'),
    path('Login/', Login, name='login'),
]