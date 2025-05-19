from app import create_app, db
from app.models import User, Room, Resident, Payment
from werkzeug.security import generate_password_hash
from flask import Flask
from datetime import datetime, timedelta

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Room': Room, 'Resident': Resident, 'Payment': Payment}

# Функция для создания администратора
def create_admin_user():
    # Проверяем, существует ли админ
    admin = User.query.filter_by(username='admin').first()
    if admin is None:
        # Создаем админа
        admin = User(
            username='admin',
            email='admin@example.com',
            is_admin=True
        )
        admin.set_password('admin123')  # Используем метод set_password модели
        db.session.add(admin)
        db.session.commit()
        print('Создан пользователь admin с паролем admin123')

# Добавляем глобальный контекст для шаблонов
@app.context_processor
def inject_dates():
    return {
        'today': datetime.today().date(),
        'yesterday': (datetime.today() - timedelta(days=1)).date()
    }

if __name__ == '__main__':
    # Проверяем и создаем админа перед запуском
    with app.app_context():
        create_admin_user()
    
    app.run(debug=True)
