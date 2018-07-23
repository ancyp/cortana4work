from flask import Flask, render_template
app = Flask(__name__)

def dummy_fn():
    print("dummy")

@app.route("/")
def template_test():
    return render_template('template.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])

@app.route("/login")
def login_page():
    return render_template('login.html')

@app.route("/input")
def input_page():
    return render_template('command_input.html', clever_function=dummy_fn)

@app.route("/forward")
def forward():
    return render_template('template.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])

if __name__ == '__main__':
    app.run(debug=True)