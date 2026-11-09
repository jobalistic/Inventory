from django.shortcuts import render
from invent import views


def index(request):
  context_dict={'boldmessage':"Mango, Apple, Banana, Cashew, Guava, Ginger"}
  return render(request,'invent/index.html',context=context_dict)
# Create your views here.
