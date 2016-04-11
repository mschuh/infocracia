  app
    // directive class-sm
    .directive("classSm", [
      "$mdMedia",
      function($mdMedia) {
        if ($mdMedia("sm")) {
          return {
            restrict: "A",
            link: function(scope, elem, attrs) {
              elem.addClass(attrs.classSm);
            }
          };
        }
      }
    ])
    // directive class-gt-sm
    .directive("classGtSm", [
      "$mdMedia",
      function($mdMedia) {
        if ($mdMedia("gt-sm")) {
          return {
            restrict: "A",
            link: function(scope, elem, attrs) {
              elem.addClass(attrs.classGtSm);
            }
          };
        }
      }
    ])
    // directive class-md
    .directive("classMd", [
      "$mdMedia",
      function($mdMedia) {
        if ($mdMedia("md")) {
          return {
            restrict: "A",
            link: function(scope, elem, attrs) {
              elem.addClass(attrs.classMd);
            }
          };
        }
      }
    ])
    // directive class-gt-md
    .directive("classGtMd", [
      "$mdMedia",
      function($mdMedia) {
        if ($mdMedia("gt-md")) {
          return {
            restrict: "A",
            link: function(scope, elem, attrs) {
              elem.addClass(attrs.classGtMd);
            }
          };
        }
      }
    ])
    // directive class-lg
    .directive("classLg", [
      "$mdMedia",
      function($mdMedia) {
        if ($mdMedia("lg")) {
          return {
            restrict: "A",
            link: function(scope, elem, attrs) {
              elem.addClass(attrs.classLg);
            }
          };
        }
      }
    ])
    // directive class-gt-lg
    .directive("classGtLg", [
      "$mdMedia",
      function($mdMedia) {
        if ($mdMedia("gt-lg")) {
          return {
            restrict: "A",
            link: function(scope, elem, attrs) {
              elem.addClass(attrs.classGtLg);
            }
          };
        }
      }
    ])
  ;
