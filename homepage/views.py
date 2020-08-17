from django.shortcuts import render
from .models import History
from .forms import InputForm
import subprocess

# Create your views here.
def index_view(request):
    #Howard Post assisted me with this code
    output = ''
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            History.objects.create(text=data.get('text'))
            text = data.get('text')
            output = subprocess.check_output(['cowsay', text], text=True)
            
    form = InputForm()
    return render(request, 'index.html', {'form': form, 'output': output})


def history_view(request):
    data = History.objects.all()[:10]
    return render(request, 'history.html', {'data': data})        


