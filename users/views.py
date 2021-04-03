from django.contrib.auth import logout, login, authenticate
from django.http.response import  HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


# Create your views here.
def logout_view(request):
    """Faz o logout do usuario"""
    logout(request)
    return  HttpResponseRedirect(reverse('learning_log:index'))
    

def register(request):
    """Cria uma conta de usuario"""
    if request.method != "POST":
        form = UserCreationForm
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticate_user = authenticate(username=new_user.username, password= request.POST["password1"])
            login(request, authenticate_user)
            return  HttpResponseRedirect(reverse("learning_log:index"))
    context= {"form": form}
    return render(request, "users\\register.html", context )
