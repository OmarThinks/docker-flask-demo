from flask import (Flask,jsonify)

app = Flask(__name__)

@app.route("/")
def home():
	return jsonify({"success":True,"details":"The app is running"}),200

if __name__ == '__main__':
	app.run(debug=True, port=5000,host="0.0.0.0")