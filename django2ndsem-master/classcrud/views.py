from django.shortcuts import render
from django.utils import timezone

from django.urls import reverse_lazy #url wrapper
from django.views.generic.list import ListView #데이터를 보여주기 위함
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView #데이터 생성, 업데이트 삭제 위함
from .models import ClassBlog

# Create your views here.
def main(request):
    return render(request, 'main.html')

class BlogView(ListView): #블로그의 글들을 띄워주기 위함
    model = ClassBlog #클래스블로그라는 모델에 있는 객체들을 보도록 하겠다!

class BlogCreate(CreateView): #글을 작성하기 위함.
    model = ClassBlog #클래스블로그에 정의한 형식대로 적고 싶어!
    fields = ['title', 'body']
    success_url = reverse_lazy('list') #리다이렉션입니다. 성공했다면 해당 url로 넘겨줍니다. 

class BlogDetail(DetailView): #상세 객체를 봅니다.
    model = ClassBlog

class BlogUpdate(UpdateView): #글을 수정합니다.
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')

class BlogDelete(DeleteView): #글을 지웁니다. 
        model = ClassBlog
        success_url = reverse_lazy('list')