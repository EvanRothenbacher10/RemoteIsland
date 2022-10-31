from speciesClass import *

class island:
    population = None
    numAcres = None
    Species = None
    biome1 = None
    biome2 = None

    def __init__(self, population, numAcres, Species, biome1, biome2):
        self.population = population
        self.numAcres = numAcres
        self.Species = Species
        self.biome1 = biome1
        self.biome2 = biome2

    def printInfo():
        print("This islands name is")
