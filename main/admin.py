from django.contrib import admin
from django import forms
from .models import HomeSection, ServiceSection, Service, Certificate, SidebarAuthor, Work, WorksSection, EmailSettings, ContactMessage

class ServiceInline(admin.TabularInline):
    model = Service
    extra = 1

class ServiceSectionAdmin(admin.ModelAdmin):
    inlines = [ServiceInline]

class WorkInline(admin.TabularInline):
    model = Work
    extra = 1

class WorksSectionAdmin(admin.ModelAdmin):
    inlines = [WorkInline]
    fields = ('title', 'description')

class EmailSettingsAdminForm(forms.ModelForm):
    class Meta:
        model = EmailSettings
        fields = '__all__'
        widgets = {
            'email_host_password': forms.PasswordInput(render_value=True),
        }

class EmailSettingsAdmin(admin.ModelAdmin):
    form = EmailSettingsAdminForm

admin.site.register(SidebarAuthor)
admin.site.register(Certificate)
admin.site.register(ServiceSection, ServiceSectionAdmin)
admin.site.register(HomeSection)
admin.site.register(WorksSection, WorksSectionAdmin)
admin.site.register(EmailSettings, EmailSettingsAdmin)
admin.site.register(ContactMessage)
