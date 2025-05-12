from models import db
from flask import Flask
from flask_migrate import Migrate
from config import DevelopmentConfig
from routers.questions import questions_bp
from routers.answers import answers_bp
from routers.categories import categories_bp

if __name__ == '__main__':
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app=app, db=db)
    app.register_blueprint(questions_bp, url_prefix="/questions")
    app.register_blueprint(answers_bp, url_prefix="/answers")
    app.register_blueprint(categories_bp, url_prefix="/categories")
    app.run(debug=True)

    #http://127.0.0.1:5000/questions