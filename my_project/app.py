from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<page>')
def welcome(page):
    return render_template('welcome.html', page_var=page)

if __name__ == "__main__":
    app.run(debug=True)