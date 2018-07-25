from flask import Flask, render_template, redirect, request, json
from skills.skill_hr import skill_hr
from skills.skill_addevent import skill_addevent, get_events
from login_or_register import login_or_register
from skills.flask_luis import get_intent
from intent_resolver import resolve_intent
import datetime

from OpenSSL import SSL
# context = SSL.Context(SSL.SSLv23_METHOD)
# context.use_privatekey_file('/home/pavan/cortana4work/a.key')
# context.use_certificate_file('/home/pavan/cortana4work/a.cert')

app = Flask(__name__)
app.register_blueprint(skill_hr)
app.register_blueprint(login_or_register)
app.register_blueprint(skill_addevent)


def dummy_fn():
    print("dummy")


@app.route("/")
def template_test():
    items = get_events(datetime.datetime.now())
    return render_template('index.html', items=json.loads(items))


@app.route("/input")
def input_page():
    return render_template('command_input.html', clever_function=dummy_fn)


@app.route("/chat")
def chat():
    return render_template('chat.html')


@app.route("/interpret-command", methods=['POST'])
def forward():
    intent = get_intent(command=request.form.keys()[0])
    task_executor = resolve_intent(intent)
    return task_executor(intent)


if __name__ == '__main__':
    context = ('a.cert', 'a.key')
    app.run(ssl_context=context,
            threaded=True, debug=True)
    # app.run(debug=True, host='172.20.10.14', ssl_context=context)
