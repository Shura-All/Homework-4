from django.shortcuts import render
from django.http import HttpResponse as HttpR


def index(request):
    return HttpR('<h1 style="text-align: center; background-color: #FFFF00">Домашка по 4 занятию</h1>')
