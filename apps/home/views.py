# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Tugas, MataKuliah
from .forms import MatkuliahForm, TugasForm
from django.db.models import Count


# @login_required(login_url="/login/")
def index(request):
    context = {
        "head": "dashboard",
        "segment": "index",
        "tugas": Tugas.objects.all(),
        "mk": MataKuliah.objects.all().annotate(count=Count('tugas')).annotate(
            done=Count('tugas__status', filter=0, distinct=True)
        )
    }

    html_template = loader.get_template("home/index.html")
    return HttpResponse(html_template.render(context, request))


"""TUGAS"""


@login_required(login_url="/login/")
def list_tugas(request):
    context = {
        "head": 'tugas',
        "segment": "list-tugas",
        "data": Tugas.objects.all(),
    }
    html_template = loader.get_template("tugas/list.html")
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def create_tugas(request):
    form_tugas = TugasForm(request.POST or None)
    # check if form data is valid
    if form_tugas.is_valid():
        # save the form data to model
        form_tugas.save()
        return HttpResponseRedirect(redirect_to=reverse('tugas_list'))
    context = {
        "head": 'tugas',
        "segment": "create-tugas",
        "form_tugas": form_tugas,
    }

    html_template = loader.get_template("tugas/create.html")
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def get_tugas(request, tugas_id):
    data = Tugas.objects.get(id=tugas_id)
    context = {
        "head": 'tugas',
        "segment": "detail-tugas",
        "data": data
    }
    html_template = loader.get_template("tugas/detail.html")
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def delete_tugas(request, tugas_id):
    obj = get_object_or_404(Tugas, id=tugas_id)
    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect(redirect_to=reverse('tugas_list'))


@login_required(login_url='/login/')
def mark_as_done(request, tugas_id):
    tugas = Tugas.objects.get(id=tugas_id)
    tugas.status = not tugas.status
    tugas.save()
    if request.POST["goto"]:
        dest = request.POST["goto"]
        return HttpResponseRedirect(redirect_to=reverse(dest))
    else:
        return HttpResponseRedirect(redirect_to=reverse('tugas_get', kwargs={'tugas_id': tugas_id}))


@login_required(login_url="/login/")
def edit_tugas(request, tugas_id=None):
    # fetch the object related to passed id
    obj = get_object_or_404(Tugas, id=tugas_id)

    # pass the object as instance in form
    form = TugasForm(instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if request.method == "POST":
        form = TugasForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(redirect_to=reverse('tugas_get', kwargs={'tugas_id': tugas_id}))

    context = {
        "page": "tugas",
        "segment": "edit-tugas",
        "form": form,
    }
    # add form dictionary to context
    html_template = loader.get_template("tugas/edit.html")
    return HttpResponse(html_template.render(context, request))


"""MK"""


@login_required(login_url="/login/")
def create_mk(request):
    form = MatkuliahForm(request.POST or None, request.FILES or None)
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        return HttpResponseRedirect('/mk')
    context = {
        "head": 'mk',
        "segment": "create-mk",
        "form": form
    }

    html_template = loader.get_template("mata_kuliah/create.html")
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def get_mk(request, mk_id):
    data = MataKuliah.objects.get(id=mk_id)
    context = {
        "head": 'mk',
        "segment": "list-mk",
        "data": data,
    }
    html_template = loader.get_template("mata_kuliah/detail.html")
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def delete_mk(request, mk_id):
    obj = get_object_or_404(MataKuliah, id=mk_id)
    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect(redirect_to=reverse('mk_list'))


@login_required(login_url="/login/")
def edit_mk(request, mk_id=None):
    # fetch the object related to passed id
    obj = get_object_or_404(MataKuliah, id=mk_id)

    # pass the object as instance in form
    form = MatkuliahForm(instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if request.method == "POST":
        form = MatkuliahForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(redirect_to=reverse('mk_get', kwargs={'mk_id': mk_id}))

    context = {
        "segment": "edit-mk",
        "form": form,
    }

    # add form dictionary to context
    html_template = loader.get_template("mata_kuliah/edit.html")
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def list_mk(request):
    data = MataKuliah.objects.all()
    context = {
        "head": 'mk',
        "segment": "list-mk",
        "data": data,
    }

    html_template = loader.get_template("mata_kuliah/list.html")
    return HttpResponse(html_template.render(context, request))


"""AUTH"""


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split("/")[-1]

        if load_template == "admin":
            return HttpResponseRedirect(reverse("admin:index"))
        context["segment"] = load_template

        html_template = loader.get_template("home/" + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:
        try:
            load_template = request.path.split("/")[-1]

            if load_template == "admin":
                return HttpResponseRedirect(reverse("admin:index"))
            context["segment"] = load_template

            html_template = loader.get_template("tugas/" + load_template)
            return HttpResponse(html_template.render(context, request))

        except template.TemplateDoesNotExist:

            html_template = loader.get_template("home/page-404.html")
            return HttpResponse(html_template.render(context, request))

        except:
            html_template = loader.get_template("home/page-500.html")
            return HttpResponse(html_template.render(context, request))


    except:
        html_template = loader.get_template("home/page-500.html")
        return HttpResponse(html_template.render(context, request))
