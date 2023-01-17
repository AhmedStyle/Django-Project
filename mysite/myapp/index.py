from django.shortcuts import render

def webhome(request):
    return render(request, 'home.html')


def webdemand(request):
    return render(request, 'demand.html')


def webskills(request):
    return render(request, 'skills.html')


def webgeo(request):
    return render(request, 'geography.html')


def weblatest_jobs(request):
    return render(request, 'latest_jobs.html')
