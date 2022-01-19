from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,PasswordField, FloatField,DateField
from  wtforms.validators import DataRequired,Email, equal_to


class Signinform(FlaskForm):    
    
    username=StringField('Username',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])
    submit=SubmitField('Login')


class Signupform(FlaskForm):
    
    first_name= StringField('First Name',validators=[DataRequired()])
    last_name= StringField('Last Name',validators=[DataRequired()])
    email=StringField('Email',validators=[DataRequired(),Email()])
    username=StringField('Username',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])
    confirm_password= StringField('Confirm Password',validators=[DataRequired(),equal_to('password')])
    submit=SubmitField('Create Free Account')

class updateUsernameForm(FlaskForm):   
   
    newusername=StringField('New Username',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])
    submit=SubmitField('Update userName')


class updatePasswordForm(FlaskForm):   
   
    username=StringField('Username',validators=[DataRequired()])
    newpassword=PasswordField('Password',validators=[DataRequired()])
    confirm_newpassword= StringField('Confirm Password',validators=[DataRequired(),equal_to('newpassword')])
    submit=SubmitField('Update password')


class asset(FlaskForm): 
    company_name=StringField('Company Name',validators=[DataRequired()])
    date_=DateField('Balance Sheet Date',validators=[DataRequired()])
    cash=FloatField('Cash')
    account_receivable=FloatField('Account Receivable')
    inventory=FloatField('Inventory')
    prepaid_expense=FloatField('Prepaid Expenses')
    notes_receivable=FloatField('Notes Receivable')
    other_asset=FloatField('Other Current Assets')
    lt_investments=FloatField('Long-Term Investments')
    land=FloatField('Land')
    building=FloatField('Building')
    acc_depr_building=FloatField('(Accumulated Depreciation - Building)')
    equipments=FloatField('Equipments')
    acc_depr_equip=FloatField('(Accumulated Depreciation -Equipments)')
    fnf=FloatField('Furniture and Fixtures')
    acc_depr_fnf=FloatField('(Accumulated Depreciation - Furniture and Fixtures)')
    other_fixed_asset=FloatField('Other Fixed Assets')
    accounts_payable=FloatField('Accounts Payable')
    accrued_wages= FloatField('Accrued Wages')
    accrued_payroll_taxes= FloatField('Accrued Payroll Taxes')
    accrued_employee_benefit= FloatField('Accrued Employee Benefit')
    interest_payable= FloatField('Interest Payable')
    short_term_notes= FloatField('Short Term Notes')
    deferred_income= FloatField('Deferred Income')
    mortgage= FloatField('Mortgage')
    other_long_term_liabilities= FloatField('Other Long Term Liabilities')
    paid_in_capital= FloatField('Paid-in-Capital')
    other_equity= FloatField('Other Equity')
    retained_earnings= FloatField('Retained Earnings')
    current_year_earnings= FloatField('Current Year Earnings')
    submit=SubmitField('Submit and Continue...')


#class fixedasset(FlaskForm): 
 #   lt_investments=FloatField('Long-Term Investments',validators=[DataRequired()])
  #  land=FloatField('Land',validators=[DataRequired()])
   # building=FloatField('Building',validators=[DataRequired()])
    #acc_depr_building=FloatField('Accumulated Depreciation - Building',validators=[DataRequired()])
    #equipments=FloatField('Equipments',validators=[DataRequired()])
    #acc_depr_equip=FloatField('Accumulated Depreciation -Equipments',validators=[DataRequired()])
    #fnf=FloatField('Furniture and Fixtures',validators=[DataRequired()])
    #acc_depr_fnf=FloatField('Accumulated Depreciation - Furniture and Fixtures',validators=[DataRequired()])
    #other_fixed_asset=FloatField('Other Fixed Assets',validators=[DataRequired()])
    #submit=SubmitField('Submit and Continue...')


    



