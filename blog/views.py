from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.




# function based views

def home(request):
    context = {
        "posts" : Post.objects.all()
    }
    return render(request, "blog/home.html", context)

class PostListView(ListView):
    model = Post
    template_name = "blog/home.html" # Standardtemplage = <app> / <model>_<viewtype>.html
    context_object_name = "posts"
    ordering = ['-date_posted'] # v10 ordering: sortiert  - dreht die sortierung um
    paginate_by = 2 #V11 hierdurch wird die Anzahl der Datensätze je Seite auf 2 begrenzt es fehlt aber noch an der Pagination im Template
                    # im browser blättern geht durch url: http://127.0.0.1:8000/blog/?page=2
    

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    # redirect erfolgt über get_absolute_url und reverse im model (methode)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # !!! ACHTUNG !!! die Mixins müssen links von der view - inheritance stehen
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    # redirect erfolgt über get_absolute_url und reverse im model (methode)

    def test_func(self): # die Vererbung UserPassesTestMixin ruft eine Funktion mit diesem Namen auf.
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self): # die Vererbung UserPassesTestMixin ruft eine Funktion mit diesem Namen auf.
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

    

def landing(request):
    return render(request, "blog/landing.html")

def about(request):
    return render(request, "blog/about.html")


# Class based views

