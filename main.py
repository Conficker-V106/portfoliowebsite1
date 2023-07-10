from flask import Flask, render_template

app = Flask(__name__)

VAR = 0


@app.route('/')
def index():
    global VAR
    if VAR == 0:
        VAR = 1
        return render_template('home.html', Job_Name="Python Developer")
    else:
        VAR = 0
        return render_template('home.html', Job_Name="Cyber Security Enthusiast")


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/downcv')
def downcv():
    return render_template('downcv.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


if __name__ == '__main__':
    app.run(debug=True)
