from flask import Blueprint, render_template, json
from flask_login import login_required
from app import db
from app.models import Room, Resident, Payment
from sqlalchemy import func, desc
from datetime import datetime, timedelta

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@main_bp.route('/index')
def index():
    return render_template('index.html', title='Главная')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    # Получаем статистику комнат по этажам с учетом жильцов
    floors_stats = []
    floors = db.session.query(Room.floor).distinct().order_by(Room.floor).all()
    
    for floor_tuple in floors:
        floor = floor_tuple[0]
        
        # Получаем все комнаты на этаже
        rooms_on_floor = Room.query.filter_by(floor=floor).all()
        
        total_rooms = len(rooms_on_floor)
        occupied_rooms = 0
        total_residents = 0
        
        # Подсчитываем занятые комнаты и общее число жильцов
        for room in rooms_on_floor:
            residents_count = Resident.query.filter_by(room_id=room.id, check_out_date=None).count()
            total_residents += residents_count
            if residents_count > 0:
                occupied_rooms += 1
        
        # Вычисляем количество свободных комнат
        vacant_rooms = total_rooms - occupied_rooms
        
        # Добавляем данные в статистику
        floors_stats.append({
            'floor': floor,
            'total': total_rooms,
            'occupied': occupied_rooms,
            'vacant': vacant_rooms,
            'residents_count': total_residents
        })
    
    # Для отладки выводим данные в консоль сервера
    print("Статистика заселения:", floors_stats)
    
    # Передаем данные в шаблон в виде JSON для безопасного использования в JavaScript
    floors_stats_json = json.dumps(floors_stats)
    
    # Получение данных о последних действиях
    recent_actions = []  # Если данных о действиях нет, используем пустой список
    
    return render_template('dashboard.html', 
                          title='Панель управления',
                          floors_stats=floors_stats,
                          floors_stats_json=floors_stats_json,
                          recent_actions=recent_actions,
                          today=datetime.now().date(),
                          yesterday=(datetime.now() - timedelta(days=1)).date())
