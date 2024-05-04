import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { HttpClient, HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet, FormsModule, HttpClientModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'my-vector-search';

  dirPath = '';
  searchterm = '';

  results: any = null;

  backendUrl = 'http://localhost:5000';
  loading = false;
  searching = false;

  constructor(private http: HttpClient) {}

  onSubmit() {
    if(this.loading){
      return;
    }
    console.log(this.dirPath);
    this.loading = true;
    this.http.post(this.backendUrl + '/index_folder', {path: this.dirPath}).subscribe(data => {
      console.log("response:" + data);
      this.loading = false;
    });
  }

  search(){
    if(this.searching){
      return
    }
    if(this.searchterm == ""){
      this.results = null;
      return
    }
    console.log(this.dirPath);
    this.searching = true;
    this.http.post(this.backendUrl + '/search', {searchterm: this.searchterm}).subscribe(data => {
      console.log("response:" + data);
      this.results = data;
      this.results["hits"] = this.results["hits"].filter((hit: any) => hit._score >= 0.6);
      this.searching = false;
    });
  }
}
