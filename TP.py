#git stash; git pull; git stash pop;

from flask import Flask, request, jsonify
from classes.Person import Person
from utils.functions import *
import sys
import csv
import os

@app.route('/')
def home():
	return '''<h1>Salut !</h1>'''

## E1: Enregistrer une transaction
## E3 : Afficher une liste des transactions dans l’ordre chronologique liées à une personne.
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


## E2: Afficher une liste de toutes les transactions dans l’ordre chronologique
@app.route('/list', methods=['GET'])
def get_tuple():
	transactions = sort_dates()
	return stringifyTransactions()


## E4 : Afficher le solde du compte de la personne
@app.route('/solde/int:id', methods=['GET'])
def show_solde(id):
     person = next((p for p in people if p.id == id), None)
     if person:
          return jsonify({'id': person.id, 'firstname': person.firstname, 'name':person.name,'solde': person.solde})
     else:
          return jsonify({'error': 'La personne est introuvable'})
       

## E5: Importer des données depuis un fichier csv
@app.route('/csv', methods=['POST'])
def uploadCSV():
    data = []
    if request.method == 'POST':
        if request.files:
            file = request.files['transactions']
            filepath = os.path.join(app.config['FILE_UPLOADS'], file.filename)
            file.save(filepath)

            with open(filepath) as csv_file:
                reader = csv.reader(csv_file)
                for row in reader:
                    addTransaction(P1=getPersonByID(int(row[0])), P2=getPersonByID(int(row[1])), sum=row[3], date=row[2])
        else:
            print("No")
    return stringifyTransactions()

	
if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "check_syntax":
            print("Build [ OK ]")
            exit(0)
        else:
            print("Passed argument not supported ! Supported argument : check_syntax")
            exit(1)
    app.run(debug=True)