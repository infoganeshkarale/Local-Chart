from django.shortcuts import render, redirect
from .models import PMSData
from .forms import PMSDataFrom

# Create your views here.

def index(request):
    data = PMSData.objects.all()
    context = {
        'data': data,
    }
    return render(request, 'dashboard/index.html', context)

def addinfo(request):
    if request.method == 'POST':
        form = PMSDataFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PMSDataFrom()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/addinfo.html', context)


#next funcation