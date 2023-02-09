from flask import Flask, request
from Operation import Operation

app = Flask(__name__)
operationsList = {}

def appendOperation(type: str, n1: int, n2: int):
    operation = Operation(len(operationsList), type, n1, n2)
    operationsList[str(operation.id)] = operation
    return operation.id

@app.route('/')
def home():
	return '''<h1>Effectuer une opération mathematiques avec les routes <ul><li>/add</li><li>/sub</li><li>/multiply</li><li>/divide</li></ul></h1>'''

@app.route('/api/operation', methods=['POST'])
def operation():
    n1 = request.args.get('n1')
    n2 = request.args.get('n2')
    type = request.args.get('type')
    if n1 != None and n2 != None and type != None:
        return str(appendOperation(type, n1, n2)) + "\n"
    else:
        return "ELEMENT NULL"

@app.route('/api/result')
def getResult():
    id = request.args.get('id')
    if id != None:
        return str(operationsList[id].result) + "\n"
    else:
        return "ELEMENT NULL"

if __name__ == '__main__':
    app.run(debug=True)
