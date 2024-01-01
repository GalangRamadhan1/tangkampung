from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import FormMembers
from .models import Member


def members(request):
    if request.method == "POST":
        form = FormMembers(request.POST, request.FILES)
        if form.is_valid():
            simpanData = Member.objects.create(
                firstname=form.cleaned_data.get("firstname"),
                lastname=form.cleaned_data.get("lastname"),
            )
            simpanData.save()
            return redirect("members")
    else:
        form = FormMembers()

    template = loader.get_template("myfirst.html")
    data = Member.objects.all().values()
    context = {
        "data": data,
        "form": FormMembers,
    }
    return HttpResponse(template.render(context, request))


def hapus_produk(request, data_id):
    data = Member.objects.get(id=data_id)
    data.delete()
    return redirect("members")


def dashboard(request):
    template = loader.get_template("dashboard.html")
    return HttpResponse(template.render())


def user(request):
    template = loader.get_template("user.html")
    return HttpResponse(template.render())


def order(request):
    template = loader.get_template("order.html")
    return HttpResponse(template.render())
