from django.contrib import admin
from .models import Editor,Photos,tags

class PhotosAdmin(admin.ModelAdmin):
    filter_horizontal=('tags',)

# Register your models here.
admin.site.register(Editor)
admin.site.register(Photos,PhotosAdmin)
admin.site.register(tags)