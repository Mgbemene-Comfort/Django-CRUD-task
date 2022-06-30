from ast import Return
from dataclasses import fields
from multiprocessing import context
from pydoc import render_doc
from pyexpat import model
from sre_constants import SUCCESS
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
# Create your views here.
from .models import Post

def PostListView(Post):
    context = {}
    model = Post
    Return render(Post, 'Blog/post_list.html', context)

def PostCreateView(Post):
    context = {}
    model = Post
    fields = "__all__"
    SUCCESS_url = reverse_lazy("blog:all")
    Return render(Post, 'Blog/post_list.html', context)

def PostDetailsView(Post):
    context = {}
    model = Post

def PostUpdateView(Post):
    model = Post
    fields = "__all__"
    SUCCESS_url = reverse_lazy("blog:all")

def PostDeleteView(Post):
    model = Post
    fields = "__all__"
    SUCCESS_url = reverse_lazy("blog:all")
