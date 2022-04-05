from flask import Blueprint,render_template,redirect
from .MyForm import MyForm

form_bp=Blueprint("bp_form", __name__,template_folder='templates')

@form_bp.route('/submit', methods=['GET', 'POST'])
def submit():
    form = MyForm()
    if form.validate_on_submit():
        print(form.name.data)
        print(form.password.data)
        return redirect('/success')
    return render_template('submit.html', form=form)



@form_bp.route('/success', methods=['GET', 'POST'])
def submit2():
    return 'ok~~~~'