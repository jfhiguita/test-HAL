"""Poll views"""

# Django
from django.shortcuts import render, redirect

from .forms import CreateQuestionsForm
from .models import Questions


def home(request):
    """Home Page"""
    poll = Questions.objects.all()
    context = {'poll': poll}
    return render(request, 'home.html', context)


def create(request):
    """Create Page"""
    if request.method == 'POST':
        form = CreateQuestionsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateQuestionsForm()
    context = {'form': form}
    return render(request, 'create.html', context)
