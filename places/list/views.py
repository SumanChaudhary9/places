from django.shortcuts import render
import os
import json
# Create your views here.
file_path = os.path.join(os.path.dirname(__file__),'places.json')

with open(file_path,"r") as file:
    data = json.load(file)
def listing(request):
    print("data",data)
    return render(request,"list.html",{"data":data})
