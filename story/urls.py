from django.urls import path
from . import views
import story
app_name='story'

urlpatterns = [
    path('', views.story_list,name='story_list'),
    path('<slug:category_slug>',views.story_list,name="story_category"),
    path('<int:id>/',views.story_detail,name="story_detail"),
    path('tag/<slug:tag_slug>',views.story_list,name="story_by_tag")
]