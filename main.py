import os
import jsonify
from flask import Flask, request, jsonify

app = Flask(__name__)

# set up root route
@app.route("/")
def hello_world():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR']
    response = {
        "message": "Hello World",
        "source_ip": ip,
        "status": 200
    }
    return jsonify(response)

# Get the PORT from environment
port = os.getenv('PORT', '8080')
if __name__ == "__main__":
	app.run(host='0.0.0.0',port=int(port))

