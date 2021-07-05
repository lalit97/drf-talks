from polls.models import Question
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    extra_field = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ("question_text", "extra_field")

    def get_extra_field(self, obj):
        return "extra information"
