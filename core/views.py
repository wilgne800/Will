from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import ContatoForm
from django.contrib import messages

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def form_valid(self, form, *args, **kwargs):
        form.send_email()
        messages.success(self.request, 'Email enviado com sucesso!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        form.send_email()
        messages.success(self.request, 'Erro ao enviar o email!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)
