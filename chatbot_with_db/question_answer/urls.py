from django.urls import path
from question_answer import views

urlpatterns = [
    path('addquestion', views.create_question),
	path('ask', views.question_list),
]