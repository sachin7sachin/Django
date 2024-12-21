from django.shortcuts import render
from django.http import HttpResponse
from .models import ChaiVariety,store
from django.shortcuts import get_object_or_404
from .forms import ChaiVarietyForm

# Create your views here.
# def home(request):
#     return HttpResponse("<h1>Hello! Welcome to Tea Snack</h1>")

def all_chai(request):
    chais = ChaiVariety.objects.all()
    return render(request,'all_chai.html',{"title": "all_chais", "chais":chais})

def chai_details(request,id):
    chai = get_object_or_404(ChaiVariety,pk=id)
    return render(request,"chai_details.html",{"chai":chai})

def chai_store_view(request):
    stores = None
    form = ChaiVarietyForm()
    if request.method == "POST":
        form = ChaiVarietyForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data["chai_variety"]
            stores = store.objects.filter(chai_varieties = chai_variety) 

    return render(request,"chai_store.html", {"form":form, "stores": stores})