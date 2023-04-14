from django.shortcuts import render, get_object_or_404
from .models import Post, Image, PostComments
from .forms import Post_form, Image_form, Image_Upload, UserCreate, PostCreate
from django.contrib.auth.forms import UserCreationForm, User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from functools import reduce
from django.http import HttpResponse
from django.core import signing
from django.core.paginator import Paginator


def all_posts(request):
    posts = Post.objects.all()       # assign all created posts to variable posts
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # next we want to render this post our html file in varaible
    return render(request, 'base/main.html', {'posts': page_obj})


def all_posts_inherit(request):
    posts = Post.objects.all()       # assign all created posts to variable posts
    images = Image.objects.all()
    print(images)
    image = lambda x:Image.objects.all().filter(post=x)

    # next we want to render this post our html file in varaible
    return render(request, 'base/detail.html',
                        {'posts': posts, 'images': images, 'fun': image})


def photos_to_posts(post_name):
    photos = Image.objects.all().filter(post=post_name)
    return photos


def post_detail(request, title):
    post = get_object_or_404(Post, title=title)
    print(post)
    comments = PostComments.object.all().filter(post=post)

    if request.method == "POST":
        username = request.session['name']
        user_obj = User.objects.all().get(username=username)
        try:
            post_count = PostComments.object.all().filter(user=user_obj)
            if post_count.count() < 18:
                try:
                    obj, post_form = PostComments.object.get_or_create(post=post, user=user_obj, text=request.POST['text'])
                    if post_form:
                        obj.save()
                        return redirect('projects_list')
                except Exception as e:
                    print('form is invalid')
                    raise e
        except UnboundLocalError as e:
            print("too much comments")
            return redirect("post_list")
    else:
        post_form = PostCreate()
    return render(request, 'base/post_description.html', {'post_detail': post,
                                                          'comments': comments,
                                                          'post_form': post_form
                                                         })


# logical part - creating post
# check a exist of post
def post_validate(title):
    num_of_digits_title = len(list(x for x in title if x.isdigit()))
    titles = list(x[1] for x in Post.objects.all().values_list())
    if num_of_digits_title > 5:
        print("Too much nums in title")
        return False
    if title in titles:
        print("Error post in database")
        return False
    return True


def post_display(request, title):
    post_elements = Post.objects.all().filter(title=title)
    return render(request, 'base/post_description.html', {'data':post_elements})


@login_required()
def post_create(request):
    global image
    context = {}
    if request.method == 'POST':
        form = Post_form(request.POST)      # creat a form to inpout our data
        files = request.FILES.getlist("image")   # use to grab a photos from our post - name of field in db
        if form.is_valid():
            title = request.POST['title']
            content = request.POST['content']
            if post_validate(title):
                post_key = form.save()
                image = Image_form()
                for photo in files:
                    Image.objects.create(post=post_key, image=photo)
                return redirect('/website')
        else:
            print("Error")
    else:
        form = Post_form()
        image = Image_form()
    return render(request, 'base/form_post.html', {'form':form, 'image_add':image})
'''
def post_create(request):
    if request.method == 'POST':
        post_create = Post_form(request.POST)
        #files = request.FILES['upload_to']
        images = request.FILES.getlist('images')
        print(images)
        if post_create.is_valid():
            title = request.POST['title']
            content = request.POST['content']
            post = Post.objects.create(title=title, content=content)
            for image in images:
                Image.objects.create(post=post, upload_to=image)
            return redirect('/website')
    else:
        post_create = Post_form()
    return render(request, 'base/form_post.html', {'form':post_create})
'''


def title_key(title):
    '''
        This function return a list with all posts with [(id,title,content),(id,title,content)]
    '''
    return Post.objects.all().filter().values_list().filter(
        title=title)[0][0]


def display_images(request):
    photos = Image.objects.all(post='fsafsa')
    return render(request, 'base/photos.html', {"photos":photos})


def links_nav(request):
    pass


# function to create an objects of users
def register(request):
    form = UserCreate()
    if request.method == "POST":
        form = UserCreate(request.POST)
        if form.is_valid():
            form.save()
            print('ok')
            return redirect('login')
    return render(request, 'base/register.html', {'form': form})


# function to log in and start session
def login_page(request):
    if request.method == "POST":
        username = request.POST['login']
        password = request.POST['login_password']
        user = authenticate(request, username=username, password=password)
        request.session.modified = True
        context = {}
        if user is not None:
            request.session['name'] = username
            print(request.user.is_authenticated)
            #request.session['user'] = serializers.serialize('json', user_obj)
            print("ok")
            login(request, user)

            return redirect('post_list')

    return render(request, 'base/login.html')


# logout function
def log_out(request):
    logout(request)
    return redirect('post_list')

