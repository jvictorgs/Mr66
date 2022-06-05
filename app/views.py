from django.shortcuts import render, redirect
from app.forms import MotosForm, ComprasForm
from app.models import Motos, Compras
from django.core.paginator import Paginator

def home(request):
    data = {}
    all = Motos.objects.all()
    paginator = Paginator(all, 10)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    return render(request, 'listmotos.html', data)

def form(request):
    data = {}
    data['form'] = MotosForm()
    return render(request, 'cadmotos.html', data)

def form1(request):
    data = {}
    data['form1'] = ComprasForm()
    return render(request, 'cadclientes.html', data)

def create(request):
    form = MotosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def create1(request):
    form = ComprasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cad')

def view(request, pk):
    data = {}
    data['db'] = Motos.objects.get(pk=pk)
    return render(request, 'visumotos.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Motos.objects.get(pk=pk)
    data['form'] = MotosForm(instance=data['db'])
    return render(request, 'cadmotos.html', data)

def edit1(request, pk):
    data = {}
    data['db'] = Compras.objects.get(pk=pk)
    data['form1'] = ComprasForm(instance=data['db'])
    return render(request, 'cadclientes.html', data)

def update(request, pk):
    data = {}
    data['db'] = Motos.objects.get(pk=pk)
    form = MotosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def update1(request, pk):
    data = {}
    data['db'] = Compras.objects.get(pk=pk)
    form = ComprasForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('cad')

def delete(request, pk):
    db = Motos.objects.get(pk=pk)
    db.delete()
    return redirect('home')

def delete1(request, pk):
    db = Compras.objects.get(pk=pk)
    db.delete()
    return redirect('cad')

def cad(request):
    data = {}
    all = Compras.objects.all()
    paginator = Paginator(all, 10)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    return render(request, 'listclientes.html', data)