import json
from django.http import HttpResponse
from django.shortcuts import render
from photo import models


def photo_list_api(request):
    all_dates = models.PhotoDate.objects.all()
    final_object = {}
    for single_date in all_dates:
        images_list = []
        all_photos = models.Photo.objects.filter(photodate=single_date)
        for photo in all_photos:
            photo_str = str(photo.photo)
            images_list.append(photo_str)

        final_object[str(single_date.uploaded_date)] = images_list

    final_object = json.dumps(final_object)

    return HttpResponse(final_object)
