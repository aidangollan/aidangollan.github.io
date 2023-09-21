from flask import Flask, render_template as RenderTemplate, request, redirect
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/health')
def health_check():
    return "Healthy", 200

@app.route('/', methods = ["GET", "POST"])
def graph():
    return RenderTemplate("index.html")

if __name__ == "__main__":
    app.run(debug=True)