from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.db.models import Q
from unicodedata import category

from  .models import *
from django.shortcuts import get_object_or_404, redirect

class HomeView(View):
    def get(self, request):

        top_articles = Article.objects.order_by('-important', '-views')[:10]
        latest_news = Article.objects.order_by('-created_at', )[:10]



        context = {
            'top_articles': top_articles,
            'latest_news': latest_news,

        }

        return render(request, 'index.html', context)

class ArricleDetailsView(View):
    def get(self, request, slug):

        article = get_object_or_404(Article, slug=slug)

        session = f"viewed_article_{article.id}"

        if not request.session.get(session):
            article.views += 1
            article.save()
            request.session[session] = True


        like_articles = Article.objects.filter(category=article.category)


        context = {
            'article': article,
            'like_articles': like_articles,
        }
        return render(request, 'detail-page.html', context)


class NewsLetterCreateView(View):
    def post(self, request):
        Newsletter.objects.create(
            email=request.POST['email'],
        )

        return HttpResponseRedirect('/')

class CommentCreateView(View):
    def post(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        Comment.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            text=request.POST['text'],
            article=article,
        )

        return redirect('details', slug=article.slug)

from django.shortcuts import get_object_or_404

class ArticleCategoriesView(View):
    def get(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        articles = Article.objects.filter(category=category).order_by('-created_at')



        search = request.GET.get('search')
        if search:
            articles = Article.objects.filter(Q(title__icontains=search)|Q(intro__icontains=search))



        context = {
            'articles': articles,
            'category': category,
            'search': search,
        }
        return render(request, 'category-details.html', context)


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')



class ContactView(View):
        def get(self, request):
            return render(request, 'contact.html')

        def post(self, request):
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone_number = request.POST.get('phone_number')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            Contact.objects.create(
                name=name,
                email=email,
                phone_number=phone_number,
                subject=subject,
                message=message
            )
            return redirect('home')