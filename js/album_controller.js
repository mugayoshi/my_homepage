(function () {
	'use strict';

	var btn_prev = document.getElementById('btn_prev');
	var btn_next = document.getElementById('btn_next');

	var currentPos = 0;
	init();
	function init(){
		console.log('init()');
		var slides = document.getElementsByClassName("slide_pic");
		slides[0].style.display = "block";
	};
	//console.log(currentPos);
	btn_prev.addEventListener('click', function () {
		//get current index
		console.log('button prev ' + currentPos);
		currentPos--;
		showPic();
		
	});
	btn_next.addEventListener('click', function () {
		console.log('button next ' + currentPos);
		currentPos++;
		showPic()
		
	});
	function showPic() {
		//console.log('showPic n = ' + n );
		var slides = document.getElementsByClassName("slide_pic");
		var i;
		if (currentPos < 0){
			currentPos = slides.length - 1;
			showPic();
			return;
		}else if (currentPos === slides.length ){
			currentPos = 0;
			showPic();
			return;
		}
		for (i = 0; i < slides.length; i++) {
			slides[i].style.display = "none";
		}
		slides[currentPos].style.display = "block";
	};
})();
