from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    isPublished = models.BooleanField(default=False)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'
        ordering = ['-createdAt', 'title']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True)

    def __str__(self):
        return self.title

    def number_news(self):
        num_news = News.objects.filter(category=self.id).count()
        return num_news

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']
