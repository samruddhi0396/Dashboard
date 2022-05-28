#import packages
from flask import Flask, render_template, request
import os
import random
from flask import request, jsonify
import requests
#creating an instance flask and storing in variable app
app=Flask(__name__)

database={'mis':'123','danlaw':'123'}
path = os.getcwd()+r'\db.txt'

loginStatus = 0
storeMachData = 0
@app.route('/') #default url
def firstpage():
    return render_template("login.html")
    #return render_template("home.html",name="Aalekh")


@app.route('/form_login', methods=['POST','GET'])
def login():
    global loginStatus
    if(loginStatus == 0):
        loginStatus = 1 
        name=request.form['username']
        pwd=request.form['psw']
        #print(name,pwd)
        if name not in database:
            return render_template('login.html', info='invalid user')
        else:
            if database[name]!=pwd :
                return render_template('login.html', info='invalid password')
            else:
                file = open('data.txt','r')
                data = file.readlines()
                '''    
                t = random.randint(23, 50)
                c = random.randint(3, 9)
                x = random.randint(0, 3)
                y = random.randint(0, 3)
                z = random.randint(0, 3)
                ''' 
                value = data[len(data)-1].split(',')
                #print(value.split(','))
                t = int(value[0].strip())
                c = int(value[1].strip())
                x = int(value[2].strip())
                y = int(value[3].strip())
                z = int(value[4].strip())
                return render_template('plotg.html',t1=t,c1=c,h1=x,v1=y,a1=z)
                #requests.post(url="http://127.0.0.1:5000/dataDisplay")
    else:
            file = open('data.txt','r')
            data = file.readlines()

            value = data[len(data)-1].split(',')
            #print(value.split(','))
            t = int(value[0].strip())
            c = int(value[1].strip())
            x = int(value[2].strip())
            y = int(value[3].strip())
            z = int(value[4].strip())
            return render_template('plotg.html',t1=t,c1=c,h1=x,v1=y,a1=z)

@app.route('/data', methods=['GET'])
def getSensorData():
    query_parameters = request.args
    file = open('data.txt','a')
    
    temp = query_parameters.get('temp')
    current = query_parameters.get('current')
    x_axis = query_parameters.get('x')
    y_axis = query_parameters.get('y')
    z_axis = query_parameters.get('z')
    data = str(temp) + ',' + str(current) + ',' + str(x_axis) + ',' + str(y_axis) + ',' + str(z_axis)+'\n'
    #print(temp,current,x,y,z)
    file.write(data)
    file.close()
    return jsonify(200)


@app.route('/dataDisplay', methods=['POST','GET'])
def dataDisplay():
    global storeMachData
    if(storeMachData == 0):
        storeMachData = 1
        file = open('machine.txt','a')
        cmpName = request.form['company']
        equipmentnm = request.form['equipmentnm']
        Equiploc = request.form['Equiploc']
        Ratedspeed = request.form['Ratedspeed']
        power = request.form['power']
        data = cmpName+','+ equipmentnm+','+Equiploc+','+Ratedspeed+','+power+'\n'
        #print(data1)
        file.write(data)
        file.close()


    file = open('data.txt','r')
    data = file.readlines()

    value = data[len(data)-1].split(',')
    #print(value.split(','))
    t = int(value[0].strip())
    c = int(value[1].strip())
    x = int(value[2].strip())
    y = int(value[3].strip())
    z = int(value[4].strip())
    print('Display data')
    return render_template('plotg.html',t1=t,c1=c,h1=x,v1=y,a1=z)

@app.route('/machineRegData', methods=['POST','GET'])
def machRegData():
    global storeMachData
    storeMachData = 0
    return render_template('NewMachineReg.html')
    

if __name__=='__main__':
    #app.debug = True
    app.run()
