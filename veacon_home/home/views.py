from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import FormContact


def home(request):
    if request.POST:
        form_contact = FormContact(request.POST)

        if form_contact.is_valid():
            form_contact.save()
            messages.success(request, "Sua mensagem foi recebida! Em breve entraremos em contato (:")
        else:
            messages.error(request, "Sua mensagem não foi enviada ):")

        return redirect('home')

    return render(request, 'home.html')
