from flask import Blueprint, flash,request,redirect,url_for
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from psycopg2 import connect, sql
from app.models import db,Asset
from app.forms import asset,modifyasset,modifyLiability,modifyEquity,search
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

           

           

            new_total_asset=Asset(form.company_name.data, form.date_.data, form.cash.data,form.account_receivable.data,form.inventory.data,form.prepaid_expense.data,form.notes_receivable.data,form.other_asset.data, form.lt_investments.data,
            form.land.data,form.building.data,form.acc_depr_building.data,form.equipments.data,form.acc_depr_equip.data,form.fnf.data,form.acc_depr_fnf.data,form.other_fixed_asset.data, 
            form.accounts_payable.data ,form.accrued_wages.data , form.accrued_payroll_taxes.data , form.accrued_employee_benefit.data , form.interest_payable.data , form.short_term_notes.data ,form.deferred_income.data, 
            form.mortgage.data,form.other_long_term_liabilities.data, form.paid_in_capital.data, form.other_equity.data, form.retained_earnings.data,form.current_year_earnings.data)
            
            new_total_asset.calc()
            
            
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


@financialstmt.route('/modify_asset/<string:id>' ,methods=['GET','POST'])
@login_required
def assetmodify(id):
    form=modifyasset()
    if request.method =='POST':
        if form.validate_on_submit():         
            asset_to_be_updated = Asset.query.get(id)          
            asset_to_be_updated.cash= form.new_cash.data
            asset_to_be_updated.account_receivable=form.new_account_receivable.data
            asset_to_be_updated.inventory=form.new_inventory.data
            asset_to_be_updated.prepaid_expense=form.new_prepaid_expense.data
            asset_to_be_updated.notes_receivable=form.new_notes_receivable.data
            asset_to_be_updated.other_asset=form.new_other_asset.data
            asset_to_be_updated.lt_investments=form.new_lt_investments.data
            asset_to_be_updated.land=form.new_land.data
            asset_to_be_updated.building=form.new_building.data
            asset_to_be_updated.acc_depr_building=form.new_acc_depr_building.data
            asset_to_be_updated.equipments=form.new_equipments.data
            asset_to_be_updated.acc_depr_equip=form.new_acc_depr_equip.data
            asset_to_be_updated.fnf=form.new_fnf.data
            asset_to_be_updated.acc_depr_fnf=form.new_acc_depr_fnf.data
            asset_to_be_updated.other_fixed_asset=form.new_other_fixed_asset.data
            asset_to_be_updated.calc()
            db.session.commit()
            print(Asset.building, Asset.fnf)
            flash('Your Asset Info has been updated', category="info")
            return redirect(url_for('financialstmt.view'))  
        else: 
            flash('Please re-enter  all the Asset Info', category="danger")
            return redirect(url_for('financialstmt.view'))
    return render_template('AssetModify.html',form=form)



@financialstmt.route('/modify_liability/<string:id>' ,methods=['GET','POST'])
@login_required
def liabilitymodify(id):
    form=modifyLiability()
    if request.method =='POST':
        if form.validate_on_submit(): 
            asset_to_be_updated = Asset.query.get(id)
            asset_to_be_updated.accounts_payable= form.new_accounts_payable.data
            asset_to_be_updated.accrued_wages= form.new_accrued_wages.data
            asset_to_be_updated.accrued_payroll_taxes= form.new_accrued_payroll_taxes.data
            asset_to_be_updated.accrued_employee_benefit= form.new_accrued_employee_benefit.data
            asset_to_be_updated.interest_payable= form.new_interest_payable.data
            asset_to_be_updated.short_term_notes= form.new_short_term_notes.data
            asset_to_be_updated.deferred_income= form.new_deferred_income.data
            asset_to_be_updated.mortgage= form.new_mortgage.data
            asset_to_be_updated.other_long_term_liabilities= form.new_other_long_term_liabilities.data
            asset_to_be_updated.calc()
            db.session.commit()
            print(Asset.interest_payable, Asset.mortgage)
            flash('Your Liability Info has been updated', category="info")
            return redirect(url_for('financialstmt.view'))  
        else: 
            flash('Please re-enter all the Liability Info', category="danger")
            return redirect(url_for('financialstmt.view'))
    return render_template('LiabilityModify.html',form=form)


@financialstmt.route('/modify_equity/<string:id>' ,methods=['GET','POST'])
@login_required
def equitymodify(id):
    form=modifyEquity()
    if request.method =='POST':
        if form.validate_on_submit():   
 
            asset_to_be_updated = Asset.query.get(id)
            asset_to_be_updated.paid_in_capital = form.new_paid_in_capital.data
            asset_to_be_updated.other_equity = form.new_other_equity.data
            asset_to_be_updated.retained_earnings = form.new_retained_earnings.data
            asset_to_be_updated.current_year_earnings = form.new_current_year_earnings.data
            asset_to_be_updated.calc()
            print(asset_to_be_updated.total_equity)
            db.session.commit()
            print(asset_to_be_updated.total_equity)
            print(Asset.paid_in_capital, Asset.current_year_earnings)
            flash('Your Equity Info has been updated', category="info")
            return redirect(url_for('financialstmt.view'))  
        else: 
            flash('Please re-enter  all the Equity Info', category="danger")
            return redirect(url_for('financialstmt.view'))

    return render_template('EquityModify.html',form=form)


@financialstmt.route('/delete/<string:id>' ,methods=['GET','POST'])
@login_required
def deleteinfo(id):
    p=Asset.query.get(id)
    if not p:
        return flash('Delete failed : No Info of that ID exist',category='warning')
    db.session.delete(p)
    db.session.commit()
    return redirect(url_for('financialstmt.view'))



@financialstmt.route('/search' ,methods=['GET'])
@login_required
def searchBS():
    form=Asset.query.order_by( Asset.id ).all()   
    return render_template('SearchBS.html',form=form)


@financialstmt.route('/search/view/<string:id>' ,methods=['GET'])
@login_required
def searchBSview(id):
    form=Asset.query.get(id)   

    #forms=Asset.query(id).filter(Asset.id == request.form["id"])
    return render_template('SearchBSview.html',form=form)


