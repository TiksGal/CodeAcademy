from flask import Flask

from config import Config
from app.main import bp as main_bp
from app.posts import bp as posts_bp
from app.questions import bp as questions_bp
from app.extensions import db


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    with app.app_context():
        db.create_all()
    # Register blueprints here
    app.register_blueprint(main_bp)
    app.register_blueprint(posts_bp, url_prefix='/posts')
    app.register_blueprint(questions_bp, url_prefix='/questions')
    
    @app.route('/test/')
    def test_page():
        
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app