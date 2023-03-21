from django.shortcuts import render, redirect
from .models import TextObject
from .forms import TextForm

# Create your views here.


def index(request):
    objs = TextObject.objects.all()
    return render(request, 'object_editor/index.html', context={'objs': objs})


def edit_page(request, pk):
    obj = TextObject.objects.get(id=pk)

    if request.method == 'POST':
        form = TextForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('objs:index')
    else:
        form = TextForm(instance=obj)
        
    return render(request, 'object_editor/edit_page.html', context={'obj': obj, 'form': form})


def delete_page(request, pk):
    obj = TextObject.objects.get(id=pk)

    if request.method == 'POST':
        obj.delete()
        return redirect('objs:index')

    return render(request, 'object_editor/delete_page.html', context={'obj': obj})
