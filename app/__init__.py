import os
from flask import Flask, jsonify, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint


def create_app():
    app = Flask(__name__)

    @app.get("/")
    def home():
        return jsonify({
            "message": "API K365 - Etapa 1",
            "docs": "/docs",
            "health": "/api/health"
        })

    @app.get("/openapi.yaml")
    def openapi_spec():
        docs_dir = os.path.abspath(os.path.join(app.root_path, "..", "docs"))
        return send_from_directory(docs_dir, "openapi.yaml")

    swagger_ui_blueprint = get_swaggerui_blueprint(
        "/docs",
        "/openapi.yaml",
        config={"app_name": "API K365 - Etapa 1"}
    )
    app.register_blueprint(swagger_ui_blueprint, url_prefix="/docs")

    from app.routes.health import health_bp
    from app.routes.products import products_bp
    from app.routes.cart import cart_bp

    app.register_blueprint(health_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(cart_bp)

    return app
