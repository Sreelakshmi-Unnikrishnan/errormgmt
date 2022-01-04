from django.shortcuts import render

# Create your views here.

def handler404(request, exception):
    return render(request, 'err/404.html', status=404)