'use strict';


var app = angular.module('politics', [
    'ngMaterial',
    'ui.router',
    'ngMdIcons'
  ]);

  app.run(function($rootScope, $location, $state, $anchorScroll) {
      $rootScope.$on( '$stateChangeSuccess', function(e, toState  , toParams
                                                 , fromState, fromParams) {

      });
  });

