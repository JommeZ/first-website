from django.http import HttpResponse

def index(request):
    return HttpResponse(" Hello, you're in the app bla bla")