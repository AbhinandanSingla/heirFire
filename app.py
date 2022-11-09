from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def hello_world():  # put application's code here
    return render_template('pages/index.html')

@app.route('/about')
def about():
    return render_template('pages/About.html')


@app.route('/contact')
def contact():
    return render_template('pages/About.html')


@app.route('/employability')
def employability():
    return render_template('pages/Get-Employability-Score.html')


@app.route('/score')
def score():
    return render_template('pages/Score.html')


if __name__ == '__main__':
    app.run()
