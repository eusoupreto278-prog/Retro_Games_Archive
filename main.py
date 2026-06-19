from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/tetris.html')
def tetris():
    return render_template('tetris.html')

@app.route('/pong.html')
def pong():
    return render_template('pong.html')

@app.route('/snake.html')
def snake():
    return render_template('snake.html')

@app.route('/space_invaders.html')
def space_invaders():
    return render_template('space_invaders.html')

if __name__ == '__main__':
    app.run()