class speciesClass:
    name = None
    weight = None
    agression = None
    ability = None

    def __init__(self, name, weight, agression, ability):
        self.name = name
        self.weight = weight
        self.agression = agression
        self.ability = ability

    def printInfo(self):
        print("The major island species is called the " + self.name + ". It weighs " + self.weight + " pounds on average. It is typically " + self.agression + ". Its special ability is " + self.ability + ".")