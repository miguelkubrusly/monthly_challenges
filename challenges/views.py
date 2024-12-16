from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "End Django course.",
    "february": "Fix LinkedIn, WorkaLove and personal web portfolio.",
    "march": "Maintain a 3,5/week Jiu-Jitsu attendance average.",
    "april": "Make back-end in Django for Maria's website.",
    "may": "Learn to work and automate ads and ad analysis.",
    "june": "Clean my work desk every day.",
    "july": "Meditate every day.",
    "august": "Learn some Java framework.",
    "september": "Make my bed every day.",
    "october": "Watch a video for each major opening I use in my repertoire.",
    "november": "Start demo investment portfolio.",
    "december": "Finish ethical hacking course.",
}


# Create your views here.


def index(request):
    months = list(monthly_challenges.keys())
    res = render(
        request,
        "challenges/index.html",
        {
            "months": months,
        },
    )

    return HttpResponse(res)


def monthly_challenge(request, month):
    month = month.lower()
    challenge = monthly_challenges[month]
    try:
        res = render(
            request,
            "challenges/challenges.html",
            {
                "month": month,
                "challenge": challenge,
            },
        )
        return HttpResponse(res)

        response = render_to
        # return HttpResponse(f"""
        #   <p>{monthly_challenges[month]}</p>
        #   <a href="/challenges"><small>Back</small></a>
        # """)
    except KeyError:
        return HttpResponseNotFound("Month not supported.")


def month_number_redirect(request, numeric_month):
    if 1 <= numeric_month <= len(monthly_challenges):
        month = list(monthly_challenges.keys())[numeric_month - 1]
        month_url = reverse("monthly_challenge", args=[month])
        return HttpResponseRedirect(month_url)
    else:
        return HttpResponseNotFound("Month not supported.")
