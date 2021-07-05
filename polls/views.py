import json

from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from polls.models import Question
from polls.serializers import QuestionSerializer


def question_list_view(request):
    questions = Question.objects.all()
    context = {"questions": questions}
    return render(request, "polls/question_list.html", context)


def question_list_api(request):
    questions = Question.objects.all()
    questions_list = []
    for item in questions:
        ques = {"question_text": item.question_text}
        questions_list.append(ques)
    questions_in_json = json.dumps(questions_list, indent=2)
    return JsonResponse(questions_in_json, safe=False)


class QuestionListApi(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        questions = Question.objects.all()
        questions_list = []
        for item in questions:
            ques = {"question_text": item.question_text}
            questions_list.append(ques)
        return Response(questions_list, status=status.HTTP_200_OK)


class QuestionListAdvancedApi(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class QuestionListSuperAdvancedApi(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
