<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Muga Yoshikawa</title>
	<link rel="stylesheet" href="css/normalize.css">

	<link rel="stylesheet" href="css/font-awesome.min.css">
	<!-- Bootstrap CSS -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">

	<link rel="stylesheet" href="css/style_common.css">
	<link rel="stylesheet" href="css/style_films.css">
	<link href="https://fonts.googleapis.com/css?family=Amatic+SC:700" rel="stylesheet">
	<link href="https://fonts.googleapis.com/css?family=Anton" rel="stylesheet">
	<link href="https://fonts.googleapis.com/css?family=Cherry+Swash:700" rel="stylesheet">
</head>

	<body>
		<?php include('header.php'); ?>

		<div id="modal-content">
			<div class="container">
				<div class="row">
					<div class="film">
						<img class="slide_pic" src="img/phantom_menace.jpeg">
						<p>Episode I Phantom Menace</p>
					</div>
					<div class="film">
						<img class="slide_pic" src="img/attack_clones.jpeg">
						<p>Episode II Attack of the Clones</p>
					</div>
					<div class="film">
						<img class="slide_pic" src="img/revenge_sith.jpeg">
						<p>Episode III Revenge of the Sith</p>
					</div>
					<div class="film">
						<img class="slide_pic" src="img/new_hope.jpg">
						<p>Episode IV A New Hope</p>
					</div>
					<div class="film">
						<img class="slide_pic" src="img/empire.jpg">
						<p>Episode V The Empire Strikes Back</p>
					</div>

					<div class="film">
						<img class="slide_pic" src="img/jedi.jpg">
						<p>Episode VI Return of the Jedi</p>
					</div>
					<div class="film">
						<img class="slide_pic" src="img/awakens.jpeg">
						<p>Episode VII The Force Awakens</p>
					</div>
					<div class="film">
						<img class="slide_pic" src="img/rogue_one.jpeg">
						<p>Rogue One</p>
					</div>
					<div class="film">
						<img class="slide_pic" src="img/blade_runner2.jpg">
						<p>Blade Runner</p>
					</div>
					<div class="film">
						<img class="slide_pic" src="img/2049.jpg">
						<p>Blade Runner 2049</p>
					</div>
				</div>
			<!-- <img src="img/2049.jpg">
			<p>Blade Runner 2049</p> -->
				<div class="row">
					<p>「閉じる」か「背景」をクリックするとモーダルウィンドウを終了します。
						<a id="modal-close" class="button-link"><i class="fa fa-times" aria-hidden="true"></i>閉じる</a>
					</p>
					<div class="btn" id="btn_prev"><i class="fa fa-arrow-circle-o-left" aria-hidden="true"></i></div>
					<div class="btn" id="btn_next"><i class="fa fa-arrow-circle-o-right" aria-hidden="true"></i></div>
				</div>
			</div>
		</div>
		<div id= "modal-overlay"></div>
		<!-- Page Content -->
		<div class="container">

			<h1 class="my-4 text-center text-lg-left">My Favourite Films</h1>

			<div class="row text-center text-lg-left">

				<div class="col-lg-3 col-md-4 col-xs-6">
					<a href="#" class="d-block mb-4 h-100">
						<img class="img-fluid img-thumbnail" id="0" src="img/phantom_menace.jpeg" alt="">
					</a>
				</div>
				<div class="col-lg-3 col-md-4 col-xs-6">
					<a href="#" class="d-block mb-4 h-100">
						<img class="img-fluid img-thumbnail" id="1" src="img/attack_clones.jpeg" alt="">
					</a>
				</div>
				<div class="col-lg-3 col-md-4 col-xs-6">
					<a href="#" class="d-block mb-4 h-100">
						<img class="img-fluid img-thumbnail" id="2" src="img/revenge_sith.jpeg" alt="">
					</a>
				</div>
				<div class="col-lg-3 col-md-4 col-xs-6">
					<a href="#" class="d-block mb-4 h-100">
						<img class="img-fluid img-thumbnail" id="3" src="img/new_hope.jpg" alt="">
					</a>
				</div>
				<div class="col-lg-3 col-md-4 col-xs-6">
					<a href="#" class="d-block mb-4 h-100">
						<img class="img-fluid img-thumbnail" id="4" src="img/empire.jpg" alt="">
					</a>
				</div>
				<div class="col-lg-3 col-md-4 col-xs-6">
					<a href="#" class="d-block mb-4 h-100">
						<img class="img-fluid img-thumbnail" id="5" src="img/jedi.jpg" alt="">
					</a>
				</div>
				<div class="col-lg-3 col-md-4 col-xs-6">
					<a href="#" class="d-block mb-4 h-100">
						<img class="img-fluid img-thumbnail" id="6" src="img/awakens.jpeg" alt="">
					</a>
				</div>
				<div class="col-lg-3 col-md-4 col-xs-6">
					<a href="#" class="d-block mb-4 h-100">
						<img class="img-fluid img-thumbnail" id="7" src="img/rogue_one.jpeg" alt="">
					</a>
				</div>
				<div class="col-lg-3 col-md-4 col-xs-6">
					<a href="#" class="d-block mb-4 h-100">
						<img class="img-fluid img-thumbnail" id="8" src="img/blade_runner2.jpg" alt="">
					</a>
				</div>
				<div class="col-lg-3 col-md-4 col-xs-6">
					<a href="#" class="d-block mb-4 h-100">
						<img class="img-fluid img-thumbnail" id="9" src="img/2049.jpg" alt="">
					</a>
				</div>

			</div>

		<div id="footer">
				created by Muga Yoshikawa
		</div>
		<script src="https://code.jquery.com/jquery-3.2.1.js" integrity="sha256-DZAnKJ/6XZ9si04Hgrsxu/8s717jcIzLy3oi35EouyE=" crossorigin="anonymous"></script>
	 	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js" integrity="sha384-vFJXuSJphROIrBnz7yo7oB41mKfc8JzQZiCq4NCceLEaO4IHwicKwpJf9c9IpFgh" crossorigin="anonymous"></script>
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js" integrity="sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ" crossorigin="anonymous"></script>
		<script type="text/javascript" src="js/footerFixed.js"></script>
		<script type="text/javascript" src="js/films_controller.js"></script>


	</body>




</html>