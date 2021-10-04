from django.core import paginator
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Page, PageNotAnInteger, Paginator, EmptyPage
from .models import Story, Category
from taggit.models import Tag

def story_list(request,category_slug = None, tag_slug = None):
    category = None
    categories = Category.objects.all()
    story = Story.objects.all()
    paginator = Paginator(story,9)
    page = request.GET.get('page')
    tag = None
    try:
        story = paginator.page(page)
    except PageNotAnInteger:
        story = paginator.page(1)
    except EmptyPage:
        story = paginator.page(paginator.num_pages)    
    if category_slug:
        story = Story.objects.all()
        category = get_object_or_404(Category,slug=category_slug)
        story = story.filter(category=category)
        paginator = Paginator(story,9)
        page = request.GET.get('page')
        try:
            story = paginator.page(page)
        except PageNotAnInteger:
            story = paginator.page(1)
        except EmptyPage:
            story = paginator.page(paginator.num_pages)         
    if tag_slug:
        tag = get_object_or_404(Tag,slug=tag_slug)
        story = Story.objects.filter(tags__in=[tag])
        paginator = Paginator(story,9)
        page = request.GET.get('page')
        try:
            story = paginator.page(page)
        except PageNotAnInteger:
            story = paginator.page(1)
        except EmptyPage:
            story = paginator.page(paginator.num_pages)               
    return render(request,'story/story_list.html',{'categories':categories,
                                                'category':category,
                                                'story':story,
                                                'page':page,
                                                'tag':tag,})

def story_detail(request,id):
    story=get_object_or_404(Story,id=id)

    post_tags_ids = Story.tags.values_list('id', flat=True)

    return render(request,'story/story_detail.html',{'story':story,})