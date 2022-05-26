from django.urls import path
from . import views as my_app_views

urlpatterns=[
    path('', my_app_views.home, name = 'home'),
    path('archives/', my_app_views.archive, name = 'archives'),
    path('healings-are-forever/', my_app_views.healings , name = 'healings'),
    path('pastoring-pastors/', my_app_views.blogpage , name = 'blog'),
    path('legacy/', my_app_views.legacy , name = 'legacy'),
    path('power-crusades/', my_app_views.power_crusades , name = 'power-crusades'),
    path('post-detail/<int:pk>/', my_app_views.post_detail, name = 'post-detail'),
        
]