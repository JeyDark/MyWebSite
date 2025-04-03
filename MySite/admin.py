from django.contrib import admin
from .models import ContactModel
# Register your models here.


admin.site.site_header='ADMIN MYSITE'
admin.site.site_title = 'ADMIN MYSITE'
admin.site.index_title='ADMIN MYSITE'

@admin.register(ContactModel)
class ParametAdmin(admin.ModelAdmin):
     ordering = ('name',)
     list_display = ['name','number', 'email', 'message']

