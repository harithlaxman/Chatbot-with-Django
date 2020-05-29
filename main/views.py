from django.shortcuts import render,redirect
# from .models import details
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, UserName
from django.contrib.auth import authenticate, login, logout
from .models import FriendDetails
import requests
from bs4 import BeautifulSoup
# Create your   views here.
def refresh(request, user_name):
    url = f"https://www.codechef.com/users/{user_name}"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    name = str(soup.findAll('h2')[1]).strip('<h2/>')
    table = soup.find('div', attrs = {'class':'rating-number'})
    if table is not None:
        table = table.text
    detail = FriendDetails.objects.get(friend_user_name=user_name)
    detail.friend_name = name
    detail.rating = table
    detail.save()
    return redirect("/main/")
def home(request):
    details = {}
    if request.user.is_authenticated:
        user = request.user
        details = FriendDetails.objects.filter(user=user)
    if request.method == "POST":
        form = UserName(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('user_name')
            url = f"https://www.codechef.com/users/{user_name}"
            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'html5lib')
            name = str(soup.findAll('h2')[1]).strip('<h2/>')
            table = soup.find('div', attrs = {'class':'rating-number'})
            if table is not None:
                table = table.text
                detail = FriendDetails(friend_name=name, friend_user_name=user_name, rating=table)
                detail.user = user
                detail.save()
                return(render(request, 'main/home.html', context={'details':details,'form':form}))
            else:
                messages.error(request, f"{user_name} is not a valid Username")
    form = UserName
    # email = details.objects.all
    # template = loader.get_template('/index.html')
    # context = {'email': email}
    return render(request, 'main/home.html', {'form':form, 'details':details})

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_name = form.cleaned_data.get('username')
            messages.success(request, f"User {user_name} created successfully")
            return redirect("/main/")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg} : {form.error_messages[msg]}")

            return render(request = request,
                          template_name = "main/register.html",
                          context={"form":form})

    form = SignUpForm
    return(render(request, 'main/register.html', context={'form':form}))

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/main/")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(user_name, password)
            user = authenticate(request, username=user_name, password=password)
            if user is not None:
                messages.success(request, "You are now logged in !")
                login(request, user)
                return redirect("/main/")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")

    form = AuthenticationForm
    return(render(request, "main/login.html", context={'form':form}))
