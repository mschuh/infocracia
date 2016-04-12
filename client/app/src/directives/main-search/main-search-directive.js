app.directive('plMainSearch', ["$q", "$timeout", function($q, $timeout) {
  return {
    link: function(scope, element, attrs, controllers) {
	scope.searchEntityText = "";
	
	var data = [
		{ name: "Dilma Roussef", photoUrl:"http://cenariotocantins.com.br/principal/wp-content/uploads/2012/09/presidente-dilma-rousseff-pesquisa-aumenta-popularidade-da-presidente-brasil.jpg"},
		{ name: "Jair Bolsonaro", photoUrl: "http://curitibainenglish.com.br/wp-content/uploads/2014/12/jair-bolsonaro-racista.jpg"}
	    ];

	scope.querySearchEntity = function(query) {
	    var deferred = $q.defer();
	    $timeout(function () { 
		var res = data.filter(function(entity){ 
		    return entity.name.indexOf(query) >= 0; 
		});
		deferred.resolve(res); 
	    }, Math.random() * 1000, false);
	    return deferred.promise;
	}
    },
    templateUrl: './src/directives/main-search/main-search-directive.html'
  };
}]);
