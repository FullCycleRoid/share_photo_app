from django.contrib import admin

# Register your models here.
# from .models import Photo
#
#
# class PhotoAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'url': ('id',)}
#
#
from .models import Photo

admin.site.register(Photo)
