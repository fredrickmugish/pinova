from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html')
def about_page(request):
    return render(request, 'about.html')
def services_page(request):
    return render(request, 'services.html')
def work_page(request):
    return render(request, 'work.html')
def contact_page(request):
    return render(request, 'contact.html')


