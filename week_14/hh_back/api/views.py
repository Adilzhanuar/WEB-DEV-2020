from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from api.models import Company, Vacancy
from django.http import HttpResponse

from corsheaders.defaults import default_headers

def greeting(request):
    return HttpResponse("""<h1>Welcome to our website!</h1>
    <h2>There you can find the most valuable companies</h2>
    <h2>If you are searching for the job, we can provide list of vacancies</h2>""")

def all_companies(request):
    companies = Company.objects.all()
    companies_json = [company.short() for company in companies]
    return JsonResponse(companies_json, safe=False)

def company_detail(request, id):
    try:
        company = Company.objects.get(id=id)
        company_json = company.full()
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(company_json)

def vacancies_of_company(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    vacancies = company.vacancy_set.all()
    vacancies_json = [vacancy.short() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)

def all_vacancies(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.short() for vacancy in vacancies]
    return JsonResponse(vacancies_json,safe=False)

def vacancy_detail(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
        vacancy_json = vacancy.full()
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(vacancy_json)

def top_ten_vacancies(request):
    vacancies = Vacancy.objects.order_by('-salary')
    top = [vacancy.full() for vacancy in vacancies[:10]]
    return JsonResponse(top, safe=False)

