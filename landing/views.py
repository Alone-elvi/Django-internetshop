from django.shortcuts import render
from .forms import SubscriberForm


def landing(request):
    form = SubscriberForm(request.POST or None)
    print(request.method)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        saved_form = form.save()

    return render(request, 'landing/comingsoon.html', locals())
