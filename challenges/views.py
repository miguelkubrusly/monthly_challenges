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


# def capitalize(text):
#     words = text.split(" ")
#     capitalized_words = [
#         word[0].upper() + word[1:] if len(word) > 1 else word[0].upper()
#         for word in words
#     ]
#     return " ".join(capitalized_words)


# Create your views here.


def index(request):
    def render_month(month):
        month_url = reverse("monthly_challenge", args=[month])
        return f"<li><a href={month_url}>{month}</a></li>"

    months_html = [render_month(month) for month in monthly_challenges.keys()]
    index_html = "<ol>"

    for html in months_html:
        index_html += f"{html}"
    index_html += "</ol>"

    return HttpResponse(index_html)


def monthly_challenge(request, month):
    month = month.lower()
    challenge = monthly_challenges[month]
    try:
        res = render_to_string(
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
