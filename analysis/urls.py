from django.urls import path
from analysis.views import index
from analysis.views import detail

urlpatterns = [
    path('', index.IndexView.as_view(), name='index'),
    path('detail/', detail.DetailView.as_view(), name='detail'),
]
