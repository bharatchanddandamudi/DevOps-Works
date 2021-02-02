from django.shortcuts import render
from .models import usertype, user 

# Create your views here.
def get(request):
    userdisplay =  user.objects.all()
    utdisplay = usertype.objects.all()
    


