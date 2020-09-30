from django.urls import path

from . import views

urlpatterns = [
    path('',views.upload_file, name = 'upload_file'),

    path('upload_file_path',views.read_data,name = 'read_data'),
    path('show_feed',views.newfeeds ,name = 'newfeeds'),
    path('newsfeed/<str:tag_words>/',views.newsfeed ,name = 'feed'),
    path('newsfeed/<str:tag_words>/export_page/', views.export_page, name = 'export_excel'),
    path("register", views.register_profile, name="register"),
    # path("logout", views.logout_request, name="logout"),
]