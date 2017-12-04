(function () {
	'use strict';

  var films = $(".film");
	var currentPos = 0;
	init();
	function init(){
		console.log('init()');
    $(".film").not(":first").hide();
	};
  $("#btn_prev").click (function(){
    console.log('btn prev is clicked');
    var f = $(".film").get(currentPos);
    $(f).hide();
    currentPos--;
    if (currentPos < 0){
			currentPos = $(".film").length - 1;
		}
    var f_prev = $(".film").get(currentPos);
    $(f_prev).fadeIn(1000);
  });
  $("#btn_next").click (function(){
    console.log('btn next is clicked');
    var f = $(".film").get(currentPos);
    $(f).hide();
    currentPos++;
    if (currentPos === $(".film").length ){
			currentPos = 0;
		}
    var f_next = $(".film").get(currentPos);
    $(f_next).fadeIn(1000);
  });

})();
