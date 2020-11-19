from django.shortcuts import render, redirect, HttpResponse
import random, datetime

# Create your views here.
def index(request):
    request.session['gold']
    return render(request, 'index.html')

def farm(request):
    tens = round(random.random()*10) + 10
    request.session['gold'] += tens
    now = datetime.datetime.now().strftime('%Y/%m/%d %I:%M %p')
    print("Earned", tens, "golds from the farm! (", now,")")
    return redirect('/')

def cave(request):
    fives = round(random.random()*5) + 5
    request.session['gold'] += fives
    now = datetime.datetime.now().strftime('%Y/%m/%d %I:%M %p')
    print("Earned", fives, "golds from the cave! (", now,")")
    # print(f"this is {request.session['gold']}")
    return redirect('/')

def house(request):
    threes = round(random.random()*3) + 2
    request.session['gold'] += threes
    now = datetime.datetime.now().strftime('%Y/%m/%d %I:%M %p')
    print("Earned", threes, "golds from the house! (", now,")")
    # print(f"this is {request.session['gold']}")
    return redirect('/')

def casino(request):
    fifty = round(random.uniform(-1,1)*50)
    request.session['gold'] += fifty
    now = datetime.datetime.now().strftime('%Y/%m/%d %I:%M %p')
    print("Earned/Lost", fifty, "golds from the casino! (", now,")")
    # print(f"this is {request.session['gold']}")
    return redirect('/')