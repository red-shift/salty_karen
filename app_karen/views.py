from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy

from .models import KarenPost, Comment
from .forms import KarenPostForm, UpdateCommentForm


# <editor-fold desc="Karen Post Views">
class IndexView(ListView):
    model = KarenPost
    template_name = 'app_karen/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return super().get_queryset().order_by('-created_at')


class KarenPostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = KarenPost
    template_name = 'app_karen/forms/post-create.html'
    form_class = KarenPostForm
    success_url = reverse_lazy('index')
    success_message = 'Karen post has been created!'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class KarenPostDetailView(DetailView):
    model = KarenPost
    template_name = 'app_karen/karen-post-detail.html'
    context_object_name = 'post'


class KarenPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = KarenPost
    template_name = 'app_karen/forms/post-update.html'
    form_class = KarenPostForm
    success_url = reverse_lazy('index')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class KarenPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = KarenPost
    template_name = 'app_karen/confirm_delete_karenpost.html'
    context_object_name = 'post'
    success_url = reverse_lazy('index')
    success_message = 'Post has been successfully deleted!'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
# </editor-fold>


# <editor-fold desc="Comment Views">
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'base/base.html'
    # Use fields attribute to submit to form from another view, otherwise use form_class
    fields = ['content']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = KarenPost.objects.get(slug=self.kwargs['slug'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post-detail', kwargs={'slug': self.kwargs['slug']})


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    template_name = 'app_karen/forms/comment-update.html'
    form_class = UpdateCommentForm

    def get_object(self):
        return Comment.objects.get(uuid=self.kwargs.get('uuid'))

    def get_success_url(self):
        comment = self.get_object()
        return reverse('post-detail', kwargs={'slug': comment.post.slug})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Comment
    template_name = 'app_karen/confirm_delete_comment.html'
    context_object_name = 'comment'
    success_message = 'Comment has been successfully deleted!'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    def get_object(self):
        return Comment.objects.get(uuid=self.kwargs.get('uuid'))

    def get_success_url(self):
        comment = self.get_object()
        return reverse('post-detail', kwargs={'slug': comment.post.slug})
# </editor-fold>


# <editor-fold desc="Karen Post Views">
class AdminPostsReviewView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = KarenPost
    template_name = 'app_karen/admin-posts-review.html'
    context_object_name = 'posts'

    def test_func(self):
        return self.request.user.is_superuser

    def get_queryset(self):
        return super().get_queryset().order_by('-created_at')


class AdminCommentsReviewView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = KarenPost
    template_name = 'app_karen/admin-comments-review.html'
    context_object_name = 'comments'

    def test_func(self):
        return self.request.user.is_superuser

    def get_queryset(self):
        return super().get_queryset().order_by('-created_at')

# </editor-fold>
