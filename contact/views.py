from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm


def contactView(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data['message']
            send_mail(subject,
                      message,
                      from_email, ["admin@django-hotel.com"])
            return redirect("success")
    return render(request, "contact.html", {"form": form})


def successView(request):
    return render(request, "contact_success.html")
