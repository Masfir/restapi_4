from django.urls import path
from mypp import views

urlpatterns =[
    
    path('ContactList/', views.ContactList.as_view()),
    path('ContactDetail/<int:pk>/', views.ContactDetail.as_view()),
]