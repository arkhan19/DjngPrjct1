from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
def translate(request):
    original = request.GET['Text1']
    translation = ''
    for word in original.split():
        if word[0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            translation += word[1:]
        else:
            translation += word[0]
            translation += 'PenCho'
    return render(request, 'translate.html', {'original':original, 'translate':translation})


