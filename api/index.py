from flask import Flask, request
from http import cookies




app = Flask(__name__)



@app.route('/')

def home():
  
    public_ip = request.headers.get('Set-Cookie: id=new-value')
    return f"Your public IP is: {public_ip}"




