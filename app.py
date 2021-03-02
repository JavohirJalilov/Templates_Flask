from flask import Flask,render_template
from jinja2 import Template
app = Flask(__name__)

html_tmp = Template('''
<html lang="en">
<head>
    <title>{{title}}</title>
</head>
<body>
    <h1>{{content}}</h1>
    {{link}}
</body>
</html>''')

@app.route('/home')
@app.route('/')
def home():
    title = 'Home page'
    content = '<h3>Home page</h1>'
    link = '''
        <br>
        <a href="/home">Home</a>
        <a href="/about">About</a>
        <a href="/product">Product</a>
        <a href="/contact">Contact</a>
        <a href="/help">Help</a>
    '''
    return render_template('home.html',title=title)

@app.route('/product')
def product():
    title = 'Product page'
    content = '<h3>Product page</h1>'
    link = '''
        <br>
        <a href="/home">Home</a>
        <a href="/about">About</a>
        <a href="/product">Product</a>
        <a href="/contact">Contact</a>
        <a href="/help">Help</a>
    '''
    return html_tmp.render(title=title,content=content,link=link)

@app.route('/contact')
def contact():
    title = 'content page'
    content = '<h3>Contact page</h1>'
    link = '''
        <br>
        <a href="/home">Home</a>
        <a href="/about">About</a>
        <a href="/product">Product</a>
        <a href="/contact">Contact</a>
        <a href="/help">Help</a>
    '''
    return html_tmp.render(title=title,content=content,link=link)

@app.route('/about')
def about():
    title = 'About page'
    content = '<h3>About page</h1>'
    link = '''
        <br>
        <a href="/home">Home</a>
        <a href="/about">About</a>
        <a href="/product">Product</a>
        <a href="/contact">Contact</a>
        <a href="/help">Help</a>
    '''
    return html_tmp.render(title=title,content=content,link=link)

@app.route('/help')
def help():
    title = 'Help page'
    content = '<h3>Help page</h1>'
    link = '''
        <br>
        <a href="/home">Home</a>
        <a href="/about">About</a>
        <a href="/product">Product</a>
        <a href="/contact">Contact</a>
        <a href="/help">Help</a>
    '''
    return html_tmp.render(title=title,content=content,link=link)

if __name__ == "__main__":
    app.run(debug=True)