from django.shortcuts import render

# Create your views here.
from django.http import HTTPResponse
def hai(request):
    return HTTPResponse('this is our first FBV')
    