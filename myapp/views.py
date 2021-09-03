from django.shortcuts import render,redirect,get_object_or_404
from .models import*
from .forms import myform
from django.http import  HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

def home(request):
    all_models=Profile.objects.all()
    return render(request,'myapp/home.html',{'all_models':all_models})


def detail(request,val):
    sanu =Profile.objects.get(id=val)
    return render(request,'myapp/detail.html',{'sanu':sanu})


def add_new(request):

    if request.method=="POST":
        form=myform(request.POST, request.FILES)
        if form.is_valid():
            form.save()


        return redirect('/')
    else:
        form=myform()

        return render(request,'myapp/add_new.html',{'form':form})


def edit_form(request,val):
    treasure=get_object_or_404(Profile,pk=val)

    if request.method=="POST":
        form=myform(request.POST,request.FILES ,instance=treasure )
        if form.is_valid():
            form.save()

            return redirect( 'myapp:detail',val=treasure.pk)

    else:
        form=myform(instance=treasure)

        return render(request,'myapp/edit_form.html',{'form':form})



def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.save()
            login(request,user)
            return redirect('/')


    else:
        form=UserCreationForm()
        return render(request,'registration/signup.html',{'form':form})

#

#### extra ###



#def login_req(request):
#    if request.method=='POST':
#        form=AuthenticationForm(data=request.POST)
#        if form.is_valid():
#            username=form.cleaned_data.get('username')
 #           raw_password=form.cleaned_data.get('password')
  #          user=authenticate(username=username,password=raw_password)
   #         login(request,user)
    #        return redirect('/')
    #else:
     #   form=AuthenticationForm()
      #  return render(request,'registration/login.html',{'form':form})
