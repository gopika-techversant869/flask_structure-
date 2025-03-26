from flask import Flask
from flask_migrate import Migrate
from flask_simple.db_service.db import db
# from config.config import get_config
from flask_simple.config.config import get_config
import logging


migrate = Migrate()

def create_app():
    app = Flask(__name__)

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s | %(levelname)s | %(filename)s | %(funcName)s | Line:%(lineno)d | %(message)s",
        handlers=[
            logging.StreamHandler()  
        ]
    )
    app_config = get_config()
    app.config.from_object(app_config)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from flask_simple.routes.test_route import bp
        app.register_blueprint(bp, url_prefix="/api")


    @app.route('/health')
    def health_check():
        return {'status': 'healthy'}, 200
    
    return app



