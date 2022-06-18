from flask import Flask, jsonify, request
from googletrans import Translator
translator = Translator(service_urls=['translate.googleapis.com'])

app = Flask(__name__)
#route to entertain our post and get request from flutter app
@app.route('/', methods = ['GET', 'POST'])
def nameRoute():
    kata = "Saya"
    data = translator.translate(kata, dest='en')
    t = data.text
    return(t)
if __name__ == "__main__":
    app.run()