import sys
import argparse
import subprocess
import shlex
import urllib
sys.path.append('../') # Just to make the GIT source more cleaner without creating a module. In YOUR project you DON'T have to do that
from extended_BaseHTTPServer import serve,route

current_playing = []

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
parser.add_argument('--player', action='store',help='Path to VLC command line (/usr/bin/cvlc --play-and-exit)')
args = parser.parse_args()
args.player = shlex.split(args.player)

serve(ip="0.0.0.0", port=5000)
