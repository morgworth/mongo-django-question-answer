from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from chatbot import services


@csrf_exempt
def ask(request):
    if request.method == 'POST':
        question = request.body.decode('UTF-8')
        return HttpResponse(services.ChatbotServices.respond(question), status=200)
