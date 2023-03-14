import json 
import pickle

import helpers.search as search
from helpers.simulate import simulate
from load_bots import load_bot
import numpy as np
from parallelHillclimberUnpickled import PARALLEL_HILL_CLIMBER_UNPICKLED

import matplotlib.pyplot as plt


def run_sim():

    controlCreatures = [load_bot("Data/ControlGravityCreature.json_" + str(i)) for i in range(5)]
    moonCreatures = [load_bot("Data/MoonGravityCreature.json_" + str(i)) for i in range(5)]
    jupiterCreatures = [load_bot("Data/JupiterGravityCreature.json_" + str(i)) for i in range(5)]
    
    locations = ["Control", "Moon", "Jupiter"]
    fitnesses = {"ControlCreatures": [], "MoonCreatures": [], "JupiterCreatures": []}


    #change when changing gravity
    environment = "Control"


    #evolve each on moon, earth, and gravity (briefly, get fitnesses)
    #change gravity in simulation.py each time

    for groupIndex, group in enumerate([controlCreatures, moonCreatures, jupiterCreatures]):
        for index, creature in enumerate(group):
            creatures = search.random_evolved_from_pickle(seed = creature, show=False)
            creature_fitnesses = creatures[0]
            best = creatures[1]

            fitnesses[locations[groupIndex] + "Creatures"].append(creature_fitnesses)

            with open("Data/Best/{}".format(locations[groupIndex]+"In"+str(environment)+str(index)+".json"), 'wb') as f:
                pickle.dump(best, f)


            
            
    # print(fitnesses)
    

    #avg graph
    fig, ax = plt.subplots()
    plt.title("Average Creature Evolution Fitness in Control Environment")
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    
    for loc in ["ControlCreatures", "MoonCreatures", "JupiterCreatures"]:
        avg = []
        for c in range(len(fitnesses[loc][0])):
            avg_ = 0
            for g in range(len(fitnesses[loc])):
                avg_ += fitnesses[loc][g][c]
            avg.append(avg_)
                
        avg2 = [i / 5 for i in avg]
        # arr = np.average(np.array(fitnesses[loc]), axis=1)
        plt.plot(avg2, label=str(loc))
    plt.legend()
    
    plt.savefig('Graphs/averages_control.png')
    plt.cla()

    #control fitness
    plt.title("Control Creature Fitness in " + str(environment) + " Environment")
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    for index, creature in enumerate(fitnesses["ControlCreatures"]):
        plt.plot(creature, label=str(index))
    
    plt.savefig('Graphs/ControlIn' + str(environment) + ".png")
    plt.cla()
    
    #moon fitness
    plt.title("Moon Creature Fitness in " + str(environment) + "Environment")
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    for index, creature in enumerate(fitnesses["MoonCreatures"]):
        plt.plot(creature, label=str(index))
    
    plt.savefig('Graphs/MoonIn' + str(environment) + ".png")
    plt.cla()


    #jupiter fitness
    plt.title("Jupiter Creature Fitness in " + str(environment) + "Environment")
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    for index, creature in enumerate(fitnesses["JupiterCreatures"]):
        plt.plot(creature, label=str(index))
    
    plt.savefig('Graphs/JupiterIn' + str(environment) + ".png")
    plt.cla()

'''
planet train, sim: "Jupiter", "Moon", or "Earth"
'''
def view_best_bots(planet_train, planet_sim):
    for i in range(5):
        bot = load_bot("Data/Best/" + str(planet_train) + "In" + str(planet_sim) + str(i) + ".json")
        bot_phc = PARALLEL_HILL_CLIMBER_UNPICKLED(bot)
        bot_phc.Show_Best()
        input("\n\npress enter to see next bot\n\n") 

def main():

    print("\n\nOptions:\n\n 1. Run simulation\n 2. View Robots\n\n(Type the number corresponding to the task and hit enter)\n")
    task = input("> ")
    if task == "1":
        run_sim()
    elif task == "2":
        planet_train_ = ""
        planet_sim_ = ""
        print("\n\n Robots were trained on 3 different planets. Which ones would you like to see?\n\n1. Earth (control)\n 2. Luna\n 3. Jupiter\n\n (Type the number corresponding to the task and hit enter)\n")
        planet_train = input("> ")
        # print(planet_train)
        
        if planet_train == "1":
            planet_train_ = "Control"
        elif planet_train == "2":
            planet_train_ = "Moon"
        else:
            planet_train_ = "Jupiter"
    

        print("\n\n Robots trained on " + str(planet_train_) + " were tested on 3 different planets. Which ones would you like to see?\n\n1. Earth (control)\n 2. Luna\n 3. Jupiter\n\n (Type the number corresponding to the task and hit enter)\n")
        planet_sim = input("> ")
        # print(planet_sim)
        if planet_sim == "1":
            planet_sim_ = "Control"
        elif planet_sim == "2":
            planet_sim_ = "Moon"
        else:
            planet_sim_ = "Jupiter"
       
        print(planet_train_)
        print(planet_sim_)
        view_best_bots(planet_train_, planet_sim_)

        

        


    


    #initial training of random creatures in respective environments
    '''
    for seed in range(5):
        creature = search.random_evolved_pickle(seed = seed)
        with open("Data/{}".format(file_name+"_"+str(seed)), 'wb') as f:
            pickle.dump(creature, f)
    '''


    
if __name__ == "__main__":
    main()

