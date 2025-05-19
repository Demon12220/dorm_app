from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app(config_class=Config):
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(config_class)
    
    db.init_app(app)
    login_manager.init_app(app)
    
    from app.routes.main import main_bp
    from app.routes.auth import auth_bp
    from app.routes.residents import residents_bp
    from app.routes.rooms import rooms_bp
    from app.routes.payments import payments_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(residents_bp, url_prefix='/residents')
    app.register_blueprint(rooms_bp, url_prefix='/rooms')
    app.register_blueprint(payments_bp, url_prefix='/payments')
    
    with app.app_context():
        db.create_all()
    
    return app
