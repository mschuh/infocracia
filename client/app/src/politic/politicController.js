'use strict';

 app.controller('PoliticController',
      ['$scope', '$timeout', '$location', '$state', '$window',
      function PoliticController($scope, $timeout, $location, $state, $window) {
	  $scope.politic = { 
	      name: "Joao da silva",
	      photo: "http://zblogged.com/wp-content/uploads/2015/11/17.jpg"
	  };

  }]);
