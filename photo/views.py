from django.shortcuts import render


def home_page(request):
    file_name = "home_page.html"
    context = {}
    return render(request, file_name, context)