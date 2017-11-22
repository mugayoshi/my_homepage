(function () {
	'use strict'
	var prevIndex = 0;
	var albums = ['italy1', 'spain', 'uk']
	var i;
	for (i = 0; i < albums.length; i++) {
		showPreviews(albums[i], prevIndex);
	}

	function showPreviews(album, internal_index) {
		var i;
		var slides = document.getElementsByClassName("slide_pic" + " " + album);
		for (i = 0; i < slides.length; i++) {
			slides[i].style.display = "none";
		}
		// prevIndex++;
		// if (prevIndex > slides.length) {
		// 	prevIndex = 1;
		// }
		internal_index++;
		if (internal_index > slides.length) {
			internal_index= 1;
		}
		//console.log('showPreviews ' + album + ', prevIndex =  ' + prevIndex);
		console.log('showPreviews ' + album + ', prevIndex =  ' + internal_index);
		slides[internal_index - 1].style.display = "block";
		setTimeout(function(){showPreviews(album, internal_index)}, 2000);

	}
}());
