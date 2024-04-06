"""Creating the Pet related views"""
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Pet
from .forms import PetForm
# Create your views here.

def index(request):
    return render(request, 'pet/index.html')

def show(request):
    pets = Pet.objects.all()
    return render(request, 'pet/pet.html', {"boi": pets})

def details(request, petid):
    pet = Pet.objects.get(pk=petid)
    return render(request, 'pet/details.html',{'pet': pet})

def update(request, petid):
    pet = Pet.objects.get(pk=petid)
    form = PetForm(request.POST or None, instance=pet)
    if form.is_valid():
        form.save()
        return redirect('show')
    return render(request, 'pet/update.html',{'pet': pet, 'form': form})

def delete(request, petid):
    pet = Pet.objects.get(pk=petid)
    pet.delete()
    return redirect('show')

def contact(request):
    """renders"""
    return render(request, 'pet/contact.html')


def addpet(request):
    """Function to add pet"""
    submitted = False
    if request.method == "POST":
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pet/addpet?submitted=True')
    else:
        form = PetForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'pet/addpet.html', {'form': form, 'submitted': submitted})
