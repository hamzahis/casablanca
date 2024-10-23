from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def home():
  
    public_ip = request.headers.get('Set-Cookie: yummy_cookie=chocolate')
    return f"Your public IP is: {public_ip}"




