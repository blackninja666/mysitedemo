from django.http import HttpResponse


def view_page(request):
    return HttpResponse("Hello World")