from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post,Feedback
from .forms import PostForm,FeedbackForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView,FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse



# Create your views here. ** for newbranch**

class PostList(ListView):
    model = Post
    context_object_name = 'posts'


class PostCreate(LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = 'blog/post_edit.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.published_date = timezone.now()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class PostUpdate(LoginRequiredMixin, UpdateView):
    form_class = PostForm

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})

class PostFeedback(FormView):
    template_name = 'blog/post_feedback.html'
    form_class = FeedbackForm
    success_url = 'list/'

class PostFeedbackList(ListView):
    model = Feedback
    context_object_name = 'feedbacks'
    template_name = 'blog/post_feedbackList.html'

