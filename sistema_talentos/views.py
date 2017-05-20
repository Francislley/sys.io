from django.forms import ModelForm
from .models import *
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.

class PerfilForm(ModelForm):
    class Meta:
        model = Perfil
        fields = ['nome', 'cpf', 'email']


def perfil_list(request, template_name='perfil_list.html'):
    perfil = Perfil.objects.all()
    perfils = {'lista': perfil}
    return render(request, template_name, perfils)


def perfil_new(request, template_name='perfil_form.html'):
    form = PerfilForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('perfil_list')
    return render(request, template_name, {'form': form})


def perfil_edit(request, pk, template_name='perfil_form.html'):
    perfil = get_object_or_404(Perfil, pk=pk)
    if request.method == "POST":
        form = PerfilForm(request.POST, instance=perfil)
        if form.is_valid():
            perfil = form.save()
            return redirect('perfil_list')
    else:
        form = PerfilForm(instance=perfil)
    return render(request, template_name, {'form': form})


def perfil_remove(request, pk):
    perfil = Perfil.objects.get(pk=pk)
    if request.method == "POST":
        perfil.delete()
        return redirect('perfil_list')
    return render(request, 'perfil_delete.html', {'perfil': perfil})
