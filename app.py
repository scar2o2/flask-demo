from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('username')
    if not name:
        return render_template('result.html', message="Please enter a name!")
    return render_template('result.html', message=f"Hello, {name}! Welcome to Flask 😊")

if __name__ == '__main__':
    # Use the port provided by Render or default to 5000
    port = int(os.environ.get("PORT", 5000))
    # 0.0.0.0 is required so Render can access the app externally
    app.run(host='0.0.0.0', port=port)
