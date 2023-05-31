from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, BooleanField, PasswordField, EmailField, IntegerField, FileField
from wtforms.validators import InputRequired, Length, DataRequired, EqualTo, Email, NumberRange

class UserCreateForm(FlaskForm):
    username = StringField('이름', validators = [DataRequired(), Length(min = 2, max = 25)])
    password1 = PasswordField('비밀번호', validators = [DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다.')])
    password2 = PasswordField('비밀번호 확인', validators = [DataRequired()])
    email = EmailField('이메일', validators = [DataRequired(), Email()])

class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators = [DataRequired(), Length(min = 2, max = 25)])
    password = PasswordField('비밀번호', validators = [DataRequired()])

class ItemForm(FlaskForm):
    store_name = StringField('가게 이름', validators = [DataRequired('가게 이름을 입력해주세요.')])
    rate = IntegerField('별점', validators = [DataRequired('별점을 입력해주세요.'), NumberRange(min=1, max=5, message="Rate must be between 1 and 5")])
    img = FileField('이미지',  validators=[DataRequired('이미지를 입력해주세요.')])
    desc = TextAreaField('후기글', validators = [DataRequired('후기를 입력해주세요.')])
    location = RadioField('지역선택', choices = ['중구', '동구', '서구', '남구', '북구','수성구', '달서구', '달성군'], validators = [InputRequired()])