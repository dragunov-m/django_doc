from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import *


def index(request):
    template = loader.get_template('posts/index.html')
    post_list = Posts.objects.all()
    user_list = User.objects.all()
    context = {
        'post_list': post_list,
        'user_list': user_list,
    }
    return HttpResponse(template.render(context, request))


def post_view(request):
    post_id = request.GET.get('id')
    post = get_object_or_404(Posts, id=post_id)
    comments = Comments.objects.all()
    template = loader.get_template('posts/post.html')
    context = {
        'object': post,
        'comments': comments,
    }
    return HttpResponse(template.render(context, request))


# Get parameter
def get_parameter(request):
    age = request.GET.get('age', 0)
    name = request.GET.get('name', 'Undefined')
    return HttpResponse(f'<h2>Name: {name} Age: {age}</h2>')

