from flask import Flask, request



app = Flask(__name__)



@app.route('/')

def home():

    document.cookie = "yummy_cookie=blueberry"
    add = document.cookie

    public_ip = request.headers.get('add')
    return f"Your public IP is: {public_ip}"




