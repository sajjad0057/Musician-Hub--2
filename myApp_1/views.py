from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView,ListView, DetailView , CreateView, UpdateView , DeleteView
from myApp_1 import models
from django.urls import reverse_lazy



# Create your views here .
#
# class IndexView(TemplateView):
#     template_name = 'myApp_1/index.html'
#     def get_context_data(self,**kwargs):
#         x = super().get_context_data(**kwargs)
#         x['text_1']='Text 1 blalalalalaala'
#         x['text_2']='Text 22222 blalalalalaala'
#         return x



class IndexView(ListView):
    context_object_name = 'musician_list'
    model = models.Musician
    template_name = 'myApp_1/index.html'

class MusicianDetail(DetailView):
    context_object_name = 'musician'
    model = models.Musician
    template_name = 'myApp_1/musician_details.html'


class AddMusician(CreateView):
    fields = ('first_name','last_name','instrument')
    model = models.Musician
    template_name = 'myApp_1/musician_form.html'


class UpdateMusician(UpdateView):
    fields = ('first_name','last_name','instrument')
    model = models.Musician
    template_name = 'myApp_1/musician_form.html'

class DeleteMusician(DeleteView):
    context_object_name = 'musician'
    model = models.Musician
    template_name = 'myApp_1/delete_musician.html'
    success_url = reverse_lazy('myApp_1:index')
