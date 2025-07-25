from .op_routes import op_bp
from .stack_routes import stack_bp

def register_blueprints(app):
    """Register all blueprints with the Flask application."""
    app.register_blueprint(op_bp)
    app.register_blueprint(stack_bp)