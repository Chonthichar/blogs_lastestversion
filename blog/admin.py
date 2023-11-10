from django.contrib import admin
from .models import Fields, Profile, Add_comment
# Register your models here.

class FieldsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'updated_on', 'content', 'created_on', 'image', 'video', 'user')

# class FiledProfile(admin.ModelAdmin):
#     list_display = ('id', 'user')

admin.site.register(Fields, FieldsAdmin)
admin.site.register(Profile)
admin.site.register(Add_comment)

