from django.urls import path
from analysis.views import views
from analysis.views import detail

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detail/', detail.DetailView.as_view(), name='detail'),
]
