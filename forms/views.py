from django.shortcuts import render
# from django.http import HttpResponse
from .forms import ModelForm, NotModelForm
from .models import *


def form_1(request):

    text = request.GET.get('text')
    error = 'This field is required'

    if text:
        if len(text) > 3:
            error = 'Your value bigger then 3 characters'
    else:
        text = ''

    return render(request, 'forms/form_1.html', {'text': text, 'error': error})


def form_2(request):

    text = request.POST.get('text')
    error = 'This field is required'

    if text:
        if len(text) > 3:
            error = 'Your value bigger then 3 characters'
    else:
        text = ''

    return render(request, 'forms/form_2.html', {'text': text, 'error': error})


def form_3(request):
    form = ModelForm()

    if request.method == 'GET':
        form = ModelForm(request.GET)
        form.text = request.GET.get('text')
        if form.is_valid():
            form.save()

    obj = Text.objects.all()
    return render(request, 'forms/form_3.html', {'form': form, 'obj': obj})


def form_4(request):
    form = ModelForm()

    if request.method == 'GET':
        form = ModelForm(request.GET)
        form.text = request.GET.get('text')
        if form.is_valid():
            form.save()

    obj = Text.objects.all()
    return render(request, 'forms/form_4.html', {'form': form, 'obj': obj})


def form_5(request):
    form = ModelForm()

    if request.method == 'POST':
        form = ModelForm(request.POST)
        form.text = request.POST.get('text')
        if form.is_valid():
            form.save()

    obj = Text.objects.all()
    return render(request, 'forms/form_5.html', {'form': form, 'obj': obj})


def form_6(request):
    form = ModelForm()

    if request.method == 'POST':
        form = ModelForm(request.POST)
        form.text = request.POST.get('text')
        if form.is_valid():
            form.save()

    obj = Text.objects.all()
    return render(request, 'forms/form_6.html', {'form': form, 'obj': obj})


def form_7(request):
    form = NotModelForm()

    if request.method == 'GET':
        form = NotModelForm(request.GET)
        form.text = request.GET.get('text')

    if form.text:
        if len(form.text) > 3:
            form.text = ''
    else:
        form.text = ''

    return render(request, 'forms/form_7.html', {'form': form, 'text': form.text})


def form_8(request):
    form = NotModelForm()
    text = ''

    if request.method == 'POST':
        form = NotModelForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text', '')

    return render(request, 'forms/form_8.html', {'form': form, 'text': text})


def form_9(request):
    form = NotModelForm()
    form.text = ''

    if request.method == 'GET':
        form = NotModelForm(request.GET)
        form.text = request.GET.get('text')

    return render(request, 'forms/form_9.html', {'form': form, 'text': form.text})


def form_10(request):
    form = NotModelForm()
    form.text = ''

    if request.method == 'POST':
        form = NotModelForm(request.POST)
        form.text = request.POST.get('text')

    return render(request, 'forms/form_10.html', {'form': form, 'text': form.text})
