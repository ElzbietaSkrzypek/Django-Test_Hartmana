from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question


class IndexView(generic.ListView):
    model = Question
    template_name = "polls/index.html"

    def get_queryset(self):
        """
        Return the last published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class HomeView(generic.ListView):
    model = Question
    template_name = "polls/home.html"


def vote(request):
    sum_a_votes = 0
    sum_b_votes = 0
    sum_c_votes = 0
    sum_d_votes = 0
    if request.method == "POST":
        for k, v in request.POST.items():
            if 'question_' in k:
                if "choice1" in v:
                    sum_a_votes += 1
                if "choice2" in v:
                    sum_b_votes += 1
                if "choice3" in v:
                    sum_c_votes += 1
                if "choice4" in v:
                    sum_d_votes += 1
        return render(
                    request,
                    "polls/results.html",
                    {
                        "sum_a_votes": sum_a_votes,
                        "sum_b_votes": sum_b_votes,
                        "sum_c_votes": sum_c_votes,
                        "sum_d_votes": sum_d_votes
                    },
                )
    else:
        return HttpResponseRedirect(reverse("polls:index"))
