from django.http import HttpResponse,Http404
from django.shortcuts import render,redirect
from .models import Photos,Editor,tags,Photos_two,Photos_three

# Create your views here.
def index(request):
    title='Beautiful'

    tag=tags.objects.all()
    photos=Photos.objects.all()
    div_two=Photos_two.objects.all()
    div_three=Photos_three.objects.all()
    # try:
    #     photo = Photos.objects.get(id = photo_id)
    # except DoesNotExist:
    #     raise Http404()

    return render(request,'all-temp/index.html',{"tag":tag,"photos":photos,"div_two":div_two,"div_three":div_three})

def tags_page(request,tags_id):

    try:
        tagz=tags.objects.all()
        tag=tags.objects.filter(id=tags_id)
        print(tag)

    except DoesNotExist:
        return Http404()

    return render(request,"all-temp/tags.html",{"tag":tag,"tagz":tagz})

def search_results(request):

    if 'photo' in request.GET and request.GET["photo"]:
        search_term=request.GET.get("photo")
        searched_photo=Photos.search_by_title(search_term)
        message=f"{search_term}"
        return render(request,'all-temp/search.html',{"message":message,"photo":searched_photos})
    
    else:
        message='You havent searched for any term'
        return render(request,'all-temp/search.html',{"message":message})