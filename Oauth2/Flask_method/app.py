from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return "Servidor Flask em execução!"

if __name__ == "__main__":
    app.run(port=3000)
