import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {CompanyService} from '../company.service';
import {Vacancy} from '../interfaces';

@Component({
  selector: 'app-vacancy',
  templateUrl: './vacancy.component.html',
  styleUrls: ['./vacancy.component.css']
})
export class VacancyComponent implements OnInit {
  vacancies: Vacancy[];

  constructor(private route: ActivatedRoute, private companyService: CompanyService,) { }

  ngOnInit(): void {
    this.getVacancies();
  }

  getVacancies(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.companyService.getVacancy(id).subscribe(vacancy => this.vacancies = vacancy);
  }

}
