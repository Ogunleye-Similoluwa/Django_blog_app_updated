from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView, PasswordResetView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post


# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('list')


class PasswordReset(PasswordResetView):
    template_name = "Reset.html"
    model = Post


class Register(FormView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'create_post.html'
    success_url = reverse_lazy('list')


class PostListView(ListView):
    template_name = 'post_list.html'
    model = Post
    context_object_name = 'posts'


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    context_object_name = 'post'
    template_name = 'delete_post.html'

    def get_success_url(self):
        return reverse_lazy('list')


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    context_object_name = 'post'
    fields = ['title', 'body']
    template_name = 'update_post.html'

    def get_success_url(self):
        return reverse_lazy('list')
