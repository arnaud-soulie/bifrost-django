from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    """
    Main page
    """
    numbers=range(97,1,-1)
    return render(request,'bifrost_app/index.html',{'numbers':numbers})
