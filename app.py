'''
Source:

Author: Altair


'''
from flask import Flask,render_template, jsonify, request
import random
import json
import data_c


app  = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def startpy():

    result = {

        "Greetings" : "Altair"
    }

    #return jsonify(result)
    return render_template("ca-wildfires.html") 

'''
http://0.0.0.0:3091/api/data
'''

@app.route("/api/data", methods=["GET"])
def api_get_data():

    result = data_c.get_data()

    # result_dict = {

    #     'year'       : year,
    #     'pytorch'    : pytorch,
    #     'tensorFlow' : tensorFlow

    # }

    return jsonify(result)

'''
http://0.0.0.0:3091/api/add
http://0.0.0.0:3091/api/add?year=2017&ontario_tourist=20345&quebec_tourist=200
http://0.0.0.0:3000/api/add?year=2021&pytorch=180&tensorFlow=90
http://127.0.0.1:6969/api/add?year=&wildfires=
'''
@app.route("/api/add", methods=["GET"])
def api_add_data():
 
    year            = request.values.get('year')
    wildfires         = request.values.get('wildfires')

    result = {
        'year'          : year,
        'wildfires'       : wildfires

    }
    result_data = data_c.add_row(year, wildfires)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug = True,port = 6969 )
