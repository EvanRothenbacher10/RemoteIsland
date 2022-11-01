from speciesClass import *
from biomeClass import *

class islandClass:
    name = None
    population = None
    numAcres = None
    Species = None
    biome1 = None
    biome2 = None

    def __init__(self, name, population, numAcres, Species, biome1, biome2):
        self.name = name
        self.population = population
        self.numAcres = numAcres
        self.Species = Species
        self.biome1 = biome1
        self.biome2 = biome2

    def printInfo(self):
        print("This islands name is " + self.name + ". The population is " + str(self.population) + ". The island has " + str(self.numAcres) + " Acres. The two main biomes on the island are " + self.biome1 + " and " + self.biome2 + ".")
