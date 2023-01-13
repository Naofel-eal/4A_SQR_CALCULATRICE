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

def addTransaction(P1 : Person, P2 : Person, sum : float, date : str):
    tuple = (P1.id, P2.id, date, sum)
    print(tuple)
    transaction.append(tuple)

def sort_dates():
	transac = sorted(transaction, key=lambda x: datetime.strptime(x[2], '%d/%m/%Y'))
	return transac