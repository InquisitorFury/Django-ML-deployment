from django.shortcuts import render

# Create your views here.
def predictor(request):
    return render(request, 'main.html')