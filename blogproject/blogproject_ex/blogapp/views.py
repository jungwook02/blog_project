from urllib import request
from django.shortcuts import render , redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm,CommentForm

def home(request):
    # 블로그 객체들을 모조리 띄우는 코드
    # posts = Blog.objects.all()
    # 내가 가지고 오고 싶은 것을 필터링 해서 가져오는 것
    posts = Blog.objects.filter().order_by('-date')
    return render(request,'index.html',{'posts':posts})



# 블로그에 글 작성 html을 보내주는 함수
def new(request):
    return render(request,'new.html')

# 블로그에 글을 생성하게 해주는 함수
def create(request):
    if(request.method == 'POST'):
        post= Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home')


# django form 이용해서 입력값을 받는 함수
# get 요청과 (입력값을 받을 수 있는 html 갖다 줘야함)
# post 요청 (입력한 내용을 데이터베이스한테 저장,form 에서 입력한 내용을 처리)
# 둘 다 가능한 함수
def formcreate(request):
    
     # 입력을 받을 수 있는 html을 갖다주기
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')


    else:
        form = BlogForm()
    return render(request,'form_create.html',{'form':form})

# django modelform 으로 입력값을 받는 함수
def modelformcreate(request):
    if request.method == 'POST' or request.method == 'FILES' :
        form = BlogModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')


    else:
        form = BlogModelForm()
    return render(request,'form_create.html',{'form':form})



def detail(request,blog_id):
    # blog_id 번째 블로그 글을  데이터베이스로부터 갖고와서
    blog_detail = get_object_or_404(Blog, pk=blog_id) 
    # blog_id 번쨰 블로그 글을 detail.html로 띄워주는 코드
    

    comment_form = CommentForm()

    return render(request, 'detail.html',{'blog_detail':blog_detail, 'comment_form':comment_form})


def create_comment(request,blog_id):
    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():
       finished_form = filled_form.save(commit=False)
       finished_form.post = get_object_or_404(Blog,pk=blog_id)
       finished_form.save()

    return redirect('detail',blog_id)