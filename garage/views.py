from django.shortcuts import render, redirect
from . models import Contact
from . forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail


def home(request):
    all_Contact = Contact.objects.all
    return render(request, 'garage/index.html', {'all':all_Contact})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            name = request.POST['name']
            email = request.POST['email']
            message = request.POST['message']

            send_mail(
                name, # subject
                email, # from email
                message, # message
                [bonanzaautogarage@gmail.com], # To email
                fail_silently=False,
            )

            messages.success(request, ('There was an error with your submission, please try again'))
            #return redirect('contact')
            return render(request, 'garage/contact.html', {
                'name': name,
                'email': email,
                'message': message,
            })

        messages.success(request, ('Your message has been sent successfully'))
        return redirect('home')

    else:
        return render(request, 'garage/contact.html', {})