from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
from django.utils.translation import activate, get_language, gettext
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
            message = "To sporočilo je bilo poslano preko spletne strani.\n\n" + "Ime in priimek: " + sender_name + "\nTelefon: " + sender_number + "\nE-pošta: " + sender_email + "\n\nSporočilo:\n" + form.cleaned_data['message'] + "\n\n\nSlišal/-a sem zate preko:" + str(feedback)

            sender = "Poizvedba " + sender_name + " " + "<" + sender_number + ">"
            
            #send_mail(sender, message, sender_email, ['barbara.bergant3@gmail.com'])
            from django.core.mail import EmailMessage
            email = EmailMessage(
                    sender,
                    message,
                    sender_email,
                    ['barbara.kacin@gmail.com'],
                    reply_to=[sender_email],
                )
            email.send(fail_silently=False)
            return render(request, 'barbara/contact.html', {'sender_name': sender_name})
    else:
        form = ContactForm()
    return render(request, 'barbara/contact.html', {'form': form})

def services(request):
    return render(request, 'barbara/services.html')

def set_language_from_url(user_language):
    cur_language = get_language()
    try:
        activate(user_language)
    finally:
        activate(cur_language)
    pass