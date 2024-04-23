

from flask import Flask, render_template


app = Flask(__name__) # type: ignore

@app.route('/')
def home():
    return render_template('home.html') # type: ignore

@app.route('/about')
def about():
    return render_template('about.html') # type: ignore

if __name__ == '__main__':
    app.run()