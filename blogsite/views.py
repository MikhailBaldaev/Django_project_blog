from django.shortcuts import render, get_object_or_404
from blogsite.models import Myblog


# Create your views here.
def all_blogs(request):
    blog_list = Myblog.objects.all()
    context = {'articles': blog_list}
    return render(request, 'allblogs.html', context)


def blog_post(request, slug):
    a_blog = get_object_or_404(Myblog, slug=slug)
    context = {'a_blog': a_blog}
    return render(request, 'a_blog.html', context)
