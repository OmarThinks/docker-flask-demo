from flask import (Flask,jsonify)

app = Flask(__name__)

@app.route("/")
def home():
	return jsonify({"success":True,"details":"The app is running"}),200

if __name__ == '__main__':
	app.run(debug=True)