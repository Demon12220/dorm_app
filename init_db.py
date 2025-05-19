from app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash

app = create_app()

def init_db():
    with app.app_context():
        db.create_all()
        
        # Проверка наличия администратора
        admin = User.query.filter_by(username='admin').first()
        if admin is None:
            # Создание админа
            admin = User(
                username='admin',
                email='admin@example.com',
                password_hash=generate_password_hash('admin123'),
                is_admin=True
            )
            db.session.add(admin)
            db.session.commit()
            print('Создан пользователь admin с паролем admin123')

if __name__ == '__main__':
    init_db()
    print('База данных инициализирована')
