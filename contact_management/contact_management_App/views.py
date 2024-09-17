from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Contact
from .forms import ContactForm
from django.http import HttpResponse


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')


def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'add_contact.html', {'form': form})

def home(request):
    contacts = Contact.objects.all()
    return render(request, 'home.html', {'contacts': contacts})

def contact_detail(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    return render(request, 'contact_detail.html', {'contact': contact})
def edit_contact(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'edit_contact.html', {'form': form, 'contact': contact})
def delete_contact(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    if request.method == 'POST':
        contact.delete()
        return redirect('home')
    return render(request, 'delete_contact.html', {'contact': contact})
def search_contacts(request):
    query = request.GET.get('q')
    contacts = Contact.objects.filter(first_name__icontains=query) | Contact.objects.filter(email__icontains=query)
    return render(request, 'home.html', {'contacts': contacts})
