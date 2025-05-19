import os
import sys
import webview
import threading
from app import create_app
from app.models import User, Room, Resident, Payment
from datetime import datetime, timedelta

def create_admin_user(app):
    from app import db
    # Проверяем, существует ли админ
    with app.app_context():
        admin = User.query.filter_by(username='admin').first()
        if admin is None:
            # Создаем админа
            admin = User(
                username='admin',
                email='admin@example.com',
                is_admin=True
            )
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
            print('Создан пользователь admin с паролем admin123')

def start_flask():
    app = create_app()
    
    # Добавляем глобальный контекст для шаблонов
    @app.context_processor
    def inject_dates():
        return {
            'today': datetime.today().date(),
            'yesterday': (datetime.today() - timedelta(days=1)).date()
        }
    
    # Создаем админа
    create_admin_user(app)
    
    # Запускаем Flask приложение на localhost:5000
    app.run(host='127.0.0.1', port=5000, threaded=True)

def main():
    # Запускаем Flask в отдельном потоке
    t = threading.Thread(target=start_flask)
    t.daemon = True
    t.start()
    
    # Создаем окно для PyWebView
    webview.create_window(
        title="Система управления общежитием",
        url="http://127.0.0.1:5000",
        width=1024,
        height=768,
        resizable=True,
        min_size=(800, 600)
    )
      # Запускаем основной цикл PyWebView
    webview.start(debug=False)

if __name__ == '__main__':
    main()
