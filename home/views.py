from django.shortcuts import render, redirect,get_object_or_404
from .forms import users, addInfo, ApproveInfo
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import State, Information, Continent
from django.db.models import Count
# Create your views here.

# @login_required(redirect_field_name='home/home.html')
def homepage(request):
    template = "home/home.html"
    emrat_kontinentet = Continent.objects.all()

    return render(request,"home/home.html",{'emrat':emrat_kontinentet})


def UserRegister(request):
    if(request.method == 'POST'):
        form = users(request.POST)
        if(form.is_valid()):
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'U krijua faqja per {username}!')
            return redirect('sign-up')
    else:
        form = users()
    return render(request, 'home/signup.html', {'form': form})

def shtetet_search(request):
    query = request.GET.get('q')
    if(query):
        rezultatet = State.objects.filter(Name__icontains = query)
    elif(query==''):
        return redirect('home')
    else:
        return redirect('home')
    return render(request,"home/shtetet_kerkuara.html",{'shtetet':rezultatet})

def shtetet_info(request, pk):
    template = "home/shtetet_info.html"

    informata = Information.objects.filter(IdState = pk, confirm = True)
    print(informata)
    print(pk)
    return render(request,"home/shtetet_info.html",{'info':informata, 'id': pk})

def unapproved_info(request):
    template = "home/shtetet_info_approve.html"

    informata = Information.objects.filter(confirm = False).order_by('-IdState')
    print(informata)
    return render(request,"home/shtetet_info_approve.html",{'info':informata})

def approve_info(request, pk):
    info = Information.objects.get(id=pk)
    info.confirm = True
    info.save()
    return render(request, "home/approve.html")

def dissapprove_info(request, pk):
    info = Information.objects.get(id=pk)
    info.delete()
    return render(request, "home/dissapprove.html")

def shtetet_flags(request, pk):
    template = "home/Eu.html"

    fotot = State.objects.filter(IdContinents = pk).order_by('Name')
    kontinenti = Continent.objects.get(id = pk)
    return render(request,"home/Eu.html",{'info':fotot,'kontinenti':kontinenti})


@login_required(redirect_field_name='home/home.html')
def Addinfo(request, shteti = ''):
    if(request.method == 'POST'):
        form = addInfo(request.POST, request.FILES or None)
        if(form.is_valid()):
            information = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Te dhenat u regjistruan')
            return redirect('/shtetet_info/' + str(information.IdState.id))
    else:
        form = addInfo()

    if (shteti != '') :
        state = State.objects.get(id=shteti)
        form.initial['IdContinents'] = state.IdContinents
        form.initial['IdState'] = state.id

    return render(request, 'home/shkruaj.html', {'form': form})


@login_required(redirect_field_name='home/home.html')
def like(request, pk):
    post = get_object_or_404(State,  id=pk)
    post.dislikes.remove(request.user)
    post.likes.add(request.user)
    return redirect('/kontinentet/' + str(post.IdContinents.id))

    return render(request,"home/Eu.html",{'info':post})

@login_required(redirect_field_name='home/home.html')
def dislike(request, pk):
    post = get_object_or_404(State,  id=pk)
    post.likes.remove(request.user)
    post.dislikes.add(request.user)
    return redirect('/kontinentet/' + str(post.IdContinents.id))

    return render(request,"home/Eu.html",{'info':post})

def sorting(request, pk):
    sort = State.objects.filter(IdContinents=pk).annotate(like_count=Count('likes')).order_by('-like_count')
    kontinenti = Continent.objects.get(id = pk)
    return render(request,"home/Eu_sorted.html",{'sorted':sort,'kontinenti':kontinenti})