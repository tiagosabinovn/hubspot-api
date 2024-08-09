from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask server running!"

if __name__ == "__main__":
    app.run(port=3000)

