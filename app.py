from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/ngo')
def ngo():
    return render_template('ngo.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Define routes for individual college pages
@app.route('/cmrit')
def cmrit():
    return render_template('cmrit.html')

@app.route('/ramaiah')
def ramaiah():
    return render_template('ramaiah.html')

@app.route('/rvce')
def rvce():
    return render_template('rvce.html')

@app.route('/acs')
def acs():
    return render_template('acs.html')

@app.route('/oxf')
def oxf():
    return render_template('oxf.html')

@app.route('/choices_known')
def choicee():
    return render_template('choices_known.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/client_portal')
def client_portal():
    return render_template('client_portal.html')

@app.route('/choices_to_learn')
def choice():
    return render_template('choices_to_learn.html')


if __name__ == '__main__':
    app.run()
