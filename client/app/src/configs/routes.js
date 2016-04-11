app.config(function ($stateProvider,$urlRouterProvider) {
  $urlRouterProvider.otherwise("/");

        $stateProvider
        .state('home', {
	    url: "/",
	    templateUrl: "src/home/home.html",
	    controller: 'HomeController'
	})
        .state('politician', {
	    url: "/politician",
	    templateUrl: "src/politician/politician.html",
	    controller: 'PoliticianController'
	})

});
