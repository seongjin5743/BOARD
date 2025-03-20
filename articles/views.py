from django.shortcuts import render, redirect
from .models import Article

# 'articles' 앱의 메인 페이지를 렌더링하는 함수
def index(request):
    articles = Article.objects.all()  # 모든 Article 객체를 가져옴
    context = {
        'articles': articles  # 템플릿에 전달할 데이터
    }
    return render(request, 'index.html', context)

# 특정 Article의 상세 페이지를 렌더링하는 함수
def detail(request, id):
    article = Article.objects.get(id=id)  # 주어진 id에 해당하는 Article 객체를 가져옴
    context = {
        'article': article  # 템플릿에 전달할 데이터
    }
    return render(request, 'detail.html', context)

# 새로운 Article을 작성하는 페이지를 렌더링하는 함수
def new(request):
    return render(request, 'new.html')

# 새로운 Article을 생성하고 저장하는 함수
def create(request):
    title = request.POST.get('title')  # POST 요청에서 제목 데이터를 가져옴
    content = request.POST.get('content')  # POST 요청에서 내용 데이터를 가져옴
    article = Article()  # 새로운 Article 객체 생성
    article.title = title  # 제목 설정
    article.content = content  # 내용 설정
    article.save()  # 데이터베이스에 저장
    return redirect('articles:detail', id=article.id)  # 생성된 Article의 상세 페이지로 리다이렉트

# 특정 Article을 삭제하는 함수
def delete(request, id):
    article = Article.objects.get(id=id)  # 주어진 id에 해당하는 Article 객체를 가져옴
    article.delete()  # Article 객체 삭제
    return redirect('articles:index')  # 메인 페이지로 리다이렉트

# 특정 Article을 수정하는 페이지를 렌더링하는 함수
def edit(request, id):
    article = Article.objects.get(id=id)  # 주어진 id에 해당하는 Article 객체를 가져옴
    context = {
        'article': article  # 템플릿에 전달할 데이터
    }
    return render(request, 'edit.html', context)

# 특정 Article을 업데이트하고 저장하는 함수
def update(request, id):
    title = request.POST.get('title')  # POST 요청에서 제목 데이터를 가져옴
    content = request.POST.get('content')  # POST 요청에서 내용 데이터를 가져옴
    article = Article.objects.get(id=id)  # 주어진 id에 해당하는 Article 객체를 가져옴
    article.title = title  # 제목 업데이트
    article.content = content  # 내용 업데이트
    article.save()  # 데이터베이스에 저장
    return redirect('articles:detail', id=article.id)  # 업데이트된 Article의 상세 페이지로 리다이렉트