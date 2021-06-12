from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__ (self):
        return self.title

    def get_absolute_url(self): # die get_absolute_url funktion kann über das model zur zugeordnete (mit der selben PK) detail url navigieren
        return reverse("blog-detail", kwargs={"pk": self.pk})
    
    
"""
https://stackoverflow.com/questions/54964703/redirect-vs-reverse-django

Reverse and redirect have a different meaning. 
Here is a simple explanation:

reverse in Django is used to find the URL of a given resource. 
Let's say that you have a blog website and from the main page, 
you want to provide links to your blog posts. You can of course
just hard-code /posts/123/ and just change the ID of your blog
post in URL, but that makes it hard to change your URL for the
post in the future. That's why Django comes with reverse
function. All you need to do is to pass the name of
your URL path (defined in your urlpatterns) and Django
will find for you the correct URL. It is called reverse
because it is a reverse process of determining which view
should be called for a given URL (which process is called
resolving).

Redirects are not specific to Django or any other web frameworks. Redirect means that for a given URL (or action), the user should be instructed to visit a specific URL. This can be done by sending a special redirect request and from there the browser will handle it for the user, so no user action is required in that process. You can use reverse in redirect process to determine the URL that the user should be redirected to.
"""



