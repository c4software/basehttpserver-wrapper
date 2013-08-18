# basehttpserver-wrapper

Simple layer to simplify the usage of BaseHTTPServer. Useful for simple API in embed project.

*To be clear this wrapper is not the way to create a full website (like you can do with Flask or Bottle.py) its just a simple way to do some internal API for your application*


### Example :

```python
from extended_BaseHTTPServer import serve,route 

@route("/",["GET"])
def main(**kwargs):
	return "Hello Wrapper"

if __name__ == '__main__':
	serve(ip="0.0.0.0", port=5000)
```

### Functionalities

Supported:
* GET/POST method.
* Serve function.
* Redirect function.
* Header Overriding (via dict).
* Minimal route decorator.
* 404 Method, Overriding the default behaviour (via @override("404"))
* Handle Internal Error (500 error), Overriding the default behaviour (via @override("500"))
* Overriding the static file delivery (via @override("static")). PS: You have to raise an exception if you want to raise a 404 error

Planned:
* Full route decorator with dynamic param (@route("/demo/:demo:/")).

