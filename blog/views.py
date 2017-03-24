from django.http import JsonResponse


def index(request):
    if request.method == 'GET':
        print request.__dict__
        return JsonResponse({"message": "Hello, world. You're at the aplatform index."})