from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

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


def monthly_challenge(request, month):
  if month.lower() in monthly_challenges:
    return HttpResponse(monthly_challenges[month])
  else:
    return HttpResponseNotFound("Month not supported.")
