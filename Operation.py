class Operation:
    id: int;
    type: str;
    n1: float;
    n2: float;
    result: float;

    def __init__(self, id: int, type: str, n1: float, n2: float):
        self.id = int(id);
        self.n1 = float(n1);
        self.n2 = float(n2);
        if type == 'add':
            self.result = self.n1 + self.n2;
        elif type == 'sub':
            self.result = self.n1 - self.n2;
        elif type == "mul":
            self.result = self.n1 * self.n2;
        elif type == "div":
            self.result = self.n1 / self.n2;
        else:
            self.result = 0;
