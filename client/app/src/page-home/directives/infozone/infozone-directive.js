(function(){
    'use strict';

    angular.module('app.pageHome').directive('plInfozone', plInfozone);
 
    function plInfozone() {
	return {
	    scope: {
		// same as '=customer'
		title: '@',
		text: '@',
		photo: '@'
	    },
	    link: function(scope, element, attrs, controllers) {
		
	    },
	    templateUrl: './src/page-home/directives/infozone/infozone-directive.html'
	};
    }
})();
