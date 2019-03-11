from rest_framework import serializers
from question_answer.models import QuestionAnswer
import string

def get_questions_with_answers(request):
    request_as_string=request.decode('utf8')
    request_no_punctuation = remove_punctuation(request_as_string)
    request_words = request_no_punctuation.split()
    questions_with_answers = QuestionAnswer.objects.none()
    for word in request_words:
        questions_with_word = QuestionAnswer.objects.filter(keywords__icontains=word)
        questions_with_answers = questions_with_answers | questions_with_word
    return questions_with_answers

def remove_punctuation(str):
    exclude = set(string.punctuation)
    string_no_punct = ''.join(ch for ch in str if ch not in exclude)
    return string_no_punct