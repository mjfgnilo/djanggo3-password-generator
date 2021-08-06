from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home (request):
    str = "aaaaaa"
    return render(request, 'generator/home.html')

def password(request):
    data_dict = dict()

    characters = list('abcdefghijklmnopqrstuvwxyz')
    if (request.GET.get('upper_char')):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if (request.GET.get('special_char')):
        characters.extend('!@#$%^&*()_+-=[]{}\|;:,./<>?')
    if (request.GET.get('num')):
        characters.extend('1234567890')

    length = int(request.GET.get('length',10))
    thispassword = ""

    for x in range (length):
        thispassword += random.choice(characters)

    #send password into dict
    data_dict.update({'password': thispassword})

    return render(request, 'generator/password.html', data_dict)

def about(request):
    return render(request, 'generator/about.html')
