from django.shortcuts import render


def auto_mngr(request):
    return render(request, 'auto_mngr/auto_mngr.html', locals())

# Create your views here.
