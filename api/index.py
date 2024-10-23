from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def home():
  #  Set-Cookie: tasty_cookie=strawberry
    public_ip = request.headers.get('Cookie')
    return f"Your public IP is: {public_ip}"




