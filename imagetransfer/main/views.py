from django.shortcuts import render,redirect
from .forms import PostForm
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'main/main.html')

def result(request):
    return render(request, 'main/result.html')

def FileUpload(request):
    
    if request.method == 'POST':
        title = request.POST['postname']
        img = request.FILES['mainphoto']
        contents = request.POST['contents']
        post = Post(postname=title, mainphoto=img, contents=contents)
        post.save()
        return redirect('post')
    
    else:
        postForm = PostForm
        context = {'postForm':postForm}
        return render(request, 'result.html', context)
