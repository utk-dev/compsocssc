from django.shortcuts import render, redirect
from .models import Submission
from .forms import SubmissionForm


def home(request):
    data = {}
    template = 'logo/home.html'
    if request.method == 'GET':
        form = SubmissionForm()
    else:
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('logo:success')
        else:
            form = SubmissionForm()
    data['form'] = form
    return render(request, template, data)


def success(request):
    template = 'logo/success.html'
    return render(request, template)
