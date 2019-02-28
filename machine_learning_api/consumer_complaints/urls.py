from django.urls import path
from consumer_complaints import views

urlpatterns = [
    path('predict/', views.predict),
]