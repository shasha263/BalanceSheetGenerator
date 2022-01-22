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
    acc_depr_building=FloatField('(Accumulated Depreciation-Building)')
    equipments=FloatField('Equipments')
    acc_depr_equip=FloatField('(Accumulated Depreciation-Equipments)')
    fnf=FloatField('Furniture and Fixtures')
    acc_depr_fnf=FloatField('(Accumulated Depreciation-Furniture and Fixtures)')
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


class modifyasset(FlaskForm):  
    new_cash=FloatField('Cash')
    new_account_receivable=FloatField('Account Receivable')
    new_inventory=FloatField('Inventory')
    new_prepaid_expense=FloatField('Prepaid Expenses')
    new_notes_receivable=FloatField('Notes Receivable')
    new_other_asset=FloatField('Other Current Assets')
    new_lt_investments=FloatField('Long-Term Investments')
    new_land=FloatField('Land')
    new_building=FloatField('Building')
    new_acc_depr_building=FloatField('(Accumulated Depreciation-Building)')
    new_equipments=FloatField('Equipments')
    new_acc_depr_equip=FloatField('(Accumulated Depreciation-Equipments)')
    new_fnf=FloatField('Furniture and Fixtures')
    new_acc_depr_fnf=FloatField('(Accumulated Depreciation-Furniture and Fixtures)')
    new_other_fixed_asset=FloatField('Other Fixed Assets')
    submit=SubmitField('Update Asset Info')


class modifyLiability(FlaskForm):
    new_accounts_payable=FloatField('Accounts Payable')
    new_accrued_wages= FloatField('Accrued Wages')
    new_accrued_payroll_taxes= FloatField('Accrued Payroll Taxes')
    new_accrued_employee_benefit= FloatField('Accrued Employee Benefit')
    new_interest_payable= FloatField('Interest Payable')
    new_short_term_notes= FloatField('Short Term Notes')
    new_deferred_income= FloatField('Deferred Income')
    new_mortgage= FloatField('Mortgage')
    new_other_long_term_liabilities= FloatField('Other Long Term Liabilities')
    submit=SubmitField('Submit and Continue...')


class modifyEquity(FlaskForm):
    new_paid_in_capital= FloatField('Paid-in-Capital')
    new_other_equity= FloatField('Other Equity')
    new_retained_earnings= FloatField('Retained Earnings')
    new_current_year_earnings= FloatField('Current Year Earnings')
    submit=SubmitField('Submit and Continue...')


