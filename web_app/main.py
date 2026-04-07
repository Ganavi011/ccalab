from flask import Flask, render_template

app = Flask(__name__) # Fixed the underscores here

@app.route('/')
def home():
    # Ensure you have an 'index.html' file inside a folder named 'templates'
    return render_template('index.html', title="Home page")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
