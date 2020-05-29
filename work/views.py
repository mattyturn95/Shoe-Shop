from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.utils import timezone
from django.contrib import messages
from posts.models import Post
from posts.forms import BlogPostForm


def work(request):
    """A view that displays the work page"""
    posts = Post.objects.filter(published_date__lte=timezone.now()
                                ).order_by('-published_date')
    return render(request, "work.html", {'posts': posts})
