(function(){

    'use strict';

    angular.module('app').config(function ($stateProvider,$urlRouterProvider) {
	$urlRouterProvider.otherwise("/");

        $stateProvider
            .state('home', {
		url: "/",
		templateUrl: "src/page-home/pageHome.html",
		controller: 'PageHomeCtrl',
		controllerAs: 'pageHome'
	    })
            .state('politician', {
		url: "/politician",
		templateUrl: "src/page-politician/pagePolitician.html",
		controller: 'PagePoliticianCtrl',
		controllerAs: 'pagePolitician'
	    })
	    .state('party', {
		url: "/party",
		templateUrl: "src/page-party/pageParty.html",
		controller: 'PagePartyCtrl',
		controllerAs: 'pageParty'
	    })
    });
})();
