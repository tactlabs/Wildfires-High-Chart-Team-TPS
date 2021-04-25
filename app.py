from flask import Flask,render_template, jsonify, request
import random
import json
import data


app  = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def startpy():

    result = {

        "Greetings" : "SAM"
    }

    #return jsonify(result)
    return render_template("index.html") 

@app.route("/api/data", methods=["GET"])
def api_get_data():

    result = data.get_data()

    return jsonify(result)

@app.route("/api/add", methods=["GET"])
def api_add_data():
 
    millionaire       = request.values.get('millionaire')
    worth        = request.values.get('worth')

    result = {
        'millionaire'          : millionaire,
        'worth'       : worth

    }
    result_data = data.add_row(millionaire, worth)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug = True,port = 6969 )