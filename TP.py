#git stash; git pull; git stash pop;

from flask import Flask, jsonify, request
from datetime import datetime
import json
from types import SimpleNamespace
from classes.Person import Person
from utils.functions import *

app = Flask(__name__)

@app.route('/')
def home():
	return '''<h1>Salut !</h1>'''

transaction = [
    (0, 1, '14/02/2023', 380),
    (1, 0, '28/01/2023', 52),
    (1, 2, '11/08/2022', 12),
    (0, 1, '16/12/2022', 33)
]

people = [
	Person(id=0, firstname="Naofel", name="EL ALOUANI", solde=300),
 	Person(id=1, firstname="Anisse", name="OUTSSAKKI", solde=100),
    Person(id=2, firstname="Omar", name="AMANA", solde=1200)
]

@app.route("/add", methods=['POST'])
def add():
    data = request.get_json()
    P1firstname = data['P1']['firstname']
    P1name = data['P1']['firstname']
    P2firstname = data['P2']['firstname']
    P2name = data['P2']['name']
    date = data['date']
    value = data['value']
    
    P1 = getPersonByNames(firstname=P1firstname, name=P1name)
    P2 = getPersonByNames(firstname=P2firstname, name=P2name)

    addTransaction(P1=P1, P2=P2, date=date, sum=value)
    return data

@app.route('/tuple', methods=['GET'])
def get_tuple():
	tran = sort_dates()
	response = "<h1>Transactions: </h1><ul>"
	for transac in tran:
				response += "<li>" + transac[2] + " : " + getPersonByID(transac[0]).firstname + " a viré " + str(transac[3]) + "€ à " + getPersonByID(transac[1]).firstname +"</li>"
	return response

	
if __name__ == '__main__':
    app.run()
    if len(sys.argv) > 1:
        if sys.argv[1] == "check_syntax":
            print("Build [ OK ]")
            exit(0)
        else:
            print("Passed argument not supported ! Supported argument : check_syntax")
            exit(1)
    app.run(debug=True)