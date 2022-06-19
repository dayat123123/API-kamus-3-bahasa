from flask import Flask, jsonify, request
import json
from googletrans import Translator
translator = Translator(service_urls=['translate.googleapis.com'])

#declared an empty variable for reassignment
response = ''

#creating the instance of our flask application
app = Flask(__name__)

#route to entertain our post and get request from flutter app
@app.route('/name', methods = ['GET', 'POST'])
def nameRoute():

    #fetching the global response variable to manipulate inside the function
    global response
    global adda
    global adc
    global hasil
    #checking the request type we get from the app
    if(request.method == 'POST'):
        request_data = request.data #getting the response data
        request_data = json.loads(request_data.decode('utf-8')) #converting it from json to key value pair
        name = request_data['name'] #assigning it to name
        adda = f'kamu {name}' #re-assigning response with the name we got from the user
        adc =  translator.translate(adda, dest='en')
        hasil = adc.text
        response = hasil
        return " " #to avoid a type error
    else:
        return jsonify({'name' : response}) #sending data back to your frontend app

if __name__ == "__main__":
    app.run()