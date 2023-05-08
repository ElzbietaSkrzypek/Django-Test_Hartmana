from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("polls/", views.IndexView.as_view(), name="index"),
    path("", views.HomeView.as_view(), name="home"),
    # path("results/", views.ResultsView.as_view(), name="results"),
    path("results/", views.vote, name="vote"),
]