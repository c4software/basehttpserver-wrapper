import sys
sys.path.append('../') # Just to make the GIT source more cleaner without creating a module. In YOUR project you DON'T have to do that
from extended_BaseHTTPServer import serve,route,redirect, override

@route("/",["GET"])
def main(**kwargs):
	if "name" in kwargs:
		return "Bonjour {0} <br /> <a href='/redirect'>Retour</a>".format(kwargs["name"][0])
	else:
		return "Index <br /> <a href='/?name=valentin'>Test Valentin</a><br /> <a href='/form'>Form Test</a>"

@route("/form",["GET","POST"])
def form(**kwargs):
	return "<form method='post'><input type='submit' /><input type='text' name='name' /></form>"


@override("404")
def handler_404(o, arguments, action):
	return "Contenu introuvable."

@override("500")
def handler_500(o, arguments, action):
	return "Erreur Interne."

@override("static")
def handler_static(o, arguments, action):
	raise Exception("Fichier introuvable")

# Not yet Implemented
# @route("/bonjour/:name:",["GET"])
# def hello(**kwargs):
# 	return "Bonjour {name}"

@route("/echo",["GET"])
def test(**kwargs):
	print kwargs
	return {"content":"Test","code":200,"Content-type":"text-plain"}

@route("/redirect",["GET"])
def redirect(**kwargs):
	return redirect("/")


if __name__ == '__main__':
	serve(ip="0.0.0.0", port=5000)
