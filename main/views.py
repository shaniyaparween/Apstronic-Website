from django.shortcuts import render
from .models import Domain

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def domains(request):
    domain_list = Domain.objects.all()
    return render(request, 'main/domains.html', {'domains': domain_list})

def contact(request):
    return render(request, 'main/contact.html')

from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/contact.html', {'form': ContactForm(), 'success': True})
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib import messages

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # You can save this to DB or send email here
        print(f"Message from {name} ({email}): {subject} - {message}")
        
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')

    return render(request, 'main/contact.html')
