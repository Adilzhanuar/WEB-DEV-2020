import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable, of} from 'rxjs';
import {Company, IsAuthRespone, Vacancy} from './interfaces';
import { catchError, map, tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class CompanyService {
  BASE_URL = 'http://127.0.0.1:8000/';

  constructor(private http: HttpClient) {
  }

  getCompanyList(): Observable<Company[]> {
    return this.http.get<Company[]>(`${this.BASE_URL}api/companies/`).pipe(
      catchError(this.handleError<Company[]>('getCompanies', []))
    );
  }

  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
      console.error(error); // log to console instead
      return of(result as T);
    };
  }
  deleteCategory(id): Observable<any> {
    return this.http.delete(`${this.BASE_URL}${id}`);
  }

  getVacancy(id): Observable<Vacancy[]> {
    return this.http.get<Vacancy[]>(`${this.BASE_URL}api/companies/${id}/vacancies`).pipe(
      catchError(this.handleError<Vacancy[]>('getVacancies', []))
    );
  }

  login(username, password): Observable<IsAuthRespone> {
    return this.http.post<IsAuthRespone>(`${this.BASE_URL}login/`, {
      username,
      password
    });
  }
}
