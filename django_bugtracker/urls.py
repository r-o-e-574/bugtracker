"""django_bugtracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bugtracker import views



urlpatterns = [
    path('', views.index_view, name="homepage"),
    path('ticket/<int:ticket_id>/edit/', views.edit_ticket, name="edit_ticket"),
    path('ticket/<int:ticket_id>/', views.ticket_detail, name="ticket_view"),
    path('user/<int:user_id>/', views.user_detail, name="user_view"),
    path('addticket/', views.add_ticket, name="addticket"),
    path('inprogress/<int:ticket_id>/', views.ticket_inprogress, name="inprogress"),
    path('completed/<int:ticket_id>/', views.ticket_completed, name="completed"), 
    path('invalid/<int:ticket_id>/', views.ticket_invalid, name="invalid"),      
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('admin/', admin.site.urls),
]
