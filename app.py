from flask import Flask,render_template
from jinja2 import Template
app = Flask(__name__)

@app.route('/home')
@app.route('/')
def home():
    title = 'Home page'
    content = 'Home page'
    return render_template('home.html',title=title,content=content)

@app.route('/product')
def product():
    title = 'Product page'
    content = 'Product page'
    return render_template('home.html',title=title,content=content)

@app.route('/contact')
def contact():
    title = 'content page'
    content = 'Contact page'
    return render_template('home.html',title=title,content=content)

@app.route('/about')
def about():
    title = 'About page'
    content = 'About page'
    return render_template('home.html',title=title,content=content)

@app.route('/help')
def help():
    title = 'Help page'
    content = 'Help page'

    return render_template('home.html',title=title,content=content)

if __name__ == "__main__":
    app.run(debug=True)