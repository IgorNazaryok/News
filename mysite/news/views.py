from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import News, Category

def news (request):
    news = News.objects.all()
    categories = Category.objects.all()

    context = {
        'news': news,
        'categories': categories,
        'title': "List Title",
    }
    return render(request, 'news/index.html', context)


def get_category_news (request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)

    context = {
        'news': news,
        'categories': categories,
        'category': category,
    }
    return render(request, 'news/category.html', context)

# def posts (request):
#     print(request)
#     return HttpResponse('<h1>Page Posts</h1>')
#
# def users (request):
#     print(request)
#     return HttpResponse('<h1>Page Users</h1>')


# python manage.py runserver
# python manage.py migrate
# python manage.py makemigrations





