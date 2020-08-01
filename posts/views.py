from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
# одна строка вместо тысячи слов на SQL
    latest = Post.objects.order_by("-pub_date")[:10]
    # собираем тексты постов в один, разделяя новой строкой
    output = []
    for item in latest:
        output.append(item.text)
    return render(request, "index.html", {"posts": latest})

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by("-pub_date")[:12] #posts - это список?
    return render(request, "group.html", {"group": group, "posts": posts})