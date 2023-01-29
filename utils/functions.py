from classes.Person import Person
from datetime import datetime
from flask import Flask, request
import os

app = Flask(__name__)

# Définit un emplacement spécifique pour stocker les fichiers téléchargés par l'application
app.config['FILE_UPLOADS'] = os.path.dirname(os.path.abspath(__file__))

# Notre liste de transactions de type tuple
transactions = [
    """(0, 1, '14/02/2023 15:56', 380),
    (1, 0, '28/01/2023 13:22', 52),
    (1, 2, '11/08/2022 19:50', 12),
    (0, 1, '16/12/2022 10:03', 33)"""
]

# Notre liste de personnes de type tuple
people = [
	Person(id=0, firstname="Naofel", name="EL ALOUANI", solde=300),
 	Person(id=1, firstname="Anisse", name="OUTSSAKKI", solde=100),
    Person(id=2, firstname="Omar", name="AMANA", solde=1200)
]

# Fonction affichant les transactions pour les methodes GET en HTML
def stringifyTransactions(transaction) -> str:
    response = "<h1>Transactions: </h1><ul>"
    for transac in transaction:
        response += "<li>" + transac[2] + " : " + getPersonByID(transac[0]).firstname + " a viré " + str(transac[3]) + "€ à " + getPersonByID(transac[1]).firstname +"</li>"
    return response

# Fonction permettant d'avoir notre personne grâce à son nom et prénom
def getPersonByNames(firstname, name) -> Person:
    for person in people:
        if person.name == name and person.firstname == firstname:
            return person
    
    newPerson = Person(id=len(people), firstname=firstname, name=name, solde=0.0)
    people.append(newPerson)
    return newPerson

# Fonction permettant d'avoir notre personne grâce à son ID
def getPersonByID(id: int) -> Person:
    for person in people:
        if person.id == id:
            return person
    print("Person not found !")
    return None

# Fonction ajout de transaction dans notre tableau
def addTransaction(P1 : Person, P2 : Person, sum : float, date : str):
    tuple = (P1.id, P2.id, date, sum, hash((P1, P2, sum)))
    transactions.append(tuple)

# Fonction de tri des dates par ordre chronologique (tri par année puis mois et enfin jour)
def sort_dates(tran):
	transac = sorted(tran, key=lambda x: datetime.strptime(x[2], '%d/%m/%Y'))
	return transac