from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models import Resident, Room
from app.forms import ResidentForm

residents_bp = Blueprint('residents', __name__)

@residents_bp.route('/')
@login_required
def index():
    residents = Resident.query.all()
    return render_template('residents/list.html', title='Жильцы', residents=residents)

@residents_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = ResidentForm()
    if form.validate_on_submit():
        resident = Resident(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            middle_name=form.middle_name.data,
            birth_date=form.birth_date.data,
            passport=form.passport.data,
            phone=form.phone.data,
            email=form.email.data,
            check_in_date=form.check_in_date.data,
            check_out_date=form.check_out_date.data if form.check_out_date.data else None,
            room_id=form.room_id.data
        )
        db.session.add(resident)
        db.session.commit()
        flash('Житель успешно добавлен!')
        return redirect(url_for('residents.index'))
    return render_template('residents/add.html', title='Добавить жильца', form=form)

@residents_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    resident = Resident.query.get_or_404(id)
    form = ResidentForm(obj=resident)
    if form.validate_on_submit():
        resident.first_name = form.first_name.data
        resident.last_name = form.last_name.data
        resident.middle_name = form.middle_name.data
        resident.birth_date = form.birth_date.data
        resident.passport = form.passport.data
        resident.phone = form.phone.data
        resident.email = form.email.data
        resident.check_in_date = form.check_in_date.data
        resident.check_out_date = form.check_out_date.data
        resident.room_id = form.room_id.data
        db.session.commit()
        flash('Данные жильца обновлены!')
        return redirect(url_for('residents.index'))
    return render_template('residents/edit.html', title='Редактировать жильца', form=form)

@residents_bp.route('/delete/<int:id>')
@login_required
def delete(id):
    resident = Resident.query.get_or_404(id)
    db.session.delete(resident)
    db.session.commit()
    flash('Житель удален!')
    return redirect(url_for('residents.index'))
