from django.shortcuts import render
from django.http import HttpResponse
from . models import movieInfo

# Create your views here
def index(request):
    #return HttpResponse("My movie project")
    return render(request, 'blank_layout.html')

def create(request):
    if request.POST:
        title=request.POST.get('title')
        year=request.POST.get('year')
        des=request.POST.get('summary')
        movie_obj=movieInfo(title=title,year=year,desciption=des)
        movie_obj.save()
    return render(request,'create.html') 

def list(request):
    movie_data=movieInfo.objects.all()
    #print(movie_data)
    return render(request,'list.html',{'movies':movie_data}) 

def edit(request):
    return render(request,'edit.html') 
