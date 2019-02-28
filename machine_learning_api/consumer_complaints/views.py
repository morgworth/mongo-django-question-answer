from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from consumer_complaints import services


@csrf_exempt
def predict(request):
    if request.method == 'POST':
        complaint_text = request.body.decode("UTF-8")
        return HttpResponse(services.ComplaintClassifierService.make_classification(complaint_text), status=200)
