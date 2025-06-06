from django.db import models

# Create your models here.
class SidebarAuthor(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='author_images/')

    def __str__(self):
        return self.name

class HomeSection(models.Model):
    title = models.CharField(max_length=100, default="About Me")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Certificate(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='certificates/')
    is_left_image = models.BooleanField(default=True)  # True for left-image-post, False for right-image-post

    def __str__(self):
        return self.title

class ServiceSection(models.Model):
    title = models.CharField(max_length=200, default="What I’m good at?")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Service(models.Model):
    section = models.ForeignKey(ServiceSection, on_delete=models.CASCADE, related_name='services', null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    icon_class = models.CharField(max_length=50, blank=True, null=True)  # e.g. 'first-service-icon'

    def __str__(self):
        return self.title

class Work(models.Model):
    works_section = models.ForeignKey('WorksSection', on_delete=models.CASCADE, related_name='works', null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='works/', blank=True, null=True)

    def __str__(self):
        return self.title

class WorksSection(models.Model):
    title = models.CharField(max_length=200, default='أعمالي')
    description = models.TextField(default='بعض من المشاريع التي عملت عليها')

    def __str__(self):
        return self.title

class EmailSettings(models.Model):
    email_host_user = models.EmailField(verbose_name="Email Host User")
    email_host_password = models.CharField(max_length=255, verbose_name="Email Host Password")

    def __str__(self):
        return self.email_host_user

    class Meta:
        verbose_name = "Email Settings"
        verbose_name_plural = "Email Settings"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject} ({self.created_at:%Y-%m-%d %H:%M})"