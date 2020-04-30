import { Component, OnInit } from '@angular/core';
import { CompanyService } from '../company.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-authentification',
  templateUrl: './authentification.component.html',
  styleUrls: ['./authentification.component.css']
})
export class AuthentificationComponent implements OnInit {

  constructor(private companyService: CompanyService, private route: Router) { }

  username = '';
  password = '';
  // tslint:disable-next-line:variable-name
  private _logged = false;

  ngOnInit(): void {
    const token = localStorage.getItem('token');
    if (token) {
      this._logged = true;
    }
  }
  login(): void {
    this.companyService.login(this.username, this.password).subscribe( res => {
      localStorage.setItem('token', res.token);
      this._logged = true;
      this.username = '';
      this.password = '';
    });
  }

}
