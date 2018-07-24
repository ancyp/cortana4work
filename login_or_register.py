from flask import Blueprint

login_or_register = Blueprint('login_or_register',__name__)

login_or_register.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')
