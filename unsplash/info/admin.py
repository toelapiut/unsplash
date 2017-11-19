from django.contrib import admin
from .models import Editor,Photos,tags,Photos_two,Photos_three

class PhotosAdmin(admin.ModelAdmin):
    filter_horizontal=('tags',)

# Register your models here.
admin.site.register(Editor)
admin.site.register(Photos,PhotosAdmin)
admin.site.register(Photos_two,PhotosAdmin)
admin.site.register(Photos_three,PhotosAdmin)
admin.site.register(tags)