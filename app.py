from googletrans import Translator
translator = Translator(service_urls=['translate.googleapis.com'])
from flask import Flask
app = Flask(__name__)
@app.route("/")
def main():
    kata = "kamu jelek sekali"
    data = translator.translate(kata, dest='en')
    t = data.text
    return(t)
if __name__ == "__main__":
    app.run()