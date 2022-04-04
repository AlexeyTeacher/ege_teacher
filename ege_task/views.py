from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddTaskForm
from .models import *
from .utils import *


class EgeTaskHome(DataMixin, ListView):
    model = Task
    template_name = 'ege_task/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Task.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        context.update(c_def)
        return context


def about(request):
    user_menu = menu.copy()
    if not request.user.is_authenticated:
        user_menu.pop(1)
    return render(request, "ege_task/about.html", {'title': "О сайте", 'menu': user_menu})


# class ShowTask(DetailView):
#     model = Task
#     template_name = 'ege_task/show_task.html'
#     slug_field = 'number_task_slug'


def show_task(request, number_task):
    task = get_object_or_404(Task, number_task=number_task)
    if task.video_url:
        video = task.video_url
        video = video.replace('https://youtu.be/', 'https://www.youtube.com/embed/')
        task.video_url = video
        task.save()
    user_menu = menu.copy()
    if not request.user.is_authenticated:
        user_menu.pop(1)
    context = {
        'task': task,
        'menu': user_menu,
        'title': task.title,
        'cat_selected': number_task
    }
    return render(request, "ege_task/show_task.html", context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')


class AddTask(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddTaskForm
    template_name = 'ege_task/add_task.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление страницы')
        context.update(c_def)
        return context


def contact(request):
    return render(request, "ege_task/contact.html", {'title': "Обратная связь"})


def login(request):
    return render(request, "ege_task/login.html", {'title': "Авторизация"})


class EgeTaskCategory(DataMixin, ListView):
    model = Task
    template_name = 'ege_task/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Task.objects.filter(is_published=True, cat__id=self.kwargs['cat_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=f"Made by {context['posts'][0].cat}",
                                      cat_selected=context['posts'][0].cat_id)
        context.update(c_def)
        return context

# def show_category(request, cat_id):
#     posts = Task.objects.filter(cat_id=cat_id)
#     if len(posts) == 0:
#         raise Http404
#     context = {'posts': posts,
#                'title': 'Отображение по рубрикам',
#                'cat_selected': cat_id
#                }
#     return render(request, "ege_task/index.html", context=context)
