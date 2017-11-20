from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import Photos,Editor,tags,Photos_two,Photos_three,NewsLetterRecipients
from .forms import NewsLetterForm
from .email import send_welcome_email

# Create your views here.
def index(request):
    title='Beautiful'

    tag=tags.objects.all()
    photos=Photos.objects.all()
    div_two=Photos_two.objects.all()
    div_three=Photos_three.objects.all()
    
    if request.method =='POST':
        form =NewsLetterForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['your_name']
            email=form.cleaned_data['email']

            recipient=NewsLetterRecipients(name=name,email=email)
            recipient.save()
        
            send_welcome_email(name,email)

            HttpResponseRedirect('index')
    else:
        form=NewsLetterForm()

    return render(request,'all-temp/index.html',{"tag":tag,"photos":photos,"div_two":div_two,"div_three":div_three,"letterForm":form})

def tags_page(request,tags_id):

    try:
        tagz=tags.objects.all()
        tag=tags.objects.filter(id=tags_id)
        print(tag)

    except DoesNotExist:
        return Http404()

    return render(request,"all-temp/tags.html",{"tag":tag,"tagz":tagz})

def search_results(request):
    
    if 'title' in request.GET and request.GET["title"]:
        print("hello world")
        search_term = request.GET.get("title")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-temp/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-temp/search.html',{"message":message})

def new_photos(request):

    new_one=Photos.objects.all().order_by('-pub_date')
    new_two=Photos_two.objects.all().order_by('-pub_date')
    new_three=Photos_three.objects.all().order_by('-pub_date')
    tag=tags.objects.all()

    return render(request,'all-temp/new.html',{"new_one":new_one,"new_two":new_two,"new_three":new_three,"tag":tag})
