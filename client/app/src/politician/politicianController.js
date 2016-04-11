'use strict';

 app.controller('PoliticianController',
      ['$scope', '$timeout', '$location', '$state', '$window',
      function PoliticController($scope, $timeout, $location, $state, $window) {
	  $scope.personalData = { 
	      name: "Joao da silva",
	      photoUrl: "http://zblogged.com/wp-content/uploads/2015/11/17.jpg",
	      party: "PMDB"
	  };

  }]);
