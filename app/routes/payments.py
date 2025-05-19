from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models import Payment, Resident
from app.forms import PaymentForm

payments_bp = Blueprint('payments', __name__)

@payments_bp.route('/')
@login_required
def index():
    payments = Payment.query.all()
    return render_template('payments/list.html', title='Платежи', payments=payments)

@payments_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = PaymentForm()
    if form.validate_on_submit():
        payment = Payment(
            amount=form.amount.data,
            period_start=form.period_start.data,
            period_end=form.period_end.data,
            status=form.status.data,
            resident_id=form.resident_id.data
        )
        db.session.add(payment)
        db.session.commit()
        flash('Платеж успешно добавлен!')
        return redirect(url_for('payments.index'))
    return render_template('payments/add.html', title='Добавить платеж', form=form)

@payments_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    payment = Payment.query.get_or_404(id)
    form = PaymentForm(obj=payment)
    if form.validate_on_submit():
        payment.amount = form.amount.data
        payment.period_start = form.period_start.data
        payment.period_end = form.period_end.data
        payment.status = form.status.data
        payment.resident_id = form.resident_id.data
        db.session.commit()
        flash('Данные платежа обновлены!')
        return redirect(url_for('payments.index'))
    return render_template('payments/edit.html', title='Редактировать платеж', form=form)

@payments_bp.route('/delete/<int:id>')
@login_required
def delete(id):
    payment = Payment.query.get_or_404(id)
    db.session.delete(payment)
    db.session.commit()
    flash('Платеж удален!')
    return redirect(url_for('payments.index'))
