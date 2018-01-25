(function () {
	'use strict';

  var films = $(".film");
	var currentPos = 0;
	init();
	function init(){
		console.log('init()');
    $(".film").not(":first").hide();
		$("#modal-overlay").hide();
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

	$(".img-thumbnail").click(function(){
	// $("#modal-open").click(function(){
		//[id:modal-open]をクリックしたら起こる処理
		var overlay_visible = $("#modal-overlay").is(':visible');
		console.log($("#modal-overlay").is(':visible'));
		$(this).blur() ;	//ボタンからフォーカスを外す
		if($("#modal-overlay").is(':visible') === true)
			return false ;		//新しくモーダルウィンドウを起動しない [下とどちらか選択]
			//if($("#modal-overlay")[0]) $("#modal-overlay").remove() ;		//現在のモーダルウィンドウを削除して新しく起動する [上とどちらか選択]

			//オーバーレイ用のHTMLコードを、[body]内の最後に生成する
		// $("body").append('<div id="modal-overlay"></div>');

			//[$modal-overlay]をフェードインさせる
		console.log('before modal overlay fadein');
		$("#modal-overlay").fadeIn("slow");
		var pic_id = $(this).attr('id');

		if (overlay_visible === false) {
			var f = $(".film").get(currentPos);
	    $(f).hide();
			var f_selected = $(".film").get(pic_id);
			$(f_selected).fadeIn(1000);
			currentPos = pic_id;
			console.log('pic-id: ' + pic_id)
		}
		console.log($("#modal-overlay").is(':visible'));
		//[$modal-content]をフェードインさせる
		centeringModalSyncer();
		console.log('currentpos = ' + currentPos + ' left ' + $("#modal-content").css('left') + ', top: ' + $("#modal-content").css('top'));
		$("#modal-content").fadeIn("slow");
	});

	$("#modal-overlay,#modal-close").unbind().click(function(){
	//[#modal-overlay]、または[#modal-close]をクリックしたら起こる処理

	//[#modal-overlay]と[#modal-close]をフェードアウトする
		$("#modal-content,#modal-overlay").fadeOut("slow",function(){
	//フェードアウト後、[#modal-overlay]をHTML(DOM)上から削除
			$("#modal-overlay").hide();
			// $("#modal-overlay").remove();
		});
	});
	//リサイズされたら、センタリングをする関数[centeringModalSyncer()]を実行する
	$(window).resize(centeringModalSyncer);

	function centeringModalSyncer(){
		var w = $(window).width();
		var h = $(window).height();
		var cw = $("#modal-content").outerWidth();
		var ch = $("#modal-content").outerHeight();

		var pxleft = ((w - cw)/2);
		var pxtop = ((h - ch)/2);

		$("#modal-content").css({"left": pxleft + "px"});
		$("#modal-content").css({"top": pxtop + "px"});

	};
	$("#modal-close").hover(function (){
		$(this).css({"text-decoration" : "underline", "cursor": "pointer"});
		$(".fa-times").css({"text-decoration" : "underline", "cursor": "pointer"});
		}, function (){
			$(this).css({"text-decoration" : "none"});
			$(".fa").css({"text-decoration" : "none"});
	});
})();
