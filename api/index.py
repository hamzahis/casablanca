from flask import Flask



app = Flask(__name__)



@app.route('/')

def home():

    public_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    return f"Your public IP is: {public_ip}"




