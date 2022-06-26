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
        adda = f'{name}' #re-assigning response with the name we got from the user
        adc =  translator.translate(adda, dest='en')
        hasil = adc.text
        response = hasil
        return " " #to avoid a type error
    else:
        return jsonify({'name' : response}) #sending data back to your frontend app

@app.route('/name2', methods = ['GET', 'POST'])
def nameRoute2():

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
        adda = f'{name}' #re-assigning response with the name we got from the user
        adc =  translator.translate(adda, dest='id')
        hasil = adc.text
        response = hasil
        return " " #to avoid a type error
    else:
        return jsonify({'name' : response}) #sending data back to your frontend app
@app.route('/api', methods = ['GET'])
def returnvalue():
    global hasilbanjar
    d = {}
    inputchr = str(request.args['query'])
    hasilbanjar = translator.translate(inputchr, dest='en')
    answer = hasilbanjar.text
    d['output'] = answer
    return d
@app.route('/api2', methods = ['GET'])
def returnvalue2():
    global indoinggris
    d = {}
    inputchr = str(request.args['query'])
    indoinggris = translator.translate(inputchr, dest='ja')
    answer = indoinggris.text
    d['output'] = answer
    return d
@app.route('/api3', methods = ['GET'])
def returnvalue3():
    global inggrisindo
    d = {}
    inputchr = str(request.args['query'])
    inggrisindo = translator.translate(inputchr, dest='id')
    answer = inggrisindo.text
    d['output'] = answer
    return d

if __name__ == "__main__":
    app.run()