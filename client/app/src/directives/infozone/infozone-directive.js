app.directive('plInfozone', function() {
  return {
    scope: {
	// same as '=customer'
	title: '@',
	text: '@',
	photo: '@'
    },
    link: function(scope, element, attrs, controllers) {
      
    },
    templateUrl: './src/directives/infozone/infozone-directive.html'
  };
});
