from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello_world():
    return 'Hello world'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

if __name__ == '__main__':
    app.run(debug=True)
