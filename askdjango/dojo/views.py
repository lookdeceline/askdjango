from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import HttpResponse
import os
# Create your views here.
from .models import Post
from . import models
from . import forms


def post_new(request):
    if request.method == 'POST':
        form = forms.PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            # post = models.Post(title = form.cleaned_data['title'],
            #                    content = form.cleaned_data['content'])

            #or
            # post = models.Post.objects.create(title = form.cleaned_data['title'],
            #                    content = form.cleaned_data['content'])

            # or
            # post = models.Post.objects.create(**form.cleaned_data)
            post.save()
            return redirect('/dojo/')
    else:
        form = forms.PostForm()
    return render(request, 'dojo/post_form.html', {
        'form':form,
    })


def post_edit(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        form = forms.PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            # post = models.Post(title = form.cleaned_data['title'],
            #                    content = form.cleaned_data['content'])

            #or
            # post = models.Post.objects.create(title = form.cleaned_data['title'],
            #                    content = form.cleaned_data['content'])

            # or
            # post = models.Post.objects.create(**form.cleaned_data)
            post.save()
            return redirect('/dojo/')
    else:
        form = forms.PostForm(instance=post)
    return render(request, 'dojo/post_form.html', {
        'form':form,
    })


def mysum(request, x):
    return HttpResponse(x + 100)

def hello(request, name, age):
    return HttpResponse('Hi. I am {} and I am {} years old.'.format(name, age))

# w/out template
def post_list1(request):
    name = 'celine'
    return HttpResponse('''
        <h1>AskDjango</h1>
        <p>{user_name}</p>
        <p>this is a post_list1 test.</p>
        '''.format(user_name = name))

# using template
# maps this function to 'templates/dojo/post_list2.html'
def post_list2(request):
    name = 'celine'
    return render(request, 'dojo/post_list2.html', {'user_name': name})


# def post_list3(request):
#     return JsonResponse({
#         'message': 'message blank. now returning JsonResponse.',
#         'items': ['python', 'django', 'celery','azure','aws'],
#     }, json_dumps_params={'ensure_ascii': False})


# download attachment request
def excel_download(request):
    #filepath = '/home/celine/example.xls'
    filepath = os.path.join(settings.BASE_DIR, 'example.xls')
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type = 'application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename ="{}"'.format(filename)
        return response