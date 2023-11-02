from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def print_hello(request):
    movie_details={'movies':[{'title':'Romanjam','year':'2023','summary':'Horror Movie','success':True},
                   {'title':'Kannu Squad','year':'2023','summary':'Thriller Movie','success':True},
                   {'title':'Guppy','year':'2018','summary':'Drama Movie','success':True},
                   {'title':'Ambili','year':'2019','success':False}
                   ]}
    return render(request,'my_project.html',movie_details)