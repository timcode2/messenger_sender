from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main.models import Massage


def home_page(request):
    return render(request, "main/home.html")


class MassageListView(ListView):
    model = Massage


class MassageDetailView(DetailView):
    model = Massage


class MassageCreateView(CreateView):
    model = Massage
    fields = ('subject', 'subject_body')
    success_url = reverse_lazy('main:messenger_list')


class MassageUpdateView(UpdateView):
    model = Massage
    fields = ('subject', 'subject_body')
    success_url = reverse_lazy('main:messenger_list')


class MassageDeleteView(DeleteView):
    model = Massage
    success_url = reverse_lazy('main:messenger_list')
