from flask import Flask, render_template, redirect, request
from skills.skill_hr import skill_hr
from login_or_register import login_or_register
from skills.flask_luis import get_intent
from intent_resolver import resolve_intent

app = Flask(__name__)
app.register_blueprint(skill_hr)
app.register_blueprint(login_or_register)


def dummy_fn():
    print("dummy")


@app.route("/")
def template_test():
    return render_template('template.html', my_string="Wheeeee!", my_list=[0, 1, 2, 3, 4, 5])


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
    app.run(debug=True)
