from typing import Any
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from feed.forms import CommentForm, PostForm
from feed.models import PostModel
from accounts.models import Profile
from django.views.generic.edit import FormMixin
from django.db.models import Q
from django.http import JsonResponse
# Create your views here.

class SearchResultsView(LoginRequiredMixin, ListView):
    login_url = 'accounts:log_in'
    model = Profile
    template_name = "search_results.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['this_objects'] = self.get_queryset()
        print(context['this_objects'])
        return context
    
    def get_queryset(self):
        query = self.request.GET.get("q")
        this_objects = Profile.objects.filter(
            Q(username__icontains=query) | 
            Q(first_name__icontains=query) | 
            Q(email__icontains=query)
        )
        return this_objects
    
class FeedView(LoginRequiredMixin, ListView):
    login_url = 'accounts:log_in'
    template_name = 'feed.html'
    context_object_name = 'post_obj'
    model = PostModel


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['post_obj'] = PostModel.objects.all().order_by('date_add')
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = 'accounts:log_in'
    template_name = 'content/new_post.html'
    form_class = PostForm
    model = PostModel

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        print(kwargs)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
    def form_invalid(self, form):
        print(form.data)
        print(form.errors)
        print(self.request.POST.dict())
        return redirect('feed')
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect('feed')
 

def post_like_view(request):  
    post = PostModel.objects.get(id=request.POST.get('postid'))
    icon = ''
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        icon = '<i class="bi bi-heart text-danger fs-2"></i>'
    else:
        post.likes.add(request.user)
        icon = '<i class="bi bi-heart-fill text-danger fs-2"></i>'
    return JsonResponse({'count': post.likes.count(), 'icon': icon})


class PostDetailedView(LoginRequiredMixin, FormMixin, DetailView):
    login_url = 'accounts:log_in'
    template_name = 'detailed_post.html'
    model = PostModel
    form_class = CommentForm
    context_object_name = 'post'
    pk_url_kwarg = 'post_pk'

    def get_success_url(self, **kwargs) -> str:
        return reverse_lazy('feed')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.post_model = self.get_object()
        self.object.save()
        return super().form_valid(form)




    