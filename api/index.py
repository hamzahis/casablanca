from flask import Flask, request



app = Flask(__name__)



@app.route('/')

def home():

    public_ip = request.headers.get('Host')
    return f"Your public IP is: {public_ip}"




