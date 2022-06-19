import json
from googletrans import Translator
translator = Translator(service_urls=['translate.googleapis.com'])
from flask import Flask, jsonify, request
app = Flask(__name__)
@app.route("/")
def main():
    kata = "kamu jelek sekali"
    data = translator.translate(kata, dest='en')
    t = data.text
    return(t)
@app.route('/name', methods = ['GET', 'POST'])
def nameRoute():

    #fetching the global response variable to manipulate inside the function
    global response

    #checking the request type we get from the app
    if(request.method == 'POST'):
        request_data = request.data #getting the response data
        request_data = json.loads(request_data.decode('utf-8')) #converting it from json to key value pair
        name = request_data['name'] #assigning it to name
        response = f'Hi {name}! this is Python' #re-assigning response with the name we got from the user
        return " " #to avoid a type error
    else:
        return jsonify({'name' : response}) #sending data back to your frontend app

if __name__ == "__main__":
    app.run()

