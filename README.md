basehttpserver-wrapper
======================

Simple layer to simplify the usage of BaseHTTPServer. Useful for simple API in embed project.

Supported:
* GET/POST method.
* Serve function.
* Redirect function.
* Header overiding (via dict).
* Minimal route decorator.
* 404 Method, Overiding the default behaviour (via @overide("404"))

Planned:
* Full route decorator with dynamic param (@route("/demo/:demo:/")).
* Overiding the static file delivery (via @overide("static")).
