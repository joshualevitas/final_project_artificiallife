import matplotlib.pyplot as p 
from load_bots import load_bot

locations = ["Control", "Moon", "Jupiter"]


initial_fitnesses = { loc: [load_bot("Data/" + loc + "GravityCreature.json_" + str(bot)).fitness for bot in range(5)] for loc in locations}

