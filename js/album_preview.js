(function () {
	'use strict'
	var prevIndex = 0;
	console.log('before first showPreviews');
	showPreviews();

	function showPreviews() {
		console.log('first line in showPreviews');
		var i;
		var slides = document.getElementsByClassName("slide_pic");
		for (i = 0; i < slides.length; i++) {
			slides[i].style.display = "none";
		}
		prevIndex++;
		if (prevIndex > slides.length) {
			prevIndex = 1;
		}
		slides[prevIndex - 1].style.display = "block";
		setTimeout(showPreviews, 2000);

	}
}());
