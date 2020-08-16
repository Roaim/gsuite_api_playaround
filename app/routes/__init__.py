from .hello_route import bp as hello_bp


def init_app(app):
    app.url_map.strict_slashes = False
    app.register_blueprint(hello_bp)
