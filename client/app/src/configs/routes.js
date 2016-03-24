app.config(function ($stateProvider,$urlRouterProvider) {
  $urlRouterProvider.otherwise("/");

        $stateProvider
        .state('home', {
	    url: "/",
	    templateUrl: "src/home/home.html",
	    controller: 'HomeController'
	})
        .state('politic', {
	    url: "/politic",
	    templateUrl: "src/politic/politic.html",
	    controller: 'PoliticController'
	})

});
