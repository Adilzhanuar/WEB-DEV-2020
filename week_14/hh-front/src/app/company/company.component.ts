import { Component, OnInit } from '@angular/core';
import {CompanyService} from '../company.service';
import { Company } from '../interfaces';
import {AuthentificationComponent} from "../authentification/authentification.component";

@Component({
  selector: 'app-company',
  templateUrl: './company.component.html',
  styleUrls: ['./company.component.css']
})
export class CompanyComponent implements OnInit {

  companies: Company[];

  constructor( public companyService: CompanyService ) { }

  ngOnInit(): void {
    this.getCompanies();
  }
  getCompanies(): void {
    this.companyService.getCompanyList().subscribe(company => this.companies = company);
  }

  logout(): void {
    localStorage.clear();
    }



}
