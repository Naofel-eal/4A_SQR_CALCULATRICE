from classes.Person import Person
from datetime import datetime
from flask import Flask, request
import os

app = Flask(__name__)
app.config['FILE_UPLOADS'] = os.path.dirname(os.path.abspath(__file__))

transactions = [
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

def stringifyTransactions() -> str:
    response = "<h1>Transactions: </h1><ul>"
    for transac in transactions:
        response += "<li>" + transac[2] + " : " + getPersonByID(transac[0]).firstname + " a viré " + str(transac[3]) + "€ à " + getPersonByID(transac[1]).firstname +"</li>"
    return response

def getPersonByNames(firstname, name) -> Person:
    for person in people:
        if person.name == name and person.firstname == firstname:
            return person
    
    newPerson = Person(id=len(people), firstname=firstname, name=name, solde=0.0)
    people.append(newPerson)
    return newPerson

def getPersonByID(id: int) -> Person:
    for person in people:
        if person.id == id:
            return person
    print("Person not found !")
    return None

def addTransaction(P1 : Person, P2 : Person, sum : float, date : str):
    tuple = (P1.id, P2.id, date, sum)
    transactions.append(tuple)

def sort_dates():
	transac = sorted(transactions, key=lambda x: datetime.strptime(x[2], '%d/%m/%Y'))
	return transac