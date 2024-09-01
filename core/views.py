from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import ContatoForm
from django.contrib import messages

class IndexView(FormView):
    template_name = 'index.html'
    success_url = reverse_lazy('index')


