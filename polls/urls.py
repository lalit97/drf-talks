from django.urls import path, include
from polls import views


urlpatterns = [
    path("questions/", views.question_list_view),
    path("api/v1/questions/", views.question_list_api),
    path("api/v2/questions/", views.QuestionListApi.as_view()),
    path("api/v3/questions/", views.QuestionListAdvancedApi.as_view()),
    path("api/v4/questions/", views.QuestionListSuperAdvancedApi.as_view()),
]
