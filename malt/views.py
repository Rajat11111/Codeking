from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def home(request):
    my_title = "Hello there........."
    context = {"title": my_title}
    return render(request, "hello.html", context)


def about(request):
    title = "New advice in this file"
    context = {"title": title}
    template_name = 'about.html'
    template_obj = get_template(template_name)
    rendering = template_obj.render(context)
    return render(request, 'about.html', {"title": rendering})


def contact(request):
    title = "Some contacts"
    context = {"title": title}
    template_name = "hello.html"
    template_obj = get_template(template_name)
    rendering = template_obj.render(context)
    return render(request, 'hello.html', {"title": rendering})



def example(request):
    title = "Some examples of this file"
    context = {"title": title}
    template_name = "base.html"
    template_obj = get_template(template_name)
    rendering = template_obj.render(context)
    return render(request, 'base.html', {"title": rendering})