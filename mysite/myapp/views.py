from django.shortcuts import render
from .models import *
import requests

# Create your views here.

# Home views
def home_page(request):
    homepage = HomePage.objects.first()
    context = {'homepage': homepage}
    return render(request, 'home.html', context)

# Demand views
def demand_view(request):
    demand_data = Demand.objects.all()
    return render(request, 'demand.html', {'demand_data': demand_data})

# Geography views
def geography_view(request):
    geography_data = Geography.objects.all().order_by('-salary','-vacancies_percentage')
    return render(request, 'geography.html', {'geography_data': geography_data})

# Skills page
def skills_view(request):
    skills_data = Skills.objects.filter(profession='Frontend-программист').order_by('-year')[:10]
    return render(request, 'skills.html', {'skills_data': skills_data})

# Latest job page 
def latest_jobs(request, profession):
    # Use the requests library to interact with the HH API
    url = f'https://api.hh.ru/vacancies?text={profession}&only_with_salary=true'
    response = requests.get(url)
    data = response.json()
    # Get the first 10 vacancies that were posted on a weekday in December
    vacancies = [vacancy for vacancy in data['items'] if (vacancy['published_at'].month == 12 and vacancy['published_at'].weekday() < 5)][:10]

    for vacancy in vacancies:
        # send a GET request to get the details of the job
        vacancy_url = vacancy['url']
        vacancy_response = requests.get(vacancy_url)
        vacancy_data = vacancy_response.json()
        vacancy["description"] = vacancy_data["description"]
        vacancy["skills"] = ", ".join(vacancy_data["key_skills"])
    context = {
        'vacancies': vacancies
    }
    return render(request, 'latest_jobs.html', context)