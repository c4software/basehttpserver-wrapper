from extended_BaseHTTPServer import serve,route,redirect, override

# TODO URL AVEC PARTIES DYNAMIQUE	
# TODO POST METHOD

@route("/",["GET"])
def main(**kwargs):
	if "name" in kwargs:
		return "Bonjour {0} <br /> <a href='/redirect'>Retour</a>".format(kwargs["name"][0])
	else:
		return "Index <br /> <a href='/?name=valentin'>Test Valentin</a><br /> <a href='/form'>Form Test</a>"

@route("/form",["GET","POST"])
def main(**kwargs):
	return "<form method='post'><input type='submit' /><input type='text' name='name' /></form>"


@override("404")
def handler_404(o, arguments):
	return "Contenu introuvable."

@override("static")
def handler_static(o, arguments):
	raise Exception("Fichier introuvable")

# Not yet Implemented
# @route("/:name",["GET"])
# def hello(**kwargs):
# 	return "Bonjour {name}"

@route("/test",["GET"])
def test(**kwargs):
	print kwargs
	return {"content":"Test","code":200,"Content-type":"text-plain"}

@route("/redirect",["GET"])
def main(**kwargs):
	return redirect("/")


if __name__ == '__main__':
	serve(ip="0.0.0.0", port=5000)
