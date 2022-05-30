from django.shortcuts import render
from .models import Blog
# Create your views here.
#def home_view(request):
def home_view(request):
    blogobject = Blog.objects.all()
    context = {'blogobject':blogobject}
    return render(request, 'index.html', context)