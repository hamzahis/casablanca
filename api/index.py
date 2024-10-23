from flask import Flask, request, make_response


app = Flask(__name__)

@app.route('/')
def home():
    response = make_response('Hello, world!')
    response.set_cookie('yummy_cookie','chocolate')
    return response
  #  public_ip = request.headers.get('Cookie')
#    return f"Your public IP is: {public_ip}"




