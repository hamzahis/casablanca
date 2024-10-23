from flask import Flask, request
import cookies





app = Flask(__name__)



@app.route('/')

def home():
  C = cookies.SimpleCookie()
  C["fig"] = "newton"
  C["sugar"] = "wafer"


  #  document.cookie = "yummy_cookie=blueberry"
    

    public_ip = request.headers.get('Cookie')
    return f"Your public IP is: {public_ip}"




