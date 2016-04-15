(function(){

    'use strict';

    angular.module("app.pageHome").controller('PageHomeCtrl',PageHomeCtrl);
    PageHomeCtrl.$inject = ['$timeout'];
    
    function PageHomeCtrl($timeout) {	     
	var vm = this;
	vm.popularPoliticians = [];
	vm.popularParties = [];
	vm.getPopularPoliticians = getPopularPoliticians;
	vm.getPopularParties = getPopularParties;
	
	activate();
	
	////////////////////////////

	function activate(){
	    getPopularPoliticians();
	    getPopularParties();
	}

	function getPopularPoliticians(){ 
	    $timeout(function () { 
		vm.popularPoliticians = [
		    { id:1, name:"Dilma Roussef",photoUrl:"https://pbs.twimg.com/profile_images/526853273546788864/xAkXA8V8.jpeg", party: "PT" },
		    { id:2, name:"Aecio Neves",photoUrl:"http://www.ilheus24h.com.br/v1/wp-content/uploads/2014/03/a%C3%A9cio-neves.jpg", party: "PSDB" },
		    { id:3, name:"Jair Bolsonaro",photoUrl:"http://www.portalguaira.com/wp-content/uploads/2014/12/bolsonaro.jpg", party: "PSDB" },
		    { id:4, name:"Luis Inacio Lula da Silva",photoUrl:"https://brasilpagina1.files.wordpress.com/2015/11/421175-970x600-1.jpeg", party: "PT" },
		    { id:5, name:"Eduardo Cunha",photoUrl:"http://s2.glbimg.com/ak-DErAX126fmjyhYYYOv3zWzPg=/s.glbimg.com/jo/g1/f/original/2015/11/05/cunha-entrevista-escolha-do-relator.jpg", party: "PMDB" },
		    { id:6, name:"Jean Wyllys",photoUrl:"http://www.revistaforum.com.br/blogdorovai/wp-content/uploads/2016/03/jean-wyllys.jpg", party: "PSOL" }

		];
	    }, Math.random() * 1000);
	}

	function getPopularParties(){
	    $timeout(function () { 
		vm.popularParties = [
		    { id:1, acronym:"PT", members: 34249, photoUrl:"http://1.bp.blogspot.com/-VHXHvirOQpg/U1xkQhxDVJI/AAAAAAAALAI/GZCEeNBXD04/s1600/PT.png" },
		    { id:2, acronym:"PSDB", members: 33247, photoUrl:"http://www.portalndnews.com.br/site/images/stories/psdb.jpg" },
		    { id:3, acronym:"PMDB", members: 74289, photoUrl:"http://www.maceio.com.br/wp-content/uploads/2014/01/logo.png" },
		    { id:4, acronym:"PSOL", members: 243, photoUrl:"http://psol50sp.org.br/saocaetano/files/2015/06/PSOL.png" },
		    { id:5, acronym:"PDT", members: 3249, photoUrl:"http://www.blogdoanderson.com/media/2012/06/PDT.png" },
		    { id:6, acronym:"PV", members: 1242, photoUrl:"https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/PV_Logo.svg/2000px-PV_Logo.svg.png" }
		];
	    }, Math.random() * 1000);
	}
    }
})();
