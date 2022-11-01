from islandClass import *
from biomeClass import *
from speciesClass import *

#island 1

island = islandClass("Florida Keys", 100, 50, "Penguins", "Tundra", "Jungle")
island.printInfo()
species = speciesClass("penguin", "15", "agressive", "sliding")
species.printInfo()
biome = biomeClass("1000", "Tundra", "50", "0.015")
biome.printInfo()
biome2 = biomeClass("750", "Jungle", "65", "1.5")
biome2.printInfo2()

#island 2

island2 = islandClass("Jeoffery Jepsteins private island", 75, 10, "sardene", "flatland", "rocky mountain")
island2.printInfo()
species2 = speciesClass("sardene", "1000", "extremely agressive", "flopping around")
species2.printInfo()
biome3 = biomeClass("25555", "flatland", "90", "0")
biome3.printInfo()
biome4 = biomeClass("0", "rocky mountain", "-50", "5")
biome4.printInfo2()

#island 3

island3 = islandClass("jacobs house", 0, 80, "Dogs", "Forest", "Farmland")
island3.printInfo()
species3 = speciesClass("Dog", "40", "happy", "dog mushing")
species3.printInfo()
biome5 = biomeClass("50", "forst", "75", "0.5")
biome5.printInfo()
biome6 = biomeClass("60", "farmland", "75", "0.05")
biome6.printInfo2()
