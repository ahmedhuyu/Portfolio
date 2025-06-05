from django.shortcuts import render
from .models import Section, SidebarAuthor

# Create your views here.
def home(request):
    about_section = Section.objects.filter(section_id='section1').first()
    sections = Section.objects.all()
    author = SidebarAuthor.objects.first()
    return render(request, "home.html", {
        "about_section": about_section,
        "sections": sections,
        "author": author,
    })