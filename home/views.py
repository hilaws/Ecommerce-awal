from django.shortcuts import render
from accounts.forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


def home(request):

    return render(request,'home.html')

def main(request):
    return render(request,'index.html')

def cart(request):
    return render(request,'cart-empty.html')

def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request,'index.html')
                else:
                    return HttpResponse("Your account has been disabled!")
            else:
                return HttpResponse("No account with this creds")
        else:
            return HttpResponse('Failed to log in')
    else:
        form = LoginForm()
        return render(request,'login.html',{'form':form})

def wishlist(request):
    return render(request,'page-wishlist-1.html')    

def order(request):
    return render(request,'page-orders-1.html')

def help(request):
    return render(request,'page-help-1.html')    

def ourStory(request):
    return render(request,'page-our-stores-1.html')

def sighnup(request):
     return render(request,'sighnupform.html')

def view_product(request):
    return render(request,'product-view.html')


def products(request):
    return render(request,'products.html')             