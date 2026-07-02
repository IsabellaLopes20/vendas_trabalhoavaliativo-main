from django.shortcuts import render

# Create yfrom django.shortcuts import render

def index(request):
    return render(request, 'index.html')
