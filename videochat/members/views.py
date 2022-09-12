from django.shortcuts import render
from django.http import HttpResponse as res, HttpResponseRedirect as red
from django.template import loader
from django.urls import reverse
from .models import Members


def index(req):
    mymembers = Members.objects.all().values()
    template = loader.get_template("index.html")
    context = {"mymembers": mymembers, "title": "Home"}
    return res(template.render(context, req))


def add(req):
    template = loader.get_template("add.html")
    return res(template.render({}, req))


def addrecord(req):
    x = req.POST["first"]
    y = req.POST["last"]
    e = req.POST["email"]
    member = Members(firstname=x, lastname=y, email=e)
    member.save()
    return red(reverse("index"))


def delete(req, id):
    member = Members.objects.get(id=id)
    member.delete()
    return red(reverse("index"))


def update(req, id):
    mymember = Members.objects.get(id=id)
    template = loader.get_template("update.html")
    context = {
        "mymember": mymember,
    }
    return res(template.render(context, req))


def updaterecord(req, id):
    first = req.POST["first"]
    last = req.POST["last"]
    email = req.POST["email"]
    member = Members.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.email = email
    member.save()
    return red(reverse("index"))
