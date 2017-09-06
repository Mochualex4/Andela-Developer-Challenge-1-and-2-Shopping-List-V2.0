from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import forms

from . import person

@person.route('/lists', methods=['GET', 'POST'])
#login required
def list_shoppinglists():
    
    #List all departments
    

    return render_template('person/lists/lists.html',
                           lists=list, title="List")

@person.route('/lists/add', methods=['GET', 'POST'])
#login reuirred
def add_list():
    
    #Add a list

    add_list = True

    form = DepartmentForm()
    if form.validate_on_submit():
        department = Department(name=form.name.data,
                                description=form.description.data)
        try:
            # add list
            
            flash('You have successfully added a new department.')
        except:
            # in case department name already exists
            flash('Error: department name already exists.')

        # redirect to departments page
        return redirect(url_for('admin.list_departments'))

    # load department template
    return render_template('admin/departments/department.html', action="Add",
                           add_department=add_department, form=form,
                           title="Add Department")

@person.route('/departments/edit/<int:id>', methods=['GET', 'POST'])
#login required
def edit_shoppinglist(id):
    """
    Edit a department
    """
    

    add_department = False

    department = Department.query.get_or_404(id)
    form = DepartmentForm(obj=department)
    if form.validate_on_submit():
        department.name = form.name.data
        department.description = form.description.data
        
        flash('You have successfully edited the department.')

        # redirect to the departments page
        return redirect(url_for('admin.list_departments'))

    form.description.data = department.description
    form.name.data = department.name
    return render_template('admin/departments/department.html', action="Edit",
                           add_department=add_department, form=form,
                           department=department, title="Edit Department")

@person.route('/departments/delete/<int:id>', methods=['GET', 'POST'])
#login required
def delete_shoppinglist(id):
    
    #Delete a List from the database

    
    department = Department.query.get_or_404(id)
    
    flash('You have successfully deleted the department.')

    # redirect to the departments page
    return redirect(url_for('admin.list_departments'))

    return render_template(title="Delete Department")
