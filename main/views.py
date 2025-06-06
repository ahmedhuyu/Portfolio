from django.shortcuts import render
from .models import SidebarAuthor, Certificate, ServiceSection, Service, HomeSection, Work, WorksSection, EmailSettings, ContactMessage
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

# Create your views here.
def home(request):
    about_section = HomeSection.objects.first()
    author = SidebarAuthor.objects.first()
    certificates = Certificate.objects.all()
    return render(request, "home.html", {
        "about_section": about_section,
        "author": author,
        "certificates": certificates,
    })

def services(request):
    section = ServiceSection.objects.first()
    services = Service.objects.filter(section=section) if section else []
    return render(request, "services.html", {
        "service_section": section,
        "services": services,
    })

def my_works(request):
    works_section = WorksSection.objects.first()
    works = works_section.works.all() if works_section else []
    return render(request, 'my_works.html', {
        'works': works,
        'works_section_title': works_section.title if works_section else 'أعمالي',
        'works_section_description': works_section.description if works_section else 'بعض من المشاريع التي عملت عليها',
    })

def get_email_settings():
    email_settings = EmailSettings.objects.first()
    if email_settings:
        return email_settings.email_host_user, email_settings.email_host_password
    return settings.DEFAULT_FROM_EMAIL, settings.EMAIL_HOST_PASSWORD

def contact_me(request):
    sent = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # Save to database
            ContactMessage.objects.create(
                name=cd['name'],
                email=cd['email'],
                subject=cd['subject'],
                message=cd['message']
            )
            # Send email as before
            email_host_user, email_host_password = get_email_settings()
            from django.core.mail import EmailMessage, get_connection
            connection = get_connection(
                host='smtp.gmail.com',
                port=587,
                username=email_host_user,
                password=email_host_password,
                use_tls=True
            )
            email = EmailMessage(
                cd['subject'],
                f"Name: {cd['name']}\nEmail: {cd['email']}\n\n{cd['message']}",
                email_host_user,
                ['ahmed.huyu@gmail.com'],
                connection=connection
            )
            email.send()
            sent = True
    else:
        form = ContactForm()
    return render(request, 'contact_me.html', {'form': form, 'sent': sent})