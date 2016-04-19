(function(){
    'use strict';

    angular.module('app.pageParty').controller('PagePartyCtrl',PagePartyCtrl);

    PagePartyCtrl.$inject = ["$timeout"];

    function PagePartyCtrl($timeout) {
	var vm = this;
	vm.acronym =  "PMDB";
	vm.name = "Partido do Movimento Democrático Brasileiro";
	vm.photoUrl = "http://www.maceio.com.br/wp-content/uploads/2014/01/logo.png";
	vm.members = "Calculating...";
	vm.politicians = [];
	

	activate();
	
	////////////////////////////

	function activate(){
	    getPoliticians();
	}

	function getPoliticians(){ 
	    $timeout(function () { 
		vm.politicians = [
		    { id:1, name:"Dilma Roussef",photoUrl:"https://pbs.twimg.com/profile_images/526853273546788864/xAkXA8V8.jpeg", party: "PT" },
		    { id:2, name:"Aecio Neves",photoUrl:"http://www.ilheus24h.com.br/v1/wp-content/uploads/2014/03/a%C3%A9cio-neves.jpg", party: "PSDB" },
		    { id:3, name:"Jair Bolsonaro",photoUrl:"http://www.portalguaira.com/wp-content/uploads/2014/12/bolsonaro.jpg", party: "PSDB" },
		    { id:4, name:"Luis Inacio Lula da Silva",photoUrl:"https://brasilpagina1.files.wordpress.com/2015/11/421175-970x600-1.jpeg", party: "PT" },
		    { id:5, name:"Eduardo Cunha",photoUrl:"http://s2.glbimg.com/ak-DErAX126fmjyhYYYOv3zWzPg=/s.glbimg.com/jo/g1/f/original/2015/11/05/cunha-entrevista-escolha-do-relator.jpg", party: "PMDB" },
		    { id:6, name:"Jean Wyllys",photoUrl:"http://www.revistaforum.com.br/blogdorovai/wp-content/uploads/2016/03/jean-wyllys.jpg", party: "PSOL" }

		];
	    }, Math.random() * 1000);
	}
    }
})();
