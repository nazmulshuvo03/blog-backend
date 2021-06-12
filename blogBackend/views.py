from django.http import HttpResponse


def index(request):
    return HttpResponse("You've reached Pvot blog backend")
