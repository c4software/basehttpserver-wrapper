basehttpserver-wrapper
======================

Simple layer to simplify the usage of BaseHTTPServer. Useful for simple API in embed project.

Supported:
* GET/POST method.
* Serve function.
* Redirect function.
* Header overiding (via dict).
* Minimal route decorator.
* 404 Method, Overiding the default behaviour (via @override("404"))
* Overriding the static file delivery (via @override("static")). PS: You have to raise an exception if you want to raise a 404 error

Planned:
* Full route decorator with dynamic param (@route("/demo/:demo:/")).

