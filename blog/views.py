from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        "author" : "Hugo",
        "title" : "Blog Post 1",
        "content" : "First Post content",
        "date_posted"  : "01.01.2020"
    },
        {
        "author" : "Hugine",
        "title" : "Blog Post 2",
        "content" : "second Post content",
        "date_posted"  : "02.01.2020"
    }

]




def home(request):
    context = {
        "posts" : posts
    }
    return render(request, "blog/home.html", context)

def landing(request):
    return render(request, "blog/landing.html")

def about(request):
    return render(request, "blog/about.html")
