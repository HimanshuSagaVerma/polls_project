from django.contrib import admin
from photo.models import Photo, PhotoDate


class PhotoAdmin(admin.ModelAdmin):
    class UploadPhotos(admin.TabularInline):
        model = Photo
        extra = 1

    inlines = [UploadPhotos]


admin.site.register(PhotoDate, PhotoAdmin)

