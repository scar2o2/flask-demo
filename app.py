from flask import Flask, render_template, request

app = Flask(__name__)

# Home page route
@app.route('/')
def home():
    return render_template('index.html')

# Form submission route
@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('username')
    if not name:
        return render_template('result.html', message="Please enter a name!")
    return render_template('result.html', message=f"Hello, {name}! Welcome to Flask 😊")

if __name__ == '__main__':
    app.run(debug=True)
 
