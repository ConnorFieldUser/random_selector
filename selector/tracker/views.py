from django.shortcuts import render

from django.views.generic import ListView, DetailView

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView


from tracker.models import List

# Create your views here.


class ListListView(ListView):
    template_name = 'index.html'
    model = List
    # def get_context_data(self):
    #     return List.objects.filter(creator=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transactions'] = List.objects.filter(creator=self.request.user)
        return context


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"


class ListDetailView(DetailView):
    model = List


class ListCreateView(CreateView):
    model = List
    success_url = "/"
    fields = ('name', 'description')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.creator = self.request.user
        return super().form_valid(form)
