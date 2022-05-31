import re
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from main.models import ToDoList, Item, Klient
from .forms import Rejestracja
# Create your views here.
count = 0

def home(request):
    global count
    count+=1
    return render(request, "main/home.html", {"text": "Siema mordko "+str(count)})

def v1(request, nr):
    list = ToDoList.objects.get(id=nr)
    if request.method == "POST":
        print(request.POST)
        if request.POST.get("save"):
            for item in list.item_set.all():
                if request.POST.get(f"c{item.id}"):
                    item.complete = True
                else:
                    item.complete = False
                item.save()
                if request.POST.get(f"d{item.id}"):
                    item.delete()
        elif request.POST.get("delete"):
            list.item_set.get(id=request.POST.get("delete")[4:]).delete()
        elif request.POST.get("nItem"):
            text = request.POST.get("newItemName")
            if len(text) > 2:
                list.item_set.create(text=text, complete=False)
        return HttpResponseRedirect("/%i" %list.id)
    return render(request, "main/view.html", {"le": list})

def name(response, value):
    return HttpResponse(value)

def siema(response):
    return render(response, "main/base.html", {})

def klientS(request, idK):
    k = Klient.objects.get(id=idK)
    return render(request, "main/klientS.html", {"k" : k})

def register(response): 
    if response.method == "POST":
        form = Rejestracja(response.POST)

        if form.is_valid():
            i = form.cleaned_data["name"]
            n = form.cleaned_data["surname"]
            t = Klient(imie=i, nazwisko=n)
            t.save()
            return HttpResponseRedirect(f"/klient/{t.id}")
    else:
        form = Rejestracja()
    return render(response, "main/register.html", {"form": form})