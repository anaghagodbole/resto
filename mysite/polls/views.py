from django.http import HttpResponse
from .models import Questions
from django.template import loader
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from django.shortcuts import render


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list }
    return HttpResponse(template.render(context, request))

    
def detail(request, question_id):
    try:
         q=Question.objects.get(id=question_id)
    except Question.DoesNotExist:
         raise Http404("question does not exist")
    return HttpResponse("You're looking at question %s." % q.question_text)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def delete(request,question_id):
    q=Question.objects.get(pk=question_id)
    q.delete()
    return HttpResponse("deleted")

def update(request,question_id):
    q=Question.objects.get(pk=question_id)
    q.question_text="question updated"
    q.save()
    return HttpResponse("updated")

@csrf_exempt
def create(request):
    if request.method=='POST':
         q=Question(question_text="What's up?", pub_date=timezone.now())
         q.save()
         return HttpResponse("question is added")
    elif request.method=='GET': 
         return HttpResponse("unauthorized error")

@csrf_exempt
def createusingp(request):
    if request.method=='POST':
        q=Question(question_text=request.POST.get("abc"),pub_date=timezone.now())
        q.save()
        return HttpResponse("QUESTION IS ADDED")
    elif request.method=='GET':
        return HttpResponse("unauthourized")

@csrf_exempt
def form(request):
    return render(request, 'polls/form.html')

@csrf_exempt
def createnewquestion(request):
    if request.method=='POST':
        q=Question(question_text=request.POST.get("question"),pub_date=timezone.now())
        q.save()
        return HttpResponse("question is added")
    elif request.method=='GET':
        return HttpResponse("unauthourized")








0