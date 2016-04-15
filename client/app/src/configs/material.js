(function(){
    'use strict';

    angular.module('app').config(function($mdThemingProvider, $mdIconProvider){
	$mdIconProvider
	    .defaultIconSet("./assets/svg/avatars.svg", 128)
	    .icon("menu"       , "./assets/svg/menu.svg"        , 24)
	    .icon("share"      , "./assets/svg/share.svg"       , 24)
	    .icon("logo"       , "./assets/svg/logoicon.svg")
	    .icon("google_plus", "./assets/svg/google_plus.svg" , 512)
	    .icon("hangouts"   , "./assets/svg/hangouts.svg"    , 512)
	    .icon("twitter"    , "./assets/svg/twitter.svg"     , 512)
	    .icon("phone"      , "./assets/svg/phone.svg"       , 512);


	$mdThemingProvider.definePalette('greenflag', {
	    '50': '#dcfbe4',
	    '100': '#98f3ae',
	    '200': '#66ed87',
	    '300': '#26e555',
	    '400': '#19d347',
	    '500': '#16b83e',
	    '600': '#139d35',
	    '700': '#0f812c',
	    '800': '#0c6622',
	    '900': '#094b19',
	    'A100': '#dcfbe4',
	    'A200': '#98f3ae',
	    'A400': '#19d347',
	    'A700': '#0f812c',
	    'contrastDefaultColor': 'light',
	    'contrastDarkColors': '50 100 200 300 400 A100 A200 A400'
	});
	$mdThemingProvider.definePalette('yellowflag', {
	    '50': '#ffffff',
	    '100': '#fffadc',
	    '200': '#fff3a4',
	    '300': '#ffe95c',
	    '400': '#ffe53e',
	    '500': '#ffe11f',
	    '600': '#ffdd00',
	    '700': '#e1c300',
	    '800': '#c2a800',
	    '900': '#a48e00',
	    'A100': '#ffffff',
	    'A200': '#fffadc',
	    'A400': '#ffe53e',
	    'A700': '#e1c300',
	    'contrastDefaultColor': 'light',
	    'contrastDarkColors': '50 100 200 300 400 500 600 700 800 900 A100 A200 A400 A700'
	});

	$mdThemingProvider.definePalette('blueflag', {
	    '50': '#dce7fb',
	    '100': '#98b9f3',
	    '200': '#6697ed',
	    '300': '#266ce5',
	    '400': '#195dd3',
	    '500': '#1651b8',
	    '600': '#13459d',
	    '700': '#0f3981',
	    '800': '#0c2d66',
	    '900': '#09214b',
	    'A100': '#dce7fb',
	    'A200': '#98b9f3',
	    'A400': '#195dd3',
	    'A700': '#0f3981',
	    'contrastDefaultColor': 'light',
	    'contrastDarkColors': '50 100 200 A100 A200'
	}); 

	$mdThemingProvider.theme('default')
	    .primaryPalette('greenflag')
	    .accentPalette('yellowflag')
	    .warnPalette('blueflag');
    });
})();
