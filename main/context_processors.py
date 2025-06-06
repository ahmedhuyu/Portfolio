from .models import SidebarAuthor

def author(request):
    return {
        'author': SidebarAuthor.objects.first()
    }
