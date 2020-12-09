from django.shortcuts import render,redirect

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def home(request):
    return render(request, 'all-capstone/home.html')

def about(request):
    return render(request, 'all-capstone/about.html')

def service(request):
    return render(request, 'all-capstone/service.html')

def recent(request):
    return render(request, 'all-capstone/recent-works.html')

def contacts(request):
    return render(request, 'all-capstone/contacts.html')

def shop(request):
    context = {}
    return render(request, 'all-capstone/shop.html')

