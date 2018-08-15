from django.contrib import admin
from sys_info.models import Contact, Tag
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email')
    search_fields = ('name',)
    fieldsets = (
        ['Main', {
            'fields':('name', 'age'),
        }],
        ['Other',{
            'classes':('collapse',),
            'fields':('email',)
        }]
    )

class TagAdmin(admin.ModelAdmin):
    fields = ('contact',)

admin.site.register(Contact, ContactAdmin)
admin.site.register(Tag, TagAdmin)

