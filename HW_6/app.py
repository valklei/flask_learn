import os
from flask import Flask
from config import DevelopmentConfig
from extensions import db, migrate

def create_app():
    app = Flask(__name__)

    @app.route('/health')
    def health():
        return 'OK', 200

    basedir = os.path.abspath(os.path.dirname(__file__))

    # Путь к БД
    db_path = os.path.join(basedir, 'instance', 'database.db')
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    # Конфигурация
    app.config.from_object(DevelopmentConfig)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"

    # Инициализация расширений
    db.init_app(app)
    migrate.init_app(app, db)

    # Роуты
    from routers import questions_bp, answers_bp, categories_bp
    app.register_blueprint(questions_bp)
    app.register_blueprint(answers_bp)
    app.register_blueprint(categories_bp)

    # Создание БД
    if not os.path.exists(db_path):
        with app.app_context():
            db.create_all()
            print("База данных и таблицы созданы.")

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)