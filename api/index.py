from flask import Flask, request
from http import cookies

C = cookies.SimpleCookie()
C["fig"] = "newton"
C["sugar"] = "wafer"


app = Flask(__name__)



@app.route('/')

def home():
  
    public_ip = request.headers.get('Cookie')
    return f"Your public IP is: {public_ip}"




