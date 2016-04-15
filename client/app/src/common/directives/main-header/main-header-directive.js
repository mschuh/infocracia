(function(){
    'use strict';

    angular.module('app').directive('plMainHeader', plMainHeader);
    
    function plMainHeader() {
	return {
	    templateUrl: './src/common/directives/main-header/main-header-directive.html'
	};
    }
})();
