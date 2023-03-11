from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, AddComment
#adding pagination
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
#Python function to recive a web request and return a web response

#we see the list of the all posts
class HomeView(ListView):
    model = Post
    queryset = Post.published.all()
    context_object_name = 'posts'
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        #get all categories
        cat_menu = Category.objects.all()
        # change them to dict and redirect on website
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        #get all categories
        cat_menu = Category.objects.all()

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes_func()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        # change them to dict and redirect on website
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    #fields = ('title', 'body')

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'
    #fields = ('title', 'body')

    
def CategoryViewPost(request, cat):
    category_posts = Post.objects.filter(category=cat.replace('-', ' '))

    return render(request, 'category_post.html', { 'cat':cat.title().replace('-', ' '), 'category_posts': category_posts})



    
def CategoryViewList(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_lists.html', { 'cat_menu_list': cat_menu_list})

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title','slug','body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class AddComment(CreateView):
    model = Comment
    form_class = AddComment
    template_name = 'add_comment.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)