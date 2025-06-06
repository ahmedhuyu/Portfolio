from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class SidebarAuthor(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='author_images/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('مؤلف الشريط الجانبي')
        verbose_name_plural = _('مؤلفو الشريط الجانبي')

class HomeSection(models.Model):
    title = models.CharField(max_length=100, default="About Me")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('قسم الصفحة الرئيسية')
        verbose_name_plural = _('أقسام الصفحة الرئيسية')

class Certificate(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='certificates/')
    is_left_image = models.BooleanField(default=True)  # True for left-image-post, False for right-image-post

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('شهادة')
        verbose_name_plural = _('الشهادات')

class ServiceSection(models.Model):
    title = models.CharField(max_length=200, default="What I’m good at?")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('قسم الخدمات')
        verbose_name_plural = _('أقسام الخدمات')

class Service(models.Model):
    section = models.ForeignKey(ServiceSection, on_delete=models.CASCADE, related_name='services', null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    icon_class = models.CharField(max_length=50, blank=True, null=True)  # e.g. 'first-service-icon'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('خدمة')
        verbose_name_plural = _('الخدمات')

class Work(models.Model):
    works_section = models.ForeignKey('WorksSection', on_delete=models.CASCADE, related_name='works', null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='works/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('عمل')
        verbose_name_plural = _('الأعمال')

class WorksSection(models.Model):
    title = models.CharField(max_length=200, default='أعمالي')
    description = models.TextField(default='بعض من المشاريع التي عملت عليها')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('قسم الأعمال')
        verbose_name_plural = _('أقسام الأعمال')

class EmailSettings(models.Model):
    email_host_user = models.EmailField(verbose_name=_("البريد الإلكتروني للمضيف"))
    email_host_password = models.CharField(max_length=255, verbose_name=_("كلمة مرور البريد الإلكتروني للمضيف"))

    def __str__(self):
        return self.email_host_user

    class Meta:
        verbose_name = _("إعدادات البريد الإلكتروني")
        verbose_name_plural = _("إعدادات البريد الإلكتروني")

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("الاسم"))
    email = models.EmailField(verbose_name=_("البريد الإلكتروني"))
    subject = models.CharField(max_length=200, verbose_name=_("الموضوع"))
    message = models.TextField(verbose_name=_("الرسالة"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("تاريخ الإرسال"))

    def __str__(self):
        return f"{self.name} - {self.subject} ({self.created_at:%Y-%m-%d %H:%M})"

    class Meta:
        verbose_name = _("رسالة تواصل")
        verbose_name_plural = _("رسائل التواصل")