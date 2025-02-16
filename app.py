from flask import Flask, render_template, jsonify

app = Flask(__name__)

Fashion = [
  {
    'id': 1,
    'title': 'Modern Fashion',
    'size': 'XL',
    'price': '£50'
    
  },
  {
    'id': 1,
    'title': 'Modern Fashion 1',
    'size': 'L',
    'price': '£50'

  }
]



@app.route("/")
def hello_world():
  return render_template('home.html', fashion=Fashion)
  
@app.route("/fashion")
def list_fashion():
  return jsonify(Fashion)

if __name__ == "__main__":
  app.run('0.0.0.0', debug=True)
