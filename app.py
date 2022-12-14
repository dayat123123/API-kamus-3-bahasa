from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from googletrans import Translator
import json
translator = Translator(service_urls=['translate.googleapis.com'])
import mysql.connector
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'sql6.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql6513279'
app.config['MYSQL_PASSWORD'] = '71TDCiXpb4'
app.config['MYSQL_DB'] = 'sql6513279'
mysql = MySQL(app)
# percoobaan penambahan lagi ya. 
#declared an empty variable for reassignment
response = ''

#creating the instance of our flask application
# percobaan update github

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
    indoinggris = translator.translate(inputchr, dest='en')
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
@app.route('/api4', methods = ['GET'])
def returnvalue4():
    global banjarindo
    d = {}
    inputchr = str(request.args['query'])
    cur = mysql.connection.cursor()
    row_count = cur.execute("SELECT kata_dasar FROM tb_katadasar2 where kata_daerah = %s", [inputchr])
    mysql.connection.commit()
    if row_count > 0:
        banjarindo=cur.fetchone()[0]
        answer = banjarindo
        d['output'] = answer
        return d
    else:
        hasil = "Kata belum tersedia"
        d['output'] = hasil
        return d    
@app.route('/api5', methods = ['GET'])
def returnvalue5():
    # global indobanjar
    # d = {}
    # inputchr = str(request.args['query'])
    # cur = mysql.connection.cursor()
    # row_count = cur.execute("SELECT kata_daerah FROM tb_katadasar2 where kata_dasar = %s", [inputchr])
    # mysql.connection.commit()
    # if row_count > 0:
    #     indobanjar=cur.fetchone()[0]
    #     answer = indobanjar
    #     d['output'] = answer
    #     return d
    # else:
    #     hasil = "Kata belum tersedia"
    #     d['output'] = hasil
    #     return d
    
    global indobanjar
    new_string = {}
    my_list = []
    d= {}
    string = str(request.args['query'])
    list_string = string.split()
    n = len(list_string)
    for i in range(n):
        cur = mysql.connection.cursor()
        row_count = cur.execute("SELECT kata_daerah FROM tb_katadasar2 where kata_dasar = %s", [list_string[i]])
        mysql.connection.commit()
        if row_count > 0:
            indobanjar = cur.fetchone()[0]
            answer = indobanjar
            my_list.append(answer)
        else:
            my_list.append(list_string[i])

    d['output'] = ' '.join(my_list)
    return d
@app.route('/api6', methods = ['GET'])
def returnvalue6():
    # global inggrisbanjar
    # global aa
    # d = {}
    # inputchr = str(request.args['query'])
    # inggrisbanjar = translator.translate(inputchr, dest='id')
    # answer = inggrisbanjar.text
    # cur = mysql.connection.cursor()
    # row_count = cur.execute("SELECT kata_daerah FROM tb_katadasar2 where kata_dasar = %s", [answer])
    # mysql.connection.commit()
    # if row_count > 0:
    #     aa=cur.fetchone()[0]
    #     hasil = aa
    #     d['output'] = hasil
    #     return d
    # else:
    #     hasil = "Kata belum tersedia"
    #     d['output'] = hasil
    #     return d
    global inggrisbanjar
    new_string = {}
    my_list = []
    d= {}
    string = str(request.args['query'])
    inggrisbanjar = translator.translate(string, dest='id')
    answer = inggrisbanjar.text
    list_string = answer.split()
    n = len(list_string)
    for i in range(n):
        cur = mysql.connection.cursor()
        row_count = cur.execute("SELECT kata_daerah FROM tb_katadasar2 where kata_dasar = %s", [list_string[i]])
        mysql.connection.commit()
        if row_count > 0:
            inggrisbanjar=cur.fetchone()[0]
            answer = inggrisbanjar
            my_list.append(answer)
        else:
            my_list.append(list_string[i])

    d['output'] = ' '.join(my_list)
    return d

@app.route('/api7', methods = ['GET'])
def returnvalue7():
    # global banjaringgris
    # global aa
    # d = {}
    # inputchr = str(request.args['query'])
    # cur = mysql.connection.cursor()
    # row_count = cur.execute("SELECT kata_dasar FROM tb_katadasar2 where kata_daerah = %s", [inputchr])
    # mysql.connection.commit()
    # if row_count > 0:
    #     aa=cur.fetchone()[0]
    #     banjaringgris = translator.translate(aa, dest='en')
    #     answer = banjaringgris.text
    #     hasil = answer
    #     d['output'] = hasil
    #     return d
    # elif row_count == None:
    #     hasil = "Kata belum tersedia"
    #     d['output'] = hasil
    #     return d
    # else:
    #     hasil = "Kata belum tersedia"
    #     d['output'] = hasil
    #     return d
    global banjaringgris
    global aa
    new_string = {}
    my_list = []
    d= {}
    c={}
    string = str(request.args['query'])
    list_string = string.split()
    n = len(list_string)
    for i in range(n):
        cur = mysql.connection.cursor()
        row_count = cur.execute("SELECT kata_dasar FROM tb_katadasar2 where kata_daerah = %s", [list_string[i]])
        mysql.connection.commit()
        if row_count > 0:
            aa=cur.fetchone()[0]
            my_list.append(aa)
        else:
            my_list.append(list_string[i])

    # d['output'] = ' '.join(my_list)
    c = ' '.join(my_list)
    banjaringgris = translator.translate(c, dest='en')
    d['output'] = banjaringgris.text
    return d
# ini percobaan
@app.route('/api8', methods = ['GET'])
def returnvalue8():
    global banj
    new_string = {}
    my_list = []
    d= {}
    string = str(request.args['query'])
    list_string = string.split()
    n = len(list_string)
    for i in range(n):
        cur = mysql.connection.cursor()
        row_count = cur.execute("SELECT kata_dasar FROM tb_katadasar2 where kata_daerah = %s", [list_string[i]])
        mysql.connection.commit()
        if row_count > 0:
            banj=cur.fetchone()[0]
            answer = banj
            my_list.append(answer)
        else:
            my_list.append(list_string[i])

    d['output'] = ' '.join(my_list)
    return d
    # new_string = ' '.join(list_string)
    # for i, item in enumerate (list_string):
    #     cur = mysql.connection.cursor()
    #     row_count = cur.execute("SELECT kata_dasar FROM tb_katadasar2 where kata_daerah = %s", [list_string[1]])
    #     mysql.connection.commit()
    #     if row_count > 0:
    #         banjarindo=cur.fetchone()[0]
    #         answer = banjarindo
    #         d['output'] = answer
    #         return d
    #     else:
    #         hasil = "Kata belum tersedia"
    #         d['output'] = hasil
    #         return d    
    
if __name__ == "__main__":
    app.run()