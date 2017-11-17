from django.shortcuts import render

# Create your views here.
def index(request):
    title='Beautiful'

    return render(request,'all-temp/index.html',{"title":title})