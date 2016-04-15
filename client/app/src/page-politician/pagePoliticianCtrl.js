(function(){
    'use strict';

    angular.module('app.pagePolitician').controller('PagePoliticianCtrl',PagePoliticianCtrl);

    PagePoliticianCtrl.$inject = [];

    function PagePoliticianCtrl() {
	var vm = this;
	vm.personalData = { 
	    name: "Joao da silva",
	    photoUrl: "http://zblogged.com/wp-content/uploads/2015/11/17.jpg",
	    party: "PMDB"
	};

    }
})();
