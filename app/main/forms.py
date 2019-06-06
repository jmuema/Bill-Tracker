from flask_wtf import FlaskForm
from wtforms import SelectField,TextAreaField,SubmitField,StringField
from wtforms.validators import Required

class BillForm(FlaskForm):
  title = StringField('Bill title')
  # date = wtforms.DateField ('Enter date', [wtforms.validators.required()])
  # category = SelectField('Choose category',choices=[('Housing','Housing'),('Utilities','Utilities',('Car','car'),('Food','Food'),('Living expenses','Living expenses')])
  description = StringField('Choose your bill',choices=[('Food','Food'),('Groceries','Groceries'),('Eat out','Eat out'),('clothes','clothes'),('entertainment','entertainment'),('travel','travel'),('car insurance','car insurance'),('car payment','car payment'),('gas','gas')])
  # amount = StatomringField('Enter amount',validators=[Required()]))
  transaction =  SelectField('Select your bill',choices=[('withdrawal','withdrawal'),('deposit','deposit'),('transfer','transfer')])
  account = SelectField('Select your mode of payment',choices=[('cash','cash'),('credit card','credit card'),('savings','savings')])
  submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
  bio =TextAreaField('Short description about you.',validators=[Required()])
  submit = SubmitField('Submit')

class DeleteForm(FlaskForm):
  submit = SubmitField('Submit')

