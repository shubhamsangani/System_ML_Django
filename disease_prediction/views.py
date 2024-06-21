from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # context = {
    #     'variable':"this is forst variable which is render in the home page."
    # }
    return render(request, 'index.html')
    # return HttpResponse("This is home page")

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def heart(request):
    return render(request, 'heart.html')

def parkinsons(request):
    return render(request, 'parkinsons.html')

def diabetes(request):
    return render(request, 'diabetes.html')