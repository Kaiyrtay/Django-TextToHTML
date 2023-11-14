from django.shortcuts import render
from .forms import EditorForm
# Create your views here.


def index(request):
    form = EditorForm()
    context = {'form': form}
    return render(request, 'index.html', context=context)
