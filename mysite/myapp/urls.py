from django.urls import path
from . import views , index

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('demand/', views.demand_view, name='demand'),
    path('geography/', views.geography_view, name='geography'),
    path('skills/', views.skills_view, name='skills'),
    path('latest-jobs/<str:profession>/', views.latest_jobs, name='latest_jobs'),
    path('home.html', index.webhome, name='home.html'),
    path('demand.html', index.webdemand, name='demand.html'),
    path('skills.html', index.webskills, name='skills.html'),
    path('geography.html', index.webgeo,name='geography.html'),
    path('latest_jobs.html', index.weblatest_jobs, name='latest_jobs.html'),
]