from .views import first, second, third


def init_view(app):
    app.register_blueprint(first)
    app.register_blueprint(second)
    app.register_blueprint(third)
