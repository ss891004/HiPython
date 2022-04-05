from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])  # 文本框
    password = PasswordField('password') # 密码框
    photo = FileField(validators=[FileRequired()])  # 文件上传
