from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bids/create/', views.BidCreate.as_view(), name='bid_create'),
    path('accounts/signup/', views.signup, name='signup'),

]