from django.shortcuts import render
from .forms import FeedbackForm, BlogForm, ComentForm
from .models import Blog, Coment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
from django.views.generic import DetailView
from random import randint

def index(request):
    signup(request)
    reg = UserCreationForm()
    login_form(request)
    log = AuthenticationForm()
    all_blogs = list(Blog.objects.all())
    print('--->' + str(all_blogs))
    blogs = list()
    for i in range(0, 6):
        blogs.append(all_blogs.pop(randint(0,len(all_blogs)-1)))
        if len(all_blogs) == 0:
            break
    print('--->' + str(blogs))
    return render(request, 'main/index.html', {'reg': reg, 'log':log, 'blogs': blogs})

def about(request):
    signup(request)
    reg = UserCreationForm()
    login_form(request)
    log = AuthenticationForm()
    return render(request, 'main/about.html', {'reg': reg, 'log':log})

def feedback(request):
    signup(request)
    reg = UserCreationForm()
    login_form(request)
    log = AuthenticationForm()
    if request.method == 'POST' and request.POST.get('submit') == 'feedback':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data = dict(form.clean())
            if data['notice']:
                data['notice'] = 'Yes'
            else:
                data['notice'] = 'No'
            match data['gender']:
                case '1':
                    data['gender'] = 'Male'
                case '2':
                    data['gender'] = 'Female'
            for i in FeedbackForm.internet_choices:
                if data['internet'] in i:
                    data['internet'] = i[1]
                    
            form = None
    else:
        form = FeedbackForm()
        data = None
    
    return render(request, 'main/feedback.html', {'form': form,
                                                  'data': data,
                                                  'reg': reg,
                                                  'log':log})

def useful_resources(request):
    signup(request)
    reg = UserCreationForm()
    login_form(request)
    log = AuthenticationForm()
    return render(request, 'main/useful_resources.html', {'reg': reg, 'log':log})

def blog(request):
    signup(request)
    reg = UserCreationForm()
    login_form(request)
    log = AuthenticationForm()
    blogs = Blog.objects.all()
    return render(request, 'main/blog.html', {'reg': reg, 'log':log, 'blogs': blogs})

def add_blog(request):
    signup(request)
    reg = UserCreationForm()
    login_form(request)
    log = AuthenticationForm()
    print('--->' + str(dict(request.FILES)))
    if request.method == 'POST' and request.POST.get('submit') == 'add_blog':
        new_blog = Blog.objects.create(author=request.user, 
                                       title=request.POST.get('title'), 
                                       img=request.FILES['img'], 
                                       description=request.POST.get('description'),
                                       content=request.POST.get('content'))
    add_blog = BlogForm()
    return render(request, 'main/add_blog.html', {'reg': reg, 'log':log, 'add_blog': add_blog})

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'main/blog_detail_view.html'
    context_object_name = 'blog'
    extra_context = {'coment_form': ComentForm(),
                     'reg': UserCreationForm(),
                     'log':AuthenticationForm()}

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        signup(request)
        login_form(request)
        if request.POST.get('submit') == 'coment':
            coment = Coment.objects.create(user=request.user,
                                           coment=request.POST.get('coment'))
            Blog.objects.get(pk=pk).coments.add(coment)
            print('--->' + str(Blog.objects.get(pk=pk)))
        return redirect('blog-detail', pk=pk)


def signup(request):
    if request.method == 'POST' and request.POST.get('submit') == 'signup':
        regform = UserCreationForm(request.POST)
        if regform.is_valid():
            user = regform.save()
            login(request, user)
            #return redirect(request.META['HTTP_REFERER'])

def login_form(request):
    if request.method == 'POST' and request.POST.get('submit') == 'login':
        log = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        login(request, log)

