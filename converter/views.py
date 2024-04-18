# converter/views.py

from django.shortcuts import render, redirect
from .forms import TextInputForm
from .utils import text_to_html

def text_input(request):
    if request.method == 'POST':
        form = TextInputForm(request.POST)
        if form.is_valid():
            text_input = form.save()
            text_input.html_output = text_to_html(text_input.text)
            text_input.save()
            return redirect('text_input')
    else:
        form = TextInputForm()
    return render(request, 'text_input.html', {'form': form})
