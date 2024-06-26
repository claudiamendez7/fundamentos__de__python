


from wsgiref.simple_server import make_server
from werkzeug import Response


def hello_world(request):
    return Response('Hello, world!')

if __name__ == '__main__':
    with Configurator() as config: # type: ignore
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name= 'hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()