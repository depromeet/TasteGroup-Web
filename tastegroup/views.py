from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'tastegroup/index.html')

def list(request):
    return render(request, 'tastegroup/list.html')

def detail(request):
    return render(request, 'tastegroup/detail.html')
