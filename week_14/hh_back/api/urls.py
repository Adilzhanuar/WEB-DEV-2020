from django.urls import path
from api.views_fbv import all_companies, company_detail, vacancies_of_company
from api.views_cbv import VacanciesList, VacancyDetails, TopTenVacancies

urlpatterns = [
    path('companies/', all_companies),
    path('companies/<int:id>/', company_detail),
    path('companies/<int:id>/vacancies', vacancies_of_company),
    path('vacancies/', VacanciesList.as_view()),
    path('vacancies/<int:pk>/', VacancyDetails.as_view()),
    path('vacancies/top_ten/',  TopTenVacancies.as_view())
]