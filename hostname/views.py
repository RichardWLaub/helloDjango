from django.shortcuts import render
from django.http import HttpResponse
import socket

def index(request):
    return HttpResponse("Hello from {}".format(socket.gethostname()))
