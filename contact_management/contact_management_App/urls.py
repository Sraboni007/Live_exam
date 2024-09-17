from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('home/', views.home, name='home'),
    path('add/', views.add_contact, name='add_contact'),
    path('contact/<int:contact_id>/', views.contact_detail, name='contact_detail'),
    path('contact/<int:contact_id>/edit/', views.edit_contact, name='edit_contact'),
    path('contact/<int:contact_id>/delete/', views.delete_contact, name='delete_contact'),
    path('search/', views.search_contacts, name='search_contacts'),
]
