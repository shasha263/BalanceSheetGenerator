from flask import Blueprint, flash,request,redirect,url_for
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from psycopg2 import connect, sql
from app.models import db,Asset
from app.forms import asset,modifyasset,modifyLiability,modifyEquity
from flask_login import login_required
db=SQLAlchemy()


financialstmt= Blueprint('financialstmt',__name__, template_folder='financialstmt_templates')

@financialstmt.route('/totalasset' ,methods=['GET','POST'])
@login_required
def total_asset():
    form= asset()
    if request.method=='POST':
        #print("Correct Asset Input")      
        print(form.cash.data,form.prepaid_expense.data,form.inventory.data) 
        if form.validate_on_submit():
            flash("You have succefully enter your information.", category= "info")      
            total_current_asset= form.cash.data + form.account_receivable.data + form.inventory.data + form.prepaid_expense.data + form.notes_receivable.data +form.other_asset.data
            print(total_current_asset) #tesing purpose
            total_fixed_asset= form.lt_investments.data+form.land.data+form.building.data-(form.acc_depr_building.data)+form.equipments.data-(form.acc_depr_equip.data)+form.fnf.data-(form.acc_depr_fnf.data)+form.other_fixed_asset.data
            print(total_fixed_asset) #tesing purpose
            total_asset= total_current_asset + total_fixed_asset
            print(total_asset) #tesing purpose

            total_current_liabilities= form.accounts_payable.data + form.accrued_wages.data + form.accrued_payroll_taxes.data + form.accrued_employee_benefit.data + form.interest_payable.data + form.short_term_notes.data +form.deferred_income.data
            total_long_term_liabilities= form.mortgage.data+form.other_long_term_liabilities.data
            total_liabilities= total_current_liabilities + total_long_term_liabilities

            total_equity= form.paid_in_capital.data+ form.other_equity.data + form.retained_earnings.data + form.current_year_earnings.data
            
            total_liabilities_equities= total_liabilities + total_equity

            difference= total_asset- total_liabilities_equities

            new_total_asset=Asset(form.company_name.data, form.date_.data, form.cash.data,form.account_receivable.data,form.inventory.data,form.prepaid_expense.data,form.notes_receivable.data,form.other_asset.data,total_current_asset,   form.lt_investments.data,
            form.land.data,form.building.data,form.acc_depr_building.data,form.equipments.data,form.acc_depr_equip.data,form.fnf.data,form.acc_depr_fnf.data,form.other_fixed_asset.data, total_fixed_asset, total_asset,
            form.accounts_payable.data ,form.accrued_wages.data , form.accrued_payroll_taxes.data , form.accrued_employee_benefit.data , form.interest_payable.data , form.short_term_notes.data ,form.deferred_income.data, total_current_liabilities,
            form.mortgage.data,form.other_long_term_liabilities.data, total_long_term_liabilities,total_liabilities, form.paid_in_capital.data, form.other_equity.data, form.retained_earnings.data,form.current_year_earnings.data,total_equity, total_liabilities_equities,difference)
            
           
            
            
            print(f'New Total Asset Entered-{new_total_asset.__dict__}')
            try:
                db.session.add( new_total_asset)
                db.session.commit()        
                
            except:
               print('Incorrect Info') #tesing purpose
               return redirect(url_for('financialstmt.total_asset'))

            return render_template('Balance_Sheet.html', new_total_asset=new_total_asset)        

        else:
            flash('If any of the field do not apply to your company, please enter "0"', category="danger")
            return redirect(url_for('financialstmt.total_asset'))
    return render_template('total_asset.html',form=form)


@financialstmt.route('/balancesheet')
@login_required
def balance_sheet():
    return render_template('Balance_Sheet.html')


@financialstmt.route('/view' ,methods=['GET'])
@login_required
def view():
    balanceSheetview=Asset.query.order_by( Asset.id ).all()   
    return render_template('view.html',balanceSheetview=balanceSheetview)


