from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge(request, month):
  if month.lower() == "january":
    return HttpResponse("End Django course.")
  elif month.lower() == "february":
    return HttpResponse("Fix linkedin, Workalove and portfolio.")
  elif month.lower() == "march":
    return HttpResponse("Maintain a 3,5/week Jiu Jitsu attendance average.")
  else:
    return HttpResponseNotFound("Month not supported.")
