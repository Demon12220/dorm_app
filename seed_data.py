from app import create_app, db
from app.models import Room, Resident, Payment
from datetime import datetime, timedelta
import random

app = create_app()

def seed_database():
    with app.app_context():
        # Проверка, есть ли уже данные в базе
        if Room.query.count() > 0 or Resident.query.count() > 0:
            print("В базе данных уже есть данные. Удаляем существующие данные перед созданием новых...")
            # Удаляем платежи, затем жильцов, затем комнаты (порядок важен из-за внешних ключей)
            Payment.query.delete()
            Resident.query.delete()
            Room.query.delete()
            db.session.commit()
            print("Существующие данные удалены.")

        print("Создание тестовых данных...")
        
        # Создаем комнаты: 5 этажей, 10 комнат на этаж
        print("Создание комнат...")
        rooms = []
        for floor in range(1, 6):  # 1-5 этажи
            for room_num in range(1, 11):  # 10 комнат на этаж
                room_number = f"{floor}{room_num:02d}"  # Номер в формате "этаж + номер" (101, 102, ...)
                room = Room(
                    number=room_number,
                    floor=floor,
                    capacity=2,
                    is_active=True
                )
                db.session.add(room)
                rooms.append(room)
        
        db.session.commit()
        print(f"Создано комнат: {len(rooms)}")
        print("Тестовые данные успешно созданы! Все комнаты свободны.")

if __name__ == "__main__":
    seed_database()
