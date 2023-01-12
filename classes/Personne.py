class Personne:
    id : int
    firstname : str
    name : str
    solde : float
    
    def __init__(self, firstname : str, name : str, solde : float) -> None:
        self.firstname = firstname
        self.name = name
        self.solde = solde
    
    