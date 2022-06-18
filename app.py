from flask import Flask, jsonify, request


app = Flask(__name__)
#route to entertain our post and get request from flutter app
@app.route('/', methods = ['GET', 'POST'])
def nameRoute():
    return ("aaa")
if __name__ == "__main__":
    app.run()