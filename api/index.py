from flask import Flask, request
import cookies

C = cookies.SimpleCookie()
C["fig"] = "newton"
C["sugar"] = "wafer"


app = Flask(__name__)



@app.route('/')

def home():
  


  #  document.cookie = "yummy_cookie=blueberry"
    

    public_ip = request.headers.get('Cookie')
    return f"Your public IP is: {public_ip}"




