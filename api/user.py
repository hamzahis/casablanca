from flask import Flask, request, make_response, render_template


app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':   

        name = request.form['name']
        email = request.form['email']   

        return f"Name: {name}<br>Email: {email}"
    else:
        return render_template('index.html')





#@app.route('/')
#def home():
  #  public_ip = request.headers.get('Cookie')
  #  return f"Your public IP is: {public_ip}"
 #   response = make_response('Hello, world!')
  #  response.set_cookie('yummy_cookie',   'chocolate')
  #  return response
    




