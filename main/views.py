from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def display_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'main/blogs.html', {'blogs':blogs})

def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)  
        if form.is_valid():
            blog = form.save()
            print("Saved blog:", blog.title)
            return redirect('display_blogs')
        else:
            print("Form errors:", form.errors)
    else:
        form = BlogForm()
    return render(request, 'main/add_blog.html', {'form': form})


