app.directive('plMainHeader', function() {
  return {
  /*require: ['^^myTabs', 'ngModel'],
    restrict: 'E',
    transclude: true,
    scope: {
      title: '@'
    },
  /  link: function(scope, element, attrs, controllers) {
      var tabsCtrl = controllers[0],
          modelCtrl = controllers[1];

      tabsCtrl.addPane(scope);
    }, */
    templateUrl: './src/directives/main-header/main-header-directive.html'
  };
});
