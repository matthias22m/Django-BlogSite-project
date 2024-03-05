from django.shortcuts import render
from django.views.generic import ListView,DetailView
from Blog.models import Post, Comment


bool = {
"home" : False,
"detail" : False
}

def blogs_all(request):
    posts = Post.objects.all().order_by("-created_on")
    
    bool["home"] = True
    bool["detail"] = False
    
    context = { "posts":posts, "bool":bool}
    
    return render(request,"blog/index.html",context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts' 
    ordering = ['-created_on']
    
class PostDetailView(DetailView):
    model = Post
    # tamplate_name = 'blog/post_detail.html'
    
    


def blog_categories(request,category):
    posts = Post.objects.filter(categories__name__contain = category).order_by('-created_on')    
    
    context = { "posts":posts, "category":category, "bool":bool }
    
    return render(request, "blog/category.html", context)


def blog_detail(request,pk):
    post = Post.objects.get(pk=pk)
    category = post.catagory
    bool["detail"] = True
    bool["home"] = False
    
    comments = Comment.objects.filter(post = post).order_by('-created_on')
    
    context = { "post":post , "comments":comments , "category":category, "bool":bool }
    
    return render(request, "blog/detail.html", context)