from flask_wtf import Form
from wtforms.fields import *
from wtforms.validators import Required, Email


class SignupForm(Form):
    name = TextField(u'Your name', validators=[Required()])
    password = TextField(u'Your favorite password', validators=[Required()])
    email = TextField(u'Your email address', validators=[Email()])

    eula = BooleanField(u'I did not read the terms and conditions',
                        validators=[Required('You must agree to not agree!')])

    submit = SubmitField(u'Signup')

class InfoForm(Form):
    rid = IntegerField('Row Number', validators=[Required()])
    cid = IntegerField('Column Number', validators=[Required()])
    uid = TextField('UID', validators=[Required()])
    submit = SubmitField('Submit') 
