from django.db import models

# Create your models here.
class Section(models.Model):
    title = models.CharField(max_length=100)
    section_id = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class SidebarAuthor(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='author_images/')

    def __str__(self):
        return self.name