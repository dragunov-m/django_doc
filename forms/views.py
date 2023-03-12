from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .forms import ModelForm, NotModelForm
from .models import *


def index(request):
    return render(request, 'forms/index.html', {})


def objects_view(request):
    obj = Text.objects.all()
    return render(request, 'forms/obj_view.html', {'obj': obj})


def form_1(request):
    text = request.GET.get('text', '')
    if text:
        if len(text) > 3:
            raise ValidationError('Your chars is bigger then 3')
        model = Text(text=text)
        if Text.objects.filter(text=text).exists():
            obj_exists_err = 'Your object is already exists'
            return render(request, 'forms/form_1.html', {'error': obj_exists_err})
        else:
            model.save()
            return redirect('forms:objs')
    return render(request, 'forms/form_1.html')


def form_2(request):
    text = request.POST.get('text', '')
    if text:
        if len(text) > 3:
            raise ValidationError('Your chars is bigger then 3')
        model = Text(text=text)
        if Text.objects.filter(text=text).exists():
            obj_exists_err = 'Your object is already exists'
            return render(request, 'forms/form_2.html', {'error': obj_exists_err})
        else:
            model.save()
            return redirect('forms:objs')
    return render(request, 'forms/form_2.html')


def form_3(request):
    text = request.GET.get('text', '')
    if text:
        form = ModelForm(request.GET)
        if form.is_valid():
            form.save()
            return redirect('forms:objs')
    else:
        form = ModelForm()
    return render(request, 'forms/form_3.html', {'form': form})


def form_4(request):
    text = request.GET.get('text', '')
    if text:
        form = ModelForm(request.GET)
        if form.is_valid():
            form.save()
            return redirect('forms:objs')
    else:
        form = ModelForm()
    return render(request, 'forms/form_4.html', {'form': form})


def form_5(request):
    if request.method == 'POST':
        form = ModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forms:objs')
    else:
        form = ModelForm()
    return render(request, 'forms/form_5.html', {'form': form})


def form_6(request):
    if request.method == 'POST':
        form = ModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forms:objs')
    else:
        form = ModelForm()
    return render(request, 'forms/form_6.html', {'form': form})


def form_7(request):
    if request.method == 'GET' and request.GET.get('text', ''):
        form = NotModelForm(request.GET)
        if form.is_valid():
            if Text.objects.filter(text=form.cleaned_data['text']).exists():
                form.add_error('text', 'Object already exists')
            else:
                form.save()
                return redirect('forms:objs')
    else:
        form = NotModelForm()
    context = {
        'form': form,
    }
    return render(request, 'forms/form_7.html', context)


def form_8(request):
    if request.method == 'POST':
        form = NotModelForm(request.POST)
        if form.is_valid():
            if Text.objects.filter(text=form.cleaned_data['text']).exists():
                form.add_error('text', 'Object already exists')
            else:
                form.save()
                return redirect('forms:objs')
    else:
        form = NotModelForm()
    context = {
        'form': form,
    }
    return render(request, 'forms/form_8.html', context)


def form_9(request):
    if request.method == 'GET' and request.GET.get('text', ''):
        form = NotModelForm(request.GET)
        if form.is_valid():
            if Text.objects.filter(text=form.cleaned_data['text']).exists():
                form.add_error('text', 'Object already exists')
            else:
                form.save()
                return redirect('forms:objs')
    else:
        form = NotModelForm()
    context = {
        'form': form,
    }
    return render(request, 'forms/form_9.html', context)


def form_10(request):
    if request.method == 'POST':
        form = NotModelForm(request.POST)
        if form.is_valid():
            if Text.objects.filter(text=form.cleaned_data['text']).exists():
                form.add_error('text', 'Object already exists')
            else:
                form.save()
                return redirect('forms:objs')
    else:
        form = NotModelForm()
    context = {
        'form': form,
    }
    return render(request, 'forms/form_10.html', context)
