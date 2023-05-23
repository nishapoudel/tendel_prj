from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),


    path('item', views.item, name='item'),
    path('team', views.team, name='team'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('gallery', views.gallery, name='gallery'),
    path('news', views.news, name='news'),
    path('team', views.team, name='team'),
    path('googlemap', views.googlemap, name='googlemap'),
    path('branch', views.branch, name='branch'),

    # path('', views.index, name = 'index'),
    # path('upload/', views.upload, name = 'upload-item'),
    # path('update/<int:item_id>', views.update_item),
    # path('delete/<int:item_id>', views.delete_item)
]