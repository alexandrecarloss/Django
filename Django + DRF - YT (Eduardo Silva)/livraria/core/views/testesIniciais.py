from django.http import HttpResponse, JsonResponse

def teste(request):
    return HttpResponse('Testando API REST com Django e Django REST Framework')