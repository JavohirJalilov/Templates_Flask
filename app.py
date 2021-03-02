from flask import Flask
app = Flask(__name__)

link = '''
    <br>
    <a href="/home">Home</a>
    <a href="/about">About</a>
    <a href="/product">Product</a>
    <a href="/contact">Contact</a>
    <a href="/help">Help</a>
'''

@app.route('/home')
@app.route('/')
def home():
    title = '<h3>Home page</h1>'
    page = f'{title}\n{link}'
    return page

@app.route('/product')
def product():
    title = '<h3>Product page</h1>'
    page = f'{title}\n{link}'
    return page

@app.route('/contact')
def contact():
    title = '<h3>Contact page</h1>'
    page = f'{title}\n{link}'
    return page

@app.route('/about')
def about():
    title = '<h3>About page</h1>'
    page = f'{title}\n{link}'
    return page

@app.route('/help')
def help():
    title = '<h3>Help page</h1>'
    page = f'{title}\n{link}'
    return page

if __name__ == "__main__":
    app.run(debug=True)