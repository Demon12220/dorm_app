from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, DateField, FloatField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length, Optional
from app.models import User, Resident, Room

class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')

class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зарегистрироваться')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Пожалуйста, используйте другое имя пользователя.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Пожалуйста, используйте другой email.')

class RoomForm(FlaskForm):
    number = StringField('Номер комнаты', validators=[DataRequired()])
    floor = IntegerField('Этаж', validators=[DataRequired()])
    capacity = IntegerField('Вместимость', validators=[DataRequired()])
    is_active = BooleanField('Активна')
    submit = SubmitField('Сохранить')

class ResidentForm(FlaskForm):
    first_name = StringField('Имя', validators=[DataRequired()])
    last_name = StringField('Фамилия', validators=[DataRequired()])
    middle_name = StringField('Отчество')
    birth_date = DateField('Дата рождения', validators=[DataRequired()])
    passport = StringField('Паспорт', validators=[DataRequired()])
    phone = StringField('Телефон', validators=[DataRequired()])
    email = StringField('Email', validators=[Email()])
    check_in_date = DateField('Дата заселения', validators=[DataRequired()])
    check_out_date = DateField('Дата выселения', validators=[Optional()])
    room_id = SelectField('Комната', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Сохранить')
    
    def __init__(self, *args, **kwargs):
        super(ResidentForm, self).__init__(*args, **kwargs)
        self.room_id.choices = [(room.id, room.number) for room in Room.query.filter_by(is_active=True).all()]

class PaymentForm(FlaskForm):
    amount = FloatField('Сумма', validators=[DataRequired()])
    period_start = DateField('Начало периода', validators=[DataRequired()])
    period_end = DateField('Конец периода', validators=[DataRequired()])
    status = SelectField('Статус', choices=[('оплачено', 'Оплачено'), ('не оплачено', 'Не оплачено')])
    resident_id = SelectField('Житель', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Сохранить')
    
    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.resident_id.choices = [(resident.id, f"{resident.last_name} {resident.first_name}") for resident in Resident.query.all()]
