from django.views.generic import ListView
from django.shortcuts import render


def index(request):
    return render(
        request=request,
        template_name='index.html'
    )