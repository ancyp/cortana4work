from flask import Flask, render_template, redirect, request, json
from skills.skill_hr import skill_hr
from skills.skill_addevent import skill_addevent, get_events
from login_or_register import login_or_register
from skills.flask_luis import get_intent
from intent_resolver import resolve_intent
import datetime
from flask_cors import CORS

from OpenSSL import SSL
# context = SSL.Context(SSL.SSLv23_METHOD)
# context.use_privatekey_file('/home/pavan/cortana4work/a.key')
# context.use_certificate_file('/home/pavan/cortana4work/a.cert')

app = Flask(__name__)

app.register_blueprint(skill_hr)
app.register_blueprint(login_or_register)
app.register_blueprint(skill_addevent)
CORS(app)

time_offset = 0 

def dummy_fn():
    print("dummy")


@app.route("/", methods=['GET'])
def template_test():
    global time_offset
    if(request.args.get('timedelta') is None):
        timedelta = 0
    else:
        timedelta = int(request.args.get('timedelta'))
    
    time_offset=time_offset+timedelta
    items = get_events(datetime.datetime.now()+datetime.timedelta(days=time_offset))
    return render_template('index.html', items=json.loads(items))


@app.route("/input")
def input_page():
    return render_template('command_input.html', clever_function=dummy_fn)


@app.route("/chat")
def chat():
    return render_template('chat.html')


@app.route("/interpret-command", methods=['POST'])
def forward():
    intent = get_intent(command=list(request.form)[0])
    task_executor = resolve_intent(intent)
    return task_executor(intent)

@app.route('/taskssettings', methods=['GET'])
def task_settings():
    return render_template('taskssettings.html')

if __name__ == '__main__':
    context = ('a.cert', 'a.key')
    # app.run(threaded=True, debug=True)
    app.run(debug=True, host='localhost', ssl_context=context)
