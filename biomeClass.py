class biomeClass:
    elevation = None
    name = None
    temperature = None
    treeDensity = None

    def __init__(self, elevation, name, temperature, treeDensity):
        self.elevation = elevation
        self.name = name
        self.temperature = temperature
        self.treeDensity = treeDensity

    def printInfo(self):
        print("The first biome is " + self.name + ". The elevation is " + self.elevation + " feet. The average temperature throughout the biome is " + self.temperature + " degrees fahrenheit. The tree density across the island is " + self.treeDensity + " trees per square foot.")

    def printInfo2(self):
        print("The second biome is " + self.name + ". The elevation is " + self.elevation + " feet. The average temperature throughout the biome is " + self.temperature + " degrees fahrenheit. The tree density across the island is " + self.treeDensity + " trees per square foot.")