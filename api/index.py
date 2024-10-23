from flask import Flask, request
from http import cookies




app = Flask(__name__)



@app.route('/')
C = cookies.SimpleCookie()
C["fig"] = "newton"
C["sugar"] = "wafer"
def home():
  
    public_ip = request.headers.get('Cookie')
    return f"Your public IP is: {public_ip}"




