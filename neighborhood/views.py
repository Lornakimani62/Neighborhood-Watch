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

