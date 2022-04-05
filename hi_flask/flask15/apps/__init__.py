from .v_form import form_bp

def  init_view(app):
    app.register_blueprint(form_bp)
