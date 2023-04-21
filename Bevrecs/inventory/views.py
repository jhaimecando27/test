from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from .forms import IngridientsForm


# Eto yung tricky part. Sa invetory page may 3 forms. Eh yung pinaka madali
# na implimentation ee kada form may sariling function

# Ref:
# https://stackoverflow.com/questions/5823464/django-httpresponseredirect


def index(request):
    # Need irender yung form muna, kasi papasok muna user sa site
    ingridientForm = IngridientsForm()

    context = {
        "ingridientForm": ingridientForm,
    }

    return render(request, "inventory/index.html", context)


def addIngridients(request):
    # Puro POST nmn mangyayari dito, pero imakake sure ko lng
    if request.method == "POST":
        form = IngridientsForm(data=request.POST)

        if form.is_valid():
            form.save()

    return HttpResponseRedirect(reverse("inventory:index"))
