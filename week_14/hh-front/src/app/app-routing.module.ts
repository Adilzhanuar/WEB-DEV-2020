import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CompanyComponent } from './company/company.component';
import {VacancyComponent} from './vacancy/vacancy.component';
import {AuthentificationComponent} from './authentification/authentification.component';


const routes: Routes = [
  { path: '', component: AuthentificationComponent},
  { path: 'companies', component: CompanyComponent },
  { path: 'companies/:id/vacancies', component: VacancyComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
