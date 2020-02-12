from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserLoginForm,PostForm,Subscribe,CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy,reverse
from django.views.generic.edit import CreateView
from django.contrib.auth import login, authenticate,logout
from .models import CustomUser,Post,Comment
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.template.loader import render_to_string
from myproject.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


# Create your views here.

"""class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'"""


def home(request):

    return render(request,'blog/home.html')

def log_out(request):
    logout(request)
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {"posts" : posts })

def signup(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            #raw_password = form.cleaned_data.get('password')
            #job = form.cleaned_data.get('job')
            #bio = form.cleaned_data.get('bio')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            return redirect('blog:login')
    else:
        form = UserLoginForm()
        return render(request, 'blog/signup.html', {'form': form})


def subscribe(request):
    form = Subscribe(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            #email = 'cs100priya@gmail.com'
            email = form.cleaned_data['Email']
            html_message = render_to_string('blog/email.html',{'msg':'thanks for choosing us'})
            message = "hello"
            subject="Blog subscribe"
            print(email)
            send_mail(subject,message=message,from_email=EMAIL_HOST_USER,recipient_list=[email,],html_message=html_message)
            return render(request,'blog/success_email.html',{'email':email })
        else:
            error = "invalid form"
            return render(request, 'blog/subscribe.html', {'form':form,'error':error})
    
    return render(request, 'blog/subscribe.html',{'form':form} )

    



    


def post_list(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'blog/post_list.html', {"posts" : posts })

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #print(post.author)
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_list')
    
    else:

        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print(post.author)
    user = request.user
    print(user)
    return render(request, 'blog/post_detail.html', {'post': post,"user":user})

"""def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment = post.comments.filter( parent__isnull= True)
    if request.method == "POST":
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            parent_id = request.POST.get('comment_id')
            comment_os = None
            if parent_id:
                comment_os = Comment.objects.get(id=parent_id)  

            comment = Comment.objects.create(post=post,parent=comment_os)
            comment.save()

            
            return redirect('blog:post_detail',pk=post.pk)

    form = CommentForm()
    print(post.author)
    user = request.user
    print(user)
    return render(request, 'blog/post_detail.html', 
        {'post': post,"user":user,'form':form,'comment':comment})"""

def myblogs(request):
    user = request.user
    print(user)
    post = Post.objects.filter(author=user)
    return render(request, 'blog/post_list.html', {'post': post,"user":user})





#----to add comment on blog post---functions---->**********
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


def approved_comments(self):
    return self.comments.filter(approved_comment=True)


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog:post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('blog:post_detail', pk=comment.post.pk)

"""def reply(request,pk):
    post = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():"""




#---comment ends here---->***********





@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_list')
            
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_new.html', {'form': form})