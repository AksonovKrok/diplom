from django.forms import ModelChoiceField, ModelForm
from django.contrib import admin

from .models import *


class SmartphoneAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        # if instance and not instance.sd:
        #     self.fields['sd_volume_max'].widget.attrs.update({
        #         'readonly': True, 'style': 'background: lightgray;'
        #     })

    # def clean(self):
    #     if not self.cleaned_data['sd']:
    #         self.cleaned_data['sd_volume_max'] = None
    #     return self.cleaned_data


class NotebookAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='notebooks'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class DesktopAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='desktop'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class SmartphoneAdmin(admin.ModelAdmin):

    change_form_template = 'admin.html'
    form = SmartphoneAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='smartphones'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class TabletAdmin(admin.ModelAdmin):

    change_form_template = 'admin.html'
    form = SmartphoneAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='tablet'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class TelevisionAdmin(admin.ModelAdmin):

    change_form_template = 'admin.html'
    form = SmartphoneAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='television'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class AudioAdmin(admin.ModelAdmin):

    change_form_template = 'admin.html'
    form = SmartphoneAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='audio'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class PhotographicAdmin(admin.ModelAdmin):

    change_form_template = 'admin.html'
    form = SmartphoneAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='photographic'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class OfficeAdmin(admin.ModelAdmin):

    change_form_template = 'admin.html'
    form = SmartphoneAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='office'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class AppliancesAdmin(admin.ModelAdmin):

    change_form_template = 'admin.html'
    form = SmartphoneAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='appliances'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class SoftwareAdmin(admin.ModelAdmin):

    change_form_template = 'admin.html'
    form = SmartphoneAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='software'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Smartphone, SmartphoneAdmin)
admin.site.register(Desktop, DesktopAdmin)
admin.site.register(Tablet, TabletAdmin)
admin.site.register(Television, TelevisionAdmin)
admin.site.register(Audio, AudioAdmin)
admin.site.register(Photographic, PhotographicAdmin)
admin.site.register(Office, OfficeAdmin)
admin.site.register(Appliances, AppliancesAdmin)
admin.site.register(Software, SoftwareAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)

