(function () {
	'use strict'
  var episodeSelect = document.getElementById('episodes');
	var introText = document.getElementsByClassName('intro-text');
	var content_header = document.getElementsByClassName('content-header');
	var content_body = document.getElementsByClassName('content-body');
  var episode_desc = [
    ['intro', 'header', 'body'],

  ];
  episodeSelect.addEventListener('change', function (){
    var index = this.selectedIndex;
    var value = this.options[index].value;
    var iterationCount;
    //document.getElementsByClassName('star-wars-intro').style.animationIterationCount = '3';
    console.log(value + ' ' + iterationCount);
  }, false);

  function Episode (intro, header, bd) {
    //bd = body
    this.intro = intro;
    this.header = header;
    this.bg = bd;
  }
}());
