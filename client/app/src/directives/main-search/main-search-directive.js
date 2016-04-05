app.directive('plMainSearch', function() {
  return {
    link: function(scope, element, attrs, controllers) {
      scope.search = {
	      searchEntityText: ""
	      
	  };


	var data = [
		{ name: "Dilma Roussef", photoUrl:"http://cenariotocantins.com.br/principal/wp-content/uploads/2012/09/presidente-dilma-rousseff-pesquisa-aumenta-popularidade-da-presidente-brasil.jpg"},
		{ name: "Jair Bolsonaro", photoUrl: "http://curitibainenglish.com.br/wp-content/uploads/2014/12/jair-bolsonaro-racista.jpg"}
	    ];

	scope.search.querySearchEntity = function(param){
	       
	    return data.filter(function(entity){
		return entity.name.indexOf(param) >= 0;
	    })
	    
	}
    },
    templateUrl: './src/directives/main-search/main-search-directive.html'
  };
});
