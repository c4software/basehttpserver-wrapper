import sys
sys.path.append('../') # Just to make the GIT source more cleaner without creating a module. In YOUR project you DON'T have to do that
from extended_BaseHTTPServer import serve,route

@route("/",["GET"])
def main(**kwargs):
	return "TODO"


if __name__ == '__main__':
	serve(ip="0.0.0.0", port=5000)
