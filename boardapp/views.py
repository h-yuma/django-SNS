from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import BoardModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy





# Create your views here.
def signupfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            return redirect('login')
        except IntegrityError:
            return render(request, 'signup.html', {'error':'このユーザーは既に登録されています'})
    return render(request, 'signup.html')

def loginfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'login.html', {})
    return render(request, 'login.html', {})

@login_required
def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'list.html', {'object_list':object_list})

def logoutfunc(request):
    logout(request)
    return redirect('login')

@login_required
def detailfunc(request, pk):
    object = get_object_or_404(BoardModel, pk=pk)
    return render(request, 'detail.html', {'object':object})

@login_required
def goodfunc(request, pk):
    object = get_object_or_404(BoardModel, pk=pk)
    object.good = object.good + 1
    object.save()
    return redirect('list')

@login_required
def readfunc(request, pk):
    object = get_object_or_404(BoardModel, pk=pk)
    username = request.user.get_username()
    if username in object.readtext:
        return redirect('list')
    else:
        object.read = object.read + 1
        object.readtext = object.readtext + ' ' + username
        object.save()
        return redirect('list')

@login_required
def userfunc(request, username):
    user = User.objects.get(username=username)
    object_list = BoardModel.objects.filter(author=user)
    return render(request, 'user.html', {'object_list':object_list, 'user':user})

@login_required
def deletecheckfunc(request, pk):
    object = get_object_or_404(BoardModel, pk=pk)
    return render(request, 'deletecheck.html', {'object':object})

@login_required
def deletefunc(request, pk):
    object = get_object_or_404(BoardModel, pk=pk)
    object.delete = True
    object.save()
    return redirect('list')

class BoardCreate(CreateView):
    template_name = 'create.html'
    model = BoardModel
    fields = ('title', 'content', 'author', 'sns_image')
    success_url = reverse_lazy('list')