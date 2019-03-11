from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from question_answer.models import QuestionAnswer
from question_answer.serializers import QuestionAnswerSerializer
from question_answer import services
from rest_framework.parsers import BaseParser

class PlainTextParser(BaseParser):
    """
    Plain text parser.
    """
    media_type = 'text/plain'

    def parse(self, stream, media_type=media_type, parser_context=None):
        """
        Simply return a string representing the body of the request.
        """
        return stream.read()

@api_view(['POST'])
@parser_classes((PlainTextParser,))
def question_list(request):
    """
    List questions from database that are in a given category based on keywords in the question from the request.
    """
    questions = services.get_questions_with_answers(request.data)
    serializer = QuestionAnswerSerializer(questions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_question(request):
    """
    Create a question
    """
    serializer = QuestionAnswerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
