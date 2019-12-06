from django.http import HttpResponse
from .models import Restaurant,Items
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from django.shortcuts import render

#def index(request):
    #latest_resto_list=Restaurant.objects.all()
    #context={'latest_resto_list':latest_resto_list}
   # return render(request,'restaurant/index.html',context)

#def detail(request, restaurant_id):
   # try:
    #     q=Restaurant.objects.get(id=restaurant_id)
    #except Restaurant.DoesNotExist:
     #    raise Http404("question does not exist")
    #return HttpResponse("You're looking at question %s." % q.name)

def detail(request,restaurant_id):
    rest1=Restaurant.objects.filter(pk=restaurant_id).first()
    items=Items.objects.filter(restaurant=rest1)
    context={'rest1':rest1,'items':items}
    return render(request,"restaurant/Second.html",context)



def form(request):
    return render(request,'restaurant/form.html')

@csrf_exempt
def create(request):
    if request.method=='POST':
        q=Restaurant(name=request.POST.get("restaurant"),address=request.POST.get("address"))
        q.save()
        latest_resto_list=Restaurant.objects.all()
        context={'latest_resto_list':latest_resto_list}
        return render(request,'restaurant/index.html',context)   
    elif request.method=='GET':
        return HttpResponse("unauthorized")


    
@csrf_exempt
def additem(request,restaurant_id):
    if request.method=='POST':
        rest1=Restaurant.objects.filter(pk=restaurant_id).first()
        q=Items(nameofitem=request.POST.get("item"),price=request.POST.get("price"),restaurant=rest1)
        q.save()
        items=Items.objects.filter(restaurant=rest1)
        context={'items':items,'rest1':rest1}
        return render(request,'restaurant/Second.html',context)
    elif request.method=='GET':
        return HttpResponse("unauthorized")
