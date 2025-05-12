from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_flask():  # put application's code here
    return 'Hello Flask!'

@app.route('/user/<username>')
def get_name(username):  # put application's code here
    return f'Hello {username}!'

@app.route('/hello/<name>')
def hello(name):
    return f'Hello, {name}!'

@app.route('/double/<int:num>')
def double(num):
    return f'{num} * 2 = {num * 2}'

@app.route('/square/<float:num>')
def square(num):
    return f'{num} в квадрате= {num * num}'

@app.route('/reverse/<string:text>')
def reverse(text):
    return text[::-1]



if __name__ == '__main__':
    app.run(debug=True)
