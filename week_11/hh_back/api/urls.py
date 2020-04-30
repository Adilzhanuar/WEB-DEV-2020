from django.urls import path
from api.views import all_companies, company_detail, vacancies_of_company, all_vacancies, vacancy_detail, top_ten_vacancies

urlpatterns = [
    path('companies/',all_companies ),
    path('companies/<int:id>/', company_detail),
    path('companies/<int:id>/vacancies', vacancies_of_company),
    path('vacancies/', all_vacancies),
    path('vacancies/<int:id>/', vacancy_detail),
    path('vacancies/top_ten/',  top_ten_vacancies)
]