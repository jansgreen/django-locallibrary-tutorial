class api_url {
    constructor() {
      this.Get_access = "https://api.themoviedb.org/3/discover/movie?";
      this.Api_key = "api_key=fcbf9f302d5fcc8a3d775556c623b770";
      this.in_theatres = '&primary_release_date.gte=2014-09-15&primary_release_date.lte=2014-10-22';
      this.most_popular = "&sort_by=popularity.desc";
      this.allpoke_point = `pokemon?limit=8&offset=`;
    }

  export theatres() {
        fetch(this.Get_access + this.Api_key + this.in_theatres)
          .then((response) => response.json())
          .then(function (theatres_data) {
            theatres_data.results.forEach(function (send_data) {
              show_theatres(send_data);
            });
          });
        }
}