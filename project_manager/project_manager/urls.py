# from django.contrib import admin
# from django.urls import path, include
# from projects import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.project_list, name='project_list'),
#     path('accounts/', include('django.contrib.auth.urls')),
#     path('signup/', views.signup, name='signup'),
#     path('submit/', views.submit_project, name='submit_project'),
#     path('project/<int:pk>/', views.project_detail, name='project_detail'),
# ]

from django.contrib import admin
from django.urls import path, include
from projects import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.project_list, name='project_list'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='project_list'), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('submit/', views.submit_project, name='submit_project'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
]