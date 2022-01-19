from flask import Blueprint, flash,request,redirect,url_for
from flask.templating import render_template
from app.models import db,Asset
from app.forms import asset
from flask_login import login_required


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

            return redirect(url_for('financialstmt.balance_sheet'))         

        else:
            flash('If any of the field do not apply to your company, please enter "0"', category="danger")
            return redirect(url_for('financialstmt.total_asset'))
    return render_template('total_asset.html',form=form)


@financialstmt.route('/balancesheet')
@login_required
def balance_sheet():
    return render_template('Balance_Sheet.html')






