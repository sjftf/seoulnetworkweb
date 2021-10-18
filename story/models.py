from django.db import models
from django.db.models.fields import CharField
from django.urls import reverse
from tinymce.models import HTMLField
from taggit.managers import TaggableManager

class Category(models.Model):
    name = models.CharField(max_length=150,db_index=True)
    slug = models.SlugField(unique=True)
    class Meta:
        ordering = ('-name',)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('story:story_category',args=[self.slug,])

class Story(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    body = HTMLField()
    thumbnail = models.ImageField(upload_to="story/media", blank=True)
    des = models.TextField()
    writer = models.CharField(max_length=150, blank=True, null=True)
    publish = models.DateField('date published', blank=True)
    tags = TaggableManager()
    class Meta:
        ordering = ('-publish',)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('story:story_detail',args=[self.id,]) 