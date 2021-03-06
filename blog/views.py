from crispy_forms.utils import render_crispy_form
from django.template.context_processors import csrf
from django.utils import timezone
from .models import Post,Feedback
from .forms import PostForm,FeedbackForm
from django.views.generic import View,ListView, CreateView, DetailView, UpdateView,FormView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.core.mail import send_mail

from django.http import JsonResponse


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


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        ctx = {}
        ctx.update(csrf(request))
        response = {'form': render_crispy_form(form, context=ctx)}
        return JsonResponse(response)

    def form_valid(self, form):
        self.object = form.save()
        return JsonResponse({'success': True})

    def form_invalid(self, form):
        ctx = {}
        ctx.update(csrf(self.request))
        form_html = render_crispy_form(form, context=ctx)
        return JsonResponse({'success': False, 'form_html': form_html})

class PostDelete(DeleteView):
    model = Post

    def get_success_url(self):
        return reverse('post_list')

class PostFeedback(FormView):
    template_name = 'blog/post_feedback.html'
    form_class = FeedbackForm
    success_url = 'list/'

    def form_valid(self, form):
        # send the email
        send_mail('Feedback', form.cleaned_data['feedback'],
                  form.cleaned_data['email'], ['inesmiled@softcatalyst.com'])

        return  super().form_valid(form)


class PostFeedbackList(ListView):
    model = Feedback
    context_object_name = 'feedbacks'
    template_name = 'blog/post_feedbackList.html'

