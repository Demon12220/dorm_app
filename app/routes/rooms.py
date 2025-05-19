from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models import Room
from app.forms import RoomForm

rooms_bp = Blueprint('rooms', __name__)

@rooms_bp.route('/')
@login_required
def index():
    rooms = Room.query.all()
    return render_template('rooms/list.html', title='Комнаты', rooms=rooms)

@rooms_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = RoomForm()
    if form.validate_on_submit():
        room = Room(
            number=form.number.data,
            floor=form.floor.data,
            capacity=form.capacity.data,
            is_active=form.is_active.data
        )
        db.session.add(room)
        db.session.commit()
        flash('Комната успешно добавлена!')
        return redirect(url_for('rooms.index'))
    return render_template('rooms/add.html', title='Добавить комнату', form=form)

@rooms_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    room = Room.query.get_or_404(id)
    form = RoomForm(obj=room)
    if form.validate_on_submit():
        room.number = form.number.data
        room.floor = form.floor.data
        room.capacity = form.capacity.data
        room.is_active = form.is_active.data
        db.session.commit()
        flash('Данные комнаты обновлены!')
        return redirect(url_for('rooms.index'))
    return render_template('rooms/edit.html', title='Редактировать комнату', form=form)

@rooms_bp.route('/delete/<int:id>')
@login_required
def delete(id):
    room = Room.query.get_or_404(id)
    if room.residents.count() > 0:
        flash('Невозможно удалить комнату, в которой проживают жильцы!')
        return redirect(url_for('rooms.index'))
    db.session.delete(room)
    db.session.commit()
    flash('Комната удалена!')
    return redirect(url_for('rooms.index'))
