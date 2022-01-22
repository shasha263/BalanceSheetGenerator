from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from uuid import uuid4
from flask_login import LoginManager, UserMixin

db=SQLAlchemy()

login=LoginManager()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    
    id=db.Column(db.String,primary_key=True)
    first_name=db.Column(db.String(100), nullable=True,default='')
    last_name=db.Column(db.String(100), nullable=True,default='')
    email= db.Column(db.String(150), nullable=False,unique=True)
    username= db.Column(db.String(15), nullable=False,unique=True)
    password=db.Column(db.String(150), nullable=False)

    def __init__(self,first_name,last_name,email,username,password):
        self.id= str(uuid4())
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.username=username
        self.password=generate_password_hash(password)

class Asset(db.Model):
    id=db.Column(db.String,primary_key=True)
    company_name=db.Column(db.String,nullable=False)
    date_= db.Column(db.Date,nullable=False)
    cash=db.Column(db.String,nullable=True)
    account_receivable=db.Column(db.Float, nullable = True)
    inventory=db.Column(db.String,nullable=True)
    prepaid_expense=db.Column(db.String,nullable=True)
    notes_receivable=db.Column(db.String,nullable=True)
    other_asset=db.Column(db.String,nullable=True)
    total_current_asset=db.Column(db.String,nullable=True)
    lt_investments=db.Column(db.String,nullable=True)
    land=db.Column(db.String,nullable=True)
    building=db.Column(db.String,nullable=True)
    acc_depr_building=db.Column(db.String,nullable=True)
    equipments=db.Column(db.String,nullable=True)
    acc_depr_equip=db.Column(db.String,nullable=True)
    fnf=db.Column(db.Float, nullable=True)
    acc_depr_fnf=db.Column(db.Float, nullable=True)
    other_fixed_asset=db.Column(db.Float, nullable=True)
    total_fixed_asset= db.Column(db.Float, nullable = True)
    total_asset= db.Column(db.Float, nullable = True)
    accounts_payable= db.Column(db.Float, nullable = True)
    accrued_wages=db.Column(db.Float, nullable = True)
    accrued_payroll_taxes= db.Column(db.Float, nullable = True)
    accrued_employee_benefit= db.Column(db.Float, nullable = True)
    interest_payable= db.Column(db.Float, nullable = True)
    short_term_notes= db.Column(db.Float, nullable = True)
    deferred_income= db.Column(db.Float, nullable = True)
    total_current_liabilities= db.Column(db.Float, nullable = True)
    mortgage=db.Column(db.Float, nullable = True)
    other_long_term_liabilities= db.Column(db.Float, nullable = True)
    total_long_term_liabilities= db.Column(db.Float, nullable = True)
    total_liabilities= db.Column(db.Float, nullable = True)
    paid_in_capital= db.Column(db.Float, nullable = True)
    other_equity= db.Column(db.Float, nullable = True)
    retained_earnings=db.Column(db.Float, nullable = True)
    current_year_earnings=db.Column(db.Float, nullable = True)
    total_equity=db.Column(db.Float, nullable = True)
    total_liabilities_equities= db.Column(db.Float, nullable = True)
    difference= db.Column(db.Float, nullable = True)

    def __init__(self,company_name,date_,cash,account_receivable,inventory,prepaid_expense,
    notes_receivable, other_asset,total_current_asset,lt_investments,land,building,acc_depr_building,
    equipments,acc_depr_equip,fnf,acc_depr_fnf,other_fixed_asset,total_fixed_asset,total_asset,accounts_payable,
    accrued_wages,accrued_payroll_taxes,accrued_employee_benefit,interest_payable,short_term_notes,deferred_income,total_current_liabilities,
    mortgage,other_long_term_liabilities,total_long_term_liabilities,total_liabilities,paid_in_capital,
    other_equity,retained_earnings,current_year_earnings,total_equity, total_liabilities_equities,difference):
        
        self.id= str(uuid4())
        self.company_name=company_name
        self.date_=date_
        self.cash=cash
        self.account_receivable=account_receivable
        self.inventory=inventory
        self.prepaid_expense=prepaid_expense
        self.notes_receivable=notes_receivable
        self.other_asset=other_asset
        self.total_current_asset=total_current_asset
        self.lt_investments=lt_investments
        self.land=land
        self.building=building
        self.acc_depr_building=acc_depr_building
        self.equipments=equipments
        self.acc_depr_equip=acc_depr_equip
        self.fnf=fnf
        self.acc_depr_fnf=acc_depr_fnf
        self.other_fixed_asset=other_fixed_asset
        self.total_fixed_asset=total_fixed_asset
        self.total_asset=total_asset
        self.accounts_payable=accounts_payable
        self.accrued_wages=accrued_wages
        self.accrued_payroll_taxes=accrued_payroll_taxes
        self.accrued_employee_benefit=accrued_employee_benefit
        self.interest_payable=interest_payable
        self.short_term_notes= short_term_notes
        self.deferred_income= deferred_income
        self.total_current_liabilities=total_current_liabilities
        self.mortgage= mortgage
        self.other_long_term_liabilities= other_long_term_liabilities
        self.total_long_term_liabilities= total_long_term_liabilities
        self.total_liabilities= total_liabilities
        self.paid_in_capital= paid_in_capital
        self.other_equity=other_equity
        self.retained_earnings= retained_earnings
        self.current_year_earnings= current_year_earnings
        self.total_equity=total_equity
        self.total_liabilities_equities=total_liabilities_equities
        self.difference=difference
   


    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()





 