from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
from django.utils.translation import gettext
from django.utils import translation
from django.http import HttpResponseRedirect

# Home page
def index(request):
    return render(request, 'barbara/index.html')

#About page
def about(request):
    return render(request, 'barbara/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            sender_number = form.cleaned_data['number']
            feedback = form.cleaned_data['reputation']
            message = form.cleaned_data['message'] + "\nSlišal/-a sem zate preko:" + str(feedback)

            sender = sender_name + " " + "<" + sender_number + ">"
            
            send_mail(sender, message, sender_email, ['barbara.bergant3@gmail.com'])
            return render(request, 'barbara/contact.html', {'sender_name': sender_name})
    else:
        form = ContactForm()
    return render(request, 'barbara/contact.html', {'form': form})

def services(request):
    return render(request, 'barbara/services.html')

def set_language_from_url(request, user_language):
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))