from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
	return '''<h1>Salut !</h1>'''

transaction = [
    ('Naofel', 'Anisse', '14/02/2023', 380),
    ('Omar', 'Anisse', '28/01/2023', 52)
]

@app.route('/tuple', methods=['GET'])
def get_tuple():
	sort_dates(transaction)
	response = "<h1>Transactions: </h1><ul>"
	for transac in transaction:
		response += "<li>" + transac[2] + " : " + transac[0] + " a viré " + str(transac[3]) + "€ à " + transac[1] +"</li>"
	response += "</ul>"
	return response

def sort_dates(transaction):
	return sorted(transaction, key=lambda x: (x[6:10], x[3:5], x[0:2]))

if __name__ == '__main__':
    app.run()
