from django.http import HttpResponse
from .models import Restaurant, Items
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json


# def index(request):
# resto=Restaurant.objects.all()
# List=[]
# for i in resto:
# dict={"name":i.name,"address":i.address}
# List.append(dict)
# return HttpResponse(json.dumps(List))

#def count(request):
 #r=Restaurant.objects.all().count()
 #return HttpResponse(r)

def restaurant(request):
    resto = Restaurant.objects.all()
    List = []
    for i in resto:
        dict = {"name": i.name,
                "address": i.address
                }
    List.append(dict)
    return HttpResponse(json.dumps(List))


def restaurantitem(request, restaurant_id):
    rest1 = Restaurant.objects.filter(pk=restaurant_id).first()
    items = Items.objects.filter(restaurant=rest1)
    List = []
    for i in items:
        dict = {"nameofitem": i.nameofitem,
                "price": str(i.price)
                }
    List.append(dict)
    L = {"name": rest1.name,
         "address": rest1.address,
         "Items": List
         }
    return HttpResponse(json.dumps(L))


@csrf_exempt
def restaurantusingp(request):
    if request.method == 'POST':
        r = Restaurant(name=request.POST.get("abc"),
                       address=request.POST.get("xyz")
                       )
        r.save()
        return HttpResponse(" added")
    elif request.method == 'GET':
        raise Http404("ERROR")


@csrf_exempt
def restaurantusingid(request, restaurant_id):
    if request.method == 'POST':
        rest1 = Restaurant.objects.filter(pk=restaurant_id).first()
        r = Items(nameofitem=request.POST.get("abc"),
                  price=request.POST.get("xyz"),
                  restaurant=rest1
                  )
        r.save()
        return HttpResponse(" added")
    elif request.method == 'GET':
        raise Http404("ERROR")


"""def detail(request, restaurant_id):
   # try:
    #     q=Restaurant.objects.get(id=restaurant_id)
    #except Restaurant.DoesNotExist:
     #    raise Http404("question does not exist")
    #return HttpResponse("You're looking at question %s." % q.name)"""


def detail(request, restaurant_id):
    rest1 = Restaurant.objects.filter(pk=restaurant_id).first()
    items = Items.objects.filter(restaurant=rest1)
    context = {'rest1': rest1,
               'items': items
               }
    return render(request, "resto/Second.html", context)


def form(request):
    return render(request, 'resto/form.html')


@csrf_exempt
def create(request):
    if request.method == 'POST':
        q = Restaurant(name=request.POST.get("restaurant"),
                       address=request.POST.get("address")
                       )
        q.save()
        latest_resto_list = Restaurant.objects.all()
        context = {'latest_resto_list': latest_resto_list}
        return render(request, 'resto/index.html', context)
    elif request.method == 'GET':
        return HttpResponse("unauthorized")


@csrf_exempt
def additem(request, restaurant_id):
    if request.method == 'POST':
        rest1 = Restaurant.objects.filter(pk=restaurant_id).first()
        q = Items(nameofitem=request.POST.get("item"),
                  price=request.POST.get("price"),
                  restaurant=rest1
                  )
        q.save()
        items = Items.objects.filter(restaurant=rest1)
        context = {'items': items,
                   'rest1': rest1
                   }
        return render(request, 'resto/Second.html', context)
    elif request.method == 'GET':
        return HttpResponse("unauthorized")


def count(request):
    return HttpResponse(Restaurant.objects.all().count())
