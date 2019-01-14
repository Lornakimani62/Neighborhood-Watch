from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib.auth.models import User

def index(request):

    try:
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        current_user=request.user
    except ObjectDoesNotExist:
        return redirect('profile')

    return render(request,'index.html')

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user=request.user
    profile=Profile.objects.filter(name=current_user).first()

    if request.method=="POST":
        form =ProfileForm(request.POST,instance=profile,files=request.FILES)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.name = current_user
            profile.save()
        return redirect('/')

    else:

        form = ProfileForm()
    return render(request,'profile.html',{"form":form})

# Posts all the businesses in the given neighborhood
@login_required(login_url='/accounts/login/')
def business(request):
    current_user=request.user
    posts=Business.objects.all()
    return render(request,'business.html',{'posts':posts})

# Provides the user the ability to post businesses in their neighbohood
@login_required(login_url='/accounts/login/')
def post_business(request):
    current_user=request.user
   
    if request.method=="POST":
        form =BusinessForm(request.POST,files=request.FILES)
        if form.is_valid():
            business = form.save(commit = False)
            business.save()
        return redirect('/business')

    else:

        form = BusinessForm()
    return render(request,'post_business.html',{"form":form})

# View function to display police and health services information
@login_required(login_url='/accounts/login')
def contact(request):
    current_user=request.user
    contacts = Contact.objects.all()

    return render(request,'contact.html',{'contacts':contacts})

# view function that allows users to view notifications
@login_required(login_url='/accounts/login')
def notify(request):
    current_user=request.user
    notifications=Notification.objects.all()

    return render(request,'notify.html',{'notifications': notifications})

@login_required(login_url='/accounts/login/')
def post_notify(request):
    current_user=request.user
   
    if request.method=="POST":
        form =NotifyForm(request.POST,files=request.FILES)
        if form.is_valid():
            notices = form.save(commit = False)
            notices.save()
        return redirect('/notifications')
    else:

        form = NotifyForm()
    return render(request,'post_note.html',{"form":form})

@login_required(login_url='/accounts/login/')
def search(request):
    current_user=request.user

    return render(request,'search.html')