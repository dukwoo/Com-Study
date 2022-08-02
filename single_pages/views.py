from django.shortcuts import render

def phrase(request):
    return render(
        request,
        'single_pages/phrase.html'
    )
