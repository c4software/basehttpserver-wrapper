import sys
import argparse
import subprocess
import shlex
import urllib
sys.path.append('../') # Just to make the GIT source more cleaner without creating a module. In YOUR project you DON'T have to do that
from extended_BaseHTTPServer import serve,route

current_playing = []

@route("/")
def index():
	return """
	<script src="//code.jquery.com/jquery-1.11.2.min.js"></script>
	<form style="text-align:center" id="form">
		<h1>Small-Nabz</h1>
		<input type="text" id="value" value="" placeholder="http://www..." />
		<br /><br />

		<div class="history_container">
			<ul id="listing"></ul>
		</div>

		<br /><br />

		<input type="button" value="Jouer" id="play" />
		<input type="button" value="Parler" id="say" />
		<input type="button" value="Stop" id="stop" />
	</form>
	<style>
		body {
			background: #E0E0E0;
			font-family: 'Open Sans',"Trebuchet MS",arial,sans-serif;
		}
		textarea, input:not([type=button]):not([type=submit]) {
			width: 80%;
			border: 1px solid rgba(0,0,0,.2);
			padding: 10px;
			border-radius: 2px;
		}
		.history_container{  
			max-height: 130px;
			overflow-x: auto;
			width: 80%;
			margin: auto;
		}
		input[type=button], input[type=submit] {
			display: inline-block;
			position: relative;
			margin: 0px 20px;
			padding: 6px 30px;
			background: #333;
			color: #fff;
			box-shadow: 0 4px #111;
			border: none;
			cursor: pointer;
			text-transform: uppercase;
			letter-spacing: 2px;
			outline: none;
			-webkit-transition: none;
			transition: none;
		}
		#listing {
			text-align: left;
			display: block;
			margin: 0;
			padding: 0;
			list-style-type: none;
			border-radius: 2px;
			overflow: hidden;
			min-height: 48px;
		}
		#listing > li {
			cursor:pointer;
			font-weight: 300;
			font-size: 0.9em;
			padding: 10px;
			position: relative;
			border-top: 1px solid #eee;
			border-bottom: 1px solid #eee;
			background: #fff;
			margin-top: -1px;
			margin-bottom: -1px;

			-webkit-touch-callout: none;
			-webkit-user-select: none;
			-khtml-user-select: none;
			-moz-user-select: none;
			-ms-user-select: none;
			user-select: none;
		}
	</style>
	<script>
		var histo = localStorage.getItem("histo");
		if(histo == null){
			histo = new Array();
		}else{
			histo = JSON.parse(histo);
		}

		function add_history(){
			var link = $("#value").val();
			if(histo.indexOf(link) == -1){
				histo.unshift(link);
				histo = histo.slice(0,20);
				localStorage.setItem("histo", JSON.stringify(histo))
			}
			show_history();
		}

		$("#form").bind("submit", function(e){
			e.preventDefault();
			$("#play").click();
		});
		$("#play").bind('click', function(){
			add_history()
			$.ajax({
				  url: "/play",
				  data: {file: $("#value").val()}
				});
		});

		$("#say").bind('click', function(){
			$.ajax({
				  url: "/say",
				  data: {text: $("#value").val()}
				});
		});

		$("#stop").bind('click', function(){
			$.ajax({
				  url: "/stop"
				});
		});


		// Init history
		function show_history(){
			$("#listing").html("");
			for(var i in histo){
				$("#listing").append("<li>"+histo[i]+"</li>");	
			}
		}
		show_history();
		
		$('body').on('click', 'li', function() {
			$("#value").val($(this).html());
		});

	</script>
	"""

@route("/play",["GET"])
def play(file=""):
	if current_playing:
		current_playing.pop().kill()

	try:
		# current_playing.append(subprocess.Popen("{0} {1} vlc://quit".format(args.player, file), shell=True))
		current_playing.append(subprocess.Popen(args.player+file, shell=False))			
		return "{'stream':true}"
	except:
		return "{'stream':false}"

@route("/stop",["GET"])
def stop():
	if current_playing:
		current_playing.pop().kill()
	return "{'stop':true}"

@route("/say",["GET"])
def say(text="Bonjour"):
	try:
		url = ["http://translate.google.com/translate_tts?tl=fr&q={0}".format(urllib.quote(text[0]))]
		current_playing.append(subprocess.Popen(args.player+url, shell=False))
		return "{'say':true}"
	except Exception as e:
		return "{'say':false}"


parser = argparse.ArgumentParser(description='Simple Nabz.')
parser.add_argument('--player', action='store',help='Path to VLC command line (/usr/bin/cvlc --play-and-exit  --novideo)', default="/usr/bin/cvlc --play-and-exit  --novideo")
args = parser.parse_args()
args.player = shlex.split(args.player)

serve(ip="0.0.0.0", port=8000)