@financialstmt.route('/modify_asset' ,methods=['GET','POST'])
@login_required
def assetmodify():
    form=modifyasset()
    if request.method =='POST':
        if form.validate_on_submit():            
            Asset.cash= form.new_cash.data
            Asset.account_receivable=form.new_account_receivable.data
            Asset.inventory=form.new_inventory.data
            Asset.prepaid_expense=form.new_prepaid_expense.data
            Asset.notes_receivable=form.new_notes_receivable.data
            Asset.other_asset=form.new_other_asset.data
            Asset.lt_investments=form.new_lt_investments.data
            Asset.land=form.new_land.data
            Asset.building=form.new_building.data
            Asset.acc_depr_building=form.new_acc_depr_building.data
            Asset.equipments=form.new_equipments.data
            Asset.acc_depr_equip=form.new_acc_depr_equip.data
            Asset.fnf=form.new_fnf.data
            Asset.acc_depr_fnf=form.new_acc_depr_fnf.data
            Asset.other_fixed_asset=form.new_other_fixed_asset.data
            db.session.commit()
            print(Asset.building, Asset.fnf)
            flash('Your Asset Info has been updated', category="info")
            return redirect(url_for('financialstmt.view'))  
        else: 
            flash('Please re-enter  all the Asset Info', category="danger")
            return redirect(url_for('financialstmt.view'))
    return render_template('AssetModify.html',form=form)



@financialstmt.route('/modify_liability' ,methods=['GET','POST'])
@login_required
def liabilitymodify():
    form=modifyLiability()
    if request.method =='POST':
        if form.validate_on_submit(): 
            Asset.accounts_payable= form.new_accounts_payable.data
            Asset.accrued_wages= form.new_accrued_wages.data
            Asset.accrued_payroll_taxes= form.new_accrued_payroll_taxes.data
            Asset.accrued_employee_benefit= form.new_accrued_employee_benefit.data
            Asset.interest_payable= form.new_interest_payable.data
            Asset.short_term_notes= form.new_short_term_notes.data
            Asset.deferred_income= form.new_deferred_income.data
            Asset.mortgage= form.new_mortgage.data
            Asset.other_long_term_liabilities= form.new_other_long_term_liabilities.data
            db.session.commit()
            print(Asset.interest_payable, Asset.mortgage)
            flash('Your Liability Info has been updated', category="info")
            return redirect(url_for('financialstmt.view'))  
        else: 
            flash('Please re-enter all the Liability Info', category="danger")
            return redirect(url_for('financialstmt.view'))
    return render_template('LiabilityModify.html',form=form)


@financialstmt.route('/modify_equity' ,methods=['GET','POST'])
@login_required
def equitymodify():
    form=modifyEquity()
    if request.method =='POST':
        if form.validate_on_submit():   
            Asset.paid_in_capital= form.new_paid_in_capital.data
            Asset.other_equity= form.new_other_equity.data
            Asset.retained_earnings= form.new_retained_earnings.data
            Asset.current_year_earnings=   form.new_current_year_earnings.data  
            
           # Asset.paid_in_capital.db.session.add()
            #Asset.other_equity.db.session.add()
           # Asset.retained_earnings.db.session.add()
            #Asset.current_year_earnings.db.session.add()
            # db.session.add(Asset.paid_in_capital)
            # db.session.add(Asset.other_equity)
            # db.session.add(Asset.retained_earnings)
            # db.session.add(Asset.current_year_earnings)

            db.session.commit()

            print(Asset.paid_in_capital, Asset.current_year_earnings)
            flash('Your Equity Info has been updated', category="info")
            return redirect(url_for('financialstmt.view'))  
        else: 
            flash('Please re-enter  all the Equity Info', category="danger")
            return redirect(url_for('financialstmt.view'))

    return render_template('EquityModify.html',form=form)


@financialstmt.route('/delete' ,methods=['GET','POST'])
@login_required
def deleteinfo():
    p=Asset.query.filter_by(id=Asset.id).first()
    if not p:
        return flash('Delete failed : No Info of that ID exist',category='warning')
    db.session.delete(p)
    db.session.commit()
    return redirect(url_for('financialstmt.view'))









