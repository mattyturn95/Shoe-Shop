from django.shortcuts import render

# Create your views here.


def index(request):
    """A view That Displays The Index Page"""

    return render(request, 'index.html')
