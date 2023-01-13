from flask import Flask, jsonify, request
from datetime import datetime
import json
from types import SimpleNamespace
from classes.Person import Person

app = Flask(__name__)

@app.route('/')
def home():
	return '''<h1>Salut !</h1>'''

transaction = [
    (0, 1, '14/02/2023', 380),
    (1, 0, '28/01/2023', 52)
]

people = [
	Person(id=0, firstname="Naofel", name="EL ALOUANI", solde=300),
 	Person(id=1, firstname="Anisse", name="OUTSSAKKI", solde=100)
]

@app.route('/list', methods=['GET'])
def list_tuple():
	sort_dates()
	response = "<h1>Transactions: </h1><ul>"
	for transac in transaction:
		response += "<li>" + transac[2] + " : " + getPersonByID(transac[0]).firstname + " a viré " + str(transac[3]) + "€ à " + getPersonByID(transac[1]).firstname +"</li>"
	response += "</ul>"
	return response

@app.route("/add", methods=['POST'])
def add():
    data = request.json
    jsonP1 = data.get('name')
    
    print(data.get('firstname'))
    transaction.appe
    return data

def getPerson(firstname, name) -> Person:
    for person in people:
        if person.name == name and person.firstname == firstname:
            return person
    people.append(Person(id=len(people), firstname=firstname, name=name, solde= 0.0))

def getPersonByID(id: int) -> Person:
    for person in people:
        if person.id == id:
            return person

def sort_dates():
	#return sorted(transaction, key=lambda x: (x[6:10], x[3:5], x[0:2]))
	sortedArr = []
	for transac in transaction:
		sortedArr.append(transac)
	
if __name__ == '__main__':
    app.run()
