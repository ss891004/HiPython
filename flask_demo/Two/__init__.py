from .views import two_first, two_second, two_third


def init_two(app):
    app.register_blueprint(two_first)
    app.register_blueprint(two_second)
    app.register_blueprint(two_third)
