from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
def about(request):
    return render(request,'aboutus.html')
def gallery(request):
    return render(request, 'gallery.html')