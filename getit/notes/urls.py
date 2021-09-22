from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit',views.edit, name='edit'),
    path('delete',views.delete, name='delete'),
    path('update', views.update, name='update'),
    path('tag', views.tag_1, name="tag"),
    path(f'tag-<str:tag>',views.tag_2, name="tag-filter")
]