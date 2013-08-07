import BaseHTTPServer
import logging
import os
from urlparse import urlparse,parse_qs
from mimetypes import types_map

register_route = {"GET":{},"POST":{}}
def route(path="/", method=["GET"]):
	def decorator(f):
		for m in method:
			try:
				register_route[m][path] = f
			except:
				logging.error("{0} method is not available.".format(m))
		return f
	return decorator

class extended_BaseHTTPServer(BaseHTTPServer.BaseHTTPRequestHandler):
	def log_message(self, format, *args):
		return ""
		
	def do_HEAD(s):
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()

	def do_POST(s):
		o = urlparse(s.path)
		length = int(s.headers['Content-Length'])
		arguments = parse_qs(s.rfile.read(length).decode('utf-8'))
		s.do_routing(o, arguments, "POST")

	def do_GET(s):
		o = urlparse(s.path)
		arguments = parse_qs(o.query)
		s.do_routing(o, arguments, "GET")
	
	def do_routing(s, o, arguments, action):
		if o.path in register_route[action]:
			retour = register_route[action][o.path](**arguments)

			if type(retour) is dict:
				s.send_response(retour.get("code",200))
				for header in retour:
					if header not in ["code","content"]:
						s.send_header(header, retour[header])
				s.end_headers()
				s.wfile.write(retour['content'])

			else:
				s.send_response(200)
				s.send_header("Content-type", "text/html")
				s.end_headers()
				s.wfile.write(retour)
		else:
			# Fichier static ?
			try:
				with open(os.path.join("."+o.path)) as f:
					fname,ext = os.path.splitext(o.path)
					s.send_response(200)
					s.send_header('Content-type', types_map[ext])
					s.end_headers()
					s.wfile.write(f.read())
			except Exception as e:
				s.send_response(404)
				s.send_header("Content-type", "text/html")
				s.end_headers()
				# Url introuvale et fichier static introuvable ==> 404
				s.wfile.write("TODO 404 STUFF")


def redirect(location=""):
	return {"content":"","code":301,"Location":location}

def serve(ip="0.0.0.0", port=5000):
	httpd = BaseHTTPServer.HTTPServer((ip, port), extended_BaseHTTPServer)
	try:
		httpd.serve_forever()
	except:
		pass
	httpd.server_close()